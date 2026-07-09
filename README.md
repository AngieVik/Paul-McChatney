---
name: readme
type: core
description: Mapa general del proyecto Paul McChatney.
---

# Paul McChatney

- *Sistema de composición musical para crear canciones, prompts, `style_box`, `lyrics_box`, `exclude_box` y documentación de proyectos musicales.*

---

## 1 · Qué es

- *Paul McChatney es un sistema documental/agéntico para componer obras musicales con IA.*

El repo organiza:

- Identidad y comportamiento del agente.
- Skills de trabajo.
- Mapas de consulta.
- Bibliotecas de tags.
- Guías de composición.
- Jerga y fonetización.
- Plantillas.
- Catálogo de canciones terminadas.

---

## 2 · Regla principal

- *No cargar carpetas enteras.*

Usar primero los índices de `.claude/rules/` y abrir solo el archivo necesario.

```text
Índice → archivo concreto → respuesta
```

## 3 · Estructura

| Ruta              | Uso                                                            |
| ----------------- | -------------------------------------------------------------- |
| `.claude/`        | Contexto, memoria, reglas y skills.                            |
| `.claude/skills/` | Habilidades invocables: producir, auditar, fonetizar, etc.     |
| `.claude/rules/`  | Mapas de consulta para saber qué archivo abrir.                |
| `system_prompt/`  | Identidad y comportamiento principal de Paul McChatney.        |
| `chuletas/`       | Plantillas y guías base.                                       |
| `chupilista/`     | Biblioteca de tags, géneros, efectos, estructuras y negativos. |
| `composicion/`    | Reglas técnicas de escritura, estructura, efectos y formato.   |
| `conocimientos/`  | Documentos de conocimiento transversal.                        |
| `fonetizaciones/` | Guías para simular acentos o idiomas cantados en español.      |
| `jerga/`          | Guías para inyectar modismos locales en la letra cantable.     |
| `proyectos/`      | Canciones terminadas, una carpeta por obra.                    |
| `PROYECTOS.md`    | Catálogo general de obras aprobadas.                           |

## 4 · Carpetas Ignoradas

- *Estas carpetas existen para trabajo local, referencias o material pesado, pero no forman parte del núcleo versionado:*

| Ruta                 | Uso                                                 |
| -------------------- | --------------------------------------------------- |
| `_docs/`             | Documentos de referencia.                           |
| `_hojas_sucias/`     | Borradores vivos, ideas y proyectos en curso.       |
| `_produccion/`       | Audio, referencias, stems, plugins o masterización. |
| `_prompts_antiguos/` | Prompts antiguos o descartados.                     |
| `_temp/`             | Archivos temporales.                                |

## 5 · Flujo básico

1. Leer `system_prompt/system_prompt.md`.
2. Leer `.claude/MEMORY.md`.
3. Consultar `.claude/CLAUDE.md`.
4. Usar `.claude/rules/` como mapa.
5. Abrir solo el archivo necesario.
6. Trabajar por fases con produccion.
7. Guardar obras aprobadas en `proyectos/<slug>/<slug>.md`.
8. Registrar la obra en `PROYECTOS.md`.
9. Ejecutar retrospectiva solo si la obra aprobada deja aprendizaje real.

## 6 · Skills principales

| Skill           | Uso                                        |
| --------------- | ------------------------------------------ |
| `produccion`    | Flujo completo de creación en fases.       |
| `proyecto`      | Crear, retomar, guardar, aprobar o cerrar. |
| `lirica`        | Escribir o pulir letra limpia.             |
| `style-box`     | Crear o iterar el molde sonoro.            |
| `buscar-tag`    | Buscar tags concretos en CHUPILISTA.       |
| `fusionar`      | Proponer fusiones de género.               |
| `fonetizar`     | Aplicar acento o idioma cantado.           |
| `jerga`         | Inyectar modismos locales en la letra.     |
| `auditar`       | Revisar errores, clichés y formato.        |
| `cover-art`     | Crear prompts de portada para Gemini.      |
| `retrospectiva` | Evaluar aprendizaje tras aprobar una obra. |

## 7 · Formato de obra terminada

- Cada obra aprobada vive en:
    `proyectos/<slug>/<slug>.md`
- Y debe registrarse en:
    `PROYECTOS.md`

Estructura habitual:
    ```text
    # <slug>
    ## Titulo Original
    ## Generated
    ## Master
    ## Style Box
    ## Sliders
    ## Negative Prompts
    ## Lyrics Box
    ```

## 8 · Estilo Markdown

- *La guía de estilo vive en:*
    chuletas/plantilla_estilo.md

- Reglas base:
    - YAML corto en archivos canónicos.
    - Un solo H1 por archivo.
    - Encabezados ATX.
    - Listas con `-`.
    - Sublistas de 4 espacios.
    - Bloques de código con lenguaje.
    - Rutas relativas con `/`.
    - LF como salto de línea.
    - Sin carpetas completas cargadas con `@`.

## 9 · Principio de memoria

Un prompt no aprobado es hipótesis, no conocimiento.
Solo una obra aprobada puede generar aprendizaje estable.
El aprendizaje se archiva donde se consume:

| Tipo de aprendizaje | Destino             |
| ------------------- | ------------------- |
| Principio general   | `.claude/MEMORY.md` |
| Técnica concreta    | `composicion/`      |
| Relación obra-regla | `PROYECTOS.md`      |

## 10 · Regla de cierre

Si no sabes qué abrir, no abras más archivos.
Consulta el mapa correspondiente en `.claude/rules/`, localiza el archivo exacto y trabaja solo con ese contexto.
