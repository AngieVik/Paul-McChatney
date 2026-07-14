# Validador automático — plan y estado

*Mejora del audit de reglas: preparar un chequeo automático que detecte lo que antes solo se encontraba a mano (contradicciones de política, archivos truncados, rutas rotas).*

**Comando:** `python automatizaciones/validar_proyecto/validar_proyecto.py .` (ejecutar desde la raíz del proyecto).

---

## 1 · Qué comprueba

| #   | Chequeo                                                   | Cómo                                                                                                                                                                                                                                                                                                          | Alcance                                                                                                                                                      |
| --- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Enlaces relativos rotos                                   | Resuelve enlaces Markdown y `href` contra disco                                                                                                                                                                                                                                                               | Todo `.md` del proyecto                                                                                                                                      |
| 2   | Rutas citadas entre backticks (`archivo.md`) inexistentes | Resuelve la ruta relativa al archivo y a la raíz                                                                                                                                                                                                                                                              | Todo `.md`, ignora rutas-plantilla (`<slug>`, `NN`, `ejemplo`, `texto`)                                                                                      |
| 3   | Corchetes `[Tag]` mal formados                            | Analiza cada línea de cada bloque de código con una pila de profundidad (no el total agregado del bloque): detecta un `]` sin `[` previo en esa misma línea, un `[` que no cierra antes de terminar la línea, y corchetes anidados (profundidad > 1), que no forman parte de la sintaxis de tags del proyecto | Línea por línea, dentro de bloques de código de todo `.md`                                                                                                   |
| 4   | Frontmatter incompleto / archivo truncado                 | Verifica que el bloque `---` cierre y contenga `name`/`type`/`description`; heurística de "última línea sin puntuación"                                                                                                                                                                                       | Frontmatter: todo `.md`. Truncamiento: solo carpetas de instrucción (`.claude/`, `system_prompt/`, `composicion/`, `chuletas/`, archivos sueltos en la raíz) |
| 5   | YAML de frontmatter sospechoso                            | Cada línea no indentada debe parecer `clave: valor`; detecta comillas dobles sin cerrar en la misma línea                                                                                                                                                                                                     | Frontmatter de todo `.md` (sin dependencias externas, sin PyYAML)                                                                                            |
| 6   | Fences ``` ``` ``` sin cerrar                             | Cuenta marcadores de triple backtick; si el total es impar, hay un fence abierto que nunca cierra                                                                                                                                                                                                             | Todo `.md`                                                                                                                                                   |
| 7   | Encabezados mal cerrados o con salto de nivel             | Un encabezado no debe terminar en `.`, `:` ni `;`; no debe saltar de `#` a `###` sin pasar por `##`                                                                                                                                                                                                           | Todo `.md`                                                                                                                                                   |
| 8   | Las plantillas generan documentos compatibles             | Extrae cada bloque de código de `chuletas/plantilla_*.md` y le aplica los chequeos 5-7 como si fuera un archivo real                                                                                                                                                                                          | Solo `chuletas/plantilla_*.md`                                                                                                                               |

**Por qué el punto 4 no cubre todo el árbol:** `proyectos/` (letras), `chupilista/` (listas de tags) y `fonetizar/`/`jerga/` (ejemplos fonéticos) terminan legítimamente sin punto — aplicar la heurística ahí generaba ruido casi puro. Se limita a las carpetas donde la prosa siempre debe cerrar en frase completa.

**Por qué el punto 5 no usa PyYAML:** el script no tiene dependencias — debe correr con un `python`/`python3` estándar recién instalado en Windows, sin `pip install` de por medio. El chequeo es estructural (forma de línea, comillas), no un parseo YAML completo.

## 2 · Script

- **Ubicación:** `automatizaciones/validar_proyecto/validar_proyecto.py`.
- **Uso:** `python automatizaciones/validar_proyecto/validar_proyecto.py .` desde la raíz del proyecto (o pasando la ruta como argumento; usa `python3` en vez de `python` si tu sistema lo requiere así). Añade `--incluir-personales` para no ignorar `_hojas_sucias`, `_temp`, `_produccion`, `_prompts_antiguos`, `_docs`.
- **Salida:** lista de avisos por consola + código de salida `1` si hay algo que revisar (`0` si está limpio) — pensado para poder engancharse a un hook de pre-commit o ejecutarse manualmente antes de un `aprobar`/`cerrar` grande.
- **Dependencias:** ninguna, solo `python3` estándar.

## 3 · Calibración realizada

## 4 · Naturaleza de la herramienta

Es una **heurística de apoyo, no un gate estricto**. Cada aviso debe revisarse antes de actuar — el punto 4 en particular puede marcar prosa que termina así a propósito (ejemplos, citas). Úsalo para encontrar candidatos, no para autocorregir en bucle.

## 5 · Pendiente / posibles siguientes pasos

- Detectar automáticamente si un `.claude/rules/*.md` no declara "Consumido por" (patrón visto en auditorías anteriores).
- Comprobar bidireccionalidad mapa↔skill (si `X/SKILL.md` cita `.claude/rules/X.md`, que ese mapa mencione a `X` en su "Consumido por"). Propuesto explícitamente en la ronda 3; el usuario decidió posponerlo a otra ronda en vez de implementarlo ahora — sigue siendo la mejora pendiente más útil identificada hasta la fecha.
- Integrarlo como hook de pre-commit si el repo pasa a tener commits frecuentes.
