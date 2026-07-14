# Validador automático — plan y estado

*Mejora del audit de reglas: preparar un chequeo automático que detecte lo que antes solo se encontraba a mano (contradicciones de política, archivos truncados, rutas rotas, identidad documental y bidireccionalidad mapa↔skill).*

**Comando:** `python automatizaciones/validar_proyecto/validar_proyecto.py .` (ejecutar desde la raíz del proyecto).

---

## 1 · Qué comprueba

| #   | Chequeo                                          | Cómo                                                                                                                                            | Alcance                                                                                                       |
| --- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 1   | Enlaces relativos rotos                          | Resuelve enlaces Markdown y `href` contra disco                                                                                                | Todo `.md` del proyecto                                                                                       |
| 2   | Rutas citadas entre backticks inexistentes       | Resuelve la ruta relativa al archivo y a la raíz                                                                                               | Todo `.md`, ignora rutas-plantilla (`<slug>`, `NN`, `ejemplo`, `texto`)                                      |
| 3   | Corchetes `[Tag]` mal formados                   | Analiza cada línea de cada bloque de código con una pila de profundidad (no el total agregado): `]` sin `[` previo, `[` sin cerrar, anidados   | Línea por línea, dentro de bloques de código de todo `.md`                                                   |
| 4   | Frontmatter incompleto / archivo truncado        | Verifica que el bloque `---` cierre y contenga `name`/`type`/`description`; heurística de "última línea sin puntuación" (salta tablas y citas) | Frontmatter: todo `.md`. Truncamiento: solo carpetas de instrucción (`.claude/`, `system_prompt/`, `composicion/`, `chuletas/`, raíz) |
| 5   | YAML de frontmatter sospechoso                   | Cada línea no indentada debe parecer `clave: valor`; detecta comillas dobles sin cerrar en la misma línea                                      | Frontmatter de todo `.md` (sin PyYAML)                                                                       |
| 6   | Fences de código sin cerrar                      | Recorre el archivo línea a línea con estado de apertura/cierre; solo cuentan las líneas que SON marca de fence, no los triple-backtick incrustados en prosa o tablas | Todo `.md`                                                                                                   |
| 7   | Encabezados mal cerrados o con salto de nivel    | Un encabezado no debe terminar en `.`, `:` ni `;`; no debe saltar de `#` a `###` sin pasar por `##`                                            | Todo `.md`                                                                                                   |
| 8   | Las plantillas generan documentos compatibles    | Extrae cada bloque de código de `chuletas/plantilla_*.md` y le aplica los chequeos 5-7 como si fuera un archivo real                           | Solo `chuletas/plantilla_*.md`                                                                               |
| 9   | Las plantillas declaran `type: plantilla`        | Comprueba que el frontmatter de cada `plantilla_*.md` declare `type: plantilla`                                                                | Solo `chuletas/plantilla_*.md`                                                                               |
| 10  | Un solo H1 en `chuletas/`                         | Cuenta los `# H1` fuera de bloques de código: debe haber exactamente uno                                                                       | Solo `chuletas/`                                                                                             |
| 11  | Esqueleto de proyecto completo                   | El primer bloque de `plantilla_proyecto.md` empieza con `---` y trae las secciones canónicas (Titulo Original, Generated, Master, style_box, exclude_box, lyrics_box) | Solo `plantilla_proyecto.md`                                                                                 |
| 12  | Prosa colada en el esqueleto                     | Marca viñetas que parecen instrucción en prosa (6+ palabras, cierran en `.`/`:`) sin marcador determinista; exime las plantillas de guía ricas en prosa (fonetizar, jerga) | Esqueletos de `chuletas/plantilla_*.md`                                                                      |
| 13  | La plantilla generativa trae esqueleto           | Toda `plantilla_*.md` debe contener al menos un bloque de código copiable; si no, no genera nada                                               | Solo `chuletas/plantilla_*.md`                                                                               |
| 14  | Identidad documental (H1 = name = archivo)       | El `# H1` coincide con `name`, y `name` con el nombre de archivo (o de la carpeta en los `SKILL.md`); exime nombres canónicos de raíz          | Todo `.md` con `name`, salvo README/CLAUDE/MEMORY/PROYECTOS                                                  |
| 15  | Bidireccionalidad mapa↔skill                     | Toda skill que cita `.claude/rules/<x>.md` figura en el `Consumido por` de ese mapa; y ese mapa existe                                         | `SKILL.md` de cada skill contra `.claude/rules/`                                                             |

