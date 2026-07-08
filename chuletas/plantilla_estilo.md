# plantilla_estilo

- Guía de estilo Markdown para escribir archivos del proyecto sin pelear con el linter ni con el formateo al guardar.
- Refleja la configuración real de VS Code (markdownlint de David Anson + Markdown All in One, LF, Prettier excluido de `.md`) y el estilo de la casa de Paul McChatney.
- Objetivo: que un archivo nuevo pase `source.fixAll` al guardar sin que se reordene ni salten avisos amarillos.

---

## Índice

`1 · Reglas duras (el linter las exige)`
`2 · Encabezados`
`3 · Índices de sección`
`4 · Listas (cuándo numerada, cuándo viñeta)`
`5 · Negrita y cursiva`
`6 · Código, tags y ejemplos`
`7 · Saltos de línea y espaciado`
`8 · Tablas`
`9 · Enlaces`
`10 · Estilo de la casa`
`11 · Checklist antes de guardar`

---

## 1 · Reglas duras (el linter las exige)

- *Estas son las reglas activas de tu `markdownlint.config`. Romperlas = subrayado amarillo o autocorrección al guardar.*

| Regla   | Qué obliga                                          | En corto                              |
| ------- | --------------------------------------------------- | ------------------------------------- |
| `MD003` | Encabezados estilo ATX (`#`, `##`, `###`).          | Nunca subrayados con `===`.           |
| `MD001` | No saltar jerarquía.                                | De `#` a `##`, nunca directo a `###`. |
| `MD022` | Línea en blanco antes y después de cada encabezado. | Un hueco arriba, un hueco abajo.      |
| `MD004` | Viñetas siempre con guion `-`.                      | Nada de `*` ni `+` en listas.         |
| `MD007` | Sublistas indentadas con 2 espacios.                | Cada nivel suma 2 espacios exactos.   |
| `MD005` | Misma indentación entre ítems del mismo nivel.      | No descuadrar sangrías.               |
| `MD029` | Listas numeradas en orden lógico.                   | `1.` `2.` `3.`, nunca todo `1.`.      |
| `MD050` | Negrita con dobles asteriscos.                      | `**negrita**`.                        |
| `MD031` | Bloques de código aislados por líneas en blanco.    | Hueco antes y después de la valla.    |
| `MD040` | Todo bloque de código lleva lenguaje.               | `text`, `markdown`, `jsonc`.          |
| `MD046` | Código en bloques cercados (fenced).                | Nunca código por indentación.         |
| `MD038` | Sin espacios sobrantes dentro de `código`.          | `[Tag]`, no con espacios.             |
| `MD032` | Listas rodeadas de línea en blanco.                 | Aísla cada bloque de lista.           |

- *Apagadas a tu favor* (puedes usarlas sin miedo):
    - `MD013`: sin límite de longitud de línea (escribe párrafos largos).
    - `MD009`: se permiten espacios finales (los dos espacios para salto de línea real sobreviven).
    - `MD012`: se permiten varias líneas en blanco seguidas.
    - `MD033`: se permite HTML crudo.
    - `MD034`: se permiten URLs sin `<>`.
    - `MD024`: títulos iguales permitidos si no son hermanos directos.

---

## 2 · Encabezados

- *Un solo `# H1` por archivo* (el título = el nombre del archivo o el slug).
- *Baja de nivel sin saltos:* `#` a `##` a `###`. Nunca de `#` a `###`.
- *Espacio tras la almohadilla y línea en blanco arriba y abajo:*

```markdown
párrafo anterior.

## 2 · Título de sección

Contenido de la sección.
```

- *No termines un título con signo de puntuación* (`.`, `:`, `;`). Un `)` de cierre sí vale.

---

## 3 · Índices de sección

- *Convención de la casa:* el índice va como líneas sueltas envueltas en comillas invertidas, con `·` (punto medio) separando número y título.

```markdown
## Índice

`1 · Primera sección`
`2 · Segunda sección`
    `2.1 · Subapartado`
```

- *Las subsecciones se indentan 2 espacios* bajo su sección padre, igual que una sublista.
- *El índice debe reflejar exactamente los encabezados* `## N · …` y `### N.N · …` del cuerpo. Si renombras una sección, actualiza el índice.

---

## 4 · Listas (cuándo numerada, cuándo viñeta)

- *Viñeta (`-`):* para enumerar cosas sin orden ni jerarquía: opciones, características, ejemplos sueltos. Es la lista por defecto del proyecto.
- *Numerada (`1.` `2.` `3.`):* solo cuando el orden importa: pasos de un proceso, fases, prioridad, o una secuencia que se sigue de arriba abajo.
- *Reglas de forma:*
    - Guion `-` para toda viñeta (`MD004`).
    - Sangría de sublista: exactamente 4 espacios por nivel (`MD007`).
    - Numeración correlativa real `1. 2. 3.` (`MD029`), no repetir `1.`.
    - Línea en blanco antes y después del bloque de lista (`MD032`).

```markdown
Pasos del flujo:

1. Abrir la hoja de trabajo.
2. Construir el `style_box`.
3. Escribir la letra.

Elementos sueltos:

- Reverb.
- Delay.
- Saturación.
```

---

## 5 · Negrita y cursiva

