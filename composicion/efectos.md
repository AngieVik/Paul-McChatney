---
name: efectos
type: composicion
description: Manipulación del espacio estéreo, procesamiento de señales (DSP) y comportamiento del master final.
---

# efectos

*Recordatorio: consulta por búsqueda (grep) o salto por sección.*

*⚗️ = corazonada por comprobar: técnica plausible aún no confirmada; en la retrospectiva se asciende (se quita la marca) o se degrada/elimina.*

## Índice

`1 · Efectos de audio y post-producción`
`1.1 · Control de silencios y pausas`
`1.2 · Modulación, distorsión y espacio espacial`
`1.3 · Efectos vocales específicos`
`1.4 · Glitch forzado y stutter vocal`
`1.5 · Acústica física y microfonía`
`1.6 · Parámetros de Inpainting y estilo general`
`1.7 · Texturas sonoras y compresión`
`1.8 · Transiciones, tensión armónica y SFX`

---

## 1 · Efectos de audio y post-producción

### 1.1 · Control de silencios y pausas

- *Interrupciones del flujo del secuenciador.*
    - `[quick Silence]`: Corte abrupto (*Hard stop*); detiene la generación instrumental de forma súbita. Debe ir en línea independiente.
    - `[Pausa instrumental]`: Silencia exclusivamente la pista vocal para un interludio de transición.
    - `[fermata]`: Suspensión métrica; sostiene y alarga una nota más allá de su valor rítmico antes de un corte.
    - `[Silence]`: Pausa absoluta o caída a ruido de fondo (*noise floor*) en la mezcla.

### 1.2 · Modulación, distorsión y espacio espacial

- *Procesamiento de efectos basados en tiempo y saturación.*
    - `[Hall Reverb]`, `[Room Reverb]`, `[Dry]`: Control de la respuesta a impulsos (IR). Cola larga (Hall), reflejos tempranos (Room) o señal cruda sin procesar (Dry).
    - `[Plate Reverb]`, `[Spring Reverb]`: Reverberación de placas metálicas (Plate) o efecto mecánico de muelles (Spring).
    - `[Chorus]`, `[Flanger]`, `[Phaser]`: Modulación espacial. Multiplicación de la señal `[Chorus]`, cancelación de fase variable por retardo `[Flanger]`, y alteración de fase pura `[Phaser]`.
    - `[Tremolo]`: Modulación rítmica de la amplitud (volumen) mediante un LFO.
    - `[Overdrive]`, `[Distortion]`, `[Fuzz]`: Etapas de saturación (Clipping). Calidez de válvulas `[Overdrive]`, recorte de onda agresivo `[Distortion]`, y distorsión de onda cuadrada/rasposa `[Fuzz]`.
    - `[Slapback Delay]`: Retardo ultracorto (típico del rockabilly) de una sola repetición.
    - `[Ping Pong Delay]`: Eco panorámico alternando entre el canal L y R.
- **Stereo Width Hacks:** Abre el panorama y separa instrumentos desde el `style_box`: `[immersive panning]`, `[wide stereo dispersion]`, `[clear left-right imaging]`.

### 1.3 · Efectos vocales específicos

- *Procesamiento destructivo y filtros aplicados únicamente al stem vocal.*
    - `[Vocal chop]`: Muestreo y re-secuenciación de fragmentos vocales (slicing) usados como instrumento.
    - `[Stutter-vocals]`: Efecto *Glitch* de tartamudeo rítmico basado en repetición de milisegundos.
    - `[Vocoder]`, `[Robotic voice]`: Modulación de la voz utilizando una señal portadora (sintetizador) para un timbre robótico armónico.
    - `[Heavy AutoTune No Pitch Correction]`: Fuerza artefactos de corrección tonal rígida extrema (T-Pain effect) o exige afinación humana orgánica.
    - `[Telephone Effect]`, `[Megaphone]`: Efecto paso-banda (Bandpass filter); recorta frecuencias por debajo de 300Hz y por encima de 3kHz.

### 1.4 · Glitch forzado y stutter vocal

- *Escríbelo en la letra con guiones que rompan las sílabas, combinado con tags.*
    - **Ejemplo:**
    `[Glitch effect on vocal]`
    D-d-d-dímelo en la c-c-cara
    `[System malfunction]`

### 1.5 · Acústica física y microfonía

- *Parámetros de ingeniería de sonido. Orientados al `Style Box` para dictar el comportamiento del renderizado acústico.*
    - **style_box:** `[Close-mic]`, `[slight overload]`, [`Room bleed present]`, `[worn tube amps]`, `[imperfect drums]`.
    - **exclude_box (si aplica):** `[glossy production]`, `[modern vocal polish]`, `[bright digital shimmer]`.
    - **3D Room Dynamics:** ⚗️ Asigna acústicas opuestas a elementos distintos del mismo prompt para forzar profundidad de campo estéreo.
        - **Ejemplo:** `[Close-Mic Dry Vocal, Distant Cathedral Drums]`, `[Claustrophobic Room Bass, Stadium Reverb Synths]`.
    - **Hack espacial emocional:** ⚗️ Altera la física de la mezcla estéreo con palabras de atmósfera; infiere el ancho.
        - **Cerradas (centro/mono):** `[Sensory Deprivation]`, `[Buried Alive]`, `[Claustrophobic Panic]`.
        - **Expansivas (estéreo 3D):** `[Galactic Isolation]`, `[Mountain Peak Epiphany]`.

### 1.6 · Parámetros de Inpainting y estilo general

- *Mitigación de artefactos de red neuronal en consonantes fricativas o plosivas (P, B, T, S).*
    - **style_box (Prompts de corrección):** `[smooth consonants]`, `[no vocal crackle]`, `[high quality de-esser]`.
    - **exclude_box:** `[high pitched noises]`, `[sibilance]`, `[harsh frequencies]`.

### 1.7 · Texturas sonoras y compresión

- *Tratamiento de la dinámica global y adición de capas de ruido estético (Dither/Noise).*
    - `[Lo-fi]`, `[Tape-Saturated]`, `[Vinyl Hiss]`, `[Vinyl Crackle]`: Inyección de ruido magnético (Hiss), desgaste físico o crujido de aguja sobre vinilo (Crackle), comprimiendo el rango dinámico para emular hardware antiguo.
    - `[Bitcrusher]`, `[Glitch]`, `[Granular]`: Reducción intencional de la profundidad de bits (Bitcrushing) o síntesis granular, provocando artefactos digitales (Aliasing) para IDM o electrónica experimental.
    - `[Sidechain Pumping]`: Compresión *Ducking* extrema en el master o bajo, disparada por el bombo (*Kick*), indispensable en House o Future Bass.
    - `[Punchy]`, `[Polished]`, `[Raw]`: Directrices de compresión/EQ de bus maestro. `[Punchy]` maximiza los transitorios graves; `[Polished]` aplica un limitador agresivo y brillo en agudos (mezcla de radio comercial); `[Raw]` anula el procesamiento de bus maestro.
    - **Phantom Layering:** ⚗️ invoca capas de voz procesadas como vientos o pads para textura subliminal sin saturar medios: `[Reversed Vocal Pad]`, `[Distant Choir Whispers]`, `[Gregorian Sub-Bass]`.

### 1.8 · Transiciones, tensión armónica y SFX

- *Elementos Foley y dinámicas de construcción temporal (Risers/Drops).*
    - `[Reverse Reverb]`, `[Reverse Cymbal]`: Procesamiento en reversa de una cola de reverberación o platillo para crear un "barrido" de entrada fantasmal hacia el primer tiempo del compás (Downbeat).
    - `[Risers]`, `[Sweep]`, `[Impacts]`: Elementos de transición. Síntesis de ruido blanco con filtro paso-bajo automatizado `[Sweep]`, osciladores subiendo de tono `[Risers]`, o percusión sub-frecuencial `[Impacts]`.
    - `[Record Scratch]`, `[Static]`: Interrupciones de cinta/vinilo o ráfagas de ruido estático puro para cortes transversales abruptos entre secciones dispares.
    - **Ambientación Foley:** Capas de audio estéreo de fondo para inmersión espacial, como `[Rain]` (espectro de ruido blanco/rosa), `[Thunder]` (bajas frecuencias esporádicas), o `[Crowd Murmur]` (murmullo humano).
    - **Live Bootleg:** ⚗️ trata al público como un instrumento para simular grabación en vivo. style_box: `[Live Arena Soundboard Recording]`, `[Stadium Acoustics]`, `[Bootleg Tape]`; lyrics_box: `[Crowd Swell]`, `Audience Singalong`, `Muffled Crowd Cheers`.
    - **Buffer glitch:** ⚗️ bucle/cuelgue de sistema antes del estribillo (`[Hyperpop]`, `[Cyberpunk]`); repite la última vocal como disco rayado antes del drop: `[Buffer Underrun Glitch]`, `[Fake Buffering Loop]`.
