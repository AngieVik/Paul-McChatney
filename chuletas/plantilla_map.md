---
name: <name>
type: map
description: resumen del contenido indexado
---

- *No se carga con `@`. Dos variantes reales según lo que indexa — usa la que corresponda, no asumas siempre un manual en `composicion/`:*
    - **Mapa → manual único:** abre `composicion/<name>.md` bajo demanda con la herramienta de lectura (ej. `.claude/rules/style_box.md` → `composicion/style_box.md`).
    - **Mapa → biblioteca de archivos:** funciona como índice de una carpeta con varios archivos; abre solo el archivo concreto que la tarea pida, nunca la carpeta entera (ej. `.claude/rules/fonetizar.md` → `fonetizar/<archivo>.md`, `.claude/rules/jerga.md` → `jerga/<archivo>.md`).
- **Consulta por búsqueda (grep) o salto por Índice.**
- **Consumido por:** `<skill>` y cualquier otra skill que reutilice este mapa sin llevar su mismo nombre (ej. `fusionar` consume el mapa de `style_box`), `produccion` (Fase N). Si ninguna skill lo reclama todavía, dilo explícitamente en vez de inventar un consumidor.
