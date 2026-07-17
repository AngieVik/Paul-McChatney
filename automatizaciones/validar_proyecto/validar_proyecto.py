#!/usr/bin/env python3
"""
validar_proyecto.py — Validador automático para el proyecto Paul McChatney.

Comprueba, sobre el árbol .md del proyecto:
  1. Enlaces relativos rotos (sintaxis Markdown `[texto](ruta)` y `<a href="ruta">`).
  2. Rutas mencionadas entre backticks (`archivo.md`) que no existen en disco.
     Las rutas con `/` o `\\` se resuelven contra la carpeta del archivo y la
     raíz. Los nombres SUELTOS (sin ruta) también se resuelven: contra la
     carpeta del archivo y la raíz; si aparecen en ambas se reporta ruta
     ambigua, si no aparecen en ninguna se reporta como inexistente. Los
     nombres canónicos del repo (README.md, CLAUDE.md, MEMORY.md, PROYECTOS.md,
     SKILL.md) se aceptan si el archivo existe en cualquier ubicación conocida,
     porque se citan por su nombre canónico a propósito. Se ignoran las
     rutas-plantilla (marcadores `<...>` o segmentos EXACTOS como `slug`, `NN`,
     `ejemplo`, `texto`, `archivo`): la detección es por segmento exacto, no por
     subcadena, de modo que `texto` ya no confunde a `contexto.md`.
  3. Corchetes de tags `[Tag]` mal formados dentro de bloques de código: analiza
     cada línea de cada bloque por separado (pila de profundidad), no el total
     de `[` y `]` del bloque entero — así un cierre sin apertura ya no puede
     quedar oculto porque otro tag distinto compensó el conteo global.
  4. Archivos truncados: frontmatter incompleto (falta cierre `---`, faltan
     claves `name`/`type`/`description`) o el archivo de INSTRUCCIONES
     (skills, rules, composicion, system_prompt, raíz) termina a mitad de frase.
     Además: frontmatter AUSENTE en rutas que lo exigen (ver punto 15).
  5. YAML de frontmatter inválido. Si PyYAML está disponible se hace un parseo
     real (`yaml.safe_load`); en cualquier caso se aplica una heurística
     estructural sin dependencias que detecta: línea que no parece
     `clave: valor`, falta de espacio tras los dos puntos (`clave:valor`),
     valor sin comillas que contiene `:` (YAML lo tomaría como mapa anidado),
     comilla sin cerrar y puntuación situada FUERA de la comilla de cierre
     (`"texto".`).
  6. Fences ``` sin cerrar: se usa un ÚNICO parser línea a línea
     (`scan_code_blocks`) que detecta, extrae y elimina los bloques cercados.
     Reconoce fences de 3+ backticks o 3+ tildes con hasta 3 espacios de
     sangría (CommonMark: 4+ espacios ya es un bloque indentado, no un fence);
     la fence de cierre usa el mismo carácter y al menos tantas marcas que la
     de apertura. Los ``` incrustados en prosa o dentro de una celda de tabla
     no descuadran el conteo. Ese mismo parser alimenta la extracción de
     bloques (puntos 3, 7, 8, 10, 13), de modo que hay una sola definición de
     "qué es un bloque cercado".
  7. Encabezados mal cerrados: terminan en `.`, `:` o `;` (prohibido por
     `chuletas/plantilla_estilo.md` §2) o saltan de nivel (`#` -> `###`). Se
     ignoran los encabezados incrustados dentro de bloques de código cercados:
     en las plantillas esos encabezados ya se validan como esqueletos (punto 8),
     así que analizarlos también aquí producía avisos duplicados o falsos saltos
     de nivel.
  8. Las plantillas generativas (`chuletas/plantilla_*.md`) generan un
     esqueleto compatible: se extrae cada bloque de código de la plantilla y
     se le aplican los chequeos de forma de un documento real —YAML (5),
     encabezados (7), FENCES SIN CERRAR (6) y corchetes de tags (3, analizados
     directamente sobre las líneas del esqueleto)—. `check_bracket_tags` se
     conserva como comprobación independiente en la pasada general de cada
     archivo.
  9. Todo `chuletas/plantilla_*.md` declara `type: plantilla` en su propio
     frontmatter (comparado sin comillas: `"plantilla"` == `plantilla`).
  10. El esqueleto de `plantilla_proyecto.md` empieza con frontmatter YAML y
      trae las secciones canónicas de un proyecto (Titulo Original, Generated,
      Master, style_box, exclude_box, lyrics_box).
  11. Dentro de un esqueleto copiable, ninguna línea de viñeta parece prosa
      explicativa colada (instrucción para quien rellena la plantilla) en vez
      de un marcador determinista (`<...>`, `[...]` o backticks). Las plantillas
      de guía ricas en prosa (fonetizar, jerga), cuyo esqueleto es un documento
      con secciones de prosa fija, se eximen de este punto.
  12. Toda plantilla generativa (`chuletas/plantilla_*.md`) contiene al menos
      un esqueleto (bloque de código copiable); una plantilla sin esqueleto no
      genera nada.
  13. Identidad documental: cada documento con `name` tiene EXACTAMENTE un
      `# H1` fuera de bloques de código, ese H1 coincide con `name`, y `name`
      coincide con el nombre del archivo cuando corresponde (con el nombre de la
      carpeta en los `SKILL.md`). El `name`/`type` se leen sin comillas
      exteriores. En los nombres canónicos de raíz (README.md, CLAUDE.md,
      MEMORY.md, PROYECTOS.md) se exime SOLO la igualdad `name == archivo` (su
      H1 es un título humano, no el slug), pero se sigue exigiendo exactamente
      un H1: así un H1 ausente o duplicado en esos archivos tampoco pasa
      inadvertido.
  14. Bytes nulos (`\\x00`) y caracteres de control: ningún `.md` debe contener
      NUL ni otros caracteres de control (se permiten solo `\\t`, `\\n`, `\\r`).
  15. Frontmatter exigido por ruta: los `.md` de carpetas de identidad
      (`.claude/rules/`, `.claude/skills/*/SKILL.md`, `composicion/`, `jerga/`,
      `fonetizar/`, `system_prompt/` y `chuletas/plantilla_*.md`) deben traer
      frontmatter YAML. `proyectos/` queda fuera a propósito (histórico sin
      frontmatter universal); su chequeo específico es el punto 19.
  16. Longitud de `description`: en los archivos de identidad el `description`
      no supera los 250 caracteres (regla de `chuletas/plantilla_estilo.md` §7:
      el YAML identifica, no explica; nada largo dentro del YAML).
  17. Indexación única: cada archivo de una biblioteca (`jerga/`, `fonetizar/`,
      `composicion/`, `chupilista/`, `chuletas/`) aparece EXACTAMENTE una vez en
      su mapa correspondiente (`.claude/rules/<x>.md`, o `plantillas.md` para
      `chuletas/`). Detecta huérfanos (0 apariciones) y duplicados (2+).
  18. Biblioteca `chupilista/`: las tags canónicas están escritas como líneas
      normales `[tag]` (no dentro de bloques cercados), así que se analizan
      directamente. Se detectan como ERROR: corchetes incompletos o contenido
      fuera de la tag, caracteres invisibles/tabulaciones y duplicados exactos
      dentro del archivo. Se detectan como ADVERTENCIA (no rompen el código de
      salida): espacios sobrantes y posibles duplicados por diferencias solo de
      mayúsculas, guiones o grafía.
  19. Obras del catálogo (`proyectos/<slug>/<slug>.md`): las seis secciones
      núcleo (`Titulo Original`, `Generated`, `Master`, `style_box`,
      `exclude_box`, `lyrics_box`) deben EXISTIR siempre. Las tres cajas
      (`style_box`, `exclude_box`, `lyrics_box`) deben tener CONTENIDO solo si
      la obra declara la versión de canon vigente (`canon:` en su frontmatter)
      y no está en la lista de excepciones históricas. Las obras sin marca de
      canon (histórico) quedan exentas del chequeo de contenido: el canon puede
      evolucionar y las obras antiguas pueden no cumplirlo (exclude_box vacío,
      style_box en prosa, etc.) sin que eso inunde el reporte.

Dependencias unidireccionales: cada archivo declara únicamente los recursos que
necesita consultar (sus rutas directas). El validador comprueba que esas rutas
existan, sean válidas y estén indexadas; NO mantiene ni verifica ninguna
relación inversa de "consumidores" (quién usa a quién). Un recurso no necesita
saber quién lo utiliza.

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

Salida: reporte por consola agrupado por tipo de problema (prefijo entre
corchetes) + código de salida 1 si se encontró algún problema (útil para
hooks/CI), 0 si todo está limpio. Las advertencias se listan aparte y no
alteran el código de salida.
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
# no tiene por qué coincidir con el nombre de archivo. Se exime SOLO esa
# igualdad `name == archivo`; el H1 se sigue exigiendo (punto 13).
CANONICAL_FILENAMES = {"README.md", "CLAUDE.md", "MEMORY.md", "PROYECTOS.md"}

# Nombres canónicos que pueden citarse SUELTOS (sin ruta) porque nombran
# archivos fijos y conocidos del repo (punto 2). Incluye SKILL.md, que existe
# en cada carpeta de skill.
CANONICAL_BARE_NAMES = {"README.md", "CLAUDE.md", "MEMORY.md", "PROYECTOS.md", "SKILL.md"}

# Longitud máxima del `description` en archivos de identidad (punto 16).
MAX_DESCRIPTION_LEN = 250

# Bibliotecas indexadas y su mapa (punto 17). El mapa referencia cada archivo
# como `carpeta/archivo.md`; `chuletas/` se indexa desde `plantillas.md`.
LIBRARY_MAPS = {
    "jerga": ".claude/rules/jerga.md",
    "fonetizar": ".claude/rules/fonetizar.md",
    "composicion": ".claude/rules/composicion.md",
    "chupilista": ".claude/rules/chupilista.md",
    "chuletas": ".claude/rules/plantillas.md",
}

MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HTML_HREF_RE = re.compile(r'href="([^"]+)"')
BACKTICK_PATH_RE = re.compile(r"`([\w./\\-]+\.(?:md|py|json|yaml|yml))`")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
# Una LÍNEA que ES una marca de fence (apertura o cierre): hasta 3 espacios de
# sangría + 3 o más backticks o 3 o más tildes, seguida del resto de la línea
# (info string en la apertura; vacío en el cierre). Es la ÚNICA definición de
# fence; la usa `scan_code_blocks` para detectar/extraer/eliminar bloques.
FENCE_RE = re.compile(r"^ {0,3}(?P<ticks>`{3,}|~{3,})(?P<rest>.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$", re.MULTILINE)
H1_RE = re.compile(r"^#\s+(\S.*?)\s*$", re.MULTILINE)
KEY_VALUE_RE = re.compile(r"^{key}:\s*(.+)$", re.MULTILINE)
# Caracteres de control prohibidos (se permiten \t=09, \n=0a, \r=0d).
CONTROL_CHARS_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
# Caracteres invisibles que no deben colarse dentro de una tag de chupilista.
INVISIBLE_CHARS_RE = re.compile("[\t\u00a0\u200b\u200c\u200d\u2060\ufeff]")

REQUIRED_FRONTMATTER_KEYS = ("name", "type", "description")
KEY_LINE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(.*)$")

# Secciones canónicas que debe traer una obra del catálogo y el esqueleto de
# plantilla_proyecto.md (puntos 10 y 19).
REQUIRED_PROYECTO_SECTIONS = ("Titulo Original", "Generated", "Master", "style_box", "exclude_box", "lyrics_box")
# Cajas cuyo CONTENIDO se exige en las obras que declaran el canon vigente.
PROYECTO_BOX_SECTIONS = ("style_box", "exclude_box", "lyrics_box")
# Slugs de obras eximidas EXPLÍCITAMENTE del chequeo de contenido (punto 19),
# como escape adicional a la marca de versión `canon`. Vacío por defecto: las
# obras históricas ya quedan exentas por no declarar `canon`.
HISTORICAL_PROYECTO_EXCEPTIONS = set()

# Línea de viñeta dentro de un esqueleto copiable: se compara contra estos
# marcadores para decidir si es un placeholder determinista o prosa colada.
PROSE_LEAK_RE = re.compile(r"^-\s+(.+)$")
PROSE_PLACEHOLDER_MARKERS = ("<", "[", "`")

# Terminaciones que sugieren que la frase SÍ está completa (incluye cierres
# de énfasis Markdown '*'/'_' porque son habituales al final de una nota).
SENTENCE_END_CHARS = set(".!?:`\"'”»)*_")

# Segmentos EXACTOS que delatan una ruta-plantilla (placeholder), no un archivo
# real. La comparación es por segmento (separadores `/ \\ . -`), no por
# subcadena: así `texto` ya no coincide dentro de `contexto.md`.
PLACEHOLDER_SEGMENTS = {"slug", "nn", "ejemplo", "texto", "archivo"}

# Encabezados que NO deben cerrar con puntuación (regla de plantilla_estilo.md §2).
FORBIDDEN_HEADING_ENDINGS = (".", ":", ";")

# Plantillas de GUÍA ricas en prosa: su esqueleto es un documento estructurado
# con secciones de prosa fija que aparecen en cada archivo generado (no un
# molde puramente estructural). Se eximen del chequeo de "prosa colada"
# (punto 11), que solo tiene sentido en las plantillas de estructura pura.
PROSE_RICH_PLANTILLAS = {"plantilla_fonetizar.md", "plantilla_jerga.md"}


def strip_outer_quotes(value: str) -> str:
    """Retira UN par de comillas exteriores (simples o dobles) si envuelven todo
    el valor. Así `"style_box"` -> `style_box` y `'plantilla'` -> `plantilla`,
    tanto con PyYAML como sin él."""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1].strip()
    return value


def frontmatter_value(text: str, key: str):
    """Lee el valor de una clave de nivel superior del frontmatter, ya venga
    entrecomillado o no. Con PyYAML se parsea de verdad; sin él se cae a una
    lectura por regex retirando las comillas exteriores. Es la función común que
    usan `name`, `type` y `description`, de modo que las comillas nunca se
    comparan como parte del valor."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    block = m.group(1)
    if yaml is not None:
        try:
            data = yaml.safe_load(block)
            if isinstance(data, dict) and key in data and data[key] is not None:
                return str(data[key]).strip()
        except yaml.YAMLError:
            pass  # YAML roto: lo reporta check_yaml_frontmatter_shape; caemos a regex
    km = re.search(KEY_VALUE_RE.pattern.format(key=re.escape(key)), block, re.MULTILINE)
    if km:
        return strip_outer_quotes(km.group(1))
    return None


