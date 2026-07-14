# Validador automático — plan y estado

*Mejora del audit de reglas: preparar un chequeo automático que detecte lo que antes solo se encontraba a mano (contradicciones de política, archivos truncados, rutas rotas).*

**Comando:** `python automatizaciones/validar_proyecto/validar_proyecto.py .` (ejecutar desde la raíz del proyecto).

---

## 1 · Qué comprueba

| #   | Chequeo                                                   | Cómo                                                                                                                    | Alcance                                                                                                                                                      |
| --- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Enlaces relativos rotos                                   | Resuelve enlaces Markdown y `href` contra disco                                                                         | Todo `.md` del proyecto                                                                                                                                      |
| 2   | Rutas citadas entre backticks (`archivo.md`) inexistentes | Resuelve la ruta relativa al archivo y a la raíz                                                                        | Todo `.md`, ignora rutas-plantilla (`<slug>`, `NN`, `ejemplo`, `texto`)                                                                                      |
| 3   | Corchetes `[Tag]` desbalanceados                          | Cuenta `[` vs `]` dentro de cada bloque de código                                                                       | Bloques de código de todo `.md`                                                                                                                              |
| 4   | Frontmatter incompleto / archivo truncado                 | Verifica que el bloque `---` cierre y contenga `name`/`type`/`description`; heurística de "última línea sin puntuación" | Frontmatter: todo `.md`. Truncamiento: solo carpetas de instrucción (`.claude/`, `system_prompt/`, `composicion/`, `chuletas/`, archivos sueltos en la raíz) |
| 5   | YAML de frontmatter sospechoso                            | Cada línea no indentada debe parecer `clave: valor`; detecta comillas dobles sin cerrar en la misma línea               | Frontmatter de todo `.md` (sin dependencias externas, sin PyYAML)                                                                                            |
| 6   | Fences ``` ``` ``` sin cerrar                              | Cuenta marcadores de triple backtick; si el total es impar, hay un fence abierto que nunca cierra                       | Todo `.md`                                                                                                                                                    |
| 7   | Encabezados mal cerrados o con salto de nivel              | Un encabezado no debe terminar en `.`, `:` ni `;`; no debe saltar de `#` a `###` sin pasar por `##`                      | Todo `.md`                                                                                                                                                    |
| 8   | Las plantillas generan documentos compatibles              | Extrae cada bloque de código de `chuletas/plantilla_*.md` y le aplica los chequeos 5-7 como si fuera un archivo real     | Solo `chuletas/plantilla_*.md`                                                                                                                                |

**Por qué el punto 4 no cubre todo el árbol:** `proyectos/` (letras), `chupilista/` (listas de tags) y `fonetizar/`/`jerga/` (ejemplos fonéticos) terminan legítimamente sin punto — aplicar la heurística ahí generaba ruido casi puro. Se limita a las carpetas donde la prosa siempre debe cerrar en frase completa.

**Por qué el punto 5 no usa PyYAML:** el script no tiene dependencias — debe correr con un `python`/`python3` estándar recién instalado en Windows, sin `pip install` de por medio. El chequeo es estructural (forma de línea, comillas), no un parseo YAML completo.

## 2 · Script

- **Ubicación:** `automatizaciones/validar_proyecto/validar_proyecto.py`.
- **Uso:** `python automatizaciones/validar_proyecto/validar_proyecto.py .` desde la raíz del proyecto (o pasando la ruta como argumento; usa `python3` en vez de `python` si tu sistema lo requiere así). Añade `--incluir-personales` para no ignorar `_hojas_sucias`, `_temp`, `_produccion`, `_prompts_antiguos`, `_docs`.
- **Salida:** lista de avisos por consola + código de salida `1` si hay algo que revisar (`0` si está limpio) — pensado para poder engancharse a un hook de pre-commit o ejecutarse manualmente antes de un `aprobar`/`cerrar` grande.
- **Dependencias:** ninguna, solo `python3` estándar.

## 3 · Calibración realizada

Se ejecutó contra todo el proyecto real antes de entregarlo. Primera pasada: 62 avisos, casi todos ruido (letras de canciones y ejemplos fonéticos "sin punto final", rutas-plantilla tipo `_hojas_sucias/slug.md`). Se ajustó:

- Restringir el chequeo de truncamiento a carpetas de instrucción.
- Excluir rutas-plantilla del chequeo de rutas citadas.
- Añadir cierres de énfasis Markdown (`*`) a los caracteres de "frase completa".

Segunda pasada: 3 avisos. Dos eran falsos positivos legítimos (un ejemplo de rima en `composicion/letra.md` y una fila de plantilla en `chuletas/plantilla_hoja_sucia.md`, ambos terminan sin punto a propósito). El tercero era real: `.claude/skills/fusionar/SKILL.md` terminaba en una frase sin punto final — corregido en esta misma sesión.

**Ronda 2 (checks 5-8):** al añadir YAML sospechoso, fences sin cerrar, encabezados mal cerrados/con salto de nivel y validación de esqueletos de plantilla, apareció una fuente de ruido nueva: el sistema de archivos tarda unos segundos en sincronizar los archivos recién escritos hacia el entorno donde corre el propio validador, así que una ejecución inmediatamente después de editar puede reportar "fence sin cerrar" o "truncado" sobre contenido que en realidad ya está completo — vuelve a ejecutar el script si acabas de guardar cambios y ves un aviso raro en un archivo que tú mismo tocaste. Descontando ese ruido, los únicos hallazgos reales de la ronda 2 caen en `proyectos/` (una `\`\`\`yaml` sin cerrar en `el_gato_de_carabas.md`, un salto H1→H3 en `fuga_lunar_philosophy.md`): son obras cerradas y no se tocan sin que el usuario lo pida explícitamente.

## 4 · Naturaleza de la herramienta

Es una **heurística de apoyo, no un gate estricto**. Cada aviso debe revisarse antes de actuar — el punto 4 en particular puede marcar prosa que termina así a propósito (ejemplos, citas). Úsalo para encontrar candidatos, no para autocorregir en bucle.

## 5 · Pendiente / posibles siguientes pasos

- Detectar automáticamente si un `.claude/rules/*.md` no declara "Consumido por" (patrón visto en auditorías anteriores).
- Comprobar bidireccionalidad mapa↔skill (si `X/SKILL.md` cita `.claude/rules/X.md`, que ese mapa mencione a `X` en su "Consumido por").
- Integrarlo como hook de pre-commit si el repo pasa a tener commits frecuentes.
