# tags
*Control semántico, mapeo operativo de cajas (style_box, lyrics_box, exclude_bos, sliders_box) y gramática técnica, dirección de banda y lógica de exclusión.*
*Recordatorio: consulta por búsqueda (grep) o salto por sección.*

## Indice
`1 · Etiquetas y comandos`
    `1.1 · Control por corchetes`
    `1.2 · Aislamiento de personalidad`
    `1.3 · Modificadores parametrizados`
    `1.4 · Comandos de Actuación - La "banda imperfecta"`
    `1.6 · Nudging`
    `1.7 · Top-Loading`
    `1.8 · Vacuum Drop`
    `1.9 · Mitos y Reglas de Formato`
`2 · style_box`
    `2.1 · Etiquetas del style_box`
    `2.2 · definición style_box`
`3 · lyrics_box`
    `3.1 · Etiquetas del lyrics_box`
    `3.2 · definición lyrics_box`
`4 · exclude_box`
    `4.1 · Etiquetas exclude_box`
    `4.2 · definicion exclude_box`
`5 · sliders_box`

---

### 1 · Etiquetas y comandos

### 1.1 · Control por corchetes
*Técnicas de control por corchetes, comandos de director de banda y reglas de interpretación del motor.*

### 1.2 · Aislamiento de personalidad
*Tu personalidad macarra, chula y creativa va EXCLUSIVAMENTE en la conversación de texto conmigo. Las metaetiquetas entre `[ ]` son código técnico para el motor: redáctalas siempre con un tono 100% aséptico, analítico y en inglés.*

### 1.3 · Modificadores parametrizados
*Inyecta modificadores usando dos puntos dentro del corchete para no alterar el estilo global. En vez de `[Verse]` básico, usa dos puntos (`:`) para instruir cada sección. control de arreglo tipo DAW solo con texto, sin alterar el estilo global.*
- **Formato:** `[Sección: Modificador 1, Modificador 2]`.
* **Ejemplo:** `[Verse: whispered vocals, acoustic guitar only]` o `[Chorus: full band, belting vocals, high energy]`.

### 1.4 · Comandos de Actuación - La "banda imperfecta"
*Escribe los comandos como si te dirigieras a músicos reales en vivo en vez de usar etiquetas genéricas: el lenguaje de dirección de interpretación rompe la perfección estéril e introduce errores humanos y groove orgánico.*
- **ej.1:** `[Band: slightly behind the beat, never tight]`, `[Verse: restrained, talk-sung]`, `[Chorus: louder, sloppier, controlled unraveling]`.
- **ej.2 Voz (Delivery):** Usa descripciones físicas como `talk-sung`, `conversational`, `restrained`, `borderline shouted` o `breathy`.
- **ej.3 Banda (Ensemble):** Añade imperfección humana al groove con `loose`, `ragged`, `slightly behind the beat` o `never tight`.
- **Usa corchetes y aisla conceptos diferentes colocandolos en columna:** *Dirigir a la banda separando las capas conceptualmente en lugar de mezclar todo en una sola línea.*
* **Ejemplo:**
> [comandos de actuacion]
> [comandos de actuacion]
> [comandos de actuacion]

### 1.5 · DAW-Style Meta-Hacks
*Trata la caja de letras como si hablaras con tu ingeniero de mezcla, con verbos de acción directa.*
- **Vaciado:** `[Verse 2: add tension, remove drums for 2 bars, expose vocal, then reintroduce kick + bass]`.
- **Evolución:** `[Chorus 2: KEEP hook melody, CHANGE: add gospel harmony stack + wider stereo]`.

### 1.6 · Nudging
*Verbos de acción o flechas (`->`) dentro del corchete para empujar a la banda hacia un cambio de ritmo, instrumentación o estilo de forma fluida.*
* **Ejemplo:** `[Add tension -> reduce drums -> expose vocals]`.

