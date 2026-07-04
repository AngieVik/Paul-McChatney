# exclude_box
*Prompting inverso y control de artefactos, para bloquear características, instrumentos, clichés no deseados, degradación de la señal, solapamiento de frecuencias y saturación del espacio latente en la generación.*
*Recordatorio: consulta por búsqueda (grep) o salto por sección.*
---
##  Índice

`1 · Instrucciones exclude_box`
`2 · Mitigación de Saturación y Clipping`
`3 · Supresión de Artefactos Digitales`
`4 · Control de Sibilancia y Espectro Vocal`
`5 · Claridad y Separación Frecuencial`
---
## 1 · Instrucciones exclude_box
- *Genera una línea de estilos, separados por comas para bloquear características. Puedes apoyarte en `chupilista/15_negative_prompts_and_exclude_styles.md` van exclusivamente en `exclude_box`.*
    * **Ejemplo:** 
      cuban, reggaeton, piano, grand piano, soft ambient intro, mellow, slow tempo, quiet silence, crooner, romantic ballad, latin pop, generic edm, lo-fi, standard reggaeton

## 2 · Mitigación de Saturación y Clipping
- *En géneros de alta energía, los algoritmos tienden a sobrecomprimir el bus maestro, generando un recorte de onda destructivo.*
    - `clipping`: Penaliza la tendencia del modelo a generar picos que superen los 0 dBFS.
    - `overcompressed`: Previene el efecto de "bombeo" (pumping) y preserva el rango dinámico natural.
    - `brickwall limiter`: Evita la limitación agresiva que aplasta los transitorios de la percusión.
    - `distorted master`: Filtra la saturación no deseada en la mezcla global.
---
## 3 · Supresión de Artefactos Digitales
- *Contramedidas para errores de codificación y limpieza del extremo superior del espectro (High-end).*
    - `aliasing`, `high pitched noises`: Reduce el ruido de intermodulación y los siseos agudos constantes detectados.
    - `bright digital shimmer`: Mitiga el brillo metálico artificial que suele aparecer en frecuencias de 8k-12k Hz.
    - `phase issues`, `phasing`: Previene cancelaciones de fase que provocan un sonido "hueco" o inestable en la imagen estéreo.
    - `mp3 artifacts`, `low bitrate`: Obliga al modelo a priorizar clústeres de entrenamiento de alta resolución para evitar el sonido "acuoso".
    - `robotic voice`, `synthetic artifacts`: Suprime los fallos algorítmicos en el sintetizador vocal para forzar un timbre más orgánico.
    - `scraping sounds`, `clanking artifacts`: Elimina ruidos de fricción mecánica o artefactos metálicos no deseados.
---
## 4 · Control de Sibilancia y Espectro Vocal
- *Corrección de resonancias punzantes provocadas por una síntesis defectuosa de las consonantes.*
    - `sibilance`: Actúa como un *De-Esser* algorítmico, suavizando las eses ('S') y zetas ('Z').
    - `harsh frequencies`, `piercing highs`: Penaliza las frecuencias agudas estridentes que causan fatiga auditiva.
    - `plosives`: Previene golpes de graves descontrolados producidos por consonantes explosivas ('P', 'B').
    - `vocal crackle`: Elimina chasquidos o crepitaciones digitales en la pista de voz (común en procesamientos de inpainting).
    - `modern vocal polish`: Evita el procesamiento vocal excesivo para mantener una toma más cruda, natural y humana.
---
## 5 · Claridad y Separación Frecuencial
- *Prevención del "ensuciamiento" (mud) cuando convergen múltiples capas instrumentales densas.*
    - `muddy mix`: Evita la acumulación excesiva de energía en la región crítica de los 200Hz - 500Hz.
    - `instrumental bleed`: Previene que el timbre de un instrumento contamine o se fusione erróneamente con el espectro de otro.
    - `cluttered`: Instruye al modelo a mantener una disposición espacial clara y evitar la saturación de eventos simultáneos.
    - `poor separation`: Exige una imagen estéreo definida y un espacio frecuencial dedicado para cada elemento del arreglo.
---