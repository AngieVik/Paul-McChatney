#!/usr/bin/env python3
"""
validar_proyecto.py — Validador automático para el proyecto Paul McChatney.

Comprueba, sobre el árbol .md del proyecto:
  1. Enlaces relativos rotos (sintaxis Markdown `[texto](ruta)` y `<a href="ruta">`).
  2. Rutas mencionadas entre backticks (`archivo.md`) que no existen en disco
     (ignora rutas-plantilla evidentes: <slug>, NN, ejemplo, texto...).
  3. Corchetes de tags `[Tag]` mal formados dentro de bloques de código: analiza
     cada línea de cada bloque por separado (pila de profundidad), no el total
     de `[` y `]` del bloque entero — así un cierre sin apertura ya no puede
     quedar oculto porque otro tag distinto compensó el conteo global.
  4. Archivos truncados: frontmatter incompleto (falta cierre `---`, faltan
     claves `name`/`type`/`description`) o el archivo de INSTRUCCIONES
     (skills, rules, composicion, system_prompt, raíz) termina a mitad de frase.
  5. YAML de frontmatter estructuralmente inválido (línea que no parece
     `clave: valor`, comillas sin cerrar en una misma línea).
  6. Fences ``` sin cerrar: recorre el archivo línea a línea con un estado de
     apertura/cierre (solo cuentan las líneas que SON una marca de fence, no las
     apariciones de ``` incrustadas en prosa o dentro de una celda de tabla);
     si al final queda un fence abierto, se reporta.
  7. Encabezados mal cerrados: terminan en `.`, `:` o `;` (prohibido por
     `chuletas/plantilla_estilo.md` §2) o saltan de nivel (`#` -> `###`).
  8. Las plantillas generativas (`chuletas/plantilla_*.md`) generan un
     esqueleto compatible: se extrae cada bloque de código de la plantilla y
     se le aplican los chequeos 5-7 como si fuera un documento real.
  9. Todo `chuletas/plantilla_*.md` declara `type: plantilla` en su propio
     frontmatter.
  10. Dentro de `chuletas/`, cada archivo tiene exactamente un `# H1` fuera de
      bloques de código (ni cero ni varios).
  11. El esqueleto de `plantilla_proyecto.md` empieza con frontmatter YAML y
      trae las secciones canónicas de un proyecto (Titulo Original, Generated,
      Master, style_box, exclude_box, lyrics_box).
  12. Dentro de un esqueleto copiable, ninguna línea de viñeta parece prosa
      explicativa colada (instrucción para quien rellena la plantilla) en vez
      de un marcador determinista (`<...>`, `[...]` o backticks). Las plantillas
      de guía ricas en prosa (fonetizar, jerga), cuyo esqueleto es un documento
      con secciones de prosa fija, se eximen de este punto.
  13. Toda plantilla generativa (`chuletas/plantilla_*.md`) contiene al menos
      un esqueleto (bloque de código copiable); una plantilla sin esqueleto no
      genera nada.
  14. Identidad documental: el `# H1` coincide con `name`, y `name` coincide con
      el nombre del archivo cuando corresponde (con el nombre de la carpeta en
      los `SKILL.md`). Se exceptúan los nombres canónicos de raíz (README.md,
      CLAUDE.md, MEMORY.md, PROYECTOS.md), cuyo H1 es un título, no el slug.
  15. Bidireccionalidad mapa<->skill: toda skill que cita un mapa
      `.claude/rules/<x>.md` aparece en la línea `Consumido por` de ese mapa
      (y, por los chequeos 1-2, todo mapa apunta a archivos que existen).

Uso:
    python validar_proyecto.py [ruta_raiz] [--incluir-personales] [--excluir DIR ...]
    (usa `python3` en vez de `python` si tu sistema lo requiere así)

Si no se indica ruta, usa el directorio actual. Ignora .git, node_modules y
las carpetas personales de trabajo (_hojas_sucias, _temp, _produccion,
_prompts_antiguos, _docs) salvo que se pase --incluir-personales. Con
`--excluir proyectos` (uno o varios nombres) se saltan además esas carpetas —
útil para revisar solo el núcleo actual sin que las obras históricas metan
ruido.

Nota sobre la heurística de truncamiento (punto 4): solo se aplica a las
carpetas de INSTRUCCIONES (`.claude/`, `system_prompt/`, `composicion/`,
`chuletas/` y archivos sueltos en la raíz como CLAUDE.md/MEMORY.md), donde la
prosa siempre debería cerrar en frase completa. Se excluye deliberadamente
`proyectos/`, `chupilista/`, `fonetizar/` y `jerga/`: son letras, listas de
tags y ejemplos fonéticos que legítimamente terminan sin punto. Aun así es una
heurística — revisa cada aviso, no la trates como verdad absoluta.

Salida: reporte por consola agrupado por tipo de problema + código de salida
1 si se encontró algún problema (útil para hooks/CI), 0 si todo está limpio.
"""

import argparse
import os
import re
import sys
from pathlib import Path

IGNORE_DIRS = {".git", "node_modules", ".vscode"}
PERSONAL_DIRS = {"_hojas_sucias", "_temp", "_produccion", "_prompts_antiguos", "_docs"}

# Carpetas donde la prosa es "de instrucción" y debería cerrar en frase completa.
INSTRUCTIONAL_TOP_DIRS = {".claude", "system_prompt", "composicion", "chuletas"}

# Nombres canónicos de raíz: su H1 es un título humano, no el slug, y su `name`
# no tiene por qué coincidir con el nombre de archivo. Se exceptúan del chequeo
# de identidad documental (punto 14).
CANONICAL_FILENAMES = {"README.md", "CLAUDE.md", "MEMORY.md", "PROYECTOS.md"}

MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HTML_HREF_RE = re.compile(r'href="([^"]+)"')
BACKTICK_PATH_RE = re.compile(r"`([\w./\\-]+\.(?:md|py|json|yaml|yml))`")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
CODEBLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
# Una LÍNEA que es una marca de fence (apertura o cierre), admitiendo sangría:
# se usa para el estado de apertura/cierre del punto 6. Ignora los ``` sueltos
# incrustados en medio de una línea de prosa o de una celda de tabla.
FENCE_LINE_RE = re.compile(r"^\s*```")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$", re.MULTILINE)
H1_RE = re.compile(r"^#\s+(\S.*?)\s*$", re.MULTILINE)
NAME_RE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
RULES_CITED_RE = re.compile(r"\.claude/rules/([\w-]+)\.md")
CONSUMIDO_RE = re.compile(r"Consumido por:\**\s*(.+)")

REQUIRED_FRONTMATTER_KEYS = ("name", "type", "description")

# Secciones canónicas que debe traer el esqueleto de plantilla_proyecto.md.
REQUIRED_PROYECTO_SECTIONS = ("Titulo Original", "Generated", "Master", "style_box", "exclude_box", "lyrics_box")

# Línea de viñeta dentro de un esqueleto copiable: se compara contra estos
# marcadores para decidir si es un placeholder determinista o prosa colada.
PROSE_LEAK_RE = re.compile(r"^-\s+(.+)$")
PROSE_PLACEHOLDER_MARKERS = ("<", "[", "`")

# Terminaciones que sugieren que la frase SÍ está completa (incluye cierres
# de énfasis Markdown '*'/'_' porque son habituales al final de una nota).
SENTENCE_END_CHARS = set(".!?:`\"'”»)*_")

# Fragmentos que delatan una ruta-plantilla (placeholder), no un archivo real.
PLACEHOLDER_TOKENS = ("<", ">", "slug", "NN", "ejemplo", "texto", "archivo.md")

# Encabezados que NO deben cerrar con puntuación (regla de plantilla_estilo.md §2).
FORBIDDEN_HEADING_ENDINGS = (".", ":", ";")

# Plantillas de GUÍA ricas en prosa: su esqueleto es un documento estructurado
# con secciones de prosa fija que aparecen en cada archivo generado (no un
# molde puramente estructural). Se eximen del chequeo de "prosa colada"
# (punto 12), que solo tiene sentido en las plantillas de estructura pura.
PROSE_RICH_PLANTILLAS = {"plantilla_fonetizar.md", "plantilla_jerga.md"}


def is_placeholder_path(target: str) -> bool:
    lowered = target.lower()
    return any(tok.lower() in lowered for tok in PLACEHOLDER_TOKENS)


def iter_markdown_files(root: Path, include_personal: bool, extra_excluded: set):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in dirnames
            if d not in IGNORE_DIRS
            and d not in extra_excluded
            and (include_personal or d not in PERSONAL_DIRS)
        ]
        for fname in filenames:
            if fname.endswith(".md"):
                yield Path(dirpath) / fname


