---
name: AGENTS
maps core
description: Contexto de carga, reglas de lectura y mapa principal del proyecto Paul McChatney.
---

# AGENTS

---

## Indice

1. AGENTS
    1. Indice
    2. Lectura de archivos
    3. Mentalidad Limpia
    4. Referencias de Contexto
    5. Especializaciones: Jerga y Fonetizar

---

## Lectura de archivos

- *`Carga automatica`* lee los archivos con @ siempr al completoe para iniciar:
    - `@system_prompt.md`
    - `@MEMORY.md`


- *`Carga selectiva`* El resto de archivos se lee únicamente bajo demanda o cuando la tarea lo requiera:
    - `_docs/`
    - `_hojas_sucias/`
    - `_temp/`
    - `.agents`
    - `automatizaciones/`
    - `chuletas/`
    - `chupilista/`
    - `composicion/`
    - `fonetizar/`
    - `jerga/`
    - `PROYECTOS.md`

## Mentalidad Limpia

- *Al empezar se crea un archivo .md en `_hojas_sucias` (lo abre la skill `proyecto`) que se sobrescribira a medida que avanza el proyecto, es el borrador.*
    - *Si el usuario escribe una versión nueva o una sección, se actualiza en hoja_sucia. Se podrán crear copias de seguridad a petición del usuario  `guardar`, como archivo aparte `_hojas_sucias/<slug>_NN.md`, que solo se leerá bajo demanda.*
    - *Al trabajar sobre una sección especifica, centrate unicamente en esa seccio.*
    - *En la conversación trabajaremos sobre una sola obra hasta `aprobar`, `cerrar`, o `eliminar`. Mantén un único contexto activo para conservar versiones limpias y evitar cruces entre obras.*

---

## Referencias de Contexto

- *Carga Selectiva*: Abrir con la herramienta de lectura, usando rutas sin `@`.*
- *Carga Automatica*: Se importa SIEMPRE al contexto `carga automatica` leyendos y se leen complretos, usando rutas con `@`. Mantén el contexto ligero y preciso
- *Indices*: Consulta primero `.claude/maps/`. Usa el índice adecuado y abre solo ese archivo concreto.

| Nombre           | Concepto                                                                                        | Mapa                               | Ruta                              |
|------------------|-------------------------------------------------------------------------------------------------|------------------------------------|-----------------------------------|
| Chupilista       | Vocabulario exhaustivo de tags y modificadores.                                                 | `.claude/maps/chupilista.md`       | `chupilista/NN_*.md`              |
| Composición      | Índice maestro de los archivos de composición, saber de oficio y técnica de Paul.               | `.claude/maps/composicion.md`      | `composicion/<archivo>.md`        |
| Efectos          | Post-producción, espacio estéreo, DSP, texturas, transiciones y SFX.                            | `.claude/maps/efectos.md`          | `composicion/efectos.md`          |
| Exclude Box      | Prompting inverso y control de artefactos, qué bloquear en el exclude_box.                      | `.claude/maps/exclude_box.md`      | `composicion/exclude_box.md`      |
| Fonetizar        | Instrucciones fonéticas para pronunciación, acento, edad, estado o forma de hablar.             | `.claude/maps/fonetizar.md`        | `fonetizar/<archivo>.md`          |
| Formato          | Formato final de entrega, bloques copiables, obra completa y entrega flexible.                  | `.claude/maps/formato.md`          | `composicion/formato.md`          |
| Jerga            | Guías de jerga para idiomas y dialectos, Permiten inyectar jerga específica en la letra.        | `.claude/maps/jerga.md`            | `jerga/<archivo>.md`              |
| Letra            | Escritura técnica y tipografía, narrativa, control fonético y aritmética métrica.               | `.claude/maps/letra.md`            | `composicion/letra.md`            |
| Lyrics Box       | Control por corchetes, dirección de banda, estructura y hacks temporales.                       | `.claude/maps/lyrics_box.md`       | `composicion/lyrics_box.md`       |
| Plantillas       | Índice maestro de plantillas para la creación de archivos, y estilo.                            | `.claude/maps/plantillas.md`       | `chuletas/<plantilla>.md`         |
| Style_box        | Construcción del style_box con Etiquetas.                                                       | `.claude/maps/style_box.md`        | `composicion/style_box.md`        |
| Técnicas vocales | Puntuación en la letra y dirección vocal, persona Stacking, roles, duetos y armonías multicapa. | `.claude/maps/tecnicas_vocales.md` | `composicion/tecnicas_vocales.md` |
| Proyectos        | Listado de proyectos con la ruta al archivo.                                                    | `PROYECTOS.md`                     | `proyectos/<slug>/<slug>.md`      |

---

## Especializaciones: Jerga y Fonetizar

- *Las skills `jerga` y `fonetizar` son "especializaciones": Paul puede añadir jerga o fonetizaciones desde su propio conocimiento si mejoran la calidad de la obra.*
