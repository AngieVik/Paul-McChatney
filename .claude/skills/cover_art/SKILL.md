---
name: cover_art
type: skill
description: genera 3 prompts 1:1 para Gemini a partir del sentimiento (no el argumento) de una obra.
---

# cover_art

- Convierte una obra de Paul McChatney en **3 prompts perfectos** para generar portadas (cover art) en formato **1:1**.
- No se trata de ilustrar la letra de forma literal, sino de **pescar el sentimiento**: los conceptos semánticos y las cualidades ocultas que laten dentro de la canción.

## Cuándo se activa

- **El usuario pide una portada, un cover, un cover art, una carátula o imágenes para una obra.**
- Si hay varias obras en juego, preguntar **de cuál**.

## Paso 0 — Localizar la obra

- *Antes de examinar, ubica el archivo de la obra; si hay varias en juego, pregunta de cuál.*
    - **En curso:** `_hojas_sucias/<slug>.md`.
    - **Aprobada:** `proyectos/<slug>/<slug>.md` (catalogada en `PROYECTOS.md`).
    - Si no conoces el slug, usa `proyecto` (`listar` / `retomar`) para localizar y abrir la obra.

## Paso 1 — Examinar la obra

- Antes de escribir nada, leer y entender la pieza completa:
    1. **Letra cantable** — qué cuenta, qué imágenes evoca, qué tono tiene.
    2. **Style_box / narrativa** — género, atmósfera, mood, época, paleta emocional.
    3. **El subtexto** — buscar conceptos semánticos y cualidades ocultas:
        - ¿qué se siente por debajo de las palabras? ¿qué metáfora central la sostiene?
        - ¿de qué color huele? La meta es **hallar el sentimiento**, no el argumento.

- Resumir en 1–2 frases internas el "núcleo emocional" antes de continuar.

## Paso 2 — Extraer las 3 mejores escenas fotográficas

- Sacar de la obra **las 3 mejores escenas fotográficas**, sin cuotas ni reparto obligatorio por tipo.

- Las siguientes cualidades son **criterios para juzgar cuál es "mejor"**, NO categorías a rellenar una por una:
    - **Impactante** — el golpe visual: tensión, extrañeza, fuerza que detiene el scroll.
    - **Representativa** — condensa la esencia de la obra en una sola escena.
    - **Identificativa** — el detalle-firma que cualquiera asociaría a esta canción.

- Una escena puede cumplir varias cualidades a la vez. Si las 3 mejores resultan ser todas impactantes, se quedan las 3 impactantes. **Nunca descartar una escena fuerte solo para "cubrir" otra cualidad** — manda la calidad, no el equilibrio de tipos.

- Reglas para las escenas:
    - Son **fotográficas**: piensa en encuadre, luz, sujeto, ambiente.
    - Pueden ser **ciencia ficción o cosas inventadas** — libertad total.
    - Deben nacer del **sentimiento** hallado en el Paso 1, no de la trama literal.
    - Que sean **distintas entre sí** (no tres variaciones de lo mismo).

## Paso 3 — Escribir los 3 prompts

- Cada escena se traduce a **un prompt en lenguaje natural**, pensado para que se entienda, se ejecute y se realice **sin fricción**:
    - **Fácil de comprender**: frases claras, una idea por bloque.
    - **Concreto**: sujeto, acción, entorno, luz, atmósfera y estilo.
    - **Cuadrado**: indicar siempre **aspect ratio 1:1 / square composition**.
    - Sin jerga técnica ni tags: esto es para un generador de imágenes.
    - Sin texto ni tipografía dentro de la imagen, salvo que el usuario lo pida.

- Estructura sugerida de cada prompt:

```text
[Sujeto principal] + [acción/postura] + [entorno y época] + [luz y color] + [atmósfera/emoción] + [estilo fotográfico] + **square 1:1 composition, high detail**.
```

## Formato de salida

Una primera línea con el **núcleo emocional** detectado (para que el usuario vea de dónde sale cada escena), seguida de tres bloques de código, listos para copiar y pegar en Gemini:
    ```text  
    COVER 1  
    `prompt en lenguaje natural, 1:1`  
    ```
    ```text  
    COVER 2  
    `prompt en lenguaje natural, 1:1`  
    ```
    ```text  
    COVER 3  
    `prompt en lenguaje natural, 1:1`  
    ```

## Entra → Sale

- **Entra:** una obra terminada (`letra + style_box/narrativa`).
- **Sale:** el núcleo emocional detectado + 3 prompts en lenguaje natural 1:1.

## Relación

- Posterior a una obra ya creada; independiente del flujo de 5 fases de `produccion`.
- Localiza la obra con `proyecto`: `_hojas_sucias/<slug>.md` en curso, `proyectos/<slug>/<slug>.md` aprobada, catálogo `PROYECTOS.md`.