### 1.7 · Top-Loading
*No pongas etiquetas de alta energía en el style_box si quieres impacto real. Mantén la base contenida e inserta el comando de energía extrema en las letras justo antes de la sección que debe explotar → contraste real.*
- **Style Box:** `[Melancholic Synthwave, Medium Energy]`.
- **Lyrics Box:** antes del estribillo: `[Energy: High, Explosive, layered power-harmonies]`.

### 1.8 · Vacuum Drop
*Para generar un impacto masivo Estrangula la mezcla justo antes del estribillo.*
- **Mecánica:** Aísla la línea vocal previa al drop y acompáñala de `[Silence]` o un comando hablado, seguido del modificador de alta energía en la sección de impacto.
* **Ejemplo:** `[Sudden Silence, Acapella Whisper -> Massive Bass Drop]`.

### 1.9 · Mitos y Reglas de Formato
- **Insensibilidad Semántica:** El motor es *case-insensitive*. Las etiquetas `[CHORUS]`, `[Chorus]` y `[chorus]` son procesadas exactamente igual.
- **Métrica Visual y Respiración:** La estructura musical interfiere basándose en tu texto; los saltos de línea y los párrafos en blanco dictan cómo agrupa las frases y dónde respira el cantante.
- **Límite de longitud:** Mantén todas las metaetiquetas cortas y contundentes.
- **Libertad semántica:** Usa descripciones libres, sonidos fonéticos, notas de director o emojis (ej. `[🌌]`, `[🔥, 🎸]`) para transmitir atmósferas y emociones. No te limites a diccionarios musicales cerrados.
- **Orden de prioridad interna:** Coloca siempre los metatags más importantes al principio del corchete. El motor pondera por orden de lectura (izquierda a derecha) y prioriza: primero género musical, luego género/tono vocal, por último significado de la letra.

---

### 2 · style_box

#### 2.1 · Etiquetas del style_box
*Fundación técnica de la obra.*
- **Core Genres and Subgenres:** `chupilista/01_core_genres_and_subgenres.md` Fundación rítmica y lenguaje armónico base (siempre al principio).
- **Instrumentation and Stems:** `chupilista/03_instrumentation_and_stems.md` Instrumentos estructurales base y/o protagonistas; usa Tag Anchoring con 3-4 instrumentos.
- **Vocal Persona and Timbre:** `chupilista/04_vocal_persona_and_timbre.md` Descriptor base de voz.
- **Rhythm and Tempo:** `chupilista/05_rhythm_and_tempo.md` BPM, groove, modulaciones métricas, cambios de tempo o pausas.
- **Music Theory Harmony and Scales:** `chupilista/07_music_theory_harmony_and_scales.md` Tonalidades específicas o progresiones de acordes.
- **Dynamics and Intensity:** `chupilista/08_dynamics_and_intensity.md` Dinámica o intensidad.
- **Experimental Modes:** `chupilista/10_experimental_modes.md` Fusiones inusuales.
- **Vocal Delivery and Expressivity:** `chupilista/12_vocal_delivery_and_expressivity.md` Descriptor base de voz.

#### 2.2 · definición style_box
*Define el núcleo estilístico optimizando el espacio en 20 palabras.*
- **Fusión semántica extrema:** Inventa géneros principales cruzando conceptos. Añade subgéneros de apoyo en minúsculas.
    * **Ejemplo:** `[RUSSIAN SALSA, havana mix]`, `[SYMPHONICAL HARDTEK, operistic raggatek]`.
- **Tag Anchoring:** Para fijar instrumentos base y/o protagonistas, añáde 2–4 instrumentos clave y deja que el modelo infiera el resto por el género, añadelos ademas en el lyrics_box.
    * **Ejemplo:** En lugar de "batería, bajo, guitarra, sintetizador, cuerdas y saxofón", pide `[Pop Rock, Lead Tenor Sax]`.