def frontmatter_name(text: str):
    return frontmatter_value(text, "name")


def top_level_yaml_keys(block: str) -> set:
    """Claves de NIVEL SUPERIOR de un bloque de frontmatter. Con PyYAML se
    parsean de verdad; sin él (o si el parseo falla) se cae a una heurística que
    ignora comentarios (`# ...`) y líneas indentadas (claves anidadas). Así un
    comentario como `# name:` ya no cuenta como si la clave real existiera, que
    era el falso positivo que dejaba pasar la comprobación por subcadena."""
    if yaml is not None:
        try:
            data = yaml.safe_load(block)
            if isinstance(data, dict):
                return {str(k) for k in data.keys()}
        except yaml.YAMLError:
            pass  # YAML roto: lo reporta check_yaml_frontmatter_shape; caemos a la heurística
    keys = set()
    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            continue  # indentada => clave anidada, no de nivel superior
        if line.lstrip().startswith("#"):
            continue  # comentario YAML, no una clave
        m = KEY_LINE_RE.match(line)
        if m:
            keys.add(m.group(1))
    return keys


def is_placeholder_path(target: str) -> bool:
    """True si la ruta es un marcador de plantilla, no un archivo real. Se
    considera placeholder si:
      - contiene un marcador entre ángulos (`<...>`), o
      - alguno de sus SEGMENTOS exactos (separados por `/ \\ . _ -`) es un token
        de plantilla (`slug`, `NN`, `ejemplo`, `texto`, `archivo`).
    La comparación por segmento exacto evita el falso positivo de la subcadena:
    `texto` ya no coincide con `contexto.md` (`contexto` no es igual a `texto`)."""
    if "<" in target or ">" in target:
        return True
    segments = re.split(r"[\\/._\-]", target.lower())
    return any(seg in PLACEHOLDER_SEGMENTS for seg in segments)


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


