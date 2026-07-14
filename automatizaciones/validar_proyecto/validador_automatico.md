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
| 5   | YAML de frontmatter inválido                     | Parseo real con `yaml.safe_load` si PyYAML está disponible; y siempre una heurística sin dependencias: línea que no parece `clave: valor`, falta de espacio tras `:` (`clave:valor`), valor sin comillas que contiene `:`, comilla sin cerrar y puntuación FUERA de la comilla de cierre (`"texto".`) | Frontmatter de todo `.md`                                                                                    |
| 6   | Fences de código sin cerrar                      | Recorre el archivo línea a línea con estado de apertura/cierre; solo cuentan las líneas que SON marca de fence (hasta 3 espacios de sangría — 4+ ya es bloque indentado, no fence), no los triple-backtick incrustados en prosa o tablas | Todo `.md`                                                                                                   |
| 7   | Encabezados mal cerrados o con salto de nivel    | Un encabezado no debe terminar en `.`, `:` ni `;`; no debe saltar de `#` a `###` sin pasar por `##`                                            | Todo `.md`                                                                                                   |
| 8   | Las plantillas generan documentos compatibles    | Extrae cada bloque de código de `chuletas/plantilla_*.md` y le aplica los chequeos 5-7 como si fuera un archivo real                           | Solo `chuletas/plantilla_*.md`                                                                               |
| 9   | Las plantillas declaran `type: plantilla`        | Comprueba que el frontmatter de cada `plantilla_*.md` declare `type: plantilla`                                                                | Solo `chuletas/plantilla_*.md`                                                                               |
| 10  | Un solo H1 en `chuletas/`                         | Cuenta los `# H1` fuera de bloques de código: debe haber exactamente uno                                                                       | Solo `chuletas/`                                                                                             |
| 11  | Esqueleto de proyecto completo                   | El primer bloque de `plantilla_proyecto.md` empieza con `---` y trae las secciones canónicas (Titulo Original, Generated, Master, style_box, exclude_box, lyrics_box) | Solo `plantilla_proyecto.md`                                                                                 |
| 12  | Prosa colada en el esqueleto                     | Marca viñetas que parecen instrucción en prosa (6+ palabras, cierran en `.`/`:`) sin marcador determinista; exime las plantillas de guía ricas en prosa (fonetizar, jerga) | Esqueletos de `chuletas/plantilla_*.md`                                                                      |
| 13  | La plantilla generativa trae esqueleto           | Toda `plantilla_*.md` debe contener al menos un bloque de código copiable; si no, no genera nada                                               | Solo `chuletas/plantilla_*.md`                                                                               |
| 14  | Identidad documental (H1 = name = archivo)       | El `# H1` coincide con `name`, y `name` con el nombre de archivo (o de la carpeta en los `SKILL.md`); exime nombres canónicos de raíz          | Todo `.md` con `name`, salvo README/CLAUDE/MEMORY/PROYECTOS                                                  |
| 15  | Bidireccionalidad mapa↔skill (2 direcciones)     | skill→mapa: toda skill que cita `.claude/rules/<x>.md` figura en el `Consumido por` de ese mapa (y ese mapa existe). mapa→skill: toda skill dueña declarada en un `Consumido por` (anotada `(skill)` o con el nombre del mapa) existe y cita ese mapa; `produccion` es excepción y los consumidores conceptuales se omiten | `SKILL.md` de cada skill y `Consumido por` de cada `.claude/rules/*.md`                                       |
| 16  | Bytes nulos y caracteres de control              | Ningún `.md` debe contener `\x00` ni otros caracteres de control (se permiten solo `\t`, `\n`, `\r`)                                           | Todo `.md`                                                                                                   |
| 17  | Frontmatter exigido por ruta                     | Los `.md` de carpetas de identidad (`.claude/rules/`, `.claude/skills/*/SKILL.md`, `composicion/`, `jerga/`, `fonetizar/`, `system_prompt/`, `chuletas/plantilla_*.md`) deben traer frontmatter; `proyectos/` queda fuera a propósito | Rutas de identidad (no `proyectos/`)                                                                          |

**Por qué el punto 4 no cubre todo el árbol:** `proyectos/` (letras), `chupilista/` (listas de tags) y `fonetizar/`/`jerga/` (ejemplos fonéticos) terminan legítimamente sin punto — aplicar la heurística ahí generaba ruido casi puro. Se limita a las carpetas donde la prosa siempre debe cerrar en frase completa, y dentro de ellas salta filas de tabla (`|`) y citas/blockquote (`>`).

