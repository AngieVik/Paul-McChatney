# tecnicas_vocales

<técnicas_vocales>

* **Función: Tecnicas vocales** Efectos y técnicas vocales para dar personalidad y textura a las voces.
* **Puntuación en la Letra**
  * **Uso Estratégico de Paréntesis ( ):** Emplea paréntesis para inyectar voces secundarias. Esto indica que la línea debe ser cantada exclusivamente por voces secundarias o coros. Aplícalos para:
    * **Coros y Apoyos:** Intercala coros y palabras de apoyo (ej. hay que ser torero (oleee) o (Nadie me puede parar (no, no, no))).
    * **Interjecciones Secundarias:** Inyecta interjecciones de fondo interpretadas por voces secundarias (ej. (¡ay!), (¡ouch!)).
    * **Ecos Forzados:** Repite una palabra y pon la segunda entre paréntesis para que una segunda voz cante esa palabra de fondo (ej. I want it all (all)). *Advertencia: El texto en paréntesis se canta y suma sílabas a tu métrica; si no hay espacio en el compás, sonará atropellado.*
    * **Coros sin palabras:** Usa sílabas armónicas para melodías de fondo (ej. (ai aiiiiAaAaaiiII), (nainononainonaaa)).
  * **Énfasis Especial:** El texto entre comillas proporciona un énfasis especial, haciendo que suene como un pensamiento interno o como una voz interior en la interpretación (ej. ser o no ser, esa es la cuestión…).
  * **Interjección Espontánea:** Usa el texto entre signos de exclamación para inyectar una interjección espontánea, gritando con aumento de energía y de manera cómica o teatral (ej. ¡ay!, ¡ouch!).

* **Etiquetas de Dirección Vocal**
  * **Roles Específicos:** Crea personajes atípicos utilizando corchetes, como por ejemplo: [Announcer] (presentador), [Reporter] (reportero), [Child voice] (voz de niño/a) o efectos como [Giggling] (risitas).
  * **Duetos y Personajes:** Crea interacciones asignando etiquetas de género ([Male] / [Female]) o nombres propios. *Nota de formato:* Abre cada línea de diálogo con la etiqueta del personaje correspondiente de forma estricta para minimizar el riesgo de que la IA invierta las voces (ej. [Male] Hola / [Female] Adiós).
  * **[overlapping]:** Utiliza esta etiqueta para forzar que dos voces distintas canten armónicamente de forma simultánea (armonías cruzadas, no ecos).
  * **[multiple voice chorus satb]:** Utiliza esta etiqueta para forzar a la IA a generar un coro profesional con múltiples capas simultáneas (soprano, alto, tenor y bajo).

* **Ejemplo de Aplicación (Puntuación en la Letra y Dirección Vocal)**
    [Male] I was walking down the street what a day
    [Female] (ooo) Walking down the street! (¡hey!)
    [overlapping] We met at the corner!
    [multiple voice chorus satb] And the choir started to sing

* **Ingeniería de Personaje y Estructura**
  * **Aislamiento Vocal Temporal:** Aísla cualquier cambio de técnica en medio de una sección usando transiciones claras para garantizar la fluidez y mantener el contexto de la IA.
        (Ej. [Sección A] -> texto -> [Técnica Temporal] -> texto -> [Sección A continues]).
  * **Persona Stacking (Voz desde Texto):** Construye un personaje vocal inquebrantable puramente desde texto puedes apilar hasta 4 capas en una sola etiqueta en el -lyrics_box-, al inicio de la obra:
    * **1. Demografía:** (ej. edad, tipo de voz).
    * **2. Entrega Técnica:** (ej. susurrado, potente, claro).
    * **3. Contexto Emocional:** (ej. melancólico, confiado).
    * **4. Anclaje Sonoro:** (una referencia descriptiva a un estilo o timbre. *escribelo inexactamente (ej. Dabid Visbal, Alesandro Janz...).*)

* **Ejemplo de Aplicación (Personaje y Estructura)**

```text
[25 year old Female, whispery and close, melancholic, breathy indie-pop voice]

[Instrumental Intro]

[Verse 1]
I remember the days when the sun was cold

[Chorus]
[Vocal: Hall Reverb]
Now I'm shouting to the walls!
[Chorus continues -> dry vocal]
And waiting for the echo to fall.
```

</técnicas_vocales>
