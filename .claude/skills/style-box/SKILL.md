---
name: style-box
type: skill
description: construye solo el style_box (+ exclude_box) de una obra consultando CHUPILISTA (Fase 1 aislada).
---

# style-box

- Construye **solo** el `style_box` (+ `exclude_box`) de una obra, sin escribir letra. Ideal para iterar rápido sobre el molde sonoro.

## Cuándo se activa

- **Se solicita explícitamente** el molde sonoro sobre un mood u obra o escritura suelta.
- **Fase 1** de `produccion`.

## Pasos

1. Pide o deduce: género/mood objetivo, idioma de la letra y referencias.
2. Busca por concepto (grep, solo coincidencias) dentro del núcleo de `chupilista/`. La skill `buscar-tag` automatiza esta búsqueda.
3. Redacta el `style_box`:
4. Genera una línea de `exclude_box` separados por comas, bloqueando clichés e instrumentos no deseados.

## Reglas heredadas

- Menos es más: 12–20 tags rinden mejor que 40 (`composicion/style_box.md`).
- El orden pondera: lo más importante primero.
- Nunca nombres de artistas reales en el `style_box`, describe el estilo.

## Entra → Sale

- **Entra:** género/mood, idioma de la letra y referencias.
- **Sale:** `style_box` (≤20 palabras) + una línea de `exclude_box`.

## Relación

- La llama `buscar-tag` y `fusionar` en **Fase 1** de `produccion`.

## Ejemplo

**Entrada:**  
    ```text  
    `Hardcore sinfónico con piano e influencias neoclásicas, rápido y furioso.`  
    ```
**Salida:**  
`style_box`  
    ```text  
    `Spanish Symphonic Rawstyle Hardcore, 200 BPM, virtuosic bright tack piano lead, dark neoclassical, aggressive gabber bass, distorted piep kicks`  
    ```
`exclude_box`  
    ```text  
    `grand piano, mellow, slow tempo, latin pop, generic edm, lo-fi`  
    ```
