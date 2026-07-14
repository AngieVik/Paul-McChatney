---
name: "plantilla_composicion"
type: "plantilla"
description: "Archivo técnico de referencia para construir un archivo de `composicion`."
---

# plantilla_composicion

---

## esqueleto

```markdown
---
name: <slug>
type: composicion
description: "<descripcion>"
---

# <slug>

## Referencias

## Indice

## <otros_encabezados>
```

---

## Referencias

- **Manual Técnico:**
    - **Indexado desde:** `.claude/rules/<name>.md`
    - **Consumido desde:** `.claude/skills/<name>/SKILL.md`, y cualquier otra skill que reutilice este manual sin compartir su nombre (ej. `composicion/style_box.md` lo consumen tanto `style_box` como `fusionar`).
- **Manual Transversal:**
    - **Indexado desde:** `.claude/rules/composicion.md`
    - **Consumido desde:** <lista de skills que lo usan, ej. `style_box`, `lyrics_box`, `exclude_box`, `produccion`>
- **Complementarios (cualquier variante, solo si existen):** `composicion/<x>.md` / `.claude/rules/<x>.md`
- **Canon de tags:** `buscar_tag` → `.claude/rules/chupilista.md` → `chupilista/`

---

## Variantes

Todo manual de `composicion/` es una de estas dos variantes. Elige una antes de rellenar «Referencias» y rellena solo esa — no generes ambas ni dejes un marcador de skill o mapa que no existe.

1. **Manual Técnico con mapa y skill propios** (ej. `style_box`, `lyrics_box`): tiene una skill dedicada que lo consume y un índice propio en `.claude/rules/`.
2. **Manual Transversal** (ej. `composicion/formato.md`): no tiene skill ni mapa propios; se indexa como una fila más dentro de `.claude/rules/composicion.md` y lo consumen directamente otras skills.

---
