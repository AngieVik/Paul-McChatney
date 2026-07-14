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
- # <slug>

## Titulo Original

- El título tal y como se muestra al público, con acentos y mayúsculas reales

## Generated

- La fecha de la generación de la obra aprobada.

## Master

- Cuando el usuario tenga la pista masterizada, marcara el checkbox `Masterizado` para control personal.

[ ] No Masterizado
[X] Masterizado

## style_box

- El style_box exacto usado en la generación de la obra aprobada.

## Negative Prompts

- El exclude_box exacto usado en la generación de la obra aprobada.

## lyrics_box

- Todo el lyrics_box exacto usado en la generación de la obra aprobada.
```

---

## Cómo referenciar archivos del proyecto

Usa **rutas relativas a la raíz del proyecto**. No uses rutas absolutas del sistema ni `C:/...`. Distingue las dos semánticas de carga:

- **`@ruta` = se carga SIEMPRE en contexto** (carga ansiosa). Resérvalo en `CLAUDE.md` solo para el núcleo de comportamiento (`system_prompt/` + `MEMORY.md`).
- **Ruta sin `@` = se abre bajo demanda** con la herramienta de lectura, solo cuando la obra lo pide. todo lo bajo demanda, ruta plana y lectura selectiva.
- **texto/markdown de lectura** (tablas, notas) usa enlaces http: <a href="ejemplo.md">`ejemplo.md`</a>

| Quiero referenciar…                     | Escribo (bajo demanda, sin `@`)                    |
| --------------------------------------- | -------------------------------------------------- |
| Un módulo de la chupilista              | `chupilista/01_core_genres_and_subgenres.md`       |
| Una fonetización                        | `fonetizar/es_andaluz.md`                          |
| Un conocimiento técnico                 | `composicion/tecnicas_vocales.md`                  |
| Una jerga                               | `jerga/argot_canario.md`                           |
| Un proyecto                             | `proyectos/60_granos/60_granos.md`                 |
| Carpeta entera con `@` (`@chupilista/`) | **EVITAR:** cargaría ~13.000 líneas en cada sesión |
