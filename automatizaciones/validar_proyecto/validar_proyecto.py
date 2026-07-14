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
     Además: frontmatter AUSENTE en rutas que lo exigen (ver punto 17).
  5. YAML de frontmatter inválido. Si PyYAML está disponible se hace un parseo
     real (`yaml.safe_load`); en cualquier caso se aplica una heurística
     estructural sin dependencias que detecta: línea que no parece
     `clave: valor`, falta de espacio tras los dos puntos (`clave:valor`),
     valor sin comillas que contiene `:` (YAML lo tomaría como mapa anidado),
     comilla sin cerrar y puntuación situada FUERA de la comilla de cierre
     (`"texto".`).
  6. Fences ``` sin cerrar: recorre el archivo línea a línea con un estado de
     apertura/cierre. Solo cuentan las líneas que SON una marca de fence, con
     como máximo 3 espacios de sangría (CommonMark: 4+ espacios ya es un bloque
     indentado, no un fence); los ``` incrustados en prosa o dentro de una
     celda de tabla no descuadran el conteo.
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
  15. Bidireccionalidad mapa<->skill, en las DOS direcciones:
      - skill -> mapa: toda skill que cita `.claude/rules/<x>.md` aparece en la
        línea `Consumido por` de ese mapa (y ese mapa existe).
      - mapa -> skill: toda skill declarada como dueña en el `Consumido por` de
        un mapa (anotada `(skill)` o con el mismo nombre que el mapa) existe y
        cita ese mapa. `produccion` es una excepción declarada (orquestadora:
        delega por fase y no cita mapas); los consumidores conceptuales o
        manuales — tokens que no son una skill real — se omiten.
  16. Bytes nulos (`\\x00`) y caracteres de control: ningún `.md` debe contener
      NUL ni otros caracteres de control (se permiten solo `\\t`, `\\n`, `\\r`).
  17. Frontmatter exigido por ruta: los `.md` de carpetas de identidad
      (`.claude/rules/`, `.claude/skills/*/SKILL.md`, `composicion/`, `jerga/`,
      `fonetizar/`, `system_prompt/` y `chuletas/plantilla_*.md`) deben traer
      frontmatter YAML. `proyectos/` queda fuera a propósito (histórico sin
      frontmatter universal).

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

Nota sobre PyYAML (punto 5): el parseo real solo se usa si `import yaml` está
disponible; el script NO lo exige. Sin PyYAML, la heurística estructural cubre
los mismos errores de forma. Así el validador corre con un `python`/`python3`
recién instalado en Windows sin `pip install` de por medio.

Salida: reporte por consola agrupado por tipo de problema + código de salida
1 si se encontró algún problema (útil para hooks/CI), 0 si todo está limpio.
"""

import argparse
import os
import re
import sys
from pathlib import Path

try:
    import yaml  # opcional: si está, se hace un parseo YAML real (punto 5)
except ImportError:  # el script debe correr sin dependencias externas
    yaml = None

IGNORE_DIRS = {".git", "node_modules", ".vscode"}
PERSONAL_DIRS = {"_hojas_sucias", "_temp", "_produccion", "_prompts_antiguos", "_docs"}

# Carpetas donde la prosa es "de instrucción" y debería cerrar en frase completa.
INSTRUCTIONAL_TOP_DIRS = {".claude", "system_prompt", "composicion", "chuletas"}

# Nombres canónicos de raíz: su H1 es un título humano, no el slug, y su `name`
# no tiene por qué coincidir con el nombre de archivo. Se exceptúan del chequeo
# de identidad documental (punto 14).
CANONICAL_FILENAMES = {"README.md", "CLAUDE.md", "MEMORY.md", "PROYECTOS.md"}

# Skills que pueden figurar como dueñas en un `Consumido por` sin citar el mapa
# de vuelta (punto 15, dirección mapa->skill): `produccion` orquesta por fase.
GLOBAL_CONSUMER_EXCEPTIONS = {"produccion"}

MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HTML_HREF_RE = re.compile(r'href="([^"]+)"')
BACKTICK_PATH_RE = re.compile(r"`([\w./\\-]+\.(?:md|py|json|yaml|yml))`")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
CODEBLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
# Una LÍNEA que es una marca de fence (apertura o cierre), admitiendo COMO
# MÁXIMO 3 espacios de sangría: en CommonMark, 4+ espacios ya es un bloque
# indentado y NO abre/cierra un fence, así que un ``` con 4 espacios de sangría
# no debe contar como marca de fence (se renderiza literal). Se usa para el
# estado de apertura/cierre del punto 6.
FENCE_LINE_RE = re.compile(r"^ {0,3}```")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$", re.MULTILINE)
H1_RE = re.compile(r"^#\s+(\S.*?)\s*$", re.MULTILINE)
NAME_RE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
RULES_CITED_RE = re.compile(r"\.claude/rules/([\w-]+)\.md")
CONSUMIDO_RE = re.compile(r"Consumido por:\**\s*(.+)")
# Token dueño en un `Consumido por`: `skill` (skill)  — o el homónimo del mapa.
SKILL_OWNER_RE = re.compile(r"`([\w-]+)`\s*\(skill\)")
# Caracteres de control prohibidos (se permiten \t=09, \n=0a, \r=0d).
CONTROL_CHARS_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")

REQUIRED_FRONTMATTER_KEYS = ("name", "type", "description")
KEY_LINE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(.*)$")

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


def rel_parts(path: Path, root: Path):
    try:
        return path.relative_to(root).parts
    except ValueError:
        return path.parts


def frontmatter_name(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    nm = NAME_RE.search(m.group(1))
    return nm.group(1).strip() if nm else None


def requires_frontmatter(path: Path, root: Path) -> bool:
    """Rutas de identidad que EXIGEN frontmatter YAML (punto 17). `proyectos/`
    queda fuera a propósito: el catálogo histórico no lo trae de forma
    universal y exigirlo inundaría el reporte."""
    parts = rel_parts(path, root)
    if not parts:
        return False
    name = path.name
    top = parts[0]
    if name == "SKILL.md" and top == ".claude" and len(parts) >= 2 and parts[1] == "skills":
        return True
    if top == ".claude" and len(parts) >= 2 and parts[1] == "rules":
        return True
    if top in {"composicion", "jerga", "fonetizar", "system_prompt"}:
        return True
    if top == "chuletas" and name.startswith("plantilla_"):
        return True
    return False


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


def check_control_chars(path: Path, text: str, root: Path, problems: list):
    """Punto 16 — bytes nulos y caracteres de control. Un NUL (`\\x00`) suele ser
    padding corrupto al final del archivo; otros controles rompen el render y
    delatan un guardado defectuoso."""
    hits = list(CONTROL_CHARS_RE.finditer(text))
    if not hits:
        return
    codes = sorted({f"0x{ord(h.group()):02x}" for h in hits})
    first = hits[0].start()
    problems.append(
        f"[byte de control] {rel(path, root)}: {len(hits)} carácter(es) de control "
        f"{codes} (primero en offset {first}); revisa NUL/padding o encoding"
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
    cuentan las líneas que SON una marca de fence (```) con hasta 3 espacios de
    sangría. Así un ``` incrustado en medio de prosa o dentro de una celda de
    tabla ya no puede generar un falso positivo, y un ``` con 4+ espacios de
    sangría (que Markdown renderiza literal, NO como fence) tampoco se cuenta
    como fence."""
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
    """Chequeo de YAML de frontmatter (punto 5).

    Si PyYAML está disponible, se hace un parseo real (`yaml.safe_load`) que
    captura errores estructurales que una heurística pasaría por alto. En
    cualquier caso se aplica una heurística sin dependencias que detecta los
    patrones concretos que rompen el YAML, con un mensaje accionable por línea:
      - línea que no parece `clave: valor`;
      - falta de espacio tras los dos puntos (`clave:valor`);
      - valor sin comillas que contiene `:` (YAML lo tomaría como mapa anidado);
      - comilla sin cerrar;
      - puntuación situada FUERA de la comilla de cierre (`"texto".`).
    """
    where = label or rel(path, root)
    m = FRONTMATTER_RE.match(text)
    if not m:
        return
    block = m.group(1)

    # 1) Parseo YAML real, si hay PyYAML.
    if yaml is not None:
        try:
            data = yaml.safe_load(block)
            if not isinstance(data, dict):
                problems.append(
                    f"[YAML inválido] {where}: el frontmatter no es un mapa `clave: valor`"
                )
        except yaml.YAMLError as e:  # pragma: no cover - depende de PyYAML
            first = str(e).splitlines()[0] if str(e) else "error de parseo"
            problems.append(f"[YAML inválido] {where}: {first}")

    # 2) Heurística estructural (siempre, también sin PyYAML).
    for i, line in enumerate(block.splitlines(), start=1):
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            continue  # continuación/indentada, no se valida a fondo
        if line.lstrip().startswith("#"):
            continue  # comentario YAML
        mm = KEY_LINE_RE.match(line)
        if not mm:
            problems.append(
                f"[YAML sospechoso] {where} línea {i} de frontmatter no parece `clave: valor`: {line.strip()!r}"
            )
            continue
        rest = mm.group(2)
        if rest and not rest.startswith(" "):
            problems.append(
                f"[YAML sospechoso] {where} línea {i}: falta un espacio tras ':' ({line.strip()!r})"
            )
            continue
        val = rest.strip()
        if not val:
            continue
        if val[0] in "\"'":
            q = val[0]
            if val.count(q) < 2:
                problems.append(
                    f"[YAML sospechoso] {where} línea {i}: comilla {q} sin cerrar: {line.strip()!r}"
                )
            else:
                closing = val.rfind(q)
                if val[closing + 1:].strip():
                    problems.append(
                        f"[YAML sospechoso] {where} línea {i}: puntuación fuera de las comillas de cierre: {line.strip()!r}"
                    )
        else:
            if ": " in val or val.endswith(":"):
                problems.append(
                    f"[YAML sospechoso] {where} línea {i}: valor sin comillas contiene ':' (entrecomíllalo): {line.strip()!r}"
                )


