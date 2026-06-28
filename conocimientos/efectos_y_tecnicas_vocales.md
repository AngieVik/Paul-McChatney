# efectos_y_tecnicas_vocales

**Archivos vivos** Todos los documentos de `conocimientos/` evolucionan, creando una entrada en `changelog_conocimientos`

---

## PUNTUACIÓN EN LA LETRA

**Función:** Aplicación de signos para dar personalidad, textura y ritmo a las voces.

### Uso Estratégico de Paréntesis `( )`

Inyecta voces secundarias o coros. *Advertencia:* El texto en paréntesis se canta y suma sílabas a la métrica.

* **Coros y Apoyos:** `hay que ser torero (oleee)` | `(Nadie me puede parar (no, no, no))`
* **Interjecciones Secundarias:** `(¡ay!)` | `(¡ouch!)`
* **Ecos Forzados:** Repite la palabra en paréntesis para el eco. Ej: `I want it all (all)`
* **Coros sin palabras:** Sílabas armónicas de fondo. Ej: `(ai aiiiiAaAaaiiII)` | `(nainononainonaaa)`

### Énfasis Especial `" "`

Simula un pensamiento interno o una voz interior en la interpretación.

* **Ejemplo:** `"ser o no ser, esa es la cuestión..."`

### Interjección Espontánea `¡ !`

Grito con aumento de energía, de manera cómica o teatral.

* **Ejemplo:** `¡ay!` | `¡ouch!`

---

## ETIQUETAS DE DIRECCIÓN VOCAL

### Roles Específicos y Duetos

Abre cada línea de diálogo con la etiqueta del personaje estricta para evitar que la IA invierta las voces.

* **Roles:** `[Announcer]` | `[Reporter]` | `[Child voice]` | `[Giggling]`
* **Duetos:** `[Male] Hola` | `[Female] Adiós`

### Armonías y Coros Multicapa

* **`[overlapping]`:** Fuerza a dos voces distintas a cantar armónicamente de forma simultánea.
* **`[multiple voice chorus satb]`:** Genera un coro profesional con múltiples capas simultáneas (soprano | alto | tenor | bajo).

### 📌 Ejemplo de Aplicación

```t
[Male] I was walking down the street "what a day"
[Female] (ooo) Walking down the street! (¡hey!)
[overlapping] We met at the corner!
[multiple voice chorus satb] And the choir started to sing
```

---

## INGENIERÍA DE PERSONAJE Y ESTRUCTURA

### Aislamiento Vocal Temporal

Aísla cambios de técnica en medio de una sección usando transiciones claras para mantener el contexto de la IA.

* **Estructura:** `[Sección A]` -> texto -> `[Técnica Temporal]` -> texto -> `[Sección A continues]`

### Persona Stacking (Voz desde Texto)

Construye un personaje vocal inquebrantable apilando estas 4 capas en una sola etiqueta al inicio del Style Box:

1. **Demografía:** edad | género | tipo de voz
2. **Entrega Técnica:** susurrado | potente | claro
3. **Contexto Emocional:** melancólico | confiado
4. **Anclaje Sonoro:** referencia descriptiva a un estilo o timbre (escríbelo inexactamente si es muy famoso).

### 📌 Ejemplo de Aplicación

```t
[Style Box: 25 year old Female | whispery and close | melancholic | breathy indie-pop voice]

[Verse 1]
I remember the days when the sun was cold

[Chorus]
[Vocal: Hall Reverb]
Now I'm shouting to the walls!
[Chorus continues -> dry vocal]
And waiting for the echo to fall.
```

---

## CONTROL DE SILENCIOS Y PAUSAS

* **`[quick Silence]`:** Corte repentino. Detiene los instrumentos de forma súbita (en línea independiente).
* **`(pause)`:** Pequeño respiro o pausa vocal. Úsala estratégicamente junto a las palabras en un verso.
* **`[Pausa instrumental]`:** Silencia la voz para dar paso a una breve melodía de transición entre estrofas.
* **`[fermata]`:** Sostiene y alarga el sonido de una nota antes de un silencio, creando tensión.
* **`[Silence]`:** Pausa absoluta o atmósfera ambiental en la mezcla de audio (en línea independiente).

### Ejemplo de Aplicación

```t
[Verse 1]
Caminando por la ciudad (pause) sin mirar atrás
[fermata] Y el tiempo se detuvo
[quick Silence]

[Chorus]
¡Y de repente el mundo estalla!
[Pausa instrumental]

[Verse 2]
[Silence]
Vuelve la calma a la habitación
```

---

## TÉCNICAS DE INTERPRETACIÓN VOCAL

* **`[Falsetto]`:** Voz aguda, ligera y con aire.
* **`[Vibrato]`:** Oscilación controlada y prolongada del tono al final de las frases.
* **`[Melismatic]`:** Alarga una sola sílaba moviéndose a través de varias notas musicales distintas.
* **`[Staccato Vocals]`:** Notas muy cortas, picadas y separadas.
* **`[Legato Vocals]`:** Canto extremadamente suave y conectado, sin pausas entre notas.
* **`[Performance: conversational]`:** Voz "habla-canto", muy íntima, cercana y natural.
* **`[Vocal: breathy]`:** Añade realismo forzando ruidos de respiración audibles o suspiros.
* **Texturas de Tono:** `[Warm Voice]` (cálida) | `[Bright Voice]` (brillante).

---

## EFECTOS DE AUDIO Y POST-PRODUCCIÓN

* **`[Echo]`:** Acústica de retardo en la voz sin sumar sílabas a la métrica.
* **`[Robotic voice filter]` / `[Vocoder]`:** Aplica un filtro sintético o robótico a la voz.
* **`[Stutter-vocals]`:** Efecto de tartamudeo o corte rítmico digital en la pista.
* **`[Vocal chop]`:** Recortes de voz como instrumento rítmico durante un drop o puente.
* **`[Slapback Delay]`:** Eco vocal muy corto y rápido.
* **`[Ping Pong Delay]`:** Eco que rebota de izquierda a derecha en el panorama estéreo.
* **`[Hall Reverb]` / `[Room Reverb]` / `[No Reverb]`:** Control del espacio acústico (gran sala de conciertos | habitación íntima | seco y directo).
