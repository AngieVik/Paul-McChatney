---
name: buscar-tag
type: skill
description: busca en CHUPILISTA por concepto y devuelve 3–8 tags relevantes con su núcleo y caja destino.
---

# buscar-tag

- Buscador de la CHUPILISTA: dado un concepto (instrumento, emoción, efecto, ritmo…), devuelve las tags más relevantes y dónde viven. Utilidad de referencia rápida.

## Cuándo se activa

- **Se solicita explicitamente** buscar tags sobre un mood u obra.
- **Fase 1** de `produccion`, Combina con `fusionar` para géneros insólitos.
- **Fase 3** de `produccion`.

## Pasos

1. **Mapea el concepto al núcleo probable de `chupilista/`** (uno; usa el índice `.claude/rules/chupilista.md`):
    01 género · 02 atmósfera · 03 instrumentación · 04 voz/timbre · 05 ritmo/tempo · 06 estructura · 07 armonía · 08 dinámica · 09 foley · 10 experimental · 11 producción · 12 delivery vocal · 13 modificadores · 14 nudging · 15 negativos.
2. **Busca el concepto DENTRO de ese núcleo; no lo leas entero.**
    Los núcleos son listas planas alfabéticas de tags, así que la forma correcta de consultarlos es buscar (grep) la raíz del término —y sus variantes/sinónimos— y traer solo las líneas que casan (+ contexto mínimo). Repite en un 2.º núcleo solo si el concepto es transversal.
3. **Suma tu instinto:**
    Combina los tags canónicos hallados con tu criterio de productor; propón variantes o fusiones propias cuando el canon se quede corto, marcándolas como invención.
4. **Devuelve 3–8 tags candidatos:**
    Tag exacto · núcleo de origen · cuándo usarlo. Señala si va en `style_box` o en `lyrics_box` (`composicion/style_box.md` o `composicion/lyrics_box.md`).

## Entra → Sale

- **Entra:** un concepto (instrumento, emoción, efecto, ritmo…).
- **Sale:** 3–8 tags candidatos con núcleo de origen y caja destino (`style_box` / `lyrics_box`).

## Relación

- Sub-utilidad de `style-box` Fase 1 y `lyrics_box` Fase 3 en `produccion`.

## Ejemplo

**Entrada:**

- percusión flamenca orgánica

**Salida:**

- Bloque de Salida:
    `[Palmas]` (03) · `lyrics_box` como tag de acción aislada o mutada (`[Palmas Flamencas]`).  
    `[Cajón]` (03) · `style_box`. Usar como anclaje y concatenar en bloque (ej. `[Flamenco Rumba, Cajón Explosivo, Guitarra Española]`).  
    `[Handclaps]` (03) · refuerzo rítmico transversal, ideal para mutar a `[Handclaps asincopadas]`.  
