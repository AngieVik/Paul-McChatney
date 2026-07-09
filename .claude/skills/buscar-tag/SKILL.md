---
name: buscar-tag
type: skill
description: Microservicio agnóstico de extracción RAG para localizar y validar etiquetas sintácticas exactas en la base de datos canónica
---

# buscar-tag

## 1 · Propósito

Actúa como un microservicio de extracción de datos (RAG). Tu función es localizar, extraer y validar etiquetas sintácticas exactas (`[Tag]`) desde los módulos de conocimiento estáticos en el directorio `chupilista/`[cite: 2], para entregarlas a la skill consumidora manteniendo una postura analítica y neutral.

## 2 · Parámetros de Entrada

Reconoce e ingiere los siguientes parámetros enviados por la skill consumidora:

- **Concepto Objetivo:** El requerimiento acústico, rítmico, temporal o conceptual buscado (ej. "Percusión distorsionada", "Coro barroco").
- **Rutas Objetivo (Opcional):** Los archivos `.md` específicos dentro de `chupilista/`[cite: 2] donde se focaliza la búsqueda.

## 3 · Flujo de Ejecución

1. **Resolución de Índice:** Si la skill consumidora omite las *Rutas Objetivo*, mapea el archivo correcto inspeccionando exclusivamente el índice `.claude/rules/chupilista.md`[cite: 2]. Si se proporcionan las rutas, procede de inmediato al paso dos.
2. **Extracción Literal:** Lee los archivos destino estipulados y recolecta las etiquetas que representen semánticamente el *Concepto Objetivo*.
3. **Validación de Sintaxis:** Asegura que cada etiqueta extraída mantenga su formato de origen intacto, verificando la presencia del corchete de apertura `[` y el corchete de cierre `]`.
4. **Entrega Transaccional:** Transfiere a la skill consumidora una lista en texto plano que contenga exclusivamente los tags exactos y validados, finalizando tu ejecución.

## 4 · Lista de Control y Reglas de Integridad

- **Fidelidad Léxica:** Extrae única y exclusivamente las etiquetas que existan de forma literal en los archivos inspeccionados. Si un concepto solicitado carece de representación en la ruta, repórtalo explícitamente a la skill consumidora mediante el mensaje: "Concepto no localizado en la base de datos canónica".
- **Aislamiento Operativo:** Mantén la salida de datos restringida a los tags puros. Omite explicaciones adicionales, sugerencias de mezcla o análisis teóricos sobre las etiquetas entregadas.
- **Integridad Estructural:** Entrega las etiquetas siempre con su sintaxis completa y bien formada, garantizando el aislamiento de caracteres (ejemplo de formato de salida correcto: `[Hardtek]`).
