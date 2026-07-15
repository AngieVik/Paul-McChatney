---
name: plantilla_proyecto
type: plantilla
description: Plantilla canónica de consolidación. Se aplica al aprobar una obra para generar proyectos/<slug>/<slug>.md.
---

# plantilla_proyecto

---

## Esqueleto

```markdown
---
name: <slug>
type: proyecto
description: "<titulo_publico>"
---

# <slug>

## Titulo Original

<titulo_publico>

## Generated

Generated at <YYYY-MM-DD>

## Master

[ ] Masterizado

## style_box

<style_box>

## exclude_box

<exclude_box>

## lyrics_box

<lyrics_box>
```

---

### Qué va en cada marcador

- **`<slug>`:** identificador de archivo/carpeta, `snake_case`, sin acentos.
- **`<titulo_publico>`:** el título tal y como se muestra al público, con acentos y mayúsculas reales.
- **`<YYYY-MM-DD>`:** fecha de la generación de la obra aprobada.
- **`[ ] Masterizado`:** por defecto sin marcar; marca el checkbox cuando el usuario tenga la pista masterizada, es control personal, no automático.
- **`<style_box>`:** el `style_box` usado en la generación de la obra aprobada.
- **`<exclude_box>`:** el `exclude_box` usado en la generación de la obra aprobada.
- **`<lyrics_box>`:** todo el `lyrics_box` usado en la generación de la obra aprobada.

---

## Convenciones de nombre y ubicación

- **`_hojas_sucias/`:** estructura libre y sin mínimos — ideas sueltas y bocetos, sin formato fijo.
- **Obra aprobada:** las seis secciones del esqueleto (`Titulo Original`, `Generated`, `Master`, `style_box`, `exclude_box`, `lyrics_box`) son el **núcleo obligatorio** del catálogo — el validador las exige. Sobre ese núcleo, la plantilla admite **secciones adicionales opcionales** según lo que la obra necesite y puede evolucionar, siempre manteniendo la coherencia con el resto del catálogo.
- **Cada proyecto** vive en `proyectos/<slug>/<slug>.md` (carpeta propia) y se registra como fila en `PROYECTOS.md`, dentro de su LP o categoría.

---

## Cómo referenciar archivos del proyecto

- **Política de carga completa:** ver `.claude/CLAUDE.md` (fuente canónica) — no se repite aquí. Esta sección cubre solo la sintaxis de rutas dentro de un proyecto.
- **Ruta para herramientas** (la que abre el agente con la herramienta de lectura): relativa a la raíz del repositorio, sin `@`, con `/` aunque el sistema sea Windows. Ej.: `composicion/letra.md`.
- **Enlace navegable** (para que un humano haga clic desde este documento): etiqueta `<a href="<ruta_relativa>">`, con la ruta relativa al propio archivo que contiene el enlace — no a la raíz. (dos niveles arriba, típico desde `proyectos/<slug>/<slug>.md`).

| Quiero referenciar…        | Ruta para herramientas (raíz, sin `@`)       |
| -------------------------- | -------------------------------------------- |
| Un módulo de la chupilista | `chupilista/01_core_genres_and_subgenres.md` |
| Una fonetización           | `fonetizar/es_andaluz.md`                    |
| Un conocimiento técnico    | `composicion/tecnicas_vocales.md`            |
| Una jerga                  | `jerga/argot_canario.md`                     |
| Un proyecto                | `proyectos/60_granos/60_granos.md`           |

---
