---
name: <name>
type: composicion
description: <qué construye este archivo técnico>
---

# <name>

- *Archivo técnico de referencia para construir, revisar y depurar el `<name>`.*
- *Esta plantilla solo aplica al patrón "manual único"; si la skill consume una biblioteca de varios archivos (ej. `fonetizar`, `jerga`), no crees un `composicion/<name>.md` — no existe ese archivo para ese patrón.*

## Referencias

- **Skills consumidoras:** `.claude/skills/<name>/SKILL.md` y cualquier otra skill que reutilice este manual sin compartir su nombre (ej. `composicion/style_box.md` lo consumen tanto `style_box` como `fusionar`).
- **Mapa propio:** `.claude/rules/<name>.md`
- **Complementarios:** `composicion/<x>.md` / `.claude/rules/<x>.md`
- **Canon de tags:** `buscar_tag` → `.claude/rules/chupilista.md` → `chupilista/`
