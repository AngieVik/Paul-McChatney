---
name: style-box
description: construye solo el `style_box` consultando CHUPILISTA.
---

# style-box

Construye **solo** el `style_box` (+ `exclude_styles`) de una obra, sin escribir letra.
Es la Fase 1 aislada — ideal para iterar rápido sobre el molde sonoro.

## Pasos

1. Pide o deduce: género\mood objetivo, idioma de la letra y referencias.
2. Busca por concepto (grep, solo coincidencias) dentro del núcleo de `chupilista\` que toque —no lo leas entero— (sobre todo 01 género, 03 instrumentación, 04\12 voz, 05 ritmo, 08 dinámica, 10 experimental). La skill `buscar-tag` automatiza esta búsqueda.
3. Redacta el `style_box`: **género de fusión primero** (MAYÚSCULAS), subgéneros de apoyo en minúsculas, instrumentos base con **Tag Anchoring**. Máx ~30 palabras.
4. Aplica el **Anclaje Idiomático** (`@system_prompt\03_idioma.md`): antepón el idioma solo si el género es global (ej. `SPANISH HEAVY METAL`); omítelo si el género ya es propio de esa cultura (flamenco, reggaetón…).
5. Genera una línea de `exclude_styles` (comas) bloqueando clichés e instrumentos no deseados.

## Reglas heredadas

- Menos es más: 12–20 tags rinden mejor que 40 (`@.claude\MEMORY.md`).
- El orden pondera: lo más importante primero.
- Nunca nombres de artistas reales en el style_box: describe el estilo.

## Ejemplo

> Mood: villano teatral, 200 BPM.
> `SPANISH SYMPHONIC RAWSTYLE HARDCORE, 200 BPM, virtuosic bright tack piano lead, dark neoclassical, aggressive gabber bass, distorted piep kicks`
> exclude: `grand piano, mellow, slow tempo, latin pop, generic edm, lo-fi`
