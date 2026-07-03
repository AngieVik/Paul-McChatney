# tecnicas_vocales
*Arquitecturas de identidad (Persona Stacking), dirección interpretativa.*
*Recordatorio: consulta por búsqueda (grep) o salto por sección.*

## Índice
`1 · Puntuación en la letra`
    `1.1 · Paréntesis — Voces secundarias`
    `1.2 · Comillas — Énfasis especial`
    `1.3 · Exclamación — Interjección espontánea`
`2 · Etiquetas de dirección vocal`
    `2.1 · Persona Stacking`
    `2.2 · El Anclaje de Identidad Vocal`
    `2.3 · Prevención de mutación del cantante`
    `2.4 · Dirección de Interpretación Dinámica`
    `2.5 · Técnicas de interpretación vocal`
    `2.6 · Aislamiento vocal temporal`
    `2.7 · Roles y duetos`
    `2.8 · Armonías y coros multicapa`
`3 · Efectos de audio y post-producción`
    `3.1 · Control de silencios y pausas`
    `3.2 · Modulación, distorsión y espacio espacial`
    `3.3 · Efectos vocales específicos`
    `3.4 Glitch forzado y stutter vocal`
    `3.5 · Acústica física y microfonía`
    `3.6 · Parámetros de Inpainting y estilo general`
    `3.7 · Texturas sonoras y compresión`
    `3.8 · Transiciones, tensión armónica y SFX`

---

## 1 · Puntuación en la letra
*Signos tipográficos para manipular la métrica, la textura y el ritmo del modelo de generación.*

### 1.1 · Paréntesis — Voces secundarias
- *Inyección de coros y contrapuntos. Advertencia empírica: el modelo procesa el texto en paréntesis como material cantable, sumando sílabas a la métrica general de la frase.*
    - **Coros y apoyos:** 
        * **Ejemplo:**
            hay que ser torero (oleee) 
            Nadie me puede parar (no, no, no)
    - **Interjecciones secundarias:** 
        * **Ejemplo:**
            (¡ay!) 
            (¡ouch!)
    - **Ecos forzados (Delay Manual):** repetición de la palabra final. 
        * **Ejemplo:** 
            I want it all (all)
    - **Coros sin palabras (Vocalizaciones):** sílabas armónicas de fondo. 
        * **Ejemplo:** 
            (ai aiiiiAaAaaiiII)
            (nainononainonaaa)

### 1.2 · Comillas — Énfasis especial
- *Aísla la frase, induciendo al motor a simular un pensamiento interno o un cambio drástico en la articulación (frecuentemente hablado o susurrado).
    * **Ejemplo:** 
        "ser o no ser, esa es la cuestión..."

### 1.3 · Exclamación — Interjección espontánea
- *Fuerza picos dinámicos. Genera un ataque vocal con aumento de energía, a menudo con carácter teatral o percusivo.*
    * **Ejemplo:** 
        ¡ay!
        ¡ouch!

---

## 2 · Etiquetas de dirección vocal
*Metadatos de control directo sobre el timbre y la ejecución del intérprete virtual.*

### 2.1 · Persona Stacking
- *Técnica de apilamiento para construir un personaje vocal inquebrantable. Se define mediante 4 capas estructuradas en una sola etiqueta al inicio del `lyrics_box`.*
    1. **Demografía:** edad, género, tipo de voz.
    2. **Entrega técnica:** susurrado, potente, claro.
    3. **Contexto emocional:** melancólico, agresivo, confiado.
    4. **Anclaje sonoro:** referencia acústica a un género o timbre.
        * **Ejemplo:**
            `[25 year old Female, whispery and close, melancholic, breathy indie-pop voice]`
            
            `[Verse 1]`
            I remember the days when the sun was cold

### 2.2 · El Anclaje de Identidad Vocal
- *Suno determina la identidad y el "ADN" de la voz en el **segundo cero** de la generación . Para evitar mutaciones tímbricas o cambios de género inesperados, es vital fijar la voz antes de que comience la interpretación.*
    * **Técnica de la "Línea Cero":** Coloca una etiqueta de **Persona Stacking** en la primera línea del `lyrics_box`, separada por un salto de línea del resto de la letra.
        * **Ejemplo:**
            `[Vocal Identity: Close-mic breathy alto, intimate]`
            `[Verse 1]`
            Hoy el silencio pesa más que ayer...

