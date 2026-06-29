# efectos
*Efectos de audio, post-producción y control de silencios y pausas para la mezcla. Fase 3.*
*Consulta por búsqueda (grep) o salto por Índice.*

---

## Índice
`1 · Control de silencios y pausas`
`2 · Efectos de audio y post-producción`
    `2.1 · Modulación, Distorsión y Espacio`
    `2.2 · Efectos Vocales Específicos`
    `2.3 · Texturas Sonoras y Producción`
    `2.4 · Efectos de Transición, Tensión y SFX`
    `2.5 · Hacks de Inpainting\Style`

## 1 · Control de silencios y pausas
- `[quick Silence]`: corte repentino; detiene los instrumentos de forma súbita (en línea independiente).
- `(pause)`: pequeño respiro o pausa vocal; úsala junto a las palabras de un verso.
- `[Pausa instrumental]`: silencia la voz para dar paso a una breve melodía de transición entre estrofas.
- `[fermata]`: sostiene y alarga el sonido de una nota antes de un silencio, creando tensión.
- `[Silence]`: pausa absoluta o atmósfera ambiental en la mezcla (en línea independiente).

```text
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

## 2 · Efectos de audio y post-producción

### 2.1 · Modulación, Distorsión y Espacio
- `[Hall Reverb]` \ `[Room Reverb]` \ `[No Reverb]`: control del espacio acústico (gran sala · habitación íntima · seco y directo).
- `[Plate Reverb] \ [Spring Reverb]`: Reverberación metálica vintage (Plate) o el clásico efecto de guitarra surf de muelle (Spring).
- `[Chorus]` \ `[Flanger]` \ `[Phaser]`: Efectos de modulación espacial. `[Chorus]` engrosa el sonido, `[Flanger]` crea un efecto de barrido tipo "avión", y `[Phaser]` cambia la fase de la señal.
- `[Tremolo]`: Modulación rápida de amplitud o volumen.
- `[Overdrive]` \ `[Distortion]` \ `[Fuzz]`: Control de saturación. `[Overdrive]` da calidez analógica, `[Distortion]` aplica saturación pesada, y `[Fuzz]` ofrece una distorsión rasposa y vintage.
- `[Echo]`: acústica de retardo en la voz sin sumar sílabas a la métrica.
- `[Slapback Delay]`: eco vocal muy corto y rápido.
- `[Ping Pong Delay]`: eco que rebota de izquierda a derecha en el panorama estéreo.

### 2.2 · Efectos Vocales Específicos
- `[Vocal chop]`: recortes de voz como instrumento rítmico durante un drop o puente.
- `[Stutter-vocals]`: tartamudeo o corte rítmico digital en la pista.
- `[Robotic voice filter]` \ `[Vocoder]`: filtro sintético o robótico sobre la voz.
- `[AutoTune]`\ `[No AutoTune]`: Fuerza la corrección de tono digital muy notoria (común en trap\pop moderno), o la previene explícitamente para lograr voces más orgánicas.
- `[Telephone Effect]` \ `[Filtered Vocals]`: Filtra las frecuencias graves y agudas para que la voz suene como si viniera a través de un teléfono antiguo, un megáfono o una radio.
- `[Distorted Vocals]`: Voz con saturación directa, ideal para rock, metal o géneros industriales.

### 2.3 · Texturas Sonoras y Producción
- `[Lo-fi]` \ `[Tape-Saturated]` \ `[Vinyl Hiss]` \ [Vinyl Crackle]: Añaden calidez analógica, degradación intencional, ruido de cinta magnética o el característico crujido de los discos de vinilo.
- `[Glitch]` \ `[Granular]`: Generan artefactos digitales, tartamudeos robóticos o un muestreo microscópico y fragmentado del audio, ideal para música experimental o electrónica.
- `[Sidechaining]`: Efecto de "bombeo" rítmico que comprime la mezcla cada vez que golpea el bombo, esencial en EDM, House y Future Bass.
- `[Punchy]` \ `[Polished]` \ `[Raw]`: Directrices de mezcla general. `[Punchy]` da mayor impacto a las frecuencias graves y percusiones, `[Polished]` genera una mezcla comercial súper limpia, y `[Raw]` deja el sonido crudo y sin pulir (ideal para punk o garage rock).

### 2.4 · Efectos de Transición, Tensión y SFX
- `[Reverse Reverb]` \ `[Risers]` \ `[Impacts]`: Construcción de impacto. 
    `[Reverse Reverb]` crea una entrada ascendente y fantasmal a una frase. 
    `[Risers]` aumenta la tensión mediante ruido o sintetizadores antes de un "drop".
    `[Impacts]` añade golpes dramáticos a mezcla.
- `[Record Scratch]` \ `[Static]`: El clásico "scratch" de tocadiscos o ráfagas de estática \ ruido blanco para hacer transiciones agresivas entre secciones.
- Ambientación Natural (Foley): Puedes incluir capas de fondo usando etiquetas descriptivas como `[Rain]` (lluvia), `[Thunder]` (truenos), `[Ocean Waves]` (olas) o `[Fire Crackling]` (fuego crepitante).

### 2.5 · Hacks de Inpainting\Style
- Comandos textuales (no siempre entre corchetes, sino también en el cuadro de letras o estilos) como `smooth consonants`, `no vocal crackle` ayudan a limpiar chasquidos vocales en posproducción.
- Comandos negativos de exclusión como `-high pitched noises`, `-bright digital shimmer` funcionan como filtros correctores para domar artefactos agudos generados por Suno.