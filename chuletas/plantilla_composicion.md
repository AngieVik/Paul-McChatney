---
name: plantilla_composicion
type: plantilla
description: Archivo técnico de referencia para construir un archivo de `composicion`.
---

# plantilla_composicion

---

## esqueleto

```markdown
---
name: <slug>
type: composicion
description: <descripcion>
---

# <slug>

## Referencias

## Indice

## <otros_encabezados>
```

---

## Referencias

- **Manual Técnico:**
    - **Indexado desde:** `.agents/maps/<name>.md`
- **Manual Transversal:**
    - **Indexado desde:** `.agents/maps/composicion.md`
- **Complementarios (cualquier variante, solo si existen):** `composicion/<x>.md` / `.agents/maps/<x>.md`
- **Canon de tags:** `buscar-tag` → `.agents/maps/chupilista.md` → `chupilista/`

---

## Variantes

Todo manual de `composicion/` es una de estas dos variantes. Elige una antes de rellenar «Referencias» y rellena solo esa — no generes ambas ni dejes un marcador de skill o mapa que no existe.

1. **Manual Técnico con mapa y skill propios** (ej. `style_box`, `lyrics_box`): tiene un índice propio en `.agents/maps/` y una skill dedicada con nombre compatible (`style-box`, `lyrics-box`).
2. **Manual Transversal** (ej. `composicion/formato.md`): no tiene skill ni mapa propios; se indexa como una fila más dentro de `.agents/maps/composicion.md`.

---