def requires_frontmatter(path: Path, root: Path) -> bool:
    """Rutas de identidad que EXIGEN frontmatter YAML (punto 15). `proyectos/`
    queda fuera a propósito: el catálogo histórico no lo trae de forma
    universal y exigirlo inundaría el reporte (su chequeo propio es el 19)."""
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


def scan_code_blocks(text: str):
    """ÚNICO parser línea a línea de bloques cercados (CommonMark simplificado).

    Reconoce fences de 3+ backticks o 3+ tildes con hasta 3 espacios de sangría.
    Una fence de apertura de backticks no puede llevar backticks en su info
    string (regla CommonMark). La fence de cierre usa el mismo carácter y al
    menos tantas marcas que la de apertura, y no lleva texto tras las marcas.

    Devuelve una tupla `(blocks, unclosed, stripped)`:
      - `blocks`: lista con el CONTENIDO INTERNO de cada bloque (sin las líneas
        de fence), en orden de aparición; un bloque sin cerrar se incluye igual.
      - `unclosed`: True si quedó una fence abierta al llegar al final.
      - `stripped`: el texto SIN las líneas de los bloques cercados (fences
        incluidos), conservando el resto de líneas — sustituye a la vieja
        eliminación por regex `CODEBLOCK_RE.sub("", ...)`.
    """
    blocks = []
    stripped_lines = []
    open_marker = None  # (carácter, longitud) de la fence de apertura
    buf = []
    for line in text.splitlines():
        m = FENCE_RE.match(line)
        if open_marker is None:
            if m:
                char = m.group("ticks")[0]
                length = len(m.group("ticks"))
                if char == "`" and "`" in m.group("rest"):
                    # backtick fence con backticks en el info string => no es
                    # una apertura válida: se trata como línea normal.
                    stripped_lines.append(line)
                    continue
                open_marker = (char, length)
                buf = []
            else:
                stripped_lines.append(line)
        else:
            if m:
                char = m.group("ticks")[0]
                length = len(m.group("ticks"))
                if (char == open_marker[0] and length >= open_marker[1]
                        and m.group("rest").strip() == ""):
                    blocks.append("\n".join(buf))
                    open_marker = None
                    continue
            buf.append(line)
    unclosed = open_marker is not None
    if unclosed:
        blocks.append("\n".join(buf))
    return blocks, unclosed, "\n".join(stripped_lines)


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