- **Negrita `**...**`:** para etiquetas de campo (`**Ejemplo:**`, `**Regla:**`), términos clave la primera vez que aparecen y avisos críticos. Es señalización, no decoración.
- *Cursiva `*...*`:* para líneas descriptivas o meta (glosas, notas de una sección, aclaraciones) y énfasis suave. En la casa, la línea de intención bajo un encabezado va en cursiva: `- *De qué va esta sección.*`
- *Indicador de cursiva:* asterisco simple `*` (tu config lo fuerza), nunca guion bajo.
- *Sin espacios dentro de los marcadores:* `**negrita**`, no con espacios interiores.
- *Contención:* no acumules negritas ni subrayes medio párrafo. Si todo destaca, nada destaca.

---

## 6 · Código, tags y ejemplos

- *Tags y nombres de archivo en línea con comillas invertidas, sin espacios interiores:* `` `[Chorus]` ``, `` `style_box` ``, `` `composicion/letra.md` ``.
- *Bloques de código siempre cercados y con lenguaje* (`MD040` + `MD046`):

```text
[Intro: fast frantic piano solo]
[Verse: chaotic piano]
```

- *Lenguajes útiles aquí:* `text` (letra, prompts, cajas), `markdown` (mostrar sintaxis md), `jsonc` (config comentada), `json`, `bash`.
- *Aísla el bloque con una línea en blanco antes y después* (`MD031`).
- *Ejemplos dentro de una lista:* introdúcelos con un `**Ejemplo:**` en negrita y, debajo, el bloque cercado o líneas en `` `backticks` ``.

---

## 7 · Saltos de línea y espaciado

- *Fin de línea LF.* Tu config lo estandariza; no metas CRLF.
- *Separación de párrafos:* una línea en blanco entre bloques. Es la forma preferida.
- *Salto de línea real dentro de un párrafo:* dos espacios al final de la línea (permitido porque `MD009` y `trimTrailingWhitespace` están desactivados en markdown). Úsalo solo cuando lo necesites de verdad.
- *Sin tabuladores:* solo espacios (indentación de 2).
- *Fin de archivo:* una única línea en blanco final (tu `insertFinalNewline` + `trimFinalNewlines` lo garantizan). No dejes varias líneas vacías al cierre.
- *Separadores `---`:* úsalos para partir grandes bloques (cabecera, índice, cuerpo), rodeados de línea en blanco.

---

## 8 · Tablas

- *Markdown All in One realinea las tablas al guardar:* escribe la estructura correcta y deja que el formateador cuadre el ancho; no alinees a mano.
- *Toda tabla necesita fila de cabecera y fila separadora* `| --- | --- |`.

```markdown
| Campo     | Descripción         |
| --------- | ------------------- |
| style_box | El molde sónico.    |
| letra     | El alma de la obra. |
```

- *No indentes las tablas* dentro de listas si puedes evitarlo (descuadra el normalizador).

---

## 9 · Enlaces

- *Enlaces relativos entre archivos del proyecto:* `[letra.md](../composicion/letra.md)`.
- *URLs sueltas permitidas* (`MD034` off), pero para texto limpio prefiere `[texto](url)`.
- *HTML permitido* (`MD033` off) solo si Markdown no llega; por defecto, evítalo.
- *Al mover un archivo, VS Code corrige los enlaces internos* (`updateLinksOnFileMove`), pero revisa que no quede ninguno roto.

---

## 10 · Estilo de la casa

- *Convenciones propias del proyecto, además de las reglas del linter:*
    - *H1* = nombre del archivo o slug (`# letra`, `# escuela_de_calor`).
    - *Línea de intención** bajo el título o el encabezado, en cursiva: `- *Para qué sirve esto.*`
    - *Recordatorio de consulta** en las hojas de conocimiento: `*Recordatorio: consulta por búsqueda (grep) o salto por sección.*`
    - *Secciones* `## N · Título`, *subsecciones* `### N.N · Título`, con `·` de separación.
    - *Etiquetas de campo* en negrita con dos puntos: `**Ejemplo:**`, `**Regla:**`, `**Sintaxis:**`.
    - *Tags de Suno* siempre entre `backticks`.
    - *Separadores `---`* entre cabecera, índice y cuerpo.
    - [Corchete]: "Esto es una etiqueta". Le dice a la máquina que lo que hay dentro es una categoría o un ajuste, no texto normal.
    - **Negrita**: "¡Orden absoluta!". Indica que esa instrucción es crítica, de prioridad máxima e innegociable.
    - *Cursiva*: "Fíjate un poco aquí". Un subrayado ligero para darle un poco más de peso a esa palabra.
    - "Comillas": "Literalmente esto". Obliga a usar exactamente lo escrito, letra por letra, sin interpretaciones.
    - `Backtick`: "No lo toques, es código". Avisa de que la palabra es técnica y no debe analizarse como lenguaje natural.
    - <Nombre>: "Hueco a rellenar" o "Caja de texto". Marca dónde irá un dato futuro o envuelve un bloque de reglas.
    - {Nombre}: "Paquete de datos". Agrupa información emparejada (como una ficha) para no mezclarla.
    - ^Nombre^: "Posición exacta". Fija el inicio de un texto al milímetro o marca un superíndice matemático.

---

## 11 · Checklist antes de guardar

1. Un solo `# H1`; jerarquía sin saltos (`#` a `##` a `###`).
2. Línea en blanco antes y después de cada encabezado, lista y bloque de código.
3. Viñetas con `-`; sublistas a 2 espacios; numeradas correlativas.
4. Negrita `**...**`, cursiva `*...*`; sin espacios dentro de los marcadores.
5. Bloques de código cercados y con lenguaje.
6. Índice alineado con los encabezados reales.
7. Tablas con cabecera y separadora (deja que el formateador las cuadre).
8. LF, indentación de 2 espacios, una única línea en blanco al final.
