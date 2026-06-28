# distribucion_etiquetas

<distribución_etiquetas>

**Función:** Clasifica y distribuye las etiquetas guiandote por estas categorías operativas.

<etiquetas_style_box>

* **Función: etiquetas -style_box-** Aplica estas etiquetas en el -style_box- para establecer la fundación técnica de la obra.
  * **Core Genres and Subgenres:** Establece la fundación rítmica y el lenguaje armónico base (deben ir siempre al principio).
  * **Instrumentation and Stems:** Para los instrumentos estructurales base y/o protagonistas, usa **Tag Anchoring**.
  * **Vocal Persona and Timbre, Vocal Delivery and Expressivity:** Para un descriptor base de 1 o 2 palabras.
  * **Rhythm and Tempo:** Para establecer BPM, groove, modulaciones métricas, cambios de tempo o pausas.
  * **Music Theory Harmony and Scales:** Usa tonalidades específicas o progresiones de acordes.
  * **Dynamics and Intensity:** Para definir la dinamica o intensidad.
  * **Experimental Modes:** Aplica fusiones inusuales.
</etiquetas_style_box>

<etiquetas_lyrics_box>

* **Función: etiquetas -lyrics_box-** Úsalas entre corchetes [ ] dentro del -lyrics_box- para indicar el momento exacto en que debe ocurrir un evento temporal específico dentro de la narrativa.
  * **Atmosphere and Mood:** Genera en la etiqueta global [MOOD] o en corchetes temporales, para directrices de mezcla, ingeniería de audio, saturación y amplitud estéreo.
  * **Instrumentation and Stems:** Inyecta momentos donde un instrumento toma el protagonismo absoluto o entra en la mezcla (ej. [Guitar Solo]),  usa **Tag Anchoring**.
  * **Vocal Persona and Timbre, Vocal Delivery and Expressivity:** Para construir el -Persona Stacking- completo al inicio, para forzar segundas voces, duetos o arreglos corales puntuales. Intercala estas directrices junto a la letra para alterar la intención, técnica o volumen de la voz.
  * **Rhythm and Tempo:** Para reafirmar, o cambiar BPM, groove, modulaciones métricas, cambios de tempo o pausas.
  * **Song Structure and Sections:** Crea elementos estructurales y secciones, para dictar el flujo narrativo.
  * **Music Theory Harmony and Scales:** Crea o modula entre tonalidades específicas o progresiones de acordes.
  * **Dynamics and Intensity:** Inyecta un cambio dramático o una transición de energía.
  * **Foley and Sound Design FX:** Detona efectos de sonido ambiental o ruido no musical.
  * **Experimental Modes:** Aplica fusiones inusuales.
  * **Production and Effect:** Genera en la etiqueta global [PRODUCTION] o en corchetes temporales, para directrices de mezcla, ingeniería de audio, saturación y amplitud estéreo.
  * **Advanced Modifiers Allowed:** Genera en la etiqueta global [PRODUCTION] o en corchetes temporales, para directrices de mezcla, ingeniería de audio, saturación y amplitud estéreo.
  * **Nudging and Callbacks:** Aplica en los cierres o inicios de sección para empujar la transición o instruir al modelo a reutilizar motivos anteriores (ej. [Callback: continue with same vibe as chorus]).
  * **Negative Prompts and exclude_styles:** Estilos para bloquear características, instrumentos o clichés no deseados en exclude_styles.
</etiquetas_lyrics_box>

<definicion_style_box>

* **Función: definición -style_box-** Define el núcleo estilístico optimizando el espacio de 30 palabras.
  * **Fusión Semántica Extrema:** Inventa géneros principales cruzando conceptos (ej. RUSSIAN SALSA, HARDTEK POCOYO). Añade subgéneros de apoyo en minúsculas.
  * **Tag Anchoring:** Para fijar los instrumentos base y/o protagonistas a la obra, añade los instrumentos al -style_box- y al -lyrics_box-.
</definicion_style_box>

<exclude_styles>

* **Función: definición -exclude_styles-** Define el nucleo generando prompts negativos:
  * **Negative Prompts and exclude_styles:** Genera una línea de estilos negativos para bloquear características, instrumentos o clichés no deseados. Sepáralos por comas (ej. cuban, reggaeton, piano).
</exclude_styles>
</distribución_etiquetas>
