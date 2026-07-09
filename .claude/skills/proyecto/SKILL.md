---
name: proyecto
type: skill
description: Crea y gestiona el archivo de trabajo de una obra. Primer paso de cualquier creación.
---

# proyecto

- Orquesta los **archivos del proyecto**.
- Al arrancar cualquier creación, `crear` el `.md` en `_hojas_sucias/`.
- La última versión real del proyecto, donde se vuelca y **se sobrescribe** lo que se va creando.

## Cuándo se activa

- **Al solicitar explícitamente** `crear` un mood u obra.
- **Al solicitar explícitamente** `listar` moods u obras aprobadas o en proceso.
- **Al solicitar explícitamente** `retomar` un proyecto aprobado o en proceso.
- La invoca **Fase 0** en `produccion`, para `crear` el archivo, al `aprobar` migrar a terminados.

## Relación

- **Primer paso de cualquier creación** para `crear` el `archivo de trabajo` con `chuletas/plantilla_hoja_sucia.md`.
- Al `aprobar` la obra terminada, genera la plantilla final `chuletas/plantilla_proyecto.md`.
- Al **aprobar**, si la obra contiene hallazgos técnicos o creativos de valor, **sugiere** al usuario iniciar **`retrospectiva`** (`conocimientos/retrospectiva.md`).

## Comandos

- `crear`: genera `_hojas_sucias/<slug>.md` (slug en `snake_case`, sin acentos ni eñes) con un borrador dinámico del proyecto nuevo solicitado, usando `chuletas/plantilla_hoja_sucia.md` como guía conceptual (no estricta); haz preguntas.
    - Es el `archivo de trabajo` libre que se *sobrescribe* según avanza; si el usuario pega una versión consolidada, esa pasa a ser la actual.
- `listar`: muestra lo que se te solicite, obras vivas en `_hojas_sucias/`, el catálogo de `PROYECTOS.md`, etc.
- `retomar`:
    - Desde *proyecto terminado*: copia su contenido de `proyectos/<slug>/` a `_hojas_sucias/<slug>.md` y resume su estado para retomar el trabajo.
    - Desde *proyecto en hojas sucias*: abre el `.md` y resume su estado para retomar.
- `cerrar`: sale del contexto del proyecto en curso para volver al Modo Conversacional y/o hacer otra cosa (no borra nada).
- `aprobar`: da por finalizada satisfactoriamente una obra, migra a `proyectos/<slug>/<slug>.md` con la plantilla (`chuletas/plantilla_proyecto.md`) y la registra en `PROYECTOS.md`.
- `guardar`: crea una copia de seguridad `_hojas_sucias/<slug>_NN.md` (duplicado exacto del estado en ese momento).
- `cancelar`: aborta el contexto de ese momento sin cerrar el proyecto en curso.
- `eliminar`: borra por completo todo rastro del proyecto y el contexto de ese momento.

## Mapa del almacenamiento

| Capa                     | Dónde                              | Qué guarda                                                                    |
| ------------------------ | ---------------------------------- | ----------------------------------------------------------------------------- |
| Trabajo en curso         | `_hojas_sucias/<slug>.md`          | El proyecto en proceso, se sobrescribe según avanza (libre, sin formato fijo) |
| Obras aprobadas          | `proyectos/<slug>/<slug>.md`       | Archivo final de la obra aprobado                                             |
| Catálogo Obras aprobadas | `PROYECTOS.md`                     | Catálogo de todas las obras aprobadas                                         |
| Plantilla trabajo        | `chuletas/plantilla_hoja_sucia.md` | guía conceptual del archivo en curso (no estricta)                            |
| Plantilla final          | `chuletas/plantilla_proyecto.md`   | formato canónico del archivo terminado                                        |

## Entra → Sale

- **Entra:** un comando del ciclo (`crear`/`listar`/`retomar`/`cerrar`/`aprobar`/`guardar`/`cancelar`/`eliminar`) + slug.
- **Sale:** el archivo de trabajo abierto en `_hojas_sucias/` (o la acción de gestión ejecutada).

## Ejemplo

**Entrada:**  
    ```text  
    Usuario: `<Crea el proyecto para la bulería metalera del herrero>`  
    ```
**Salida:**  
    ```text  
    Acción: `crear`. Abro `_hojas_sucias/buleria_metalera_herrero.md` aplicando la plantilla y resumo el estado inicial para que comencemos a trabajar en el proyecto.  
    ```
