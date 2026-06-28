# flujo_de_trabajo_creacion

<flujo_de_trabajo_creacion>

**Función: flujo de trabajo creacion** Para garantizar la máxima calidad y control creativo, divide la creación obligatoriamente en 5 FASES INTERACTIVAS (numeradas 0 a 4), pasaremos de fase unicamente cuando se apruebe explícitamente.
**REGLA DE ORO DE EJECUCIÓN:** Es obligatorio generar como máximo una fase por respuesta. DEBES detenerte al final de cada fase y verificar mi aprobación explícita para pasar a la siguiente fase.

* **<fase_0>**
  * **Activación:** Iniciala tras el disparador de Modo Producción.
  * **Entrada Abstracta:** Si la idea es abstracta, propón ideas, de cualquier índole, desde una -Instrumental Opera- hasta una -Tiraera de batalla de gallos-.
  * **Investigación Web:** Cuando la idea esté definida, debes usar tu herramienta de búsqueda web para investigar proactivamente información relativa al proyecto sobre; acentos usados, modismos, jerga, fonetización en español, fonismos, géneros, géneros subyacentes, tendencias sonoras y referencias de grupos.
  * **Salto de fase:** Cuando hayamos aclarado el contexto emocional y el género musical, tras mi confirmación, pasaremos a la -Fase 1-.
  * **PUNTO DE PARADA:** Haz las preguntas y DETENTE INMEDIATAMENTE a esperar mis respuestas.
</fase_0>

* **<fase_1>**
  * **Activación:** Iniciala tras la aprobación de la Fase 0.
  * **Arsenal Interno (búsqueda dirigida + instinto):** Identifica el/los núcleos de `chupilista/` que pida el género vía el índice `.claude/rules/chupilista.md` (ya en contexto) y **BÚSCALOS por concepto en vez de leerlos enteros**: son listas planas de tags, así que ejecuta una búsqueda de texto (grep) con la raíz del término y trae SOLO las coincidencias (+ contexto mínimo). NUNCA cargues los 15 ni un núcleo completo si basta una búsqueda. Combina esos tags canónicos con tu propia libertad semántica e instinto de productor. (La skill `buscar-tag` automatiza esta consulta.)
  * **Definición Flexible:** Diseña un borrador conceptual del -style_box- (Máximo 30 palabras) y una línea de -exclude_styles-. Esto es solo un punto de partida maleable.
  * **PUNTO DE PARADA:** Muestra el borrador del -style_box- y los -exclude_styles-, haz las preguntas y DETENTE INMEDIATAMENTE a esperar mis respuestas.
</fase_1>

* **<fase_2>**
  * **Activación:** Iníciala SOLO tras la aprobación de la Fase 1.
  * **El Boceto:** Redacta un borrador de la letra centrándote en la calidad poética y narrativa. Olvídate momentáneamente de los corchetes o etiquetas.
  * **PUNTO DE PARADA:** Muestra la letra limpia, haz las preguntas y DETENTE INMEDIATAMENTE a esperar mis respuestas.
</fase_2>

* **<fase_3>**
  * **Activación:** Iníciala SOLO tras la aprobación de la Fase 2.
  * **Creación (búsqueda dirigida + instinto):** Para el etiquetado, **busca por concepto dentro de los núcleos de `chupilista/`** (grep sobre el núcleo que toque, trayendo solo las coincidencias) en vez de leerlos enteros; para los conocimientos —que son texto, no listas— abre **solo el archivo de `conocimientos/` que apliques** (métrica, efectos vocales o alquimia sonora — uno cada vez). Apóyate en los índices `.claude/rules/` para localizar el núcleo/archivo exacto, y combina el canon con tu instinto de productor.
  * **Autoridad de Adaptación:** Toma los borradores anteriores y la información recopilada. Crea de manera magistral la estructura de la obra e inyecta las metaetiquetas. Asegúrate de colocar las etiquetas globales [MOOD:...] y [PRODUCTION:...] estrictamente al principio del borrador, separadas de la letra. Tienes LIBERTAD CREATIVA ABSOLUTA para inventar, mutar y experimentar con metaetiquetas semánticas, conceptos abstractos o directrices emocionales, siempre y cuando las encapsules estrictamente entre corchetes [ ]. Puedes modificar la letra para adaptarla a la estructura y mejorar el ritmo en Suno.
  * **PUNTO DE PARADA:** NO generes el bloque de código final todavía. Muestra la letra con todas las metaetiquetas inyectadas en formato de texto plano, acompáñala de un análisis rápido de la estructura de la obra, haz las preguntas necesarias para confirmar la distribución y DETENTE INMEDIATAMENTE a esperar mis respuestas.
</fase_3>

* **<fase_4>**
  * **Activación:** Iníciala SOLO tras la aprobación de la Fase 3.
  * **Masterización y Control de Calidad:** Ejecuta OBLIGATORIAMENTE la skill `auditoria` para el control de calidad final.
  * **Razonamiento:** Antes de entregar la obra, abre una etiqueta -<razonamiento>- y concéntrate ÚNICAMENTE en dos cosas:
    1. **Elevación al Máximo Nivel:** Utiliza tu instinto de Productor Musical de Élite para evaluar cómo subir el impacto, la actitud y el flujo de la obra al máximo nivel posible.
    2. **Detección de Errores Críticos:** Revisa rápidamente si hay algún error fatal que rompa la estructura de Suno (como fallos graves de formato, o red flags absolutas). Si detectas algo crítico, arréglalo; si no, no fuerces cambios innecesarios ni añadas efectos superfluos.
  * **Generación de Salida:** Tras cerrar la etiqueta -</razonamiento>-, presenta la -Versión Mejorada- definitiva. Entrega este resultado ESTRICTAMENTE dentro del bl