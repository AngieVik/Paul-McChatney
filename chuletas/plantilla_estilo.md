---
name: plantilla_estilo
type: plantilla
description: Guía de estilo Markdown del proyecto Paul McChatney: estructura, formato, linting y convenciones de escritura.
---

# plantilla_estilo

- *Guía compacta para escribir archivos Markdown limpios, legibles y compatibles con la configuración del proyecto.*

---

## Índice

`1 · Principio general`
`2 · Estructura base`
`3 · Encabezados`
`4 · Listas`
`5 · Código y tags`
`6 · Tablas`
`7 · Enlaces y rutas`
`8 · YAML`
`9 · Convenciones de casa`
`10 · Checklist final`

---

## 1 · Principio general

El Markdown del proyecto debe ser:

- **Humano:** fácil de leer sin herramientas.
- **Técnico:** fácil de consultar por un agente.
- **Predecible:** misma estructura en archivos parecidos.
- **Ligero:** sin repetir reglas innecesarias dentro del contenido.

El archivo manda por claridad, no por decoración.

---

## 2 · Estructura base

Usa esta forma cuando el archivo sea canónico, es decir: skill, regla, plantilla, conocimiento, jerga, fonetización o proyecto.

```markdown
---
name: nombre_del_archivo
type: tipo
description: Descripción corta y útil.
---

# nombre_del_archivo

- *Línea breve de intención.*

---

## Índice

`1 · Sección`

---

## 1 · Sección

Contenido.
```

Los archivos rápidos o borradores pueden ser más libres, sobre todo dentro de `_hojas_sucias/`.

---

## 3 · Encabezados

Usa encabezados ATX:

```markdown
# H1

## H2

### H3
```

Reglas:

- Un solo `# H1` por archivo.
- No saltes niveles: `#` → `##` → `###`.
- Deja una línea en blanco antes y después de cada encabezado.
- No cierres títulos con `:`, `.`, `;`.
- El H1 debe coincidir con el slug, nombre de skill o nombre conceptual del archivo.

Ejemplos:

```markdown
# letra

## Cuándo se activa

## Pasos
```

---

## 4 · Listas

Usa guion para listas normales:

```markdown
- Elemento.
- Elemento.
    - Subitem.
```

Usa listas numeradas solo cuando el orden importe:

```markdown
1. Crear el archivo.
2. Escribir el `style_box`.
3. Aprobar la obra.
```

Reglas:

- Viñetas siempre con `-`.
- Sublistas con 4 espacios.
- Numeración real: `1.`, `2.`, `3.`.
- Línea en blanco antes y después de cada bloque de lista.

---

## 5 · Código y tags

Usa backticks para nombres técnicos:

```markdown
`style_box`
`lyrics_box`
`composicion/letra.md`
`[Chorus]`
```

Todo bloque de código debe ir cercado y con lenguaje:

```text
[Verse: tense, low vocal delivery]
La noche se abre despacio
```

Lenguajes habituales:

| Uso                 | Lenguaje   |
| ------------------- | ---------- |
| Letras y prompts    | `text`     |
| Markdown de ejemplo | `markdown` |
| Configuración VS    | `json`     |
| Comandos            | `bash`     |

No uses bloques indentados como código. Usa siempre vallas de tres backticks.

---

## 6 · Tablas

Toda tabla debe tener cabecera y separador.

```markdown
| Campo     | Uso             |
| --------- | --------------- |
| style_box | Molde sonoro    |
| letra     | Texto cantable  |
| tags      | Control técnico |
```

Reglas:

- No indentes tablas dentro de listas si puedes evitarlo.
- Deja que Markdown All in One las alinee.
- No uses tablas para contenido largo; mejor secciones.

---

## 7 · Enlaces y rutas

Usa rutas relativas con `/`, aunque trabajes en Windows.

Correcto:

```markdown
[letra](../composicion/letra.md)
`proyectos/60_granos/60_granos.md`
```

Evita:

```markdown
C:\Users\Angel\...
proyectos\60_granos\60_granos.md
```

Semántica de carga:

| Forma       | Uso                                     |
| ----------- | --------------------------------------- |
| `@ruta`     | Carga ansiosa, solo núcleo pequeño.     |
| `ruta`      | Lectura bajo demanda.                   |
| `[texto]()` | Enlace Markdown para navegación humana. |

Regla de oro:

```text
No cargar carpetas enteras. Abrir solo el archivo necesario.
```

---

## 8 · YAML

El YAML sirve para que el archivo sea identificable por herramientas y agentes.

Úsalo en:

- Skills.
- Rules.
- Plantillas.
- Conocimientos.
- Jergas.
- fonetizar.
- Proyectos terminados si se quiere indexación futura.

Forma mínima:

```yaml
---
name: nombre
type: tipo
description: Descripción corta.
---
```

Tipos recomendados:

| Tipo            | Uso                         |
| --------------- | --------------------------- |
| `skill`         | Skills de `.claude/skills/` |
| `map`           | Índices de `.claude/rules/` |
| `plantilla`     | Archivos de `chuletas/`     |
| `conocimientos` | Documentos técnicos         |
| `jerga`         | Guías de jerga              |
| `fonetizacion`  | Guías de fonetización       |
| `proyecto`      | Obras cerradas              |
| `core`          | Contexto raíz               |
| `memory`        | Memoria transversal         |

No metas contenido largo en YAML. El YAML identifica; el cuerpo explica.

---

## 9 · Convenciones de casa

| Elemento       | Convención                               |
| -------------- | ---------------------------------------- |
| H1             | Slug o nombre real del archivo           |
| Índice         | Líneas con backticks y punto medio `·`   |
| Separador      | `---` entre bloques grandes              |
| Cursiva        | Línea de intención o nota suave          |
| Negrita        | Campo, aviso o concepto clave            |
| Backticks      | Tags, rutas, comandos y nombres técnicos |
| Tags musicales | En inglés si son técnicas o generadas    |
| Letra          | Español salvo indicación contraria       |
| Rutas          | Relativas y con `/`                      |

Ejemplo de línea de intención:

```markdown
- *Guía para construir el `style_box` sin cargar toda la CHUPILISTA.*
```

---

## 10 · Checklist final

Antes de guardar:

1. Hay un solo `# H1`.
2. El YAML está cerrado con `---`.
3. Los encabezados no saltan niveles.
4. Las listas usan `-` y sublistas de 4 espacios.
5. Los bloques de código tienen lenguaje.
6. Las rutas son relativas y usan `/`.
7. Las tablas tienen cabecera y separador.
8. No hay carpetas completas cargadas con `@`.
9. El archivo acaba con una única línea final.
