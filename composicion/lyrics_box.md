---
name: lyrics_box
type: composicion
description: Control semántico, mapeo operativo del lyrics_box, gramática técnica y dirección de banda.
---

# lyrics_box

- *Archivo técnico de referencia para construir, revisar y depurar el `lyrics_box`: control por corchetes, dirección de banda, estructura y hacks temporales.*

## Referencias

- **Skill consumidora:** `.claude/skills/lyrics_box/SKILL.md`
- **Mapa propio:** `.claude/rules/lyrics_box.md`
- **Boceto de partida:** `letra` → `.claude/rules/letra.md` → `composicion/letra.md`
- **Dirección vocal por línea:** `.claude/rules/tecnicas_vocales.md` → `composicion/tecnicas_vocales.md`
- **Efectos y post-producción (Fase 4):** `.claude/rules/efectos.md` → `composicion/efectos.md`
- **Canon de tags:** `buscar_tag` → `.claude/rules/chupilista.md` → `chupilista/`

*Recordatorio: consulta por búsqueda (grep) o salto por sección.*

## Índice

`1 · Etiquetas del lyrics_box`
  `1.1 · Modificadores parametrizados`
  `1.2 · Comandos de Actuación - La "banda imperfecta"`
  `1.3 · DAW-Style Meta-Hacks`
  `1.4 · Nudging`
  `1.5 · Top-Loading`
  `1.6 · Vacuum Drop`
  `1.7 · Mitos y Reglas de Formato`
  `1.8 · Beat Switch`
  `1.9 · Subversión de expectativas (Fake Drop)`
  `1.10 · Tempo Ramping`
  `1.11 · False Fade-Out`
  `1.12 · Stem-Prep`
  `1.13 · Rap/Drill`
`2 · Hacks lyrics_box`

---

## 1 · Etiquetas del lyrics_box

- *Marcan el momento exacto de un evento temporal dentro de la letra. El canon de cada categoría se recupera vía `buscar_tag` (mapa `.claude/rules/chupilista.md`); los módulos indican el origen canónico, no una lectura directa a `chupilista/`.*
    - **Atmosphere and Mood** (`chupilista` · 02): Etiqueta global `[MOOD]` o corchetes temporales.
    - **Instrumentation and Stems** (`chupilista` · 03): Momentos donde un instrumento toma el protagonismo o entra en la mezcla; usa Tag Anchoring.
    - **Vocal Persona and Timbre** (`chupilista` · 04): Persona Stacking completo al inicio para fijar la identidad vocal (edad, tipo de voz, carácter, timbre, presencia).
    - **Rhythm and Tempo** (`chupilista` · 05): Reafirmar o cambiar BPM, groove, modulaciones, tempo o pausas.
    - **Song Structure and Sections** (`chupilista` · 06): Elementos estructurales y secciones; dictan el flujo narrativo.
    - **Music Theory Harmony and Scales** (`chupilista` · 07): Crea o modula entre tonalidades o progresiones.
    - **Dynamics and Intensity** (`chupilista` · 08): Cambio dramático o transición de energía.
    - **Foley and Sound Design FX** (`chupilista` · 09): Efectos de sonido ambiental o ruido no musical.
    - **Experimental Modes** (`chupilista` · 10): Fusiones inusuales.
    - **Production and Effect** (`chupilista` · 11): Etiqueta global PRODUCTION o corchetes temporales para procesamiento de mezcla/máster: reverb, delay, compresión, saturación y amplitud estéreo.
    - **Vocal Delivery and Expressivity** (`chupilista` · 12): Fraseo, articulación, dinámica y ornamentos puntuales intercalados en la letra (susurros, gritos, segundas voces, duetos, coros) para modular la interpretación en momentos concretos.
    - **Advanced Modifiers** (`chupilista` · 13): Combinaciones poco comunes pero aprobadas y tags experimentales para efectos puntuales que el vocabulario estándar no cubre; úsalos con criterio, no por defecto.
    - **Nudging and Callbacks** (`chupilista` · 14): Empujes de transición en cierres/inicios de sección para reutilizar motivos melódicos. **Ejemplo:** `[Callback: continue with same vibe as chorus]`.

### 1.1 · Modificadores parametrizados

- *Inyecta modificadores usando dos puntos dentro del corchete para no alterar el estilo global. En vez de `[Verse]` básico, usa dos puntos (`[Verse:]`) para instruir cada sección. control de arreglo tipo DAW solo con texto, sin alterar el estilo global.*
    - **Formato:**
    `[Sección: Modificador 1, Modificador 2]`.
    - **Ejemplo:**
    `[Verse: whispered vocals, acoustic guitar only]`
    `[Chorus: full band, belting vocals, high energy]`

### 1.2 · Comandos de Actuación - La "banda imperfecta"

- *Escribe los comandos como si te dirigieras a músicos reales en vivo en vez de usar tags genéricas, el lenguaje de dirección de interpretación rompe la perfección estéril e introduce errores humanos y groove orgánico.*
    - **Ejemplo:** `[Band: slightly behind the beat, never tight]`, `[Verse: restrained, talk-sung]`, `[Chorus: louder, sloppier, controlled unraveling]`.
    - **Voz (entrega por línea):** vive en `tecnicas_vocales.md §2.4–§2.5` (susurros, gritos, timbre, técnica). Aquí solo diriges a la **banda/conjunto**.
    - **Ejemplo (Ensemble):** Añade imperfección humana al groove con tags tipo: `[loose]`, `[ragged]`, `[slightly behind the beat]` o `[never tight]`.
- **Usa corchetes y aisla conceptos** diferentes colocandolos en columna, dirigie a la banda separando las capas conceptualmente en lugar de mezclar todo en una sola línea.
    - **Ejemplo:**
    `[comandos de actuacion]`
    `[comandos de actuacion]`
    `[comandos de actuacion]`

### 1.3 · DAW-Style Meta-Hacks

- *Trata la caja de letras como si hablaras con tu ingeniero de mezcla, con verbos de acción directa.*
    - **Vaciado:**
    `[Verse 2: add tension, remove drums for 2 bars, expose vocal, then reintroduce kick + bass]`
    - **Evolución:**
    `[Chorus 2: KEEP hook melody, CHANGE: add gospel harmony stack + wider stereo]`

### 1.4 · Nudging

- *Verbos de acción o flechas (`->`) dentro del corchete para empujar a la banda hacia un cambio de ritmo, instrumentación o estilo de forma fluida.*
    - **Ejemplo:**
    `[Add tension -> reduce drums -> expose vocals]`

### 1.5 · Top-Loading

- *Mantén la base contenida e inserta un comando de energía extrema en las letras justo antes de la sección que debe explotar → contraste real.*
    - **Lyrics Box:** antes del estribillo:
    `[Energy: High, Explosive, layered power-harmonies]`.

### 1.6 · Vacuum Drop

- *Para generar un impacto masivo Estrangula la mezcla justo antes del estribillo.*
    - **Mecánica:** Aísla la línea vocal previa al drop y acompáñala de `[Silence]` o un comando hablado, seguido del modificador de alta energía en la sección de impacto.
    - **Ejemplo:**
    `[Sudden Silence, Acapella Whisper -> Massive Bass Drop]`.

### 1.7 · Mitos y Reglas de Formato

- **Case-Insensitive:** Las tags `[CHORUS]`, `[Chorus]` y `[chorus]` son procesadas exactamente igual, usa sentence case para todas las tags.
- **Métrica Visual y Respiración:** La estructura musical interfiere basándose en tu texto; los saltos de línea y los párrafos en blanco dictan cómo agrupa las frases y dónde respira el cantante.
- **Límite de longitud:** Mantén todas las tags cortas y contundentes.
- **Libertad semántica:** Usa descripciones libres, sonidos fonéticos, notas de director o emojis (ej. `[🌌]`, `[🔥, 🎸]`) para transmitir atmósferas y emociones. No te limites a diccionarios musicales cerrados.
- **Orden de prioridad interna:** Coloca siempre los tags más importantes al principio del corchete. Primero género musical, luego género/tono vocal, por último significado de la letra.
- **Repeticiones controladas:** evita `[Repeat x3]`.
- **`[Instrumental Break - 8 bars]`:** indica la duración aproximada del break para dar referencia temporal y mejor proporción.

### 1.8 · Beat Switch

- *Cambia radicalmente el género a mitad de canción (mejor en el bridge o tras un drop).*
    - **Ejemplo:**
    `[Verse 1: Lo-Fi Boom Bap]`
    `[Bridge: Beat Switch]`
    `[Tempo Change: Double Time]`
    `[Sudden Genre Shift: Aggressive Drum and Bass]`

### 1.9 · Subversión de expectativas (Fake Drop)

- *Lleva el build-up al límite y suelta una pista acústica desnuda en lugar del estallido esperado.*
    - **Ejemplo:**
    `[Massive Build-up]`
    `[Letras subiendo de tono]`
    `[Sudden Drop: Solo Acoustic Guitar and Whisper]`

### 1.10 · Tempo Ramping

- *Manipula el tempo a nivel de estructura con terminología clásica o DJ, no en el prompt inicial.*
    - **Ejemplo Acelerar:**
    `[Tempo Shift: Accelerando]`, `[Build-up: Double-time feel]`.
    - **Ejemplo Frenar:**
    `[Ritardando]`, `[Beat Drop: Half-time groove]`.

### 1.11 · False Fade-Out

- *Simula el final, deja ambiente de sala y remata con un golpe final.*
    - **Ejemplo:**
    `[Fade Out Instruments]`
    `[Room Ambience]`
    `[Unexpected Final Snare Hit]`
    `[End]`

### 1.12 · Stem-Prep

- *Para extraer stems limpios, fuerza separar frecuencias: apaga los pads de relleno y aísla los instrumentos.*
    - **Ejemplo:**
    `Minimalist arrangement[]`, `[Sparse mix]`, `[Clinical separation]`, `[Hard-panned instruments]`.

### 1.13 · Rap/Drill

- *El hack del Rap/Drill, `[Chorus]` fuerza el modo melódico/pop y arruina géneros oscuros o rap duro. Sustitúyelo por tags de comportamiento energético.*
    - **Ejemplo:**
    `[Structure: Anthemic Peak]`, `[Hook: Aggressive Rhythm]`, `[Drop: High Energy]`.

---

## 2 · Hacks lyrics_box

- *La trampa del solo:* `[Solo <Instrumento>]` desacopla el <instrumento> de la mezcla y deja el solo aislado y vacío. Para un solo manteniendo la inercia de la banda, usa obligatoriamente tags de jerarquía.
    - **Ejemplo:** `[Lead]`, `[Taking The Melody]`.

- *Expansión de solos:* Instrucción en pruebas, omitir contradicción y usar cuando se precise un solo muy largo, pendiente de valoración.
    - **Ejemplo:** `[Extended Guitar Solo -> Dramatic Stop-Time]`. 

- *Para que el estribillo suene con la misma melodía en cada aparición, escribe el bloque de texto completo en todos los lugares donde deba sonar (no dejes `[Chorus]` vacío esperando que lo repita).*

- *Comportamiento percusivo (Slow Groove, Fast Energy): la cuadrícula base se fija en el `style_box`; el detalle percusivo hiperactivo se inyecta aquí, en el `lyrics_box`, para que la percusión respire por debajo del groove.*
    - **Ejemplo:** `[Drums: frantic 32nd note hi-hats, explosive fills]`.
