---
name: plantilla_skill
type: plantilla
description: rol de orquestación en positivo
---

# <name>

## Fuentes de Consulta

- *Antes de construir o revisar, identifica cuál de los cuatro patrones reales aplica a esta skill — no todas tienen mapa y manual propios, y no todas las que sí tienen mapa apuntan a un manual único; forzarlo genera rutas falsas.*
    - **Skill técnica con mapa + manual único en `composicion/`** (ej. `style_box`, `letra`):
        - **`<name>` — Mapa:** `.claude/rules/<name>.md`
        - **`<name>` — Archivo técnico:** `composicion/<name>.md`
    - **Skill técnica con mapa + biblioteca propia** (varios archivos, no un manual único; ej. `fonetizar` → carpeta `fonetizar/`, `jerga` → carpeta `jerga/`):
        - **`<name>` — Mapa:** `.claude/rules/<name>.md` (índice de la biblioteca)
        - **`<name>` — Biblioteca:** `<name>/` (abre solo el archivo concreto que la tarea pida, nunca la carpeta entera; no existe `composicion/<name>.md`)
    - **Skill que reutiliza el mapa/manual de otra** (ej. `fusionar` usa el de `style_box`): declara cuál y por qué, no dupliques el contenido.
        - **Mapa compartido:** `.claude/rules/<otra_skill>.md`
        - **Archivo técnico o biblioteca compartidos:** `composicion/<otra_skill>.md` o `<otra_skill>/` (sección concreta si aplica)
    - **Skill orquestadora o de proceso, sin mapa ni manual propio** (ej. `proyecto`, `produccion`, `retrospectiva`, `cover_art`): omite esta sección entera.
- **Canon:** `buscar_tag` → `.claude/rules/chupilista.md` → `chupilista/` (solo si la skill consume tags).
