---
name: proyecto
description: Use when el usuario pide crear, retomar, guardar, listar, aprobar, cerrar, cancelar o eliminar una obra y su archivo de trabajo.
---

# proyecto

Gestiona el ciclo de vida y los archivos de una obra. Solo confirma una operación después de ejecutarla correctamente.

## Comandos

- `crear <slug>`: crea `_hojas_sucias/<slug>.md` desde `chuletas/plantilla_hoja_sucia.md`, con *snake_case* y estado inicial. Si existe, detente y pide confirmación antes de sobrescribir.
- `retomar <slug>`: desde `_hojas_sucias/`, lee estado, aprobado vigente y candidato; confirma obra, fase y próximo paso. Desde `proyectos/<slug>/`, copia la obra a una hoja sucia nueva. Si el destino existe, no lo pises sin confirmación.
- `aprobar <slug>`: consolida en `proyectos/<slug>/<slug>.md` el núcleo obligatorio de `chuletas/plantilla_proyecto.md`, conservando secciones adicionales. Añade o actualiza una única fila en `PROYECTOS.md`. Marca la hoja como `aprobado`, libera el contexto activo y conserva hoja y copias; no borra nada. Después puede sugerir una retrospectiva, sin ejecutarla.
- `guardar <slug>`: crea un clon exacto `_hojas_sucias/<slug>_NN.md`, usando el siguiente índice de dos dígitos; nunca sobrescribe una copia.
- `listar`: muestra hojas activas o el catálogo solicitado.
- `cerrar <slug>`: actualiza la hoja a `en pausa`, conserva última decisión y próximo paso, mantiene todos los archivos y libera el contexto.
- `cancelar`: cancela solo la operación actual; la obra continúa activa.
- `eliminar <slug>`: requiere confirmación destructiva explícita que incluya el slug. Solo entonces elimina hoja, copias y contexto; no toca la obra aprobada salvo petición inequívoca.

## Contrato de estado

- Trabaja sobre una sola obra hasta `aprobar`, `cerrar` o `eliminar`.
- Tras aprobar una fase o aceptar un cambio material, actualiza fase, aprobado vigente, candidato actual, fuentes, última decisión y próximo paso.
- El aprobado vigente y el candidato son distintos. Experimentar puede sobrescribir el candidato; solo una aprobación explícita sustituye el aprobado.
- La Fase 5 no cierra la obra. Solo `aprobar` la finaliza.
- Aprobar obra, prompt y aprendizaje son acciones independientes. `retrospectiva` puede proponerse en cualquier fase, pero nunca escribe conocimiento sin aprobación.
- El canon de consolidación es estricto en sus seis secciones obligatorias y flexible en secciones adicionales. No reformatea obras históricas sin petición.

## Resultado

Informa la operación realizada, las rutas afectadas y el estado resultante. Si no hay permiso de escritura, entrega la ruta y el contenido propuestos sin afirmar que fueron aplicados.