def is_instructional(path: Path, root: Path) -> bool:
    parts = rel_parts(path, root)
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
    elif requires_frontmatter(path, root):
        problems.append(
            f"[frontmatter ausente] {rel(path, root)}: esta ruta exige frontmatter YAML "
            f"(name/type/description)"
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
    parts = rel_parts(path, root)
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
        (con el nombre de la CARPETA en los `SKILL.md`).
      - el único `# H1` (fuera de bloques de código) coincide con `name`.
    Se exceptúan los nombres canónicos de raíz (README.md, CLAUDE.md, MEMORY.md,
    PROYECTOS.md), cuyo H1 es un título humano."""
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
    línea `Consumido por`}. Se lee directo del disco para que esté siempre
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
    """Punto 15, dirección skill -> mapa: toda skill que cita un mapa
    `.claude/rules/<x>.md` debe aparecer en la línea `Consumido por` de ese
    mapa."""
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


def check_map_owner_reciprocity(root: Path, maps: dict, problems: list):
    """Punto 15, dirección mapa -> skill: recorre el `Consumido por` de cada
    mapa y, por cada skill DUEÑA declarada (anotada `(skill)` o con el mismo
    nombre que el mapa), comprueba que esa skill existe y cita el mapa de
    vuelta. Los consumidores conceptuales/manuales (tokens que no son una skill
    real) se omiten; `produccion` es excepción declarada."""
    skills_dir = root / ".claude" / "skills"
    for map_name, consumido in maps.items():
        annotated = set(SKILL_OWNER_RE.findall(consumido))
        candidates = set(annotated)
        if (skills_dir / map_name / "SKILL.md").exists():
            candidates.add(map_name)  # el homónimo también es dueño natural
        for owner in sorted(candidates):
            if owner in GLOBAL_CONSUMER_EXCEPTIONS:
                continue
            skill_file = skills_dir / owner / "SKILL.md"
            if not skill_file.exists():
                if owner in annotated:
                    problems.append(
                        f"[consumidor (skill) inexistente] .claude/rules/{map_name}.md declara "
                        f"`{owner}` (skill), pero .claude/skills/{owner}/SKILL.md no existe"
                    )
                continue
            try:
                stext = skill_file.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            if f".claude/rules/{map_name}.md" not in stext:
                problems.append(
                    f"[bidireccionalidad incompleta mapa->skill] .claude/rules/{map_name}.md "
                    f"lista a `{owner}` como skill dueña, pero {owner}/SKILL.md no cita "
                    f"`.claude/rules/{map_name}.md`"
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

        check_control_chars(path, text, root, problems)
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

    # Dirección mapa -> skill (punto 15): se hace una sola vez sobre los mapas.
    check_map_owner_reciprocity(root, maps, problems)

    if not problems:
        print("✅ Sin problemas detectados.")
        return 0

    print(f"⚠️  {len(problems)} problema(s) detectado(s):\n")
    for p in problems:
        print(f"- {p}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
