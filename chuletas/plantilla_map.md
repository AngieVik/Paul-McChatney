---
name: plantilla_map
type: plantilla
description: Guia para generar un archivo `concepto -> mapa` en `.claude/maps/<slug>.md`.
---

# plantilla_map

1. plantilla\_map
    1. Esqueleto
    2. Mapeado
    3. Instrucciones

## Esqueleto

```markdown
---
name: <slug>
type: map
description: <Resumen>
---

# <slug>
```

- *Indice "Concepto" → "Archivo":*
    - **Abre:**
        `<ruta_objetivo>` bajo demanda con la herramienta de lectura, solo el/los que necesites.*
    - **Consulta:**
        - Búsqueda por *Grep*.
        - Salto por *Índice.*



## Mapeado

- Archivos referenciados <Indice> o <Indices>, <Modulos>, <Documentos>, <Guias>, etc.

---

## Instrucciones

- *No se carga con `@`. Dos variantes reales según lo que indexa — usa la que corresponda, no asumas siempre un manual en `composicion/`. El marcador `<ruta_objetivo>` del esqueleto se sustituye por la ruta de la variante elegida:*
    - **Mapa → manual único:** `<ruta_objetivo>` = `composicion/<name>.md`, abierto bajo demanda con la herramienta de lectura (ej. `.claude/maps/style_box.md` → `composicion/style_box.md`).
    - **Mapa → biblioteca de archivos:** `<ruta_objetivo>` = `<name>/<archivo>.md`; funciona como índice de una carpeta con varios archivos; abre solo el archivo concreto que la tarea pida, nunca la carpeta entera (ej. `.claude/maps/fonetizar.md` → `fonetizar/<archivo>.md`, `.claude/maps/jerga.md` → `jerga/<archivo>.md`).
    - **Consulta:**
        - Búsqueda por *Grep*.
        - Salto por *Índice.*

---