def frontmatter_name(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    nm = NAME_RE.search(m.group(1))
    return nm.group(1).strip() if nm else None


def check_links(path: Path, text: str, root: Path, problems: list):
    for regex in (MD_LINK_RE, HTML_HREF_RE):
        for m in regex.finditer(text):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_clean = target.split("#")[0]
            if not target_clean or is_placeholder_path(target_clean):
                continue
            resolved = (path.parent / target_clean).resolve()
            if not resolved.exists():
                problems.append(
                    f"[enlace roto] {rel(path, root)} -> '{target}' no existe (esperado en {resolved})"
                )


def check_backtick_paths(path: Path, text: str, root: Path, problems: list):
    for m in BACKTICK_PATH_RE.finditer(text):
        target = m.group(1)
        if "/" not in target and "\\" not in target:
            continue  # nombre suelto tipo `archivo.md` sin ruta, demasiado ambiguo
        if is_placeholder_path(target):
            continue
        target_norm = target.replace("\\", "/")
        for base in (path.parent, root):
            if (base / target_norm).exists():
                break
        else:
            problems.append(
                f"[ruta citada inexistente] {rel(path, root)} -> '{target}'"
            )


def check_bracket_tags(path: Path, text: str, root: Path, problems: list, label: str = None):
    """Analiza cada LÍNEA de cada bloque de código con una pila de profundidad,
    en vez de comparar el total de '[' y ']' del bloque entero. El chequeo
    agregado anterior podía ocultar un tag individual mal formado si otro tag
    distinto compensaba el conteo global (ej. una línea con ']' de más y otra
    con '[' de más sumaban 0 de diferencia y no se detectaban).

    Asume la convención real del proyecto: un tag `[Verse]`/`[Chorus: nota]`
    abre y cierra en la misma línea, sin anidar corchetes dentro de otros
    corchetes. Por eso reporta tres tipos de problema por línea:
      - ']' sin '[' previo en esa misma línea (cierre huérfano).
      - '[' que no cierra antes de terminar la línea (apertura huérfana).
      - profundidad > 1 dentro de una línea (corchetes anidados, no usados
        en la sintaxis de tags de este proyecto — casi siempre un error de
        tecleo, ej. `[Verse [ad-lib]]`).
    """
    where = label or rel(path, root)
    for block in CODEBLOCK_RE.findall(text):
        for line_no, line in enumerate(block.splitlines(), start=1):
            depth = 0
            max_depth = 0
            for ch in line:
                if ch == "[":
                    depth += 1
                    max_depth = max(max_depth, depth)
                elif ch == "]":
                    if depth == 0:
                        snippet = line.strip()[:60] or "(vacío)"
                        problems.append(
                            f"[tag mal formado] {where} línea de bloque {line_no}: "
                            f"']' sin '[' previo en la misma línea: {snippet!r}"
                        )
                    else:
                        depth -= 1
            if depth > 0:
                snippet = line.strip()[:60] or "(vacío)"
                problems.append(
                    f"[tag mal formado] {where} línea de bloque {line_no}: "
                    f"{depth} '[' sin cerrar en la misma línea: {snippet!r}"
                )
            if max_depth > 1:
                snippet = line.strip()[:60] or "(vacío)"
                problems.append(
                    f"[tag anidado sospechoso] {where} línea de bloque {line_no}: "
                    f"corchetes anidados (profundidad {max_depth}), no usado en la sintaxis "
                    f"de tags del proyecto: {snippet!r}"
                )


def check_unclosed_fences(path: Path, text: str, root: Path, problems: list, label: str = None):
    """Recorre el archivo línea a línea con un estado de apertura/cierre: solo
    cuentan las líneas que SON una marca de fence (```). Así un ``` incrustado
    en medio de prosa o dentro de una celda de tabla (ej. el propio texto de
    este validador que menciona ``` tres veces en una frase) ya no puede
    generar un falso positivo — antes se contaban todas las apariciones
    literales de ``` del archivo."""
    where = label or rel(path, root)
    open_fence = False
    fence_lines = 0
    for line in text.splitlines():
        if FENCE_LINE_RE.match(line):
            open_fence = not open_fence
            fence_lines += 1
    if open_fence:
        problems.append(
            f"[fence sin cerrar] {where}: {fence_lines} línea(s) de fence ``` "
            f"(número impar, queda un bloque de código abierto)"
        )


def check_heading_style(path: Path, text: str, root: Path, problems: list, label: str = None):
    where = label or rel(path, root)
    levels = []
    for m in HEADING_RE.finditer(text):
        hashes, title = m.group(1), m.group(2)
        level = len(hashes)
        if title and title[-1] in FORBIDDEN_HEADING_ENDINGS:
            problems.append(
                f"[encabezado mal cerrado] {where}: '{hashes} {title}' termina en '{title[-1]}'"
            )
        levels.append(level)
    # Salto de nivel (ej. # -> ### sin pasar por ##), solo dentro del mismo bloque.
    for prev, cur in zip(levels, levels[1:]):
        if cur - prev > 1:
            problems.append(
                f"[salto de nivel de encabezado] {where}: de H{prev} a H{cur} sin niveles intermedios"
            )


def check_yaml_frontmatter_shape(path: Path, text: str, root: Path, problems: list, label: str = None):
    """Chequeo estructural ligero de YAML (sin depender de PyYAML)."""
    where = label or rel(path, root)
    m = FRONTMATTER_RE.match(text)
    if not m:
        return
    block = m.group(1)
    for i, line in enumerate(block.splitlines(), start=1):
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            continue  # continuación/indentada, no se valida a fondo
        if not re.match(r"^[A-Za-z_][A-Za-z0-9_-]*:\s?.*$", line):
            problems.append(
                f"[YAML sospechoso] {where} línea {i} de frontmatter no parece `clave: valor`: {line.strip()!r}"
            )
            continue
        # Comillas sin cerrar en la misma línea (heurística: conteo de " impar).
        if line.count('"') % 2 != 0:
            problems.append(
                f"[YAML sospechoso] {where} línea {i}: comillas dobles sin cerrar: {line.strip()!r}"
            )


def is_instructional(path: Path, root: Path) -> bool:
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        parts = path.parts
    if len(parts) == 1:
        return True  # archivo suelto en la raíz (CLAUDE.md, MEMORY.md, PROYECTOS.md...)
    return parts[0] in INSTRUCTIONAL_TOP_DIRS


def check_frontmatter_and_truncation(path: Path, text: str, root: Path, problems: list):
    m = FRONTMATTER_RE.match(text)
    if text.lstrip().startswith("---") and not m:
        problems.append(f"[frontmatter incompleto] {rel(path, root)} no cierra el bloque `---`")
    elif m:
        block = m.group(1)
        missing = [k for k in REQUIRED_FRONTMATTER_KEYS if f"{k}:" not in block]
        if missing:
            problems.append(
                f"[frontmatter incompleto] {rel(path, root)} falta(n) clave(s): {', '.join(missing)}"
            )

    if not is_instructional(path, root):
        return

    stripped = text.rstrip()
    if not stripped:
        return
    last_line = stripped.splitlines()[-1].strip()
    # Se saltan filas de tabla (`|`) y citas/blockquote (`>`): las letras y
    # ejemplos citados terminan legítimamente sin puntuación (ej. un verso de
    # cierre en `composicion/letra.md`), no son prosa de instrucción truncada.
    if not last_line or last_line == "---" or last_line.startswith(("|", ">")):
        return
    last_char = last_line[-1]
    if last_char not in SENTENCE_END_CHARS and len(last_line.split()) >= 4:
        problems.append(
            f"[posible archivo truncado] {rel(path, root)} termina en: '...{last_line[-60:]}'"
        )


def check_skeleton_prose_leak(inner: str, where: str, problems: list):
    """Detecta líneas de instrucción (explicación en prosa dirigida a quien
    rellena la plantilla) coladas dentro de un esqueleto copiable, en vez de
    dejar solo marcadores deterministas. Una viñeta `- ...` se considera
    placeholder legítimo si contiene `<...>`, `[...]` o backticks; si no
    contiene ninguno de esos marcadores y tiene pinta de frase completa (6+
    palabras, cierra en '.' o ':'), se marca como sospechosa. Es heurística:
    revisa cada aviso, no la trates como verdad absoluta."""
    for line_no, line in enumerate(inner.splitlines(), start=1):
        m = PROSE_LEAK_RE.match(line.strip())
        if not m:
            continue
        content = m.group(1)
        if any(marker in content for marker in PROSE_PLACEHOLDER_MARKERS):
            continue
        words = content.split()
        if len(words) >= 6 and content.rstrip().endswith((".", ":")):
            problems.append(
                f"[instrucción colada en esqueleto] {where} línea {line_no}: "
                f"parece prosa explicativa, no un marcador determinista: {content[:60]!r}"
            )


def strip_fence(block: str) -> str:
    """Quita la línea de apertura ```lenguaje y el cierre ``` de un bloque."""
    inner = re.sub(r"\A```[a-zA-Z0-9_-]*\n", "", block)
    inner = re.sub(r"\n```\Z", "", inner)
    return inner


def check_plantilla_skeletons(path: Path, text: str, root: Path, problems: list):
    """Las plantillas generativas deben producir esqueletos compatibles con las
    convenciones reales: se extrae cada bloque de código y se le aplican los
    mismos chequeos de forma (YAML, fences, encabezados) que a un documento real.
    Además, toda plantilla generativa debe traer al menos un esqueleto."""
    if not path.name.startswith("plantilla_"):
        return
    blocks = CODEBLOCK_RE.findall(text)
    if not blocks:
        problems.append(
            f"[plantilla sin esqueleto] {rel(path, root)}: una plantilla generativa "
            f"debe traer al menos un bloque de código copiable"
        )
        return
    for idx, block in enumerate(blocks, start=1):
        inner = strip_fence(block)
        label = f"{rel(path, root)} (esqueleto #{idx})"
        check_yaml_frontmatter_shape(path, inner, root, problems, label=label)
        check_heading_style(path, inner, root, problems, label=label)
        check_bracket_tags(path, inner, root, problems, label=label)
        if path.name not in PROSE_RICH_PLANTILLAS:
            check_skeleton_prose_leak(inner, label, problems)


def check_plantilla_type(path: Path, text: str, root: Path, problems: list):
    """chuletas/plantilla_*.md deben declarar `type: plantilla` en su propio frontmatter."""
    if not (path.parent.name == "chuletas" and path.name.startswith("plantilla_")):
        return
    m = FRONTMATTER_RE.match(text)
    if not m:
        return  # ya lo marca check_frontmatter_and_truncation
    type_match = re.search(r"^type:\s*(.+)$", m.group(1), re.MULTILINE)
    if not type_match or type_match.group(1).strip() != "plantilla":
        problems.append(
            f"[type incorrecto] {rel(path, root)}: chuletas/plantilla_*.md debe declarar `type: plantilla`"
        )


def check_single_h1(path: Path, text: str, root: Path, problems: list):
    """Dentro de chuletas/, exige exactamente un H1 fuera de bloques de código."""
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        parts = path.parts
    if not parts or parts[0] != "chuletas":
        return
    text_wo_code = CODEBLOCK_RE.sub("", text)
    h1_count = len(re.findall(r"^#\s+\S", text_wo_code, re.MULTILINE))
    if h1_count != 1:
        problems.append(
            f"[H1 múltiple o ausente] {rel(path, root)}: {h1_count} encabezados H1 fuera de "
            f"bloques de código (se espera exactamente 1)"
        )


def check_proyecto_skeleton_sections(path: Path, text: str, root: Path, problems: list):
    """El esqueleto de plantilla_proyecto.md debe traer frontmatter propio y
    las secciones canónicas de un proyecto."""
    if path.name != "plantilla_proyecto.md":
        return
    blocks = CODEBLOCK_RE.findall(text)
    if not blocks:
        return  # ya lo marca check_plantilla_skeletons ([plantilla sin esqueleto])
    inner = strip_fence(blocks[0])
    if not inner.lstrip().startswith("---"):
        problems.append(
            f"[esqueleto de proyecto sin frontmatter] {rel(path, root)}: el bloque copiable no empieza con YAML `---`"
        )
    missing_sections = [s for s in REQUIRED_PROYECTO_SECTIONS if f"## {s}" not in inner]
    if missing_sections:
        problems.append(
            f"[esqueleto de proyecto incompleto] {rel(path, root)}: falta(n) sección(es): {', '.join(missing_sections)}"
        )


def check_document_identity(path: Path, text: str, root: Path, problems: list):
    """Punto 14 — identidad documental:
      - `name` (frontmatter) coincide con el nombre del archivo cuando corresponde
        (con el nombre de la CARPETA en los `SKILL.md`, cuyo archivo se llama
        siempre igual).
      - el único `# H1` (fuera de bloques de código) coincide con `name`.
    Se exceptúan los nombres canónicos de raíz (README.md, CLAUDE.md, MEMORY.md,
    PROYECTOS.md), cuyo H1 es un título humano y cuyo `name` no tiene por qué
    coincidir con el archivo."""
    if path.name in CANONICAL_FILENAMES:
        return
    name = frontmatter_name(text)
    if not name:
        return  # sin `name` no hay identidad que comparar (lo cubre el punto 4)

    if path.name == "SKILL.md":
        expected = path.parent.name
        origen = "el nombre de la carpeta"
    else:
        expected = path.name[:-3]
        origen = "el nombre de archivo"
    if name != expected:
        problems.append(
            f"[identidad: name != archivo] {rel(path, root)}: name={name!r} no coincide con {origen} ({expected!r})"
        )

    text_wo_code = CODEBLOCK_RE.sub("", text)
    h1s = H1_RE.findall(text_wo_code)
    if len(h1s) == 1 and h1s[0] != name:
        problems.append(
            f"[identidad: H1 != name] {rel(path, root)}: H1={h1s[0]!r} no coincide con name={name!r}"
        )


def collect_maps_consumido(root: Path) -> dict:
    """Pre-escanea `.claude/rules/*.md` y devuelve {nombre_mapa: texto de la
    línea `Consumido por`}. Se usa para el chequeo bidireccional (punto 15).
    Se lee directo del disco (no del recorrido filtrado) para que esté siempre
    disponible aunque se excluyan otras carpetas."""
    maps = {}
    rules_dir = root / ".claude" / "rules"
    if not rules_dir.is_dir():
        return maps
    for mp in rules_dir.glob("*.md"):
        try:
            t = mp.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        m = CONSUMIDO_RE.search(t)
        maps[mp.stem] = m.group(1) if m else ""
    return maps


def check_map_skill_bidirectional(path: Path, text: str, root: Path, maps: dict, problems: list):
    """Punto 15 — toda skill que cita un mapa `.claude/rules/<x>.md` debe
    aparecer en la línea `Consumido por` de ese mapa. `produccion` no lleva su
    nombre en cada mapa que consume por fase, pero sí aparece como
    `produccion (Fase N)`, así que el chequeo por substring ``skill``
    lo detecta igual."""
    if path.name != "SKILL.md":
        return
    skill = path.parent.name
    cited = sorted(set(RULES_CITED_RE.findall(text)))
    for c in cited:
        if c not in maps:
            problems.append(
                f"[mapa citado inexistente] {rel(path, root)}: cita `.claude/rules/{c}.md`, que no existe"
            )
            continue
        consumido = maps[c]
        if f"`{skill}`" not in consumido:
            problems.append(
                f"[bidireccionalidad rota] {rel(path, root)}: la skill `{skill}` cita "
                f"`.claude/rules/{c}.md` pero no figura en su `Consumido por`: {consumido.strip()[:80]!r}"
            )


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def main():
    parser = argparse.ArgumentParser(description="Validador automático del proyecto Paul McChatney")
    parser.add_argument("ruta", nargs="?", default=".", help="Raíz del proyecto a validar")
    parser.add_argument("--incluir-personales", action="store_true",
                         help="Incluye _hojas_sucias, _temp, _produccion, _prompts_antiguos, _docs")
    parser.add_argument("--excluir", nargs="+", default=[], metavar="DIR",
                         help="Nombres de carpeta adicionales a saltar (ej. --excluir proyectos)")
    args = parser.parse_args()

    root = Path(args.ruta).resolve()
    extra_excluded = set(args.excluir)
    problems = []

    maps = collect_maps_consumido(root)

    for path in iter_markdown_files(root, args.incluir_personales, extra_excluded):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            problems.append(f"[error de lectura] {rel(path, root)} no es UTF-8 válido")
            continue

        check_links(path, text, root, problems)
        check_backtick_paths(path, text, root, problems)
        check_bracket_tags(path, text, root, problems)
        check_frontmatter_and_truncation(path, text, root, problems)
        check_yaml_frontmatter_shape(path, text, root, problems)
        check_unclosed_fences(path, text, root, problems)
        check_heading_style(path, text, root, problems)
        check_plantilla_skeletons(path, text, root, problems)
        check_plantilla_type(path, text, root, problems)
        check_single_h1(path, text, root, problems)
        check_proyecto_skeleton_sections(path, text, root, problems)
        check_document_identity(path, text, root, problems)
        check_map_skill_bidirectional(path, text, root, maps, problems)

    if not problems:
        print("✅ Sin problemas detectados.")
        return 0

    print(f"⚠️  {len(problems)} problema(s) detectado(s):\n")
    for p in problems:
        print(f"- {p}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
