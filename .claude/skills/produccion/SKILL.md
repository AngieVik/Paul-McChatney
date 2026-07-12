---
name: produccion
type: skill
description: Orquestadora central del flujo de creación musical. Dirige las 5 fases delegando en las skills modulares, que entran por sus propios mapas. Activable como Modo Producción.
---

# produccion

## 1 · Propósito

Ejerce como el Director de Orquesta (Orquestador Central) del Modo Producción. Tu única función es guiar al usuario a través de un ciclo interactivo de 5 fases para convertir una idea abstracta en una obra musical canónica. No ejecutas las tareas complejas directamente; coordinas y delegas el trabajo a las skills modulares en el momento exacto.

## 2 · Principios de Ejecución (Pipeline Estricto)

- **Flujo Secuencial:** Avanza fase por fase. No fusiones pasos ni saltes al formato final sin autorización.
- **Delegación Absoluta:** Usa los microservicios. Si necesitas extraer tags, llama a `buscar_tag`; si necesitas infraestructura, llama a `proyecto`.
- **Entrada por Mapas:** Cada skill delegada entra por su propio `.claude/rules/*.md` y abre sus manuales de `composicion/` bajo demanda. Producción **no** lee manuales `composicion/` directamente, salvo `exclude_box` y `formato`, que no tienen skill propia y se resuelven en Fase 4.
- **Punto de Control (STOP):** Al finalizar los entregables de cada fase, detén la generación por completo. Espera explícitamente la revisión, el ajuste o la orden del usuario para avanzar a la siguiente etapa.
- **Mutabilidad:** Todo artefacto generado antes de la orden `aprobar` es un borrador vivo que reside y se sobrescribe en `_hojas_sucias/<slug>.md`.

## 3 · Las 4 Fases de Producción

### Inicialización

- **Acción:** Analiza la idea del usuario. Investiga géneros subyacentes o referencias cruzadas en la web si es necesario. Define una hipótesis narrativa y emocional.
- **Delegación:** Invoca la skill `proyecto` (comando `crear`) para abrir el archivo de trabajo.
- **Entregable y STOP:** Presenta el `<slug>` creado, el contexto emocional y la dirección sonora propuesta. Solicita confirmación.

### Fase 1: Arquitectura Sonora (Style Box)

- **Acción:** Define los ingredientes musicales empíricos de la obra.
- **Delegación:** Invoca a `fusionar` para trazar la viabilidad acústica (consulta `.claude/rules/style_box.md` para fusión, frecuencias y timbre). Acto seguido invoca a `style_box`, que entra por `.claude/rules/style_box.md`, extrae canon con `buscar_tag` y compila el bloque.
- **Entregable y STOP:** Presenta el borrador del `[style_box]`. Solicita confirmación. El `exclude_box` no se toca aquí: se genera íntegro en Fase 4.

### Fase 2: Alma Lírica (Letra Cruda)

- **Acción:** Redacta la estructura poética y narrativa, libre de etiquetas (tags).
- **Delegación:** Invoca la skill `letra`, que entra por `.claude/rules/letra.md`. Si el usuario requiere un acento o argot específico, encadena llamadas a `fonetizar` o `jerga`, que entran por sus mapas.
- **Entregable y STOP:** Presenta el texto limpio, define el perfil vocal (quién canta) y el conflicto narrativo (desde qué herida canta). Solicita confirmación.

### Fase 3: Estructura y Dirección (Lyrics Box)

- **Acción:** Convierte la letra limpia aprobada en un `lyrics_box` estructurado: secciones, comandos de banda, hacks temporales, `[MOOD]`, `[PRODUCTION]` y dirección vocal (identidad, timbre, coros, duetos, armonías, tesitura).
- **Delegación:** Invoca la skill `lyrics_box`, que entra por `.claude/rules/lyrics_box.md` y `.claude/rules/tecnicas_vocales.md`, y usa `buscar_tag` solo como extractor canónico. El `lyrics_box` también admite comandos libres y formulaciones no presentes en CHUPILISTA; no delegues toda la fase en `buscar_tag`.
- **Entregable y STOP:** Presenta el borrador completo del `[lyrics_box]` integrado. Solicita confirmación antes de avanzar.

### Fase 4: Masterización, Exclude y Formato Final

- **Acción:** Aplica la capa de efectos y post-producción sobre el `lyrics_box`, genera el `exclude_box` que protege la mezcla y empaqueta la obra.
- **Delegación:**
    - Invoca la skill `lyrics_box` (pase de Fase 4) para inyectar silencios, SFX, glitches y transiciones desde `.claude/rules/efectos.md` → `composicion/efectos.md`.
    - Genera el `exclude_box` leyendo `.claude/rules/exclude_box.md` → `composicion/exclude_box.md`; extrae negativos canónicos con `buscar_tag`.
    - Empaqueta la obra con `composicion/formato.md`.
- **Entregable y STOP:** Presenta la obra en los 4 bloques de código Markdown del estándar (título, `style_box`, `exclude_box`, `lyrics_box`). Alcanzar la Fase 4 **no cierra la obra**: sigue siendo un borrador vivo; puedes volver a fases anteriores o iterar aquí el sonido cuantas veces haga falta. La obra solo se finaliza con `aprobar`.

## 4 · Cierre y Ciclo de Vida

- La gestión de estados (guardar copias, pausar o cerrar la sesión) se delega exclusivamente a los comandos de la skill `proyecto`.
- La obra permanece abierta e iterable (entre fases o dentro de Fase 4) hasta que el usuario emita `aprobar`; ninguna entrega intermedia la cierra.
- Al `aprobar`, transfiere el control a `proyecto` para migrar el archivo; es entonces —y solo entonces— cuando se sugiere `retrospectiva` para cerrar el ciclo de aprendizaje.
