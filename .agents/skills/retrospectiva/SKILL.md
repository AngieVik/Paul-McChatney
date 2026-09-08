---
name: retrospectiva
description: Use when aparece un aprendizaje reutilizable que debe destilarse, validarse, clasificarse o archivarse con aprobación explícita del usuario.
---

# retrospectiva

Convierte una observación validada en conocimiento reutilizable sin confundir obra, prompt y aprendizaje.

## Activación

Puede usarse en cualquier fase. `aprobar` solo puede sugerirla; nunca la ejecuta. Nada se escribe en `.agents/MEMORY.md` o `composicion/` sin aprobación explícita.

## Destinos

- Principio transversal → `.agents/MEMORY.md`.
- Técnica o tag concreta → su archivo de `composicion/`, localizado por `.agents/maps/composicion.md` o el mapa específico.
- Corazonada `⚗️` → ascender, mantener y matizar, o eliminar según la prueba.

## Protocolo

1. Detecta algo no trivial que haya funcionado o fallado: técnica, decisión, corrección, prueba o cliché evitado.
2. Separa la fuente del aprendizaje. Una salida de Suno, instrucción o prompt no se convierte por sí solo en conocimiento.
3. Comprueba que sea reutilizable y que no esté ya documentado.
4. Clasifica un único destino. No dupliques entre memoria y manuales.
5. Formula una regla positiva, accionable y limitada por la evidencia disponible.
6. Presenta la propuesta y espera `Añadir`, `Modificar`, `Eliminar` o `No hacer nada`.
7. Aplica solo la acción aprobada y confirma archivo y cambio.

## Integridad

- La validación relevante es la del aprendizaje, no la aprobación de la obra.
- Aprobar obra, prompt y aprendizaje son acciones independientes.
- Un hallazgo local no se generaliza más allá de lo observado.
- No existe una retrospectiva provisional distinta: siempre se detecta, formula, aprueba y escribe mediante este proceso.
