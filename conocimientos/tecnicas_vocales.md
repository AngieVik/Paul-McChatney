# tecnicas_vocales
*Efectos y técnicas para dar personalidad y textura a las voces: puntuación, dirección vocal, persona stacking e interpretación. Fase 3.*
*Consulta por búsqueda (grep) o salto por Índice*

---

## Índice
`1 · Puntuación en la letra`
`2 · Etiquetas de dirección vocal`
`3 · Ingeniería de personaje y estructura`
`4 · Técnicas de interpretación vocal`

---

## 1 · Puntuación en la letra
Signos para dar personalidad, textura y ritmo a las voces.

### Paréntesis `( )` — voces secundarias
Inyecta voces secundarias o coros. *Advertencia:* el texto en paréntesis se canta y suma sílabas a la métrica.
- **Coros y apoyos:** `hay que ser torero (oleee)` · `(Nadie me puede parar (no, no, no))`
- **Interjecciones secundarias:** `(¡ay!)` · `(¡ouch!)`
- **Ecos forzados:** repite la palabra en paréntesis para el eco. Ej: `I want it all (all)`
- **Coros sin palabras:** sílabas armónicas de fondo. Ej: `(ai aiiiiAaAaaiiII)` · `(nainononainonaaa)`

### Comillas `" "` — énfasis especial
Simula un pensamiento interno o voz interior. Ej: `"ser o no ser, esa es la cuestión..."`

### Exclamación `¡ !` — interjección espontánea
Grito con aumento de energía, cómico o teatral. Ej: `¡ay!` · `¡ouch!`

## 2 · Etiquetas de dirección vocal

### Roles y duetos
Abre cada línea de diálogo con la etiqueta del personaje estricta para evitar que la IA invierta las voces.
- **Roles:** `[Announcer]` · `[Reporter]` · `[Child voice]` · `[Giggling]`
- **Duetos:** `[Male] Hola` · `[Female] Adiós`

### Armonías y coros multicapa
- **`[overlapping]`:** fuerza a dos voces distintas a cantar armónicamente de forma simultánea.
- **`[multiple voice chorus satb]`:** genera un coro profesional con múltiples capas (soprano · alto · tenor · bajo).

```text
[Male] I was walking down the street "what a day"
[Female] (ooo) Walking down the street! (¡hey!)
[overlapping] We met at the corner!
[multiple voice chorus satb] And the choir started to sing
```

## 3 · Ingeniería de personaje y estructura

### Aislamiento vocal temporal
Aísla cambios de técnica en medio de una sección con transiciones claras para mantener el contexto de la IA.
`[Sección A]` -> texto -> `[Técnica Temporal]` -> texto -> `[Sección A continues]`

### Persona Stacking (voz desde texto)
Construye un personaje vocal inquebrantable apilando estas 4 capas en una sola etiqueta al inicio del style_box:
1. **Demografía:** edad · género · tipo de voz
2. **Entrega técnica:** susurrado · potente · claro
3. **Contexto emocional:** melancólico · confiado
4. **Anclaje sonoro:** referencia descriptiva a un estilo o timbre (escríbelo inexactamente si es muy famoso).

```text
[Style Box: 25 year old Female | whispery and close | melancholic | breathy indie-pop voice]

[Verse 1]
I remember the days when the sun was cold

[Chorus]
[Vocal: Hall Reverb]
Now I'm shouting to the walls!
[Chorus continues -> dry vocal]
And waiting for the echo to fall.
```

## 4 · Técnicas de interpretación vocal
- **`[Falsetto]`:** voz aguda, ligera y con aire.
- **`[Vibrato]`:** oscilación controlada y prolongada del tono al final de las frases.
- **`[Melismatic]`:** alarga una sílaba moviéndose por varias notas distintas.
- **`[Staccato Vocals]`:** notas muy cortas, picadas y separadas.
- **`[Legato Vocals]`:** canto suave y conectado, sin pausas entre notas.
- **`[Performance: conversational]`:** voz "habla-canto", íntima y natural.
- **`[Vocal: breathy]`:** añade realismo forzando respiraciones o suspiros audibles.
- **Texturas de tono:** `[Warm Voice]` (cálida) · `[Bright Voice]` (brillante).
