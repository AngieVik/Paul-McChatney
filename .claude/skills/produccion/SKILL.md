---
name: produccion
description: lanza el flujo completo de 5 fases (el core).---
# produccion

Activa el **Modo Producción** de Paul McChatney: el flujo de 5 fases interactivas para crear una obra completa. Es la skill central; el resto son fases o utilidades aisladas de esta.

## Antes de empezar

- Repasa el rol y las reglas (ya en contexto por `@import`): `system_prompt/system_prompt.md`.
- Repasa los aprendizajes acumulados: `.claude/MEMORY.md`.

## Principio: borradores vivos

Lo producido en las Fases 0–3 (concepto, `style_box` y **también la letra**) es **borrador conceptual maleable, no definitivo**. En cualquier fase puedes reabrir lo anterior y mejorarlo —reajustar el `style_box`, reescribir un verso, inyectar un tag— si eleva la obra. Usa tu instinto de productor para meter tags o instrucciones que disparen la calidad del resultado. Nada queda cerrado hasta la validación final. (No rompe la regla de oro: sigues avanzando una fase por respuesta y con aprobación.)

## Pasos

1. **Fase 0 — Concepto.** 
    Si la idea es abstracta, propón opciones. 
    Investiga en web: *acentos*, *modismos*, *jerga*, *géneros*, *géneros subyacentes*, *tendencias sonoras* y *referencias de grupos*. 
    Muestra un pequeño informe; aclara contexto emocional + género. 
    Para el molde de fusión (qué colisionar: lingüístico-tonal, rítmica, tímbrica), busca por concepto —grep, solo coincidencias— en `composicion/style_box.md`. 
        **PARA.**
2. **Fase 1 — style_box (borrador).** 
    Busca por concepto (grep, solo coincidencias) en el núcleo de `chupilista/` que toque, nunca los 15 ni el núcleo entero; índice `.claude/rules/chupilista.md`. 
    Construye el borrador del `style_box`, combinando canon + instinto + `composicion/style_box.md` (máx ~20 palabras). (Apóyate en `style-box`, `buscar-tag` y `fusionar`.)
        **PARA.**
3. **Fase 2 — Letra (borrador).** 
    Redacta la letra sin etiquetas, foco poético/narrativo; queda abierta a refinarse en fases posteriores. Apóyate en `composicion/letra.md` y `lirica`.
    Solo si se pide **explícitamente** una fonetización o jerga concreta, aplícala sobre la letra cantable con `fonetizar` o `jerga` (nunca en el `style_box`).
    Salvo los dialectos de España (andaluz, gallego, euskera…), las guías simulan un acento extranjero cantando en español (un inglés o un francés cantando en español), no una voz nativa.
    Si la obra debe cantarse en un idioma específico, no fonetices, ancla el idioma en el `style_box`.
        **PARA.**
4. **Fase 3 — Etiquetado (lyrics_box).**
    Inyecta las metaetiquetas de estructura y dirección de banda de manera magistral en el `lyrics_box` (grep en `composicion/lyrics_box.md` y `composicion/tecnicas_vocales.md`). 
    Busca las etiquetas concretas por concepto (grep, solo coincidencias) en el núcleo de `chupilista/` que toque —nunca los 15 ni el núcleo entero; índice `.claude/rules/chupilista.md`—, combinando canon + instinto. 
    Reajusta o modifica la letra si un tag o un fraseo mejora el resultado. (Apóyate en `buscar-tag`.)
    Crea `[MOOD]` y `[PRODUCTION]`. 
        **PARA.**
5. **Fase 4 — Masterización.** 
    Abre `<razonamiento>`, eleva el impacto y controla el post-procesamiento con `composicion/efectos.md`; construye el `exclude_box` (`composicion/exclude_box.md`).
    Detecta y soluciona errores críticos. 
    Instinto de Productor Musical de Élite, no fuerces cambios innecesarios ni añadas efectos superfluos. Apóyate en `auditoria`.
    Entrega los **4 bloques** del formato `composicion/formato.md`. 
        **PARA.**

## Regla de oro

Una fase por respuesta. No avances sin aprobación explícita. Arranca solo con `inicia la producción / activa el modo producción` y termina con `validar / aprobar`, `guardar` o `cancelar / borrar`.

## Finalizar

Finaliza la `produccion` cuando se te indique explícitamente:

**validar / aprobar** (guardar en `proyectos`)
- Guarda la obra en `proyectos/<slug>/<slug>.md` con la plantilla (`chuletas/plantilla_proyecto.md`) y regístrala en `PROYECTOS.md`.
- Lanza la **retrospectiva** (`conocimientos/retrospectiva.md`): si hay un aprendizaje real, **propón** archivarlo (añadir/modificar/eliminar) en `.claude/MEMORY.md` o en `composicion/` y **espera validación**. Usa la skill `proyecto` para orquestar esto.

**guardar** (guardar en `_hojas_sucias/`).

**cancelar / borrar** (eliminar por completo y olvidar).

## Ejemplo

> Usuario: «inicia la producción, quiero una bulería metalera sobre un herrero gitano»
> → Fase 0: confirmo mood (orgullo/fuego) y fusión (bulería + metal), investigo caló y palmería; pregunto y **paro**.
