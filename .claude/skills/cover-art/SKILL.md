---
name: cover-art
description: crea un prompt para crear cover arts de las obras con gemini.
---

# Cover Art — Prompts para Gemini

Convierte una obra de Paul McChatney en **3 prompts perfectos** para que Gemini
genere portadas (cover art) en formato **1:1 (cuadrado)**.

No se trata de ilustrar la letra de forma literal, sino de **pescar el sentimiento**:
los conceptos semánticos y las cualidades ocultas que laten dentro de la canción.

---

## Cuándo se activa

El usuario pide una portada, un cover, un cover art, una carátula o "imágenes para
la canción". Si hay varias obras en juego, preguntar **de cuál**.

---

## Paso 1 — Examinar la obra

Antes de escribir nada, leer y entender la pieza completa:

1. **Letra cantable** — qué cuenta, qué imágenes evoca, qué tono tiene.
2. **Style_box / narrativa** — género, atmósfera, mood, época, paleta emocional.
3. **El subtexto** — buscar **conceptos semánticos y cualidades ocultas**:
   ¿qué se siente por debajo de las palabras? ¿qué metáfora central la sostiene?
   ¿de qué color huele? La meta es **hallar el sentimiento**, no el argumento.

Resumir en 1–2 frases internas el "núcleo emocional" antes de continuar.

---

## Paso 2 — Extraer las 3 mejores escenas fotográficas

Sacar de la obra **las 3 mejores escenas fotográficas**, sin cuotas ni reparto
obligatorio por tipo.

Las siguientes cualidades son **criterios para juzgar cuál es "mejor"**, NO
categorías a rellenar una por una:

- **Impactante** — el golpe visual: tensión, extrañeza, fuerza que detiene el scroll.
- **Representativa** — condensa la esencia de la obra en una sola escena.
- **Identificativa** — el detalle-firma que cualquiera asociaría a esta canción.

> Una escena puede cumplir varias cualidades a la vez. Si las 3 mejores resultan ser
> todas impactantes, se quedan las 3 impactantes. **Nunca descartar una escena fuerte
> solo para "cubrir" otra cualidad** — manda la calidad, no el equilibrio de tipos.

Reglas para las escenas:

- Son **fotográficas**: piensa en encuadre, luz, sujeto, ambiente.
- Pueden ser **ciencia ficción o cosas inventadas** — libertad total.
- Deben nacer del **sentimiento** hallado en el Paso 1, no de la trama literal.
- Que sean **distintas entre sí** (no tres variaciones de lo mismo).

---

## Paso 3 — Escribir los 3 prompts para Gemini

Cada escena se traduce a **un prompt en lenguaje natural**, pensado para que Gemini
lo entienda, lo ejecute y lo realice **sin fricción**:

- **Fácil de comprender**: frases claras, una idea por bloque.
- **Concreto**: sujeto, acción, entorno, luz, atmósfera y estilo.
- **Cuadrado**: indicar siempre **aspect ratio 1:1 / square composition**.
- Sin jerga técnica de Suno ni metatags — esto es para un generador de imágenes.
- Sin texto ni tipografía dentro de la imagen (salvo que el usuario lo pida).

Estructura sugerida de cada prompt:

> [Sujeto principal] + [acción/postura] + [entorno y época] + [luz y color] +
> [atmósfera/emoción] + [estilo fotográfico] + **square 1:1 composition, high detail**.

---

## Formato de salida

Una primera línea con el **núcleo emocional** detectado (para que el usuario vea de
dónde sale cada escena), seguida de tres bloques de código Markdown independientes,
listos para copiar y pegar en Gemini:

\`\`\`
COVER 1
<prompt en lenguaje natural, 1:1>
\`\`\`

\`\`\`
COVER 2
<prompt en lenguaje natural, 1:1>
\`\`\`

\`\`\`
COVER 3
<prompt en lenguaje natural, 1:1>
\`\`\`
