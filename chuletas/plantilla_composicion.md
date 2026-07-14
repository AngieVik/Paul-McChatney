---
name: plantilla_composicion
type: plantilla
description: <qué construye este archivo técnico>
---

# <name>

- *Archivo técnico de referencia para construir, revisar y depurar el `<name>`.*
- *Esta plantilla solo aplica al patrón "manual único"; si la skill consume una biblioteca de varios archivos (ej. `fonetizar`, `jerga`), no crees un `composicion/<name>.md` — no existe ese archivo para ese patrón.*

## Variantes

Todo manual de `composicion/` es una de estas dos variantes. Elige una antes de rellenar «Referencias» y rellena solo esa — no generes ambas ni dejes un marcador de skill o mapa que no existe.

1. **Manual técnico con mapa y skill propios** (ej. `style_box`, `lyrics_box`): tiene una skill dedicada que lo consume y un índice propio en `.claude/rules/`.
2. **Manual transversal** (ej. `composicion/formato.md`): no tiene skill ni mapa propios; se indexa como una fila más dentro de `.claude/rules/composicion.md` y lo consumen directamente otras skills.

## Referencias

- **Si es Variante 1 (manual técnico):**
    - **Skill consumidora:** `.claude/skills/<name>/SKILL.md`, y cualquier otra skill que reutilice este manual sin compartir su nombre (ej. `composicion/style_box.md` lo consumen tanto `style_box` como `fusionar`).
    - **Mapa propio:** `.claude/rules/<name>.md`
- **Si es Variante 2 (manual transversal):**
    - **Indexado desde:** `.claude/rules/composicion.md`
    - **Consumido directamente por:** <lista de skills que lo usan, ej. `style_box`, `lyrics_box`, `exclude_box`, `produccion`>
- **Complementarios (cualquier variante, solo si existen):** `composicion/<x>.md` / `.claude/rules/<x>.md`
- **Canon de tags:** `buscar_tag` → `.claude/rules/chupilista.md` → `chupilista/`