def _bare_name_exists_anywhere(root: Path, name: str) -> bool:
    """¿Existe algún archivo con este nombre en el árbol? Solo se usa para
    aceptar los nombres canónicos citados sueltos (SKILL.md, MEMORY.md...)."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        if name in filenames:
            return True
    return False


def check_backtick_paths(path: Path, text: str, root: Path, problems: list):
    """Punto 2. Rutas y nombres citados entre backticks.

    - Con `/` o `\\`: se resuelven contra la carpeta del archivo y la raíz.
    - Nombre SUELTO (sin ruta): también se resuelve, contra la carpeta del
      archivo y la raíz. Si aparece en las dos (y son rutas distintas) se marca
      como ambiguo; si no aparece en ninguna, como inexistente. Los nombres
      canónicos del repo (SKILL.md, MEMORY.md, CLAUDE.md, README.md,
      PROYECTOS.md) se aceptan si el archivo existe en cualquier ubicación
      conocida, porque se citan por su nombre canónico a propósito.
    """
    for m in BACKTICK_PATH_RE.finditer(text):
        target = m.group(1)
        if is_placeholder_path(target):
            continue
        if "/" in target or "\\" in target:
            target_norm = target.replace("\\", "/")
            for base in (path.parent, root):
                if (base / target_norm).exists():
                    break
            else:
                problems.append(
                    f"[ruta citada inexistente] {rel(path, root)} -> '{target}'"
                )
            continue

        # Nombre suelto sin ruta.
        if target in CANONICAL_BARE_NAMES:
            if not _bare_name_exists_anywhere(root, target):
                problems.append(
                    f"[nombre canónico inexistente] {rel(path, root)} -> '{target}' no existe en el repo"
                )
            continue
        # Etiqueta de un archivo referenciado por su ruta COMPLETA en el mismo
        # archivo (tablas de índice: `calo.md` junto a `../../jerga/calo.md`).
        # Si la ruta completa está presente, el nombre suelto es solo una
        # etiqueta legible, no una referencia a resolver.
        if re.search(r"[\\/]" + re.escape(target), text):
            continue
        matches = []
        for base in (path.parent, root):
            candidate = base / target
            if candidate.exists() and candidate.resolve() not in matches:
                matches.append(candidate.resolve())
        if len(matches) > 1:
            problems.append(
                f"[ruta ambigua] {rel(path, root)} -> '{target}' existe en varias ubicaciones "
                f"({', '.join(rel(mp, root) for mp in matches)}); cita la ruta completa"
            )
        elif not matches:
            problems.append(
                f"[nombre suelto inexistente] {rel(path, root)} -> '{target}' no se resuelve "
                f"contra la carpeta del archivo ni la raíz; cita la ruta completa"
            )


def check_control_chars(path: Path, text: str, root: Path, problems: list):
    """Punto 14 — bytes nulos y caracteres de control. Un NUL (`\\x00`) suele ser
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


