---
name: proyecto
description: Crea y gestiona el archivo de trabajo de una obra (crea, lista, retoma, cierra, aprueba, guarda, cancela, elimina) y la memoria de proyectos. Primer paso de cualquier creación.
---
# proyecto
  - Orquesta la **memoria de proyectos** y, sobre todo, el **archivo de trabajo**.
  - Al arrancar cualquier creación `Crea` el `.md` en `_hojas_sucias/`.
  - La última versión real del proyecto, donde se vuelca y **se sobrescribe** lo que se va creando. 
  - Después `Lista`, `Retoma`, `Cierra`, `Aprueba`, `Guarda`, `Cancela`, `Elimina`.

## Cuándo se activa
  - Al pedir **crear** algo (una obra, una idea, una pieza suelta) lo primero es abrir su archivo de trabajo.
  - Al solicitar una *lista*, o *retoma* una obra.
  - La invoca `produccion` en la *Fase 0* (crear el archivo) y al **Aprobar** (cerrar el ciclo).

## Mapa de la memoria

| Capa             | Dónde                            | Qué guarda                                                          |
| ---------------- | -------------------------------- | ------------------------------------------------------------------- |
| Trabajo en curso | `_hojas_sucias/<slug>.md`        | la obra viva; se sobrescribe según avanza (libre, sin formato fijo) |
| Obras terminadas | `proyectos/<slug>/<slug>.md`     | prompt final + retrospectiva (formato canónico)                     |
| Catálogo         | `PROYECTOS.md`                   | índice navegable por género                                         |
| Memoria global   | `.claude/MEMORY.md`              | aprendizajes que trascienden una obra                               |
| Plantilla trabajo | `chuletas/plantilla_hoja_sucia.md` | guía conceptual del archivo en curso (no estricta) |
| Plantilla final  | `chuletas/plantilla_proyecto.md` | formato canónico del archivo terminado |

## Comandos
  - *Crea* `_hojas_sucias/<slug>.md` (slug en `snake_case`, sin acentos ni eñes) con un *borrador dinámico* del proyecto nuevo solicitado, usando `chuletas/plantilla_hoja_sucia.md` como guía conceptual (no estricta); haz preguntas.
  - Es el archivo de trabajo libre que se *sobrescribe* según avanza (regla de `CLAUDE.md`); si el usuario pega una versión consolidada, esa pasa a ser la actual.
  - *Lista* lo que se te solicite, obras vivas en `_hojas_sucias/`, el catálogo de `PROYECTOS.md`, etc.
  - *Retoma* desde:
    - *Proyecto terminado* copia su contenido de `proyectos/<slug>/` a `hojas_sucias/<slug>.md` y resume su estado para retomar el trabajo.
    - *Proyecto en hojas sucias* abre el `.md` y resume su estado para retomar.
  - *Cierra* el contexto del proyecto en curso para volver al Modo Conversacional y/o hacer otra cosa (no borra nada).
  - *Valida / Aprueba* da por finalizada satisfactoriamente una obra, migra a `proyectos/<slug>/<slug>.md` con la plantilla (`chuletas/plantilla_proyecto.md`) y la registra en `PROYECTOS.md`.
  - *Retrospectiva* (`conocimientos/retrospectiva.md`) propone el aprendizaje.
  - *Guarda* una copia de seguridad `_hojas_sucias/<slug>_NN.md` (duplicado exacto del estado en ese momento).
  - *Cancela* el contexto de ese momento y el proyecto en curso (si es nuevo).
  - *Elimina* por completo todo rastro del proyecto y el contexto de ese momento.

## Regla de oro de la memoria
  - Un prompt no validado en producción es hipótesis, no conocimiento: no escala a `MEMORY.md` ni a los archivos vivos hasta que el usuario valida la obra. 
  - Todo aprendizaje se redacta en **positivo** (qué hacer).

## Entra → Sale
  - **Entra:** un comando del ciclo (crea/lista/retoma/cerrar/validar/guardar/cancelar/eliminar) + slug.
  - **Sale:** el archivo de trabajo abierto en `_hojas_sucias/` (o la acción de gestión ejecutada).

## Relación
  - **Primer paso de cualquier creación** (conversacional o `produccion` Fase 0), abre el archivo de t