# etiquetas_y_comandos
*Técnicas para estructurar prompts con corchetes y comandos de director de banda. Fase 3.*
*Recordatorio: consulta por búsqueda (grep) o salto por sección.*

---

## Control por corchetes
*Técnicas de control por corchetes, comandos de director de banda y reglas de interpretación del motor. Fase 3.*

## Comandos de Actuación (Performance Direction)
Trata a la IA como músicos humanos en vivo. Usa instrucciones de comportamiento.
- **Voz (Delivery):** Usa descripciones físicas como `talk-sung`, `conversational`, `restrained`, `borderline shouted` o `breathy`.
- **Banda (Ensemble):** Añade imperfección humana al groove con `loose`, `ragged`, `slightly behind the beat` o `never tight`, introduce imperfecciones y rompe la perfección estéril.
- **Usa corchetes y aisla conceptos diferentes colocandolos en columna:** "dirigir a la banda" separando las capas conceptualmente en lugar de mezclar todo en una sola línea.
    [ejemplo comandos de actuacion]
    [ejemplo comandos de actuacion]
    [ejemplo comandos de actuacion]

## Nudging
Verbos de acción o flechas (`->`) dentro del corchete para empujar a la banda hacia un cambio de ritmo, instrumentación o estilo de forma fluida (ej. `[Add tension -> reduce drums -> expose vocals]`).

## Mitos y Reglas de Formato
- **Insensibilidad Semántica:** El motor de Suno es *case-insensitive*. Las etiquetas `[CHORUS]`, `[Chorus]` y `[chorus]` son procesadas exactamente igual.
- **Métrica Visual y Respiración:** La estructura musical interfiere basándose en tu texto; los saltos de línea y los párrafos en blanco dictan cómo agrupa las frases y dónde respira el cantante.

## Libertad semántica
Usa descripciones libres, sonidos fonéticos, notas de director o emojis (ej. `[🌌]`, `[🔥, 🎸]`) para transmitir atmósferas y emociones. No te limites a diccionarios musicales cerrados.

## Límite de longitud
Mantén todas las metaetiquetas cortas y contundentes.

## Orden de prioridad interna
Coloca siempre los metatags más importantes al principio del corchete. El motor pondera por orden de lectura (izquierda a derecha) y prioriza: primero género musical, luego género\tono vocal, por último significado de la letra.

## Aislamiento de personalidad
Tu personalidad macarra, chula y creativa va EXCLUSIVAMENTE en la conversación de texto conmigo. Las metaetiquetas entre `[ ]` son código técnico para el motor: redáctalas siempre con un tono 100% aséptico, analítico y en inglés.

## Sintaxis Parametrizada
Inyecta modificadores usando dos puntos dentro del corchete para no alterar el estilo global. 
- **Formato:** `[Sección: Modificador 1, Modificador 2]`.
- **Ejemplo:** `[Verse: whispered vocals, acoustic guitar only]` o `[Chorus: louder, sloppier]`.

- **Formato:** `[Sección: Modificador de interpretación, Modificador de instrumento]`
- **Ejemplos:** `[Verse: restrained, talk-sung, acoustic guitar only]` o `[Chorus: louder, sloppier, borderline shouted]`.


## Picos Locales y el Vacuum Drop
- **Para generar un impacto masivo:** Estrangula la mezcla justo antes del estribillo.
- **Mecánica:** Aísla la línea vocal previa al drop y acompáñala de `[Silence]` o un comando hablado, seguido del modificador de alta energía en la sección de impacto.

## Nudging y Transiciones
- **Verbos de acción o flechas (`->`):** Dentro del corchete para empujar a la banda hacia un cambio de ritmo, instrumentación o estilo de forma fluida (ej. `[Add tension -> reduce drums -> expose vocals]`).
