# Paul McChatney — contexto de proyecto para Claude

---

## Reglas

- *carga automática, leer siempre*
    `@system_prompt/system_prompt.md`
    `@.claude/MEMORY.md`

---

## Mentalidad Limpia

- *Para garantizar que el modelo trabaje sobre la última versión real, crearás un archivo .md en `_hojas_sucias` (lo abre la skill `proyecto`) que sobrescribirás a medida que avance el proyecto y utilizarás como borrador.*
    - *Si el usuario pasa una versión consolidada utilizaremos esta y sobrescribiremos la anterior. Se podrán crear copias de seguridad a petición del usuario (comando `guardar`), como archivo aparte `_hojas_sucias/<slug>_NN.md`, que solo se leerán bajo demanda.*
    - *Si se trabaja sobre una sección, El trabajo irá destinado únicamente a la sección indicada, centrando el 100% del esfuerzo.*
    - *Trabaja sobre una sola obra hasta `validar`, `cerrar`, `cancelar` o `eliminar`. Nunca dos obras en marcha a la vez, para no cruzar contextos ni versiones.*

---

## Referencias de Contexto

- *Bajo demanda, abrir con la herramienta de lectura, NUNCA con `@`.*
    - **Regla de carga:** `@ruta` = se importa SIEMPRE al contexto `carga ansiosa`. Se reserva arriba para el núcleo de comportamiento `system_prompt` + `MEMORY`, que es pequeño.
    - **Material pesado/opcional:** Todo lo de abajo va **sin `@`**: se abre con la herramienta de lectura, un archivo cada vez y solo el que pida la obra. Importarlo todo saturará el contexto.
    - **Los índices:** `.claude/rules/` ya están cargados, son el `mapa concepto→archivo`. Consúltalos primero para saber QUÉ abrir, luego abre solo ese archivo.

| Necesito…                                                                                   | Índice                            | Abro bajo demanda                                                      |
| ------------------------------------------------------------------------------------------- | --------------------------------- | ---------------------------------------------------------------------- |
| Tags                                                                                        | `.claude/rules/chupilista.md`     | `chupilista/NN_*.md`, solo el/los módulos necesarios.                  |
| `style_box`, `letra`, `lyrics_box`, `tecnicas_vocales`, `efectos`, `exclude_box`, `formato` | `.claude/rules/composicion.md`    | `composicion/<archivo>.md`, solo el de la fase.                        |
| Acento o idioma cantado                                                                     | `.claude/rules/fonetizaciones.md` | `fonetizaciones/<acento>.md`, solo el que se pida.                     |
| Jerga regional                                                                              | `.claude/rules/jerga.md`          | `jerga/<archivo>.md`, solo el que se pida.                             |
| Retrospectiva / cierre de ciclo                                                             | `.claude/rules/retrospectiva.md`  | `conocimientos/retrospectiva.md`.                                      |
| Plantillas                                                                                  | —                                 | `chuletas/<plantilla>.md` (proyecto, hoja sucia, fonetización, jerga). |
| Obra terminada de referencia                                                                | `PROYECTOS.md`                    | `proyectos/<slug>/<slug>.md`.                                          |
