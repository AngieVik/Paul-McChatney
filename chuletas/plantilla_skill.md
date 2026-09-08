---
name: plantilla_skill
type: plantilla
description: Guia de referencia para crear una skill local en `.agents/skills/<slug>/SKILL.md`.
---

# plantilla_skill

- Las **secciones funcionales son opcionales**: varían según la naturaleza y el objetivo de cada skill, rellena solo las que apliquen. La **identidad documental sí es obligatoria** en toda skill: frontmatter con `name` y `description`, más un único `# H1` igual al `<slug>`.

## Esqueleto

```markdown
---
name: <slug>
description: <Use when + condiciones concretas de activación>
---

# <slug>

## Activación

<Reglas de activación>

## Fuentes de Consulta

<Archivos de referencia>

## Parámetros de Entrada

<Parametros de entrada>

## Flujo de Ejecución

<Flujo de ejecución>

## Principios clave

<Principios clave>

## Reglas de Integridad

<Reglas de integridad>

## Relación con otras skills

<Relación con otras skills>

## Ejemplo

<Ejemplo con `Entrada` y `Salida`>

- **Entrada**
- **Salida**

## Formato de salida

<Formato de salida>

## <otros>
```

---

### Qué va en cada marcador

- **`<slug>`:** identificador de carpeta y `name`, en minúsculas y `kebab-case`, sin acentos.
- **`<Use when + condiciones concretas de activación>`:** empieza por `Use when` y describe solo cuándo debe activarse la skill; el flujo vive en el cuerpo.
- **`<otros>`:** Otros encabezados unicos que sea necesario crear por naturaleza y/o objetivo de la skill.
- **`<Formato de salida>`:** En caso de no existir un ejemplo, puede existir simplemente un formato de salida.
- **`<Flujo de ejecución>`:** Si la skill se desarrolla en varias fases o pasos, se detallan aquí.

---

## Instrucciones

- *Antes de construir o revisar, identifica cuál de los cuatro patrones reales aplica a esta skill — no todas tienen mapa y manual propios, y no todas las que sí tienen mapa apuntan a un manual único; forzarlo genera rutas falsas.*
    - **Skill técnica con mapa + manual único en `composicion/`** (ej. `style-box`, `letra`):
        - **`<name>` — Mapa:** `.agents/maps/<name_con_guion_bajo>.md`
        - **`<name>` — Archivo técnico:** `composicion/<name_con_guion_bajo>.md`
    - **Skill técnica con mapa + biblioteca propia** (varios archivos, no un manual único; ej. `fonetizar` → carpeta `fonetizar/`, `jerga` → carpeta `jerga/`):
        - **`<name>` — Mapa:** `.agents/maps/<name>.md` (índice de la biblioteca)
        - **`<name>` — Biblioteca:** `<name>/` (abre solo el archivo concreto que la tarea pida, nunca la carpeta entera; no existe `composicion/<name>.md`)
    - **Skill que reutiliza el mapa/manual de otra** (ej. `fusionar` usa el de `style_box`): declara cuál y por qué, no dupliques el contenido.
        - **Mapa compartido:** `.agents/maps/<otra_skill>.md`
        - **Archivo técnico o biblioteca compartidos:** `composicion/<otra_skill>.md` o `<otra_skill>/` (sección concreta si aplica)
    - **Skill orquestadora o de proceso, sin mapa ni manual propio** (ej. `proyecto`, `produccion`, `retrospectiva`, `cover-art`): omite esta sección entera.
- **Composición:** si una skill aplica otra, lee y ejecuta ese flujo en el agente actual; no presupongas subagentes.
- **Canon:** `buscar-tag` → `.agents/maps/chupilista.md` → `chupilista/` (solo si la skill consume tags).

---