def check_bracket_lines(content: str, where: str, problems: list):
    """Analiza cada LÍNEA de `content` con una pila de profundidad, en vez de
    comparar el total de '[' y ']'. El chequeo agregado podía ocultar un tag
    individual mal formado si otro tag distinto compensaba el conteo global
    (ej. una línea con ']' de más y otra con '[' de más sumaban 0 y no se
    detectaban).

    Es el núcleo reutilizable: `check_bracket_tags` lo aplica a cada bloque
    cercado de un documento, y `check_plantilla_skeletons` lo aplica
    directamente sobre las líneas del esqueleto ya extraído (que casi nunca
    contiene sus propios bloques cercados internos).

    Asume la convención real del proyecto: un tag `[Verse]`/`[Chorus: nota]`
    abre y cierra en la misma línea, sin anidar corchetes dentro de otros
    corchetes. Por eso reporta tres tipos de problema por línea:
      - ']' sin '[' previo en esa misma línea (cierre huérfano).
      - '[' que no cierra antes de terminar la línea (apertura huérfana).
      - profundidad > 1 dentro de una línea (corchetes anidados, no usados
        en la sintaxis de tags de este proyecto — casi siempre un error de
        tecleo, ej. `[Verse [ad-lib]]`).
    """
    for line_no, line in enumerate(content.splitlines(), start=1):
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


def check_bracket_tags(path: Path, text: str, root: Path, problems: list, label: str = None):
    """Corchetes de tags mal formados dentro de los bloques cercados de un
    documento (punto 3). Extrae los bloques con el parser único y aplica el
    análisis por línea a cada uno. Se conserva como comprobación INDEPENDIENTE
    en la pasada general (distinta del análisis directo del esqueleto que hace
    check_plantilla_skeletons)."""
    where = label or rel(path, root)
    blocks, _unclosed, _stripped = scan_code_blocks(text)
    for block in blocks:
        check_bracket_lines(block, where, problems)


