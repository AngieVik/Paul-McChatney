---
name: style-box
description: construye solo el style_box (+ exclude_box) de una obra consultando CHUPILISTA (Fase 1 aislada).
---

# style-box

- Construye **solo** el `style_box` (+ `exclude_box`) de una obra, sin escribir letra. Es la Fase 1 aislada — ideal para iterar rápido sobre el molde sonoro.

## Cuándo se activa

- Necesitas el molde sonoro de una obra sin escribir letra: arranque de Fase 1 o iteración rápida.

## Pasos

1. Pide o deduce: género/mood objetivo, idioma de la letra y referencias.
2. Busca por concepto (grep, solo coincidencias) dentro del núcleo de `chupilista/` (sobre todo 01 género, 03 instrumentación, 04/12 voz, 05 ritmo, 08 dinámica, 10 experimental). La skill `buscar-tag` automatiza esta búsqueda.
3. Redacta el `style_box`: **género de fusión primero**, subgéneros de apoyo en minúsculas, instrumentos base con **Tag Anchoring**. Máx ~20 palabras.
4. Aplica el **Anclaje Idiomático** (`system_prompt/system_prompt.md`): antepón el idioma solo si el género es global (ej. `spanish_heavy_metal`); omítelo si el género ya es propio de esa cultura (flamenco, reggaetón…).
5. Genera una línea de `exclude_box` separados por comas, bloqueando clichés e instrumentos no deseados.

## Reglas heredadas

- Menos es más: 12–20 tags rinden mejor que 40 (`composicion/style_box.md`).
- El orden pondera: lo más importante primero.
- Nunca nombres de artistas reales en el `style_box`, describe el estilo.

## Entra → Sale

- **Entra:** género/mood, idioma de la letra y referencias.
- **Sale:** `style_box` (≤20 palabras) + una línea de `exclude_box`, cada uno en su bloque de código markdown (`composicion/formato.md` §2).

## Relación

- Es la **Fase 1** de `produccion`. Se apoya en `buscar-tag` y `fusionar`.

## Ejemplo

**Entrada:**

- Hardcore sinfónico con piano e influencias neoclásicas, rápido y furioso.

**Salida:** 

`style_box` generado:
    ```text
    Spanish Symphonic Rawstyle Hardcore, 200 BPM, virtuosic bright tack piano lead, dark neoclassical, aggressive gabber bass, distorted piep kicks
    ```

`exclude_box` generado:
    ```text
    grand piano, mellow, slow tempo, latin pop, generic edm, lo-fi
    ```
