---
name: plantilla_proyecto
type: plantilla
description: Plantilla canónica de proyecto. Cópiala para abrir una canción nueva en `proyectos/<slug>/<slug>.md`. Respeta el orden de secciones y el estilo de relleno; así los agentes futuros mantienen la coherencia del catálogo.
---

# plantilla_proyecto

## Convenciones de nombre y ubicación

- **Un proyecto evoluciona sin ritmo fijo:** no hay datos mínimos obligatorios.
- **Ideas sueltas y bocetos** viven en `_hojas_sucias/` (espacio libre, sin formato fijo).
- **Cada proyecto** vive en `proyectos/<slug>/<slug>.md` (carpeta propia) y se registra como fila en `PROYECTOS.md`, dentro de su LP o categoría.

---

## Esqueleto a copiar

```text
---
name: <slug>
type: proyecto
description: <titulo_publico>
schema_version: 1
---

# <slug>

## Titulo Original

<titulo_publico>

## Generated

<YYYY-MM-DD>

## Master

[ ] Masterizado

## style_box

<style_box_exacto>

## exclude_box

<exclude_box_exacto>

## lyrics_box

<lyrics_box_exacto>
```

- *`slider_box` queda descartado: no forma parte del esqueleto canónico. "Negative Prompts" se llama `exclude_box` en todo el sistema — usa siempre ese nombre, nunca el alias.*

### Qué va en cada marcador

- **`<slug>`:** identificador de archivo/carpeta, `snake_case`, sin acentos.
- **`<titulo_publico>`:** el título tal y como se muestra al público, con acentos y mayúsculas reales.
- **`<YYYY-MM-DD>`:** fecha de la generación de la obra aprobada.
- **`[ ] Masterizado`:** por defecto sin marcar; marca el checkbox cuando el usuario tenga la pista masterizada, es control personal, no automático.
- **`<style_box_exacto>`:** el `style_box` exacto usado en la generación de la obra aprobada.
- **`<exclude_box_exacto>`:** el `exclude_box` exacto usado en la generación de la obra aprobada.
- **`<lyrics_box_exacto>`:** todo el `lyrics_box` exacto usado en la generación de la obra aprobada.

---

## Cómo referenciar archivos del proyecto

- **Política de carga completa:** ver `.claude/CLAUDE.md` (fuente canónica) — no se repite aquí. Esta sección cubre solo la sintaxis de rutas dentro de un proyecto.
- **Ruta para herramientas** (la que abre el agente con la herramienta de lectura): relativa a la raíz del repositorio, sin `@`, con `/` aunque el sistema sea Windows. Ej.: `composicion/letra.md`.
- **Enlace navegable** (para que un humano haga clic desde este documento): etiqueta `<a href="<ruta_relativa>">`, con la ruta relativa al propio archivo que contiene el enlace — no a la raíz. Ej.: <a href="../../composicion/ejemplo.md">`ejemplo.md`</a> (dos niveles arriba, típico desde `proyectos/<slug>/<slug>.md`).

| Quiero referenciar…        | Ruta para herramientas (raíz, sin `@`)       |
| --------------------------- | ---------------------------------------------- |
| Un módulo de la chupilista | `chupilista/01_core_genres_and_subgenres.md` |
| Una fonetización           | `fonetizar/es_andaluz.md`                    |
| Un conocimiento técnico    | `composicion/tecnicas_vocales.md`            |
| Una jerga                  | `jerga/argot_canario.md`                     |
| Un proyecto                | `proyectos/60_granos/60_granos.md`           |

- **Evitar:** cargar una carpeta entera con `@` (`@chupilista/`) — cargaría ~13.000 líneas en cada sesión.
