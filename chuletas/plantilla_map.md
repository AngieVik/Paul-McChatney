---
name: plantilla_map
type: plantilla
description: Guia para generar un archivo `concepto -> mapa` en `.claude/rules/<slug>.md`.
---

# plantilla_map

## esqueleto

```markdown
---
name: <slug>
type: map
description: Resumen del contenido indexado.
---

# <slug>

- *No se carga con `@`, este índice es el mapa concepto→archivo, abre `<ruta_objetivo>` bajo demanda con la herramienta de lectura, solo el/los que necesites.*
- **Consulta por búsqueda (grep) o salto por Índice.**
- **Consumido por:** <consumidores>

## <Mapeado>

- Archivos referenciados <Indice> o <Indices>, <Modulos>, <Documentos>, <Guias>, etc.
```

---

## Instrucciones

- *No se carga con `@`. Dos variantes reales según lo que indexa — usa la que corresponda, no asumas siempre un manual en `composicion/`. El marcador `<ruta_objetivo>` del esqueleto se sustituye por la ruta de la variante elegida:*
    - **Mapa → manual único:** `<ruta_objetivo>` = `composicion/<name>.md`, abierto bajo demanda con la herramienta de lectura (ej. `.claude/rules/style_box.md` → `composicion/style_box.md`).
    - **Mapa → biblioteca de archivos:** `<ruta_objetivo>` = `<name>/<archivo>.md`; funciona como índice de una carpeta con varios archivos; abre solo el archivo concreto que la tarea pida, nunca la carpeta entera (ej. `.claude/rules/fonetizar.md` → `fonetizar/<archivo>.md`, `.claude/rules/jerga.md` → `jerga/<archivo>.md`).
- *`<consumidores>` se sustituye por la lista de skills que consumen el mapa (más las fases de `produccion` que apliquen), como en el punto siguiente.*
- **Consulta por búsqueda (grep) o salto por Índice.**
- **Consumido por:** `<skill>` y cualquier otra skill que reutilice este mapa sin llevar su mismo nombre (ej. `fusionar` consume el mapa de `style_box`), `produccion` (Fase N). Si ninguna skill lo reclama todavía, dilo explícitamente en vez de inventar un consumidor.

---
