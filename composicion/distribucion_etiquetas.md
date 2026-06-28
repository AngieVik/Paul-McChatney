# distribucion_etiquetas
*Clasifica y distribuye las etiquetas por caja operativa (style_box vs lyrics_box). Fases 1 y 3.*
*Recordatorio: consulta por búsqueda (grep) o salto por Índice.*

---

## Índice
`1 · Etiquetas del style_box`
`2 · Etiquetas del lyrics_box`
`3 · Definición del style_box`
`4 · exclude_styles`

---

## 1 · Etiquetas del style_box
Fundación técnica de la obra.
- **Core Genres and Subgenres:** fundación rítmica y lenguaje armónico base (siempre al principio).
- **Instrumentation and Stems:** instrumentos estructurales base y/o protagonistas; usa Tag Anchoring.
- **Vocal Persona and Timbre / Vocal Delivery and Expressivity:** descriptor base de 1–2 palabras.
- **Rhythm and Tempo:** BPM, groove, modulaciones métricas, cambios de tempo o pausas.
- **Music Theory Harmony and Scales:** tonalidades específicas o progresiones de acordes.
- **Dynamics and Intensity:** dinámica o intensidad.
- **Experimental Modes:** fusiones inusuales.

## 2 · Etiquetas del lyrics_box
Entre corchetes `[ ]`, marcan el momento exacto de un evento temporal dentro de la narrativa.
- **Atmosphere and Mood:** etiqueta global `[MOOD]` o corchetes temporales.
- **Instrumentation and Stems:** momentos donde un instrumento toma el protagonismo o entra en la mezcla (ej. `[Guitar Solo]`); usa Tag Anchoring.
- **Vocal Persona and Timbre / Vocal Delivery and Expressivity:** Persona Stacking completo al inicio; segundas voces, duetos o coros puntuales intercalados junto a la letra para alterar intención, técnica o volumen.
- **Rhythm and Tempo:** reafirmar o cambiar BPM, groove, modulaciones, tempo o pausas.
- **Song Structure and Sections:** elementos estructurales y secciones; dictan el flujo narrativo.
- **Music Theory Harmony and Scales:** crea o modula entre tonalidades o progresiones.
- **Dynamics and Intensity:** cambio dramático o transición de energía.
- **Foley and Sound Design FX:** efectos de sonido ambiental o ruido no musical.
- **Experimental Modes:** fusiones inusuales.
- **Production and Effect / Advanced Modifiers:** etiqueta global `[PRODUCTION]` o corchetes temporales para mezcla, ingeniería de audio, saturación y amplitud estéreo.
- **Nudging and Callbacks:** en cierres/inicios de sección para empujar la transición o reutilizar motivos (ej. `[Callback: continue with same vibe as chorus]`).
- **Negative Prompts:** clichés, instrumentos o características a bloquear → van en exclude_styles.

## 3 · Definición del style_box
Define el núcleo estilístico optimizando el espacio de 30 palabras.
- **Fusión semántica extrema:** inventa géneros principales cruzando conceptos (ej. RUSSIAN SALSA, HARDTEK POCOYO). Añade subgéneros de apoyo en minúsculas.
- **Tag Anchoring:** para fijar instrumentos base y/o protagonistas, añádelos al style_box y al lyrics_box.

## 4 · exclude_styles
Una línea de estilos negativos para bloquear características, instrumentos o clichés no deseados, separados por comas (ej. cuban, reggaeton, piano).
