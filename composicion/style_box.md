---
name: "style_box"
type: "composicion"
description: "Construye el style_box de una obra, define el núcleo estilístico optimizando el espacio en 12–20 tags, fuerza resultados emergentes y no deterministas por colisión de opuestos (lingüístico-tonal, rítmica y tímbrica)."
---

# style_box

- *Archivo técnico de referencia para construir, revisar y depurar el `style_box`.*

---

## Referencias

- **Skill consumidora:** `.claude/skills/style_box/SKILL.md`
- **Mapa propio:** `.claude/rules/style_box.md`
- **Canon de tags:** `buscar_tag` → `.claude/rules/chupilista.md` → `chupilista/`
- **Diseño conceptual previo:** `fusionar`

---

## Índice

`1 · Etiquetas style_box`
    `1.1 · Tag Anchoring`
    `1.2 · El anclaje temporal`
    `1.3 · Anclaje Idiomático`
    `1.4 · Canon y creación controlada`
    `1.5 · Orden jerárquico del style_box`
`2 · Fusión y frecuencias`
    `2.1 · Fusión lingüístico-tonal`
    `2.2 · Fusión regional`
    `2.3 · Contraste de frecuencias`
    `2.4 · Expansión estéreo`
    `2.5 · Fusión semántica extrema`
`3 · Dinámicas rítmicas y estructurales`
    `3.1 · Etiquetas rítmicas extremas`
    `3.2 · Choque de cuadrículas`
    `3.3 · Slow Groove, Fast Energy`
    `3.4 · Separación rítmica-atmosférica`
`4 · Colisión tímbrica`
    `4.1 · Textural Bleed`
    `4.2 · Instrumental Hijacking`
    `4.3 · Hack de timbre (choque cognitivo)`

---

## 1 · Etiquetas style_box

- *Fundación técnica de la obra. El canon de cada categoría se recupera vía `buscar_tag` (mapa `.claude/rules/chupilista.md`); los módulos indican el origen canónico, no una lectura directa a `chupilista/`.*
    - **Core Genres and Subgenres** (`chupilista` · 01): Fundación rítmica y lenguaje armónico base, siempre al principio.
    - **Instrumentation and Stems** (`chupilista` · 03): Instrumentos estructurales base y/o protagonistas; usa Tag Anchoring con 3-4 instrumentos.
    - **Vocal Persona and Timbre** (`chupilista` · 04): Descriptor base de voz.
    - **Rhythm and Tempo** (`chupilista` · 05): BPM, groove, modulaciones métricas, cambios de tempo o pausas.
    - **Music Theory Harmony and Scales** (`chupilista` · 07): Tonalidades específicas o progresiones de acordes.
    - **Dynamics and Intensity** (`chupilista` · 08): Dinámica o intensidad.
    - **Experimental Modes** (`chupilista` · 10): Fusiones inusuales.
    - **Vocal Delivery and Expressivity** (`chupilista` · 12): Descriptor base de voz.

- **Menos es más:** 12–20 tags bien elegidas rinden más que 40.
- **Estilo, no artista:** describe el sonido; nunca nombres propios de artistas reales.
- **`[Epic]` siempre con apoyo:** solo queda vacío.
    - **Ejemplo:** `[Epic Orchestral]`, `[Epic Cinematic]`.
- **Ghost tag:** un tag muy específico al final del `style_box`.
    - **Ejemplo:** `[Hurdy-gurdy]`.

---

### 1.1 · Tag Anchoring

- *Para fijar instrumentos base y/o protagonistas, añade 2–4 instrumentos clave y deja que el modelo infiera el resto por el género; añádelos además en el `lyrics_box` si deben actuar dentro de la estructura.*
    - **Ejemplo:** `[Pop Rock, Lead Tenor Sax]`.

### 1.2 · El anclaje temporal

- *Añadir una década o época al género ancla la precisión del modelo, asocia cada época a técnicas de producción concretas y reduce alucinaciones sónicas.*
    - **Ejemplo:** `[80s Synth Pop]`, `[90s Grunge]`, `[1980s]`, `[Vintage 90s]`, `[Modern Pop Polish]`.

### 1.3 · Anclaje Idiomático

- *Aplica la siguiente regla para asegurar la pronunciación.*
    - Si el género es originario de la cultura del idioma objetivo, omite el tag de idioma.
        - **Ejemplo:** `[Flamenco]`, `[Reggaetón]`.
    - Si el género es global o no está ligado al idioma objetivo, antepón el idioma al género.
        - **Ejemplo:** `[Spanish Heavy Metal]`, `[Spanish Pop]`.

### 1.4 · Canon y creación controlada

- *El canon de `chupilista` se recupera mediante `buscar_tag`; sirve como ancla fiable, no como límite creativo absoluto.*
    - Si existe una tag canónica suficiente, úsala.
    - Si no existe una tag exacta, puede usarse una creación controlada.
    - Toda creación controlada debe tener función sonora, narrativa o técnica.
    - Las tags creadas se redactan en inglés técnico, compacto y musicalmente útil.
    - **Ejemplo:** `Andalusian Drumstep`, `Symphonic Hardtek`, `Rustic Industrial Flamenco`.

### 1.5 · Orden jerárquico del style_box

- *Ordena el `style_box` de mayor a menor dominancia sonora.*
    - género base o fusión principal;
    - idioma o anclaje cultural si procede;
    - atmósfera;
    - instrumentación protagonista;
    - perfil vocal;
    - ritmo, tempo o groove;
    - producción y textura;
    - ghost tag o detalle diferencial.

---

## 2 · Fusión y frecuencias

- *Máximo 2 géneros principales; para más, añade un tag de fusión explícito.*

### 2.1 · Fusión lingüístico-tonal

- *Cruza un gentilicio o grupo étnico, introduce escalas microtonales y ritmos asimétricos.*
    - **Ejemplo:** `[Mandarin Math Rock]`, `[Urdu Electropop]`.

### 2.2 · Fusión regional

- *Tags de raíz cruda con prefijo geográfico opuesto: fuerza escalas latinas sobre timbres crudos de Delta Blues; saca guitarras e instrumentos nativos únicos.*
    - **Ejemplo:** `[Havana American Primitivism]`, `[Tokyo Drumstep]`, `[Russian Salsa]`.

### 2.3 · Contraste de frecuencias

- *Choca texturas limpias contra hiper-saturación: activa contraste de rango, compresión multibanda agresiva y voces nítidas flotando sobre instrumentales pesados.*
    - **Ejemplo:** `[Choral Ambient Noise Wall]`, `[Dreamy Fife And Drum Blues]`.

### 2.4 · Expansión estéreo

- *Combina subgéneros oscuros de internet con coros eclesiásticos o acústicos puros: texturas estéreo amplísimas y contrastes dinámicos pesados.*
    - **Ejemplo:** `[Drift Phonk, Gregorian Chant]`.

### 2.5 · Fusión semántica extrema

- *Inventa géneros principales cruzando conceptos. Añade subgéneros de apoyo en minúsculas.*
    - **Ejemplo:** `[Russian Salsa, Havana Mix]`, `[Symphonical Hardtek, Operistic Raggatek]`.

---

## 3 · Dinámicas rítmicas y estructurales

### 3.1 · Etiquetas rítmicas extremas

- *Combina BPMs absurdos con anclajes atmosféricos: el choque limpia las frecuencias medias para que entren las voces y genera un máster más agresivo y definido.*
    - **Ejemplo:** `[Breakcore, Monastic Choir]`.

### 3.2 · Choque de cuadrículas

- *Choca un género de cuadrícula rígida con uno de groove líquido: síncopas y polirritmias brutales, evitando ritmos robóticos.*
    - **Ejemplo:** `[Math Rock, Bossa Nova]`, `[Industrial Techno, Afrobeat]`.

### 3.3 · Slow Groove, Fast Energy

- *Cabeceo lento con percusión hiperactiva por debajo: fija la cuadrícula general en el `style_box` y el comportamiento percusivo en el `lyrics_box`.*
    - **Ejemplo:** `[85 BPM, Lo-fi Groove]`.

### 3.4 · Separación rítmica-atmosférica

- *Divide el prompt de estilo en dos capas separadas: capa rítmica y paleta atmosférica. Fuerza una mezcla más limpia y profesional, ideal para electrónica o DJ.*
    - **Ejemplo:** `[DRUM LOOP: 120 BPM organic house]`, `[Organic house atmosphere, warm ethnic vocal samples]`.

---

## 4 · Colisión tímbrica

### 4.1 · Textural Bleed

- *Invoca la física del formato analógico en vez de pedir "Lo-Fi": cruzado con voces nítidas, el modelo divide el render entre instrumental viejo y voz moderna de cabina.*
    - **Ejemplo:** `[Melted Cassette Hiss]`, `[Dusty Vinyl Crackle]`, `[Degraded Wax Cylinder + Close-Mic Hi-Fi Vocal]`.

### 4.2 · Instrumental Hijacking

- *Fuerza un instrumento acústico raro dentro de un género sintético rígido: sintetiza su tono con osciladores y genera leads alienígenas.*
    - **Ejemplo:** `[Didgeridoo Cyberpunk]`, `[Bagpipe Trap]`, `[Hurdy-Gurdy Synthwave]`.

### 4.3 · Hack de timbre (choque cognitivo)

- *Cruza tags físicas extremas de voz con géneros que no les corresponden: distorsiona la voz central manteniendo la percusión limpia.*
    - **Ejemplo:** `[Death Metal Growl]` o `[Vocal Fry]` sobre instrumental de `[Smooth Jazz]` o `[Bossa Nova]`.