**Por qué el punto 5 no depende de PyYAML:** el script no exige dependencias — debe correr con un `python`/`python3` estándar recién instalado en Windows, sin `pip install`. Si PyYAML está disponible, se usa para un parseo real (`yaml.safe_load`) que captura errores que una heurística pasaría por alto; si no lo está, la heurística estructural sin dependencias cubre los mismos patrones de error (falta de espacio tras `:`, valor sin comillas con `:`, comilla sin cerrar, puntuación fuera de la comilla). Ambas rutas detectan los mismos fallos de forma.

**Cómo el punto 6 evita falsos positivos sobre sí mismo:** cuenta solo líneas que son marca de fence real (empiezan por triple-backtick con como máximo 3 espacios de sangría — 4+ ya es bloque indentado en CommonMark, no fence), con un estado de apertura/cierre. Un triple-backtick citado en medio de una frase o de una celda de tabla ya no descuadra el conteo — antes se contaba cada aparición literal y el propio manual podía autoinculparse.

**Alcance del punto 15:** verifica la bidireccionalidad en ambos sentidos. skill→mapa: toda skill que cita un mapa aparece en su `Consumido por` y ese mapa existe. mapa→skill: recorre el `Consumido por` de cada mapa y comprueba que cada skill DUEÑA declarada (anotada `(skill)` o con el nombre del mapa) existe y cita el mapa de vuelta; `produccion` es excepción declarada (orquesta por fase) y los consumidores conceptuales o manuales — tokens que no son una skill real — se omiten.

## 2 · Script

- **Ubicación:** `automatizaciones/validar_proyecto/validar_proyecto.py`.
- **Uso:** `python automatizaciones/validar_proyecto/validar_proyecto.py .` desde la raíz del proyecto (o pasando la ruta como argumento; usa `python3` en vez de `python` si tu sistema lo requiere así).
- **`--incluir-personales`:** no ignora `_hojas_sucias`, `_temp`, `_produccion`, `_prompts_antiguos`, `_docs`.
- **`--excluir DIR [DIR ...]`:** salta además esas carpetas por nombre. `python validar_proyecto.py . --excluir proyectos` revisa solo el núcleo actual sin que las obras históricas metan ruido ni bloqueen el resultado.
- **Salida:** lista de avisos por consola + código de salida `1` si hay algo que revisar (`0` si está limpio) — pensado para engancharse a un hook de pre-commit o ejecutarse antes de un `aprobar`/`cerrar` grande.
- **Dependencias:** ninguna obligatoria, solo `python3` estándar. Si PyYAML está instalado, el punto 5 lo aprovecha para un parseo YAML real (opcional, con degradación limpia si falta).
- **Pruebas:** `python automatizaciones/validar_proyecto/test_validar_proyecto.py` ejecuta la batería de casos (YAML válido/ inválido, bytes nulos, fences con 0/3/4 espacios, mapas y skills desincronizados, plantillas sin frontmatter). Sin dependencias; devuelve `1` si algún caso falla. Ejecútalo tras tocar el validador para no reintroducir falsos positivos ni puntos ciegos.

## 3 · Calibración realizada

- *Si esta sección está vacía, es porque el usuario ya revisó y resolvió (o descartó) los avisos de la última pasada: no queda calibración pendiente registrada.*

## 4 · Naturaleza de la herramienta

Es una **heurística de apoyo, no un gate estricto**. Cada aviso debe revisarse antes de actuar — el punto 4 en particular puede marcar prosa que termina así a propósito (ejemplos, citas). Úsalo para encontrar candidatos, no para autocorregir en bucle.

## 5 · Pendiente / posibles siguientes pasos

- Detectar automáticamente si un `.claude/rules/*.md` no declara `Consumido por` (patrón visto en auditorías anteriores); el punto 15 ya usa esa línea, pero no avisa aún si falta por completo.
- Comprobar también la dirección manual→skill: que cada `composicion/*.md` declare correctamente sus skills consumidoras (sección «Referencias» de `plantilla_composicion.md`).
- Integrarlo como hook de pre-commit si el repo pasa a tener commits frecuentes.

*Hecho en la última ampliación: parseo YAML real opcional + heurística reforzada (valores sin comillas con `:`, falta de espacio tras `:`, puntuación fuera de comillas), detección de bytes nulos y caracteres de control, frontmatter exigido por ruta, fences limitados a 3 espacios de sangría, bidireccionalidad mapa→skill (además de skill→mapa) y batería de pruebas automáticas.*
