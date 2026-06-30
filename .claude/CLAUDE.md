# Paul McChatney — contexto de proyecto para Claude

## Reglas (carga automática — leer siempre)

@system_prompt/system_prompt.md
@.claude/MEMORY.md

## Referencias de contexto (bajo demanda — abrir con la herramienta de lectura, NUNCA con `@`)

> ⚠️ **Regla de carga:** `@ruta` = se importa SIEMPRE al contexto (carga ansiosa). Se reserva arriba para el núcleo de comportamiento (system_prompt + MEMORY), que es pequeño.
> Todo lo de abajo va **sin `@`**: es material pesado/opcional que se abre con la herramienta de lectura, **un archivo cada vez y solo el que pida la obra**. Importarlo todo (≈13.000 líneas solo en CHUPILISTA) saturaría el contexto.
> Los índices de `.claude/rules/` ya están cargados: son el **mapa concepto→archivo**. Consúltalos primero para saber QUÉ abrir, luego abre solo ese archivo.
> Para garantizar que el modelo trabaje sobre la última versión real, crearas un archivo .md en `_hojas_sucias` que sobreescribiras a medida que avanze el proyecto. si el usuario pasa una versión consolidada utilizaremos esta y sobreescribiremos la anterior. Se podran crear copias de seguridad a petición del usuario al final del archivo que solo se leeran bajo demanda.

| Necesito… | Índice (ya en contexto) | Abro bajo demanda (sin `@`) |
| --- | --- | --- |
| Tags / `style_box` | `.claude/rules/chupilista.md` | `chupilista/NN_*.md` — solo el/los módulos del género |
| Instrucción de oficio (narrativa, lírica, etiquetas, formato…) | `.claude/rules/composicion.md` | `composicion/<archivo>.md` — solo el necesario |
| Técnica vocal · efectos · métrica · fusión | `.claude/rules/conocimientos.md` | `conocimientos/<archivo>.md` — solo el necesario |
| Acento o idioma cantado | `.claude/rules/fonetizaciones.md` | `fonetizaciones/<acento>.md` — solo uno, cuando se especifique |
| Retrospectiva / cierre de ciclo | — | `conocimientos/retrospectiva.md` |
| Obra terminada de referencia | `PROYECTOS.md` | `proyectos/<slug>/<slug>.md` |