**Por qué el punto 4 no cubre todo el árbol:** `proyectos/` (letras), `chupilista/` (listas de tags) y `fonetizar/`/`jerga/` (ejemplos fonéticos) terminan legítimamente sin punto — aplicar la heurística ahí generaba ruido casi puro. Se limita a las carpetas donde la prosa siempre debe cerrar en frase completa, y dentro de ellas salta filas de tabla (`|`) y citas/blockquote (`>`).

**Por qué el punto 5 no usa PyYAML:** el script no tiene dependencias — debe correr con un `python`/`python3` estándar recién instalado en Windows, sin `pip install` de por medio. El chequeo es estructural (forma de línea, comillas), no un parseo YAML completo.

**Cómo el punto 6 evita falsos positivos sobre sí mismo:** cuenta solo líneas que son marca de fence real (empiezan por triple-backtick, admitiendo sangría), con un estado de apertura/cierre. Un triple-backtick citado en medio de una frase o de una celda de tabla ya no descuadra el conteo — antes se contaba cada aparición literal y el propio manual podía autoinculparse.

**Alcance del punto 15:** cubre las tres piezas de la bidireccionalidad de arquitectura — skill que cita un mapa aparece en su `Consumido por`; todo mapa citado existe; y, por los puntos 1-2, todo enlace o ruta que un mapa declara apunta a un archivo real.

## 2 · Script

- **Ubicación:** `automatizaciones/validar_proyecto/validar_proyecto.py`.
- **Uso:** `python automatizaciones/validar_proyecto/validar_proyecto.py .` desde la raíz del proyecto (o pasando la ruta como argumento; usa `python3` en vez de `python` si tu sistema lo requiere así).
- **`--incluir-personales`:** no ignora `_hojas_sucias`, `_temp`, `_produccion`, `_prompts_antiguos`, `_docs`.
- **`--excluir DIR [DIR ...]`:** salta además esas carpetas por nombre. `python validar_proyecto.py . --excluir proyectos` revisa solo el núcleo actual sin que las obras históricas metan ruido ni bloqueen el resultado.
- **Salida:** lista de avisos por consola + código de salida `1` si hay algo que revisar (`0` si está limpio) — pensado para engancharse a un hook de pre-commit o ejecutarse antes de un `aprobar`/`cerrar` grande.
- **Dependencias:** ninguna, solo `python3` estándar.

## 3 · Calibración realizada

- *Si esta sección está vacía, es porque el usuario ya revisó y resolvió (o descartó) los avisos de la última pasada: no queda calibración pendiente registrada.*

## 4 · Naturaleza de la herramienta

Es una **heurística de apoyo, no un gate estricto**. Cada aviso debe revisarse antes de actuar — el punto 4 en particular puede marcar prosa que termina así a propósito (ejemplos, citas). Úsalo para encontrar candidatos, no para autocorregir en bucle.

## 5 · Pendiente / posibles siguientes pasos

- Detectar automáticamente si un `.claude/rules/*.md` no declara `Consumido por` (patrón visto en auditorías anteriores); el punto 15 ya usa esa línea, pero no avisa aún si falta por completo.
- Comprobar también la dirección manual→skill: que cada `composicion/*.md` declare correctamente sus skills consumidoras (sección «Referencias» de `plantilla_composicion.md`).
- Integrarlo como hook de pre-commit si el repo pasa a tener commits frecuentes.