### 2.3 · Prevención de mutación del cantante
- *Forzado del anclaje del ADN vocal. Se requiere inyectar la etiqueta descriptiva original inmediatamente después de un pasaje instrumental largo.*
    * **Ejemplo:**
        `[Instrumental Solo Ends]`
        `[Vocal Return: Same Male raspy baritone]`
        `[Verse 2]`

### 2.4 · Dirección de Interpretación Dinámica
- *A diferencia de las etiquetas de estilo globales, la v5.5 responde con alta precisión a comandos de actuación inyectados directamente entre las líneas de la letra.*
    * **Uso de descriptores locales:** Inserta términos entre paréntesis `( )` para dictar cambios emocionales o físicos en la entrega sin alterar el estilo general de la banda.
    * **Comandos validados:** `(whispered)`, `(shouted)`, `(conversational)`, `(borderline shouted)`, `(breathy)`.
    * **Eficacia:** Esta técnica es superior para crear **contrastes dinámicos** que las etiquetas de estilo estáticas, permitiendo que la interpretación "respire" con la narrativa. 
        * **Ejemplo:** 
            Pasar de un susurro a un grito.

### 2.5 · Técnicas de interpretación vocal
- *Directrices de articulación y fonación para cantantes.*
    - `[Falsetto]`: Registro agudo, ligero y con alto contenido de aire (falsete).
    - `[Vibrato]`: Oscilación controlada y prolongada del tono al final de las frases.
    - `[Melismatic]`: Adorno vocal que alarga una sola sílaba moviéndose por varias notas (melisma).
    - `[Staccato Vocals]`: Ataques muy cortos, picados y sin sostenimiento.
    - `[Legato Vocals]`: Canto suave y conectado, transición fluida entre frecuencias.
    - `[Performance: conversational]`: Voz "habla-canto" (*Sprechgesang*), íntima y natural.
    - `[Vocal: breathy]`: Añade ruido blanco orgánico forzando respiraciones o suspiros audibles.
- *Texturas de tono:*
    - `[Warm Voice]` Ecualización con realce en medios-bajos.
    - `[Bright Voice]` Realce en frecuencias altas.

### 2.6 · Aislamiento vocal temporal
- *Estructura de aislamiento para evitar el sangrado de técnicas (bleeding) entre secciones.*
    * **Sintaxis: `[Sección A]` -> texto -> `[Técnica Temporal]` -> texto -> `[Sección A continues]`**
        * **Ejemplo:**
            `[Chorus]`
            `[Vocal: Hall Reverb]`
            `Now I'm shouting to the walls!
            `[Chorus continues -> dry vocal]`
            `And waiting for the echo to fall.

### 2.7 · Roles y duetos
- *Utiliza etiquetas de identidad vocal al inicio de cada línea para minimizar el intercambio accidental de voces y fijar el carácter.*
    * **Ejemplo:**
        `[Verse: Male and Female conversation]`
        `[Male Vocal: warm, intimate]` Dime por qué te vas sin decir adiós.
        `[Female Vocal: breathy, emotional]` Porque el silencio duele menos que tu voz.
- *Unísono y armonías, para partes conjuntas, la etiqueta [Both] o [Unison] es más efectiva que repetir ambos géneros.*
    * **Ejemplo:**
        `[Chorus: High Energy, Power Harmonies]`
        `[Both: unison, powerful vocals]` Nuestro tiempo se terminó,
        `[Both: harmony, vibrato]` el fuego en cenizas se convirtió.
- *Roles narrativos, define personajes con texturas vocales y propósitos comunicativos opuestos.*
    * **Ejemplo:**
        `[Verse: Dramatic Roles, Contrasting Delivery]`
        `[Announcer: authoritative, cinematic]` Señoras y señores, el tiempo se ha detenido.
        `[Reporter: urgent, frantic, filtered]` ¡La gente corre, el cielo se ha vuelto púrpura!
- *Performance Direction, dirige la actitud física de cada cantante para evitar que las voces suenen planas.-
    * **Ejemplo:**
        `[Chorus: Male and Female Duet, Power Harmonies]`
        `[Male Vocal: raspy, restrained]` Caminé mil leguas solo para encontrar tu fuego.
        `[Female Vocal: ethereal, silky delivery]` Y yo te esperé en la sombra, ignorando todo ruego.

### 2.8 · Armonías y coros multicapa
- *Directrices algorítmicas de polifonía.*
    - `[overlapping]`: Fuerza a dos entidades vocales a superponerse temporalmente.
    - `[multiple voice chorus satb]`: Invoca una estructura coral profesional a cuatro voces (Soprano, Alto, Tenor, Bajo).

---

