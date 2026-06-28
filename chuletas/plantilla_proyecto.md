# plantilla_proyecto

> **Plantilla canónica de proyecto.** Cópiala para abrir una canción nueva en `proyectos/<slug>/<slug>.md`. Respeta el orden de secciones y el estilo de relleno; así los agentes futuros mantienen la coherencia del catálogo.

---

## Convenciones de nombre y ubicación

- **Nombre de archivo = slug** en `snake_case`, sin acentos ni eñes, sin espacios. Ej.: `La Virgen Tapiada` → `la_virgen_tapiada.md`.
- **Cada proyecto** vive en `proyectos/<slug>/<slug>.md` (carpeta propia) y se registra como fila en `PROYECTOS.md`.
- **Ideas sueltas y bocetos** viven en `_hojas_sucias/` (espacio libre, sin formato fijo).
- **El `# H1` del archivo = el slug** (no el título bonito; ese va en *Titulo Original*).
- **Un proyecto evoluciona sin ritmo fijo:** no hay datos mínimos obligatorios.

---

## Esqueleto a copiar

La **línea 3** abre un bloque `yaml` que **no se cierra**: así todo el prompt luce monoespaciado y limpio.
Si la obra está masterizada, se marca el checkbox `**Masterizado**`.

# <slug>

```yaml

## Titulo Original

<El título tal y como se muestra al público, con acentos y mayúsculas reales>

## Generated

<La fecha de la generación de la obra final>

## Master

[ ] No Masterizado
[X] Masterizado

## Style Box

<El style_box exacto usado en la generación final>

## Sliders

Rareza <NN>%
Influencia estilo <NN>%

## Negative Prompts

<El exclude_styles exacto usado en la generación final>

## Lyrics Box

<Todo el lyrics_box exacto usado en la generación final>

La valla `yaml` se abre en la línea 3 y **no lleva cierre** `​``` al final del archivo.

---

## Reglas de relleno

- **Titulo Original:** texto humano, libre de slug. Si es cover o reinterpreta una obra conocida, indícalo: `<Título nuevo> (<obra original>)` o `(Cover)`.
- **Style Box:** se pega **exactamente** como entra en Suno. Género de fusión primero, en MAYÚSCULAS; subgéneros de apoyo en minúsculas. Las líneas `Style Influence` / `Audio Influence` solo si se usaron.
- **Negative Prompts:** una sola línea, comas, sin corchetes.
- **Lyrics Box:** copia íntegra y lista para producción —`[MOOD]` y `[PRODUCTION]` arriba del todo, Persona Stacking después, y la letra con sus metaetiquetas.
- **Masterizado:** opcional. Solo cuando tengas la pista masterizada, marca el checkbox `**Masterizado**`

---

## Cómo referenciar archivos del proyecto

Usa **rutas relativas a la raíz del proyecto**. No uses rutas absolutas del sistema ni `C:\...`. Distingue las dos semánticas de carga:

- **`@ruta` = se carga SIEMPRE en contexto** (carga ansiosa). Resérvalo en `CLAUDE.md` para el núcleo de comportamiento (`system_prompt/` + `MEMORY.md`), que es pequeño.
- **Ruta sin `@` = se abre bajo demanda** con la herramienta de lectura, solo cuando la obra lo pide. Es lo correcto para CHUPILISTA, fonetizaciones, conocimientos y proyectos.

| Quiero referenciar… | Escribo (bajo demanda, sin `@`) |
| --- | --- |
| Un módulo de la CHUPILISTA | `chupilista/01_core_genres_and_subgenres.md` |
| Una fonetización | `fonetizaciones/andaluz.md` |
| Un conocimiento técnico | `conocimientos/manual_alquimia_sonora.md` |
| Un módulo del system prompt | `system_prompt/05_lirica.md` |
| Un proyecto | `proyectos/60_granos/60_granos.md` |
| ⚠️ Carpeta entera con `@` (`@chupilista/`) | **EVITAR:** cargaría ~13.000 líneas en cada sesión |

- En **texto/markdown de lectura** (tablas, notas) usa enlaces relativos normales: `[andaluz](../fonetizaciones/andaluz.md)`.
- En **CLAUDE.md** reserva `@` solo para el núcleo; todo lo bajo demanda, ruta plana y lectura selectiva.
- Enlaza memorias y aprendizajes cruzados apuntando a `@.claude/MEMORY.md` y a la retrospectiva del proyecto concreto.
