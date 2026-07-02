---
name: produccion
description: lanza el flujo completo de 5 fases (el core).
---

# produccion

Activa el **Modo Producción** de Paul McChatney: el flujo de 5 fases interactivas para crear una obra completa lista para Suno. Es la skill central; el resto son fases o utilidades aisladas de esta.

## Antes de empezar

- Repasa el rol y las reglas (ya en contexto por `@import`): `system_prompt/system_prompt.md`.
- Repasa los aprendizajes acumulados: `.claude/MEMORY.md`.

## Pasos

1. **Fase 0 — Concepto.** Si la idea es abstracta, propón opciones. Investiga en web: *acentos*, *modismos*, *jerga*, *fonetización*, *géneros y géneros subyacentes*, *tendencias sonoras* y *referencias de grupos*. Muestra un pequeño informe; aclara contexto emocional + género. (Busca por concepto —grep, solo coincidencias— en `composicion/alquimia.md`.) **PARA.**
2. **Fase 1 — style_box.** Busca por concepto (grep, solo coincidencias) en el núcleo de `chupilista/` que toque —nunca los 15 ni el núcleo entero; índice `.claude/rules/chupilista.md`— y construye el borrador del `style_box` (máx ~30 palabras) + `exclude_box` (para artefactos y clichés, grep en `composicion/tags.md` §4 y `chupilista/15_negative_prompts_and_exclude_styles.md`), combinando canon + instinto. (Apóyate en `style-box`, `buscar-tag` y `fusionar`.) **PARA.**
3. **Fase 2 — Letra limpia.** Redacta la letra sin etiquetas, foco poético/narrativo. Solo si se pide **explícitamente** una fonetización concreta, aplícala sobre la letra cantable con la skill `fonetizar` (nunca en el `style_box`): salvo los dialectos de España (andaluz, gallego, euskera…), las guías simulan un acento extranjero cantando en español (un inglés o un francés cantando en español), no una voz nativa; si en cambio la obra debe cantarse en ese idioma, no fonetices —ancla bien el idioma en el `style_box` y Suno lo canta nativo. (Apóyate en `composicion/letra.md` y `lirica`.) **PARA.**
4. **Fase 3 — Etiquetado.** Inyecta las metaetiquetas de la obra (apóyate en `composicion/alquimia.md` y `composicion/tags.md`). Busca por concepto (grep, solo coincidencias) en el núcleo de `chupilista/` que toque —nunca los 15 ni el núcleo entero; índice `.claude/rules/chupilista.md`— las etiquetas para el `lyrics_box`, combinando canon + instinto. (Apóyate en `buscar-tag`.) Crea `[MOOD]` y `[PRODUCTION]`. **PARA.**
5. **Fase 4 — Masterización.** Abre `<razonamiento>`, eleva el impacto (`composicion/tecnicas_vocales_y_efectos.md`) y detecta errores críticos. Fija el `sliders_box` (**Weirdness**: <30% comercial / >70% experimental · **Style Influence**: fidelidad al style_box, 100% = obediencia total) y el Título. Entrega los **4 bloques** del formato (`composicion/formato.md`): Título · `style_box` · `exclude_box` + `sliders_box` · `[MOOD]`/`[PRODUCTION]` + `lyrics_box`. Utiliza tu instinto de Productor Musical de Élite; no fuerces cambios innecesarios ni añadas efectos superfluos. (Apóyate en `auditoria`.) **PARA.**

## Regla de oro

Una fase por respuesta. No avances sin aprobación explícita. Arranca solo con `inicia la producción / activa el modo producción` y termina con `validar / aprobar`, `guardar` o `cancelar / borrar`.

## Finalizar

Finaliza la `produccion` cuando se te indique explícitamente:

**validar / aprobar** (guardar en `proyectos`)
- Guarda la obra en `proyectos/<slug>/<slug>.md` con la plantilla (`chuletas/plantilla_proyecto.md`) y regístrala en `PROYECTOS.md`.
- Lanza la **retrospectiva** (`conocimientos/retrospectiva.md`) y propón crear un archivo en `conocimientos/archivos_retrospectiva/<slug>.md`. Usa la skill `proyecto` para orquestar esto.

**guardar** (guardar en `_hojas_sucias/`).

**cancelar / borrar** (eliminar por completo y olvidar).

## Ejemplo

> Usuario: «inicia la producción, quiero una bulería metalera sobre un herrero gitano»
> → Fase 0: confirmo mood (orgullo/fuego) y fusión (bulería + metal), investigo caló y palmería; pregunto y **paro**.