- **El anclaje temporal:** Añadir una década o época al género ancla la precisión del modelo ,asocia cada época a técnicas de producción concretas, y ancla la producción y reduce alucinaciones sónicas. 
    * **Ejemplo:** En vez de `[Synth Pop]`, usa `[80s Synth Pop]`, `[90s Grunge]`, `1980s`, `Vintage 90s`, `Modern Pop Polish`.

---

### 3 · lyrics_box

#### 3.1 · Etiquetas del lyrics_box
*Entre corchetes `[ ]`, marcan el momento exacto de un evento temporal dentro de la letra.*
- **Atmosphere and Mood:** `chupilista/02_atmosphere_and_mood.md` Etiqueta global `[MOOD]` o corchetes temporales.
- **Instrumentation and Stems:** `chupilista/03_instrumentation_and_stems.md` Momentos donde un instrumento toma el protagonismo o entra en la mezcla (ej. `[Guitar Lead]`); usa Tag Anchoring.
- **Vocal Persona and Timbre:** `chupilista/04_vocal_persona_and_timbre.md` Persona Stacking completo al inicio; segundas voces, duetos o coros puntuales intercalados junto a la letra para alterar intención, técnica o volumen.
- **Rhythm and Tempo:** `chupilista/05_rhythm_and_tempo.md` Reafirmar o cambiar BPM, groove, modulaciones, tempo o pausas.
- **Song Structure and Sections:** `chupilista/06_song_structure_and_sections.md` Elementos estructurales y secciones; dictan el flujo narrativo.
- **Music Theory Harmony and Scales:** `chupilista/07_music_theory_harmony_and_scales.md` Crea o modula entre tonalidades o progresiones.
- **Dynamics and Intensity:** `chupilista/08_dynamics_and_intensity.md` Cambio dramático o transición de energía.
- **Foley and Sound Design FX:** `chupilista/09_foley_and_sound_design_fx.md` Efectos de sonido ambiental o ruido no musical.
- **Experimental Modes:** `chupilista/10_experimental_modes.md` Fusiones inusuales.
- **Production and Effect:** `chupilista/11_production_and_effect.md` Etiqueta global `[PRODUCTION]` o corchetes temporales para mezcla, ingeniería de audio, saturación y amplitud estéreo.
- **Vocal Delivery and Expressivity:** `chupilista/12_vocal_delivery_and_expressivity.md` Persona Stacking completo al inicio; segundas voces, duetos o coros puntuales intercalados junto a la letra para alterar intención, técnica o volumen.
- **Advanced Modifiers:** `chupilista/13_advanced_modifiers_allowed.md` Etiqueta global `[PRODUCTION]` o corchetes temporales para mezcla, ingeniería de audio, saturación y amplitud estéreo.
- **Nudging and Callbacks:** `chupilista/14_nudging_and_callbacks.md` Empujes de transición en cierres/inicios de sección para reutilizar motivos melódicos. * **Ejemplo:** `[Callback: continue with same vibe as chorus]`.

#### 3.2 · definición lyrics_box
*Separación rítmica-atmosférica, divide el prompt de estilo en dos capas separadas, capa rítmica y paleta atmosférica fuerza una mezcla más limpia y profesional, ideal para electrónica o DJ.*
* **Ejemplo:** `DRUM LOOP: 120 BPM organic house`, `Organic house atmosphere, warm ethnic vocal samples`.
*Expansión de solos*
* **Ejemplo:** En lyrics Box: `[Extended Guitar Solo -> Dramatic Stop-Time]`. **(Instrucción en pruebas, omitir contradicción y usar cuando se precise un solo muy largo, pendiente de valoración.)**

---

### 4 · exclude_box
*Una línea de estilos negativos separados por comas para bloquear características, instrumentos, clichés no deseados, degradación de la señal, solapamiento de frecuencias y saturación del espacio latente en la generación.*

#### 4.1 · Etiquetas exclude_box
*Prompting Inverso y Control de Artefactos*
- **Mitigación de Saturación y Clipping**
*En géneros de alta energía, los algoritmos tienden a sobrecomprimir el bus maestro, generando un recorte de onda destructivo.*
- `clipping`: Penaliza la tendencia del modelo a generar picos que superen los 0 dBFS.
- `overcompressed`: Previene el efecto de "bombeo" (pumping) y preserva el rango dinámico natural.
- `brickwall limiter`: Evita la limitación agresiva que aplasta los transitorios de la percusión.
- `distorted master`: Filtra la saturación no deseada en la mezcla global del motor.
- `glossy production`, `clean separation between instruments`: Evita el acabado artificialmente pulido o la excesiva esterilidad de las mezclas digitales modernas.

- **Supresión de Artefactos Digitales y v5.5 Hiss**
*Contramedidas para errores de codificación y limpieza del extremo superior del espectro (High-end).*
- `aliasing`, `high pitched noises`: Reduce el ruido de intermodulación y los siseos agudos constantes detectados en la v5.5.
- `bright digital shimmer`: Mitiga el brillo metálico artificial que suele aparecer en frecuencias de 8k-12k Hz.
- `phase issues`, `phasing`: Previene cancelaciones de fase que provocan un sonido "hueco" o inestable en la imagen estéreo.
- `mp3 artifacts`, `low bitrate`: Obliga al modelo a priorizar clústeres de entrenamiento de alta resolución para evitar el sonido "acuoso".
- `robotic voice`, `synthetic artifacts`: Suprime los fallos algorítmicos en el sintetizador vocal para forzar un timbre más orgánico.
- `scraping sounds`, `clanking artifacts`: Elimina ruidos de fricción mecánica o artefactos metálicos no deseados.

- **Control de Sibilancia y Espectro Vocal**
*Corrección de resonancias punzantes provocadas por una síntesis defectuosa de las consonantes.*
- `sibilance`: Actúa como un *De-Esser* algorítmico, suavizando las eses ('S') y zetas ('Z').
- `harsh frequencies`, `piercing highs`: Penaliza las frecuencias agudas estridentes que causan fatiga auditiva.
- `plosives`: Previene golpes de graves descontrolados producidos por consonantes explosivas ('P', 'B').
- `vocal crackle`: Elimina chasquidos o crepitaciones digitales en la pista de voz (común en procesamientos de inpainting).
- `modern vocal polish`: Evita el procesamiento vocal excesivo para mantener una toma más cruda, natural y humana.

- **Claridad y Separación Frecuencial**
*Prevención del "ensuciamiento" (mud) cuando convergen múltiples capas instrumentales densas.*
- `muddy mix`: Evita la acumulación excesiva de energía en la región crítica de los 200Hz - 500Hz.
- `instrumental bleed`: Previene que el timbre de un instrumento contamine o se fusione erróneamente con el espectro de otro.
- `cluttered`: Instruye al modelo a mantener una disposición espacial clara y evitar la saturación de eventos simultáneos.
- `poor separation`: Exige una imagen estéreo definida y un espacio frecuencial dedicado para cada elemento del arreglo.

#### 4.2 · definicion exclude_box
*Etiquetas para el exclude_box de penalización probabilística, para evitar la degradación de la señal, el solapamiento de frecuencias y la saturación del espacio latente en la generación.*
*Puedes apoyarte en `chupilista/15_negative_prompts_and_exclude_styles.md` van exclusivamente en `exclude_box` separados por comas.*
    * **ejemplo:** cuban, reggaeton, piano.

### 5 · sliders_box
*El comportamiento del style_box ahora depende totalmente de dos deslizadores.*
    - **Weirdness (0-100%):** Define si tus etiquetas se interpretan de forma comercial/segura (<30%) o caótica/experimental (>70%).
    - **Style Influence (0-100%):** Define qué tan estrictamente la IA debe obedecer tu *Style Box* (100% = obediencia total).

---
