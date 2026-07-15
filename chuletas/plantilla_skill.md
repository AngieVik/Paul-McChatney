---
name: plantilla_skill
type: plantilla
description: Guia de referencia para la creacion de un archivo de skill en `.claude/skills/<slug>/SKILL.md`.
---

# plantilla_skill

- Las **secciones funcionales son opcionales**: varían según la naturaleza y el objetivo de cada skill, rellena solo las que apliquen. La **identidad documental sí es obligatoria** en toda skill: frontmatter con `name`, `type` y `description`, más un único `# H1` igual al `<slug>`.

## Esqueleto

```markdown
---
name: <slug>
type: skill
description: "<descripcion>"
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

- **`<slug>`:** identificador de archivo/carpeta, `snake_case`, sin acentos.
- **`<otros>`:** Otros encabezados unicos que sea necesario crear por naturaleza y/o objetivo de la skill.
- **`<Formato de salida>`:** En caso de no existir un ejemplo, puede existir simplemente un formato de salida.
- **`<Flujo de ejecución>`:** Si la skill se desarrolla en varias fases o pasos, se detallan aquí.

---

## Instrucciones

- *Antes de construir o revisar, identifica cuál de los cuatro patrones reales aplica a esta skill — no todas tienen mapa y manual propios, y no todas las que sí tienen mapa apuntan a un manual único; forzarlo genera rutas falsas.*
    - **Skill técnica con mapa + manual único en `composicion/`** (ej. `style_box`, `letra`):
        - **`<name>` — Mapa:** `.claude/rules/<name>.md`
        - **`<name>` — Archivo técnico:** `composicion/<name>.md`
    - **Skill técnica con mapa + biblioteca propia** (varios archivos, no un manual único; ej. `fonetizar` → carpeta `fonetizar/`, `jerga` → carpeta `jerga/`):
        - **`<name>` — Mapa:** `.claude/rules/<name>.md` (índice de la biblioteca)
        - **`<name>` — Biblioteca:** `<name>/` (abre solo el archivo concreto que la tarea pida, nunca la carpeta entera; no existe `composicion/<name>.md`)
    - **Skill que reutiliza el mapa/manual de otra** (ej. `fusionar` usa el de `style_box`): declara cuál y por qué, no dupliques el contenido.
        - **Mapa compartido:** `.claude/rules/<otra_skill>.md`
        - **Archivo técnico o biblioteca compartidos:** `composicion/<otra_skill>.md` o `<otra_skill>/` (sección concreta si aplica)
    - **Skill orquestadora o de proceso, sin mapa ni manual propio** (ej. `proyecto`, `produccion`, `retrospectiva`, `cover_art`): omite esta sección entera.
- **Canon:** `buscar_tag` → `.claude/rules/chupilista.md` → `chupilista/` (solo si la skill consume tags).

---
