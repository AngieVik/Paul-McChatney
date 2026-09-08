---
name: plantilla_map
type: plantilla
description: Guia para generar un archivo `concepto -> mapa` en `.agents/maps/<slug>.md`.
---

# plantilla_map

## esqueleto

```markdown
---
name: <slug>
type: map
description: <Resumen>
---

# <slug>

- *Este índice es el mapa concepto→archivo; abre `<ruta_objetivo>` bajo demanda, solo el/los archivos que necesites.*
- **Consulta por búsqueda o salto por Índice.**

## <Mapeado>

- Archivos referenciados <Indice> o <Indices>, <Modulos>, <Documentos>, <Guias>, etc.
```

---

## Instrucciones

- *Dos variantes reales según lo que indexa: usa la que corresponda y no asumas siempre un manual en `composicion/`. El marcador `<ruta_objetivo>` del esqueleto se sustituye por la ruta de la variante elegida:*
    - **Mapa → manual único:** `<ruta_objetivo>` = `composicion/<name>.md`, abierto bajo demanda (ej. `.agents/maps/style_box.md` → `composicion/style_box.md`).
    - **Mapa → biblioteca de archivos:** `<ruta_objetivo>` = `<name>/<archivo>.md`; funciona como índice de una carpeta con varios archivos; abre solo el archivo concreto que la tarea pida, nunca la carpeta entera (ej. `.agents/maps/fonetizar.md` → `fonetizar/<archivo>.md`, `.agents/maps/jerga.md` → `jerga/<archivo>.md`).
- **Consulta por búsqueda o salto por Índice.**

---
