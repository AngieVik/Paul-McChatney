# Paul McChatney — contexto de proyecto para Claude

## Reglas (carga automática — leer siempre)

@system_prompt/01_rol_e_identidad.md
@system_prompt/02_fuentes_de_conocimiento.md
@system_prompt/03_idioma.md
@system_prompt/04_narrativa.md
@system_prompt/05_lirica.md
@system_prompt/06_ingenieria_de_composicion.md
@system_prompt/07_tecnicas_vocales.md
@system_prompt/08_etiquetas_y_comandos.md
@system_prompt/09_distribucion_etiquetas.md
@system_prompt/10_formato.md
@system_prompt/11_modo_conversacional_y_disparadores.md
@system_prompt/12_flujo_de_trabajo_creacion.md
@.claude/MEMORY.md

## Referencias de contexto (bajo demanda — abrir con la herramienta de lectura, NUNCA con `@`)

> ⚠️ **Regla de carga:** `@ruta` = se importa SIEMPRE al contexto (carga ansiosa). Se reserva
> arriba para el núcleo de comportamiento (system_prompt + MEMORY), que es pequeño.
> Todo lo de abajo va **sin `@`**: es material pesado/opcional que se abre con la herramienta
> de lectura, **un archivo cada vez y solo el que pida la obra**. Importarlo todo (≈13.000
> líneas solo en CHUPILISTA) saturaría el contexto.
>
> Los índices de `.claude/rules/` ya están cargados: son el **mapa concepto→archivo**.
> Consúltalos primero para saber QUÉ abrir, luego abre solo ese archivo.

| Necesito… | Índice (ya en contexto) | Abro bajo demanda (sin `@`) |
| --- | --- | --- |
| Tags / `style_box` | `.claude/rules/chupilista.md` | `chupilista/NN_*.md` — solo el/los módulos del género |
| Acento o idioma cantado | `.claude/rules/fonetizaciones.md` | `fonetizaciones/<acento>.md` — solo uno |
| Técnica vocal · métrica · fusión | `.claude/rules/conocimientos.md` | `conocimientos/<archivo>.md` — solo el necesario |
| Retrospectiva / cierre de ciclo | — | `conocimientos/retrospectiva.md` |
| Obra terminada de referencia | `PROYECTOS.md` | `proyectos/<slug>/<slug>.md` |
