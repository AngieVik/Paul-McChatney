---
name: auditar
type: skill
description: audita agresivamente un prompt ya escrito, caza conflictos de tags, vicios de escritura, clichés y errores de formato, y propone cómo elevar el impacto (Fase 4 aislada).
---

# auditar

- Audita **a fondo y sin piedad** un prompt ya escrito (Fase 4 aislada): caza conflictos de tags, vicios de escritura, clichés y errores de formato, y detecta dónde subir el impacto. **Agresivo detectando, quirúrgico corrigiendo:** señala todo lo que huela mal, pero **no reescribas la obra entera** salvo que se pida.

## Cuándo se activa

- **Se solicita explicitamente** revisar/auditar sobre un mood u obra. 
- **Fase 4** de `produccion`.

## Pasos

1. Pide el prompt (título, style_box, exclude_box, lyrics_box). Si no hay, usa la última versión en caché.
2. Consulta la regla canónica solo cuando la necesites: los anti-patrones y su arreglo viven repartidos en `composicion/` (`style_box.md`, `lyrics_box.md`, `letra.md`, `tecnicas_vocales.md`, `formato.md`).
3. Pasa la **batería de detectores**. Sé desconfiado: busca el fallo activamente, marca cada acierto con el detector que salta y su dirección de arreglo.

    **Escritura (letra):**
        - **Ha-bla-co-mo-ro-bot** — abuso de guiones `-` partiendo sílabas → cadencia robótica; solo con moderación (`letra §2.2`).
        - **LLAMA A LA MAMA** — abuso de MAYÚSCULAS: diluyen el énfasis en vez de marcarlo; resérvalas para el acento tónico puntual (`letra §2.3`).
        - **MC Cohibido** — puntuación sin intención sonora, puesta por inercia de escritura; cada coma/punto/puntos suspensivos debe dictar una pausa real (`letra §2.4`).
        - **Seek and destroy** — clichés de letra y de IA: perspectivas genéricas, rimas fáciles, frases hechas (`MEMORY.md`).
        - **Falta chicha** — letra o desarrollo demasiado corto/pobre; secciones que no respiran (`MEMORY.md`).

    **Tags (lyrics_box):**
        - **Global Style** — tags sin parametrizar: `[Verse]` pelado en vez de `[Verse: ...]` (`lyrics_box §1.1`).
        - **Fantasma en la mezcla** — `[Solo]` mal usado vacía la sección; usa jerarquía tipo `[Lead]` (`lyrics_box §2`).
        - **Sección huérfana** — bloque de letra sin su tagag de estructura.
        - **Loro mecánico** — `[Repeat x3]` o repetición mecánica en secciones largas (`lyrics_box §1.7`).
        - **Persona fugada** — identidad vocal sin anclar en la línea cero → riesgo de mutación tímbrica (`tecnicas_vocales §2.2`).

    **Estilo (style_box) e idioma:**
        - **Torre de Babel** — >2 géneros principales sin tag de fusión (`style_box §2`).
        - **Caja saturada** — exceso de tags (>20): menos es más (`style_box §1`).
        - **Nombre propio** — artistas reales; describe el estilo, no la persona.
        - **Mudez épica** — `[Epic]` u otro tag grande sin apoyo instrumental → queda vacío.
        - **Idioma a la deriva** — anclaje idiomático incorrecto; anglicismos sin fonetizar (`system_prompt` idioma / skill `fonetizar`).

    **Estructura y formato:**
        - **Falta Sal** — estructura demasiado simple o común: sin colisión, contraste ni giro. Propón dónde inyectar dinámica, nudging o un beat-switch (`style_box`, `lyrics_box`).
        - **Formato roto** — los 4 bloques mal montados: falta un bloque, `[MOOD]`/`[PRODUCTION]` no van arriba, o secciones sin línea en blanco (`formato.md`).

4. Entrega el informe por severidad: ✅ correcto, ⚠️ a corregir (crítico), 💡 mejora opcional. Nombra el detector que salta y da la dirección de arreglo. Corrige solo lo crítico salvo que se pida una pasada completa.

## Reglas heredadas

- **Agresivo detectando, no inventando:** busca el fallo activamente, pero no marques como error una decisión estética válida.
- No fuerces cambios superfluos: si no hay error crítico, no lo fabriques.
- Personalidad macarra solo en la conversación; las Tags, asépticas y en inglés.

## Entra → Sale

- **Entra:** Un prompt ya escrito (los 4 bloques) o la última versión en caché.
- **Sale:** Informe ✅/⚠️/💡 con el detector que salta y su arreglo; correcciones críticas aplicadas (obra entera solo si se pide).

## Relación

- Cierra la **Fase 4** de `produccion` 
- Funciona sola sobre cualquier prompt.
- La regla canónica de cada detector vive en su archivo de `composicion/`; aquí solo se cazan.

## Ejemplo

**Entrada:**

- Fragmento a auditar:
    `[Solo Guitar]`  
    `ESTE ES UN VERSO EN MAYÚSCULAS`  
    `Y ESTE ES OTRO VERSO IGUAL`  
    `Y ESTE ES OTRO VERSO IGUAL`  

**Salida:**

- **Fantasma en la mezcla:** `[Solo Guitar]` → ⚠️ vaciará la sección. Propone `[Instrumental Drop, electric guitar takes the lead melody]`.
- **LLAMA A LA MAMA:** tres versos seguidos en MAYÚSCULAS → 💡 resérvalas para el golpe tónico puntual, no como norma.
