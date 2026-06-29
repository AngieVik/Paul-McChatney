---
name: proyecto
description: gestiona ideas de proyectos en `_hojas_sucias\` (crear, listar, retomar) y la memoria de proyectos.
---

# proyecto

Orquesta la **memoria de proyectos**: el ciclo de vida de una obra desde idea hasta aprendizaje acumulado.
Crea, lista y retoma proyectos, y cierra el bucle de retros.

## Mapa de la memoria

| Capa             | Dónde                            | Qué guarda                            |
| ---------------- | -------------------------------- | ------------------------------------- |
| Ideas \ backlog  | `@_hojas_sucias\<slug>.md`       | conceptos sin producir, bocetos       |
| Obras terminadas | `proyectos\<slug>\<slug>.md`     | prompt final + retrospectiva          |
| Catálogo         | `@PROYECTOS.md`                  | índice navegable por género           |
| Memoria global   | `@.claude\MEMORY.md`             | aprendizajes que trascienden una obra |
| Plantilla        | `chuletas\plantilla_proyecto.md` | formato canónico                      |

## Acciones

- **Crear idea:** copia la plantilla a `_hojas_sucias\<slug>.md` (slug en `snake_case` sin acentos) y rellena lo que haya.
- **Listar:** muestra ideas abiertas en `_hojas_sucias\` y\o el catálogo de `PROYECTOS.md`.
- **Retomar:** abre el `.md`, resume su estado y propón la siguiente fase.
- **Cerrar (tras validar):** migra la idea a `proyectos\<slug>\`, añade fila en `PROYECTOS.md`, y lanza la **retrospectiva** (`conocimientos\retrospectiva.md`). Sube a `@.claude\MEMORY.md` solo lo reutilizable.

## Regla de oro de la memoria

Un prompt no validado en producción es hipótesis, no conocimiento: no escala a MEMORY ni a los archivos vivos hasta que el usuario valida la obra.
Todo aprendizaje se redacta en **positivo** (qué hacer la próxima vez).

## Ejemplo

> «retoma la idea del herrero gitano» → abro `_hojas_sucias\el_herrero_gitano.md`,
> resumo que está en Fase 2 y propongo seguir con el etiquetado.
