# distribucion_etiquetas
*Clasifica y distribuye las etiquetas por caja operativa (style_box vs lyrics_box). Fases 1 y 3.*
*Recordatorio: consulta por búsqueda (grep) o salto por Índice.*

---

## Índice
`1 · Etiquetas del style_box`
`2 · Etiquetas del lyrics_box`
`3 · Definición del style_box`
`4 · exclude_styles`
`5 · creative_sliders`

---

## 1 · Etiquetas del style_box
Fundación técnica de la obra.
- **Core Genres and Subgenres:** `chupilista\01_core_genres_and_subgenres.md` Fundación rítmica y lenguaje armónico base (siempre al principio).
- **Instrumentation and Stems:** `chupilista\03_instrumentation_and_stems.md` Instrumentos estructurales base y\o protagonistas; usa Tag Anchoring con 3-4 instrumentos.
- **Vocal Persona and Timbre:** `chupilista\04_vocal_persona_and_timbre.md` Descriptor base de voz.
- **Vocal Delivery and Expressivity:** `chupilista\12_vocal_delivery_and_expressivity.md` Descriptor base de voz.
- **Rhythm and Tempo:** `chupilista\05_rhythm_and_tempo.md` BPM, groove, modulaciones métricas, cambios de tempo o pausas.
- **Music Theory Harmony and Scales:** `chupilista\07_music_theory_harmony_and_scales.md` Tonalidades específicas o progresiones de acordes.
- **Dynamics and Intensity:** `chupilista\08_dynamics_and_intensity.md` Dinámica o intensidad.
- **Experimental Modes:** `chupilista\10_experimental_modes.md` Fusiones inusuales.

## 2 · Etiquetas del lyrics_box
Entre corchetes `[ ]`, marcan el momento exacto de un evento temporal dentro de la narrativa.
- **Atmosphere and Mood:** `chupilista\02_atmosphere_and_mood.md` Etiqueta global `[MOOD]` o corchetes temporales.
- **Instrumentation and Stems:** `chupilista\03_instrumentation_and_stems.md` Momentos donde un instrumento toma el protagonismo o entra en la mezcla (ej. `[Guitar Solo]`); usa Tag Anchoring.
- **Vocal Persona and Timbre:** `chupilista\04_vocal_persona_and_timbre.md` Persona Stacking completo al inicio; segundas voces, duetos o coros puntuales intercalados junto a la letra para alterar intención, técnica o volumen.
- **Vocal Delivery and Expressivity:** `chupilista\12_vocal_delivery_and_expressivity.md` Persona Stacking completo al inicio; segundas voces, duetos o coros puntuales intercalados junto a la letra para alterar intención, técnica o volumen.
- **Rhythm and Tempo:** `chupilista\05_rhythm_and_tempo.md` Reafirmar o cambiar BPM, groove, modulaciones, tempo o pausas.
- **Song Structure and Sections:** `chupilista\06_song_structure_and_sections.md` Elementos estructurales y secciones; dictan el flujo narrativo.
- **Music Theory Harmony and Scales:** `chupilista\07_music_theory_harmony_and_scales.md` Crea o modula entre tonalidades o progresiones.
- **Dynamics and Intensity:** `chupilista\08_dynamics_and_intensity.md` Cambio dramático o transición de energía.
- **Foley and Sound Design FX:** `chupilista\09_foley_and_sound_design_fx.md` Efectos de sonido ambiental o ruido no musical.
- **Experimental Modes:** `chupilista\10_experimental_modes.md` Fusiones inusuales.
- **Production and Effect:** `chupilista\11_production_and_effect.md` Etiqueta global `[PRODUCTION]` o corchetes temporales para mezcla, ingeniería de audio, saturación y amplitud estéreo.
- **Advanced Modifiers:** `chupilista\13_advanced_modifiers_allowed.md` Etiqueta global `[PRODUCTION]` o corchetes temporales para mezcla, ingeniería de audio, saturación y amplitud estéreo.
- **Nudging and Callbacks:** `chupilista\14_nudging_and_callbacks.md` Empujes de transición en cierres\inicios de sección para reutilizar motivos melódicos. (ej. `[Callback: continue with same vibe as chorus]`).


## 3 · Definición del style_box
Define el núcleo estilístico optimizando el espacio de 14 palabras.
- **Fusión semántica extrema:** Inventa géneros principales cruzando conceptos (ej. RUSSIAN SALSA, HARDTEK POCOYO). Añade subgéneros de apoyo en minúsculas.
- **Tag Anchoring:** Para fijar instrumentos base y\o protagonistas, añáde 3-4 al style_box y al lyrics_box.

## 4 · exclude_tyles
Una línea de estilos negativos para bloquear características, instrumentos o clichés no deseados, separados por comas (ej. cuban, reggaeton, piano).
- **Negative Prompts:** `chupilista\15_negative_prompts_and_exclude_styles.md` Clichés, instrumentos o características a bloquear → van en exclude_styles.

## 5 · creative_sliders
- **El comportamiento del style_box:** Ahora depende totalmente de tres deslizadores:
    - **Weirdness (0-100%):** Define si tus etiquetas se interpretan de forma comercial\segura (<30%) o caótica\experimental (>70%).
    - **Style Influence (0-100%):** Define qué tan estrictamente la IA debe obedecer tu *Style Box* (100% = obediencia total).