def check_chupilista_tags(path: Path, text: str, root: Path, problems: list, warnings: list):
    """Punto 18 — validación específica de la biblioteca de tags `chupilista/`.

    Las tags canónicas se escriben como líneas normales `[tag]` (no dentro de
    bloques cercados), así que se analizan directamente, línea a línea. Una
    línea se considera "línea de tag" si, tras recortar espacios, empieza por
    `[` y no es un enlace Markdown (`](`).

    ERROR (rompe el código de salida):
      - corchetes incompletos o contenido fuera de la tag (`[tag` , `[tag] x`);
      - tabulaciones o caracteres invisibles dentro de la línea;
      - duplicado exacto dentro del mismo archivo.
    ADVERTENCIA (no rompe el código de salida):
      - espacios iniciales/finales o repetidos innecesariamente;
      - posible duplicado por diferencias solo de mayúsculas, guiones o grafía.
    """
    parts = rel_parts(path, root)
    if not parts or parts[0] != "chupilista":
        return
    where = rel(path, root)
    seen_exact = {}
    seen_norm = {}
    for line_no, raw in enumerate(text.splitlines(), start=1):
        s = raw.strip()
        if not s.startswith("["):
            continue
        if "](" in s:
            continue  # enlace Markdown, no una tag
        if INVISIBLE_CHARS_RE.search(raw):
            problems.append(
                f"[chupilista carácter invisible] {where} línea {line_no}: "
                f"tabulación o carácter invisible en la tag: {s[:40]!r}"
            )
        if not re.fullmatch(r"\[[^\[\]]+\]", s):
            problems.append(
                f"[chupilista tag mal formada] {where} línea {line_no}: "
                f"corchetes incompletos o contenido fuera de la tag: {s[:40]!r}"
            )
            continue
        inner = s[1:-1]
        if raw != raw.strip() or inner != inner.strip() or "  " in inner:
            warnings.append(
                f"[chupilista espacios sobrantes] {where} línea {line_no}: "
                f"espacios iniciales, finales o repetidos: {s[:40]!r}"
            )
        if s in seen_exact:
            problems.append(
                f"[chupilista tag duplicada] {where} línea {line_no}: "
                f"{s!r} ya aparece en la línea {seen_exact[s]}"
            )
        else:
            seen_exact[s] = line_no
        norm = re.sub(r"[\s\-]+", "", inner).lower()
        if norm in seen_norm and seen_norm[norm][0] != s:
            warnings.append(
                f"[chupilista posible duplicado] {where} línea {line_no}: "
                f"{s!r} se parece a {seen_norm[norm][0]!r} (línea {seen_norm[norm][1]}) "
                f"salvo por mayúsculas, guiones o espacios"
            )
        else:
            seen_norm.setdefault(norm, (s, line_no))


def check_unclosed_fences(path: Path, text: str, root: Path, problems: list, label: str = None):
    """Punto 6 — usa el parser único `scan_code_blocks`: si queda una fence
    abierta al final del texto, se reporta. Así un ``` incrustado en prosa o en
    una celda de tabla no genera falsos positivos, y un ``` con 4+ espacios de
    sangría (que Markdown renderiza literal, NO como fence) tampoco cuenta."""
    where = label or rel(path, root)
    _blocks, unclosed, _stripped = scan_code_blocks(text)
    if unclosed:
        problems.append(
            f"[fence sin cerrar] {where}: queda un bloque de código cercado sin cerrar "
            f"(marca ``` o ~~~ sin su cierre)"
        )


def check_heading_style(path: Path, text: str, root: Path, problems: list, label: str = None):
    where = label or rel(path, root)
    # Se excluyen los bloques de código cercados: un encabezado dentro de un
    # ``` no es un encabezado real del documento. En las plantillas, además, ese
    # encabezado ya se valida como esqueleto (check_plantilla_skeletons), de modo
    # que analizarlo también aquí duplicaba avisos o inventaba saltos de nivel.
    text = scan_code_blocks(text)[2]
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
        keys = top_level_yaml_keys(block)
        missing = [k for k in REQUIRED_FRONTMATTER_KEYS if k not in keys]
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


def check_description_length(path: Path, text: str, root: Path, problems: list):
    """Punto 16 — el `description` de un archivo de identidad no supera
    MAX_DESCRIPTION_LEN caracteres. El YAML identifica, no explica."""
    if not requires_frontmatter(path, root):
        return
    desc = frontmatter_value(text, "description")
    if desc is None:
        return  # la ausencia la marca check_frontmatter_and_truncation
    if len(desc) > MAX_DESCRIPTION_LEN:
        problems.append(
            f"[description larga] {rel(path, root)}: {len(desc)} caracteres "
            f"(máximo {MAX_DESCRIPTION_LEN}); resume la description en una frase"
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


def check_plantilla_skeletons(path: Path, text: str, root: Path, problems: list):
    """Las plantillas generativas deben producir esqueletos compatibles con las
    convenciones reales: se extrae cada bloque de código (con el parser único) y
    se le aplican los mismos chequeos de forma que a un documento real —YAML,
    encabezados, FENCES SIN CERRAR y corchetes de tags—. Los corchetes se
    analizan DIRECTAMENTE sobre las líneas del esqueleto (check_bracket_lines),
    no buscando bloques cercados internos que casi nunca existen dentro del
    esqueleto ya extraído. Además, toda plantilla generativa debe traer al menos
    un esqueleto."""
    if not path.name.startswith("plantilla_"):
        return
    blocks, _unclosed, _stripped = scan_code_blocks(text)
    if not blocks:
        problems.append(
            f"[plantilla sin esqueleto] {rel(path, root)}: una plantilla generativa "
            f"debe traer al menos un bloque de código copiable"
        )
        return
    for idx, inner in enumerate(blocks, start=1):
        label = f"{rel(path, root)} (esqueleto #{idx})"
        check_yaml_frontmatter_shape(path, inner, root, problems, label=label)
        check_heading_style(path, inner, root, problems, label=label)
        check_unclosed_fences(path, inner, root, problems, label=label)
        check_bracket_lines(inner, label, problems)
        if path.name not in PROSE_RICH_PLANTILLAS:
            check_skeleton_prose_leak(inner, label, problems)


def check_plantilla_type(path: Path, text: str, root: Path, problems: list):
    """chuletas/plantilla_*.md deben declarar `type: plantilla` en su propio
    frontmatter. El valor se lee sin comillas exteriores, de modo que
    `type: "plantilla"` y `type: plantilla` son equivalentes."""
    if not (path.parent.name == "chuletas" and path.name.startswith("plantilla_")):
        return
    m = FRONTMATTER_RE.match(text)
    if not m:
        return  # ya lo marca check_frontmatter_and_truncation
    type_value = frontmatter_value(text, "type")
    if type_value != "plantilla":
        problems.append(
            f"[type incorrecto] {rel(path, root)}: chuletas/plantilla_*.md debe declarar `type: plantilla`"
        )


def check_proyecto_skeleton_sections(path: Path, text: str, root: Path, problems: list):
    """El esqueleto de plantilla_proyecto.md debe traer frontmatter propio y
    las secciones canónicas de un proyecto."""
    if path.name != "plantilla_proyecto.md":
        return
    blocks, _unclosed, _stripped = scan_code_blocks(text)
    if not blocks:
        return  # ya lo marca check_plantilla_skeletons ([plantilla sin esqueleto])
    inner = blocks[0]
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
    """Punto 13 — identidad documental:
      - `name` (frontmatter, sin comillas) coincide con el nombre del archivo
        cuando corresponde (con el nombre de la CARPETA en los `SKILL.md`).
      - hay EXACTAMENTE un `# H1` fuera de bloques de código, y coincide con
        `name`.
    En los nombres canónicos de raíz (README.md, CLAUDE.md, MEMORY.md,
    PROYECTOS.md) se exime SOLO la igualdad `name == archivo` (su H1 es un título
    humano), pero se sigue exigiendo exactamente un H1."""
    h1s = H1_RE.findall(scan_code_blocks(text)[2])

    if path.name in CANONICAL_FILENAMES:
        # Solo se exime la igualdad name==archivo; el H1 sigue siendo obligatorio.
        if len(h1s) != 1:
            problems.append(
                f"[identidad: H1 múltiple o ausente] {rel(path, root)}: {len(h1s)} encabezados H1 fuera "
                f"de bloques de código (se espera exactamente 1)"
            )
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

    if len(h1s) != 1:
        problems.append(
            f"[identidad: H1 múltiple o ausente] {rel(path, root)}: {len(h1s)} encabezados H1 fuera "
            f"de bloques de código (se espera exactamente 1)"
        )
    elif h1s[0] != name:
        problems.append(
            f"[identidad: H1 != name] {rel(path, root)}: H1={h1s[0]!r} no coincide con name={name!r}"
        )


def is_proyecto_obra(path: Path, root: Path) -> bool:
    """True si `path` es una obra del catálogo: `proyectos/<slug>/<slug>.md`."""
    parts = rel_parts(path, root)
    return (
        len(parts) == 3
        and parts[0] == "proyectos"
        and parts[2] == parts[1] + ".md"
    )


def section_body(text: str, name: str):
    """Cuerpo de la sección `## name` hasta el siguiente `## ` o el final.
    Devuelve None si la sección no existe, o el texto del cuerpo (posiblemente
    vacío) si existe."""
    m = re.search(r"^##[ \t]+" + re.escape(name) + r"[ \t]*$", text, re.MULTILINE)
    if not m:
        return None
    start = m.end()
    nxt = re.search(r"^##[ \t]+", text[start:], re.MULTILINE)
    return text[start:start + nxt.start()] if nxt else text[start:]


def check_proyecto_obra(path: Path, text: str, root: Path, problems: list):
    """Punto 19 — obras del catálogo (`proyectos/<slug>/<slug>.md`).

    - Las seis secciones núcleo deben EXISTIR siempre (guardarraíl estructural
      barato: hoy todas las obras las cumplen, así que no inunda el reporte).
    - Las tres cajas deben tener CONTENIDO solo cuando la obra declara la versión
      de canon vigente (`canon:` truthy en su frontmatter) y su slug no está en
      HISTORICAL_PROYECTO_EXCEPTIONS. Las obras sin marca de canon (histórico)
      se eximen del chequeo de contenido: el canon puede evolucionar y las obras
      antiguas pueden no cumplirlo.
    """
    if not is_proyecto_obra(path, root):
        return
    slug = path.name[:-3]

    missing = [s for s in REQUIRED_PROYECTO_SECTIONS if section_body(text, s) is None]
    if missing:
        problems.append(
            f"[obra sin sección canónica] {rel(path, root)}: falta(n) sección(es): {', '.join(missing)}"
        )

    canon = frontmatter_value(text, "canon")
    is_versioned = canon not in (None, "", "0", "false", "False", "no")
    if is_versioned and slug not in HISTORICAL_PROYECTO_EXCEPTIONS:
        for box in PROYECTO_BOX_SECTIONS:
            body = section_body(text, box)
            if body is not None and body.strip() == "":
                problems.append(
                    f"[obra con caja vacía] {rel(path, root)}: la sección '{box}' está vacía "
                    f"(la obra declara canon {canon!r}, que exige contenido en las cajas)"
                )


def check_library_indexing(root: Path, problems: list):
    """Punto 17 — cada archivo de una biblioteca aparece EXACTAMENTE una vez en
    su mapa. Se cuenta cuántas veces el texto del mapa referencia
    `carpeta/archivo.md`. 0 => huérfano; 2+ => duplicado."""
    for folder, map_rel in LIBRARY_MAPS.items():
        folder_dir = root / folder
        map_file = root / map_rel
        if not folder_dir.is_dir() or not map_file.exists():
            continue
        try:
            map_text = map_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for md in sorted(folder_dir.glob("*.md")):
            ref = f"{folder}/{md.name}"
            count = map_text.count(ref)
            if count == 0:
                problems.append(
                    f"[archivo sin indexar] {ref}: no aparece en su mapa {map_rel}"
                )
            elif count > 1:
                problems.append(
                    f"[archivo indexado por duplicado] {ref}: aparece {count} veces en {map_rel} "
                    f"(se espera exactamente 1)"
                )


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def group_by_category(items: list) -> dict:
    """Agrupa los mensajes por su prefijo entre corchetes (`[categoría] ...`)."""
    grouped = {}
    for it in items:
        m = re.match(r"\[([^\]]+)\]", it)
        key = m.group(1) if m else "(sin categoría)"
        grouped.setdefault(key, []).append(it)
    return grouped


def print_grouped(header: str, items: list):
    print(header)
    grouped = group_by_category(items)
    for category in sorted(grouped):
        print(f"\n  {category} ({len(grouped[category])}):")
        for it in grouped[category]:
            print(f"    - {it}")


def collect_problems(root: Path, include_personal: bool, extra_excluded: set):
    """Recorre el árbol y devuelve `(problems, warnings)`. Aislado de `main`
    para poder ejercitar el flujo completo desde las pruebas de integración."""
    problems = []
    warnings = []
    for path in iter_markdown_files(root, include_personal, extra_excluded):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            problems.append(f"[error de lectura] {rel(path, root)} no es UTF-8 válido")
            continue

        check_control_chars(path, text, root, problems)
        check_links(path, text, root, problems)
        check_backtick_paths(path, text, root, problems)
        check_bracket_tags(path, text, root, problems)
        check_chupilista_tags(path, text, root, problems, warnings)
        check_frontmatter_and_truncation(path, text, root, problems)
        check_description_length(path, text, root, problems)
        check_yaml_frontmatter_shape(path, text, root, problems)
        check_unclosed_fences(path, text, root, problems)
        check_heading_style(path, text, root, problems)
        check_plantilla_skeletons(path, text, root, problems)
        check_plantilla_type(path, text, root, problems)
        check_proyecto_skeleton_sections(path, text, root, problems)
        check_document_identity(path, text, root, problems)
        check_proyecto_obra(path, text, root, problems)

    check_library_indexing(root, problems)
    return problems, warnings


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

    problems, warnings = collect_problems(root, args.incluir_personales, extra_excluded)

    if not problems and not warnings:
        print("OK - Sin problemas detectados.")
        return 0

    if problems:
        print_grouped(f"{len(problems)} problema(s) detectado(s):", problems)
    if warnings:
        if problems:
            print()
        print_grouped(f"{len(warnings)} advertencia(s) (no rompen el codigo de salida):", warnings)

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
