---
name: <name>
type: skill
description: rol de orquestación en positivo
---

# <name>

## Fuentes de Consulta

- *Antes de construir o revisar, identifica cuál de los tres patrones reales aplica a esta skill — no todas tienen mapa y manual propios; forzarlo genera rutas falsas.*
    - **Skill técnica con mapa/manual propio** (ej. `style_box`, `letra`, `fonetizar`, `jerga`):
        - **`<name>` — Mapa:** `.claude/rules/<name>.md`
        - **`<name>` — Archivo técnico:** `composicion/<name>.md`
    - **Skill que reutiliza el mapa/manual de otra** (ej. `fusionar` usa el de `style_box`): declara cuál y por qué, no dupliques el contenido.
        - **Mapa compartido:** `.claude/rules/<otra_skill>.md`
        - **Archivo técnico compartido:** `composicion/<otra_skill>.md` (sección concreta si aplica)
    - **Skill orquestadora o de proceso, sin mapa ni manual propio** (ej. `proyecto`, `produccion`, `retrospectiva`, `cover_art`): omite esta sección entera.
- **Canon:** `buscar_tag` → `.claude/rules/chupilista.md` → `chupilista/` (solo si la skill consume tags).
