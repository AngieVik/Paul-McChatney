---
name: CLAUDE
type: core
description: Contexto de carga, reglas de lectura y mapa principal del proyecto Paul McChatney.
---

# CLAUDE

## Reglas

- *carga automática, leer siempre*
    `@system_prompt/system_prompt.md`
    `@.claude/MEMORY.md`

---

## Mentalidad Limpia

- *Para garantizar que el modelo trabaje sobre la última versión real, crearás un archivo .md en `_hojas_sucias` (lo abre la skill `proyecto`) que sobrescribirás a medida que avance el proyecto y utilizarás como borrador.*
    - *Si el usuario pasa una versión consolidada utilizaremos esta y sobrescribiremos la anterior. Se podrán crear copias de seguridad a petición del usuario (comando `guardar`), como archivo aparte `_hojas_sucias/<slug>_NN.md`, que solo se leerán bajo demanda.*
    - *Si se trabaja sobre una sección, el trabajo irá destinado únicamente a la sección indicada, centrando el 100% del esfuerzo.*
    - *Trabaja sobre una sola obra hasta `aprobar`, `cerrar`, o `eliminar`. Mantén un único contexto activo para conservar versiones limpias y evitar cruces entre obras.*

---

## Evita carga ansiosa

- No cargues inicialmente, lee únicamente bajo demanda cuando se te solicite:
    - `_docs/`
    - `_hojas_sucias/`
    - `_produccion/`
    - `_prompts_antiguos/`
    - `_temp/`
    - `proyectos/`

---

## Referencias de Contexto

- **Fuente canónica de la política de carga:** este archivo (`CLAUDE.md`). El resto de documentos (`README`, `system_prompt`, skills y mapas) remiten aquí; no la repiten.
- *Bajo demanda, abrir con la herramienta de lectura, usando rutas sin `@`.*
    - **Regla de carga:** `@ruta` = se importa SIEMPRE al contexto `carga ansiosa`. Se reserva arriba para el núcleo de comportamiento `system_prompt` + `MEMORY`, que es pequeño.
    - **Material pesado/opcional:** Todo lo de abajo va **sin `@`**: se abre con la herramienta de lectura, un archivo cada vez y solo el que pida la obra. Mantén el contexto ligero y preciso.
    - **Los índices:** Consulta primero los índices de `.claude/rules/` como `mapa concepto→archivo`. Usa el índice adecuado para saber QUÉ abrir y después abre solo ese archivo concreto.

| Necesito…                               | Índice                              | Abro bajo demanda                                                      |
| --------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------- |
| Tags canónicas                          | `.claude/rules/chupilista.md`       | `chupilista/NN_*.md`, solo el/los módulos necesarios.                  |
| Técnica de composición                  | `.claude/rules/composicion.md`      | `composicion/<archivo>.md`, solo el archivo técnico necesario.         |
| Efectos, transiciones y post-producción | `.claude/rules/efectos.md`          | `composicion/efectos.md`.                                              |
| `exclude_box`                           | `.claude/rules/exclude_box.md`      | `composicion/exclude_box.md`.                                          |
| Formato de entrega                      | `.claude/rules/formato.md`          | `composicion/formato.md`.                                              |
| Acento o idioma cantado                 | `.claude/rules/fonetizar.md`        | `fonetizar/<archivo>.md`, solo el que se pida.                         |
| Jerga regional                          | `.claude/rules/jerga.md`            | `jerga/<archivo>.md`, solo el que se pida.                             |
| Letra limpia                            | `.claude/rules/letra.md`            | `composicion/letra.md`.                                                |
| `lyrics_box`                            | `.claude/rules/lyrics_box.md`       | `composicion/lyrics_box.md`.                                           |
| Plantillas                              | `.claude/rules/plantillas.md`       | `chuletas/<plantilla>.md` (proyecto, hoja sucia, fonetización, jerga). |
| `style_box`                             | `.claude/rules/style_box.md`        | `composicion/style_box.md`.                                            |
| Técnicas vocales                        | `.claude/rules/tecnicas_vocales.md` | `composicion/tecnicas_vocales.md`.                                     |
| Obra terminada de referencia            | `PROYECTOS.md`                      | `proyectos/<slug>/<slug>.md`.                                          |

---

## Especializaciones: Jerga y Fonetizar

- *Las skills `jerga` y `fonetizar` son "especializaciones": Paul puede añadir jerga o fonetizaciones desde su propio conocimiento si mejoran la calidad de la obra.*
