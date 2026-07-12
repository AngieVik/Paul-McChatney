---
name: readme
type: core
description: Mapa general del proyecto Paul McChatney.
---

# Paul McChatney

- *Sistema documental/agéntico de composición musical con IA: canciones, `style_box`, `lyrics_box`, `exclude_box` y documentación de obras.*

---

## 1 · Regla principal

- *No cargar carpetas enteras. Usa los índices de `.claude/rules/` para saber qué abrir, y abre solo ese archivo.*

```text
Índice → archivo concreto → respuesta
```

- *La política de carga completa y canónica vive en `.claude/CLAUDE.md`; este README solo la resume.*

---

## 2 · Estructura

| Ruta              | Uso                                              |
| ----------------- | ------------------------------------------------ |
| `.claude/`        | Contexto, memoria, reglas y skills.              |
| `.claude/rules/`  | Índices → qué archivo abrir.                     |
| `.claude/skills/` | Habilidades invocables.                          |
| `system_prompt/`  | Identidad y comportamiento de Paul.              |
| `chuletas/`       | Plantillas y guías base.                         |
| `chupilista/`     | Tags: géneros, efectos, estructuras, negativos.  |
| `composicion/`    | Reglas técnicas de escritura, efectos y formato. |
| `fonetizar/`      | Acentos e idiomas cantados.                      |
| `jerga/`          | Modismos locales para la letra.                  |
| `proyectos/`      | Obras terminadas, una carpeta por obra.          |
| `PROYECTOS.md`    | Catálogo de obras aprobadas.                     |

- *Carpetas con guion bajo (`_docs`, `_hojas_sucias`, `_produccion`, `_prompts_antiguos`, `_temp`) son locales y no se cargan por defecto — ver `.claude/CLAUDE.md`.*

---

## 3 · Flujo básico

1. Leer `system_prompt/system_prompt.md` y `.claude/MEMORY.md`.
2. Consultar `.claude/CLAUDE.md` y el índice correspondiente en `.claude/rules/`.
3. Abrir solo el archivo necesario y trabajar por fases con `produccion`.
4. Guardar la obra aprobada en `proyectos/<slug>/<slug>.md` y registrarla en `PROYECTOS.md`.
5. Ejecutar retrospectiva solo si deja aprendizaje real.

---

## 4 · Skills principales

| Skill           | Uso                                        |
| --------------- | ------------------------------------------ |
| `produccion`    | Flujo completo de creación en fases.       |
| `proyecto`      | Crear, retomar, guardar, aprobar o cerrar. |
| `letra`         | Escribir o pulir letra limpia.             |
| `style_box`     | Crear o iterar el molde sonoro.            |
| `buscar_tag`    | Buscar tags concretos en CHUPILISTA.       |
| `fusionar`      | Proponer fusiones de género.               |
| `fonetizar`     | Aplicar acento o idioma cantado.           |
| `jerga`         | Inyectar modismos locales en la letra.     |
| `cover_art`     | Crear prompts de portada para Gemini.      |
| `retrospectiva` | Evaluar aprendizaje tras aprobar una obra. |

---

## 5 · Formato de salida y Obra terminada

El formato de salida estandar para los proyectos en curso, vive en `composicion\formato.md`, formato de salida para `producción`:

```text
`título`
`style_box`
`exclude_box`
`lyrics_box`
```

Cada obra aprobada vive en `proyectos/<slug>/<slug>.md` y se registra en `PROYECTOS.md`:

```text
# <slug>
## Titulo Original
## Generated
## Master
## style_box
## Sliders
## Negative Prompts
## Lyrics Box
```

---

## 6 · Estilo y memoria

- *Guía de estilo completa: `chuletas/plantilla_estilo.md`.*

Un prompt no aprobado es hipótesis, no conocimiento. Solo una obra aprobada genera aprendizaje estable, y se archiva donde se consume:

| Tipo de aprendizaje | Destino             |
| ------------------- | ------------------- |
| Principio general   | `.claude/MEMORY.md` |
| Técnica concreta    | `composicion/`      |
| Relación obra-regla | `PROYECTOS.md`      |
