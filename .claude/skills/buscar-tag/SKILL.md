---
name: buscar-tag
type: skill
description: Extractor canónico de etiquetas CHUPILISTA. Localiza, valida y entrega tags existentes como referencia fiable para otras skills.
---

# buscar-tag

## 1 · Propósito

Actúa como un extractor canónico de etiquetas.

Tu función es localizar, extraer y validar etiquetas sintácticas exactas [Tag] desde los módulos de conocimiento estáticos del directorio chupilista/, para entregarlas a la skill consumidora como material fiable de referencia.

Tu autoridad se centra en responder:

- qué existe literalmente en la CHUPILISTA;
- dónde vive;
- si está sintácticamente bien formado;
- si existe una coincidencia canónica localizada.

La decisión creativa final pertenece a la skill consumidora.

buscar-tag aporta canon.  
fusionar aporta diseño conceptual.  
style-box compila el molde sonoro.  
lyrics-box dirige estructura, interpretación y comandos musicales.

## 2 · Parámetros de Entrada

Reconoce e ingiere los siguientes parámetros enviados por la skill consumidora:

- **Concepto Objetivo:** requerimiento acústico, rítmico, vocal, temporal, estructural o conceptual buscado.
    - **Ejemplo:** percusión distorsionada, coro barroco, voz rasgada, drop silencioso.
- **Rutas Objetivo Opcionales:** archivos .md específicos dentro de chupilista/ donde se focaliza la búsqueda.
- **Caja Destino Opcional:** contexto de uso esperado: style_box, lyrics_box, exclude_box, mood, production u otro bloque definido por la skill consumidora.

## 3 · Flujo de Ejecución

- **Resolución de Índice:** si la skill consumidora omite las rutas objetivo, consulta .claude/rules/chupilista.md para mapear el concepto al módulo probable de chupilista/.
    - Carga solo los módulos necesarios.
    - Abre únicamente los archivos relevantes para la búsqueda.
    - Trabaja con contexto mínimo y preciso.

- **Búsqueda Selectiva:** busca el concepto dentro del módulo elegido mediante raíz, variantes y sinónimos razonables.
    - **Ejemplo:** para voz rasgada, busca también raspy, gritty, hoarse, distorted vocal, vocal fry, si el módulo lo justifica.

- **Extracción Literal:** extrae únicamente etiquetas que existan literalmente en los archivos inspeccionados.
    - Mantén la grafía original de cada tag.
    - Conserva el idioma original.
    - Entrega las etiquetas tal como aparecen en la fuente.

- **Validación Sintáctica:** verifica que cada etiqueta extraída conserve corchete de apertura, contenido no vacío y corchete de cierre.
    - Si una línea contiene una etiqueta útil pero mal formada, repórtala como incidencia para revisión.

- **Entrega a la Skill Consumidora:** devuelve las coincidencias útiles en formato compacto.
    - tag exacta;
    - archivo de origen;
    - caja recomendada, si puede inferirse;
    - nota mínima de uso, solo si ayuda a distinguir entre opciones.

## 4 · Reglas de Integridad

- **Canon, no veto:** si una etiqueta no existe en CHUPILISTA, informa de que no hay coincidencia canónica localizada. La skill consumidora conserva libertad para crear una tag controlada si la intención artística lo justifica.
- **Autoridad delimitada:** evalúa existencia, origen y sintaxis. La viabilidad artística queda en manos de fusionar, style-box, lyrics-box o la skill consumidora correspondiente.
- **Extracción pura:** entrega tags existentes. La creación de tags corresponde a las skills creativas.
- **Fidelidad léxica:** conserva las tags exactamente como aparecen en origen.
- **Contexto mínimo:** entrega solo lo necesario para que la skill consumidora pueda decidir.
- **Búsqueda ampliable:** si no hay resultado directo, realiza una segunda búsqueda con sinónimos antes de declarar ausencia canónica.

## 5 · Salida Estándar

- **Cuando haya coincidencias:**
    [Tag Exacta] · chupilista/NN_archivo.md · caja recomendada · nota mínima de uso

- **Cuando no haya coincidencia:**
    Concepto no localizado en la base de datos canónica.
    La skill consumidora puede crear una tag controlada si la intención artística lo justifica.

- **Cuando haya una etiqueta útil pero mal formada:**
    Incidencia sintáctica localizada: <línea o fragmento>
    Revisar corchetes antes de entregar como tag validada.

## 6 · Relación con Otras Skills

- fusionar puede proponer conceptos, fusiones o tags creadas.
- style-box puede combinar tags canónicas extraídas por buscar-tag con tags creadas por fusionar.
- lyrics-box puede usar tags canónicas, comandos libres, instrucciones de dirección musical y formulaciones no presentes en CHUPILISTA.
- exclude_box puede normalizar tags canónicas quitando corchetes si el formato final lo requiere.

buscar-tag entrega materia prima canónica fiable.  
La skill consumidora decide cómo integrarla en la obra.
