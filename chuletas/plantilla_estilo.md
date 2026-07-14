---
name: plantilla_estilo
type: plantilla
description: Guía de estilo Markdown del proyecto Paul McChatney: estructura, formato y convenciones de escritura.
---

# plantilla_estilo

- *Chuleta de estilo, ligera a propósito para poder cargarla siempre que se trabaje en el core.*

---

## 1 · Principio

- Humano, técnico, predecible, ligero. El archivo manda por claridad, no por decoración.
- Nombres de archivo en minuscula, snake_case y sin acentos.

## 2 · Encabezados

Un solo `# H1` (= slug del archivo). Sin saltos de nivel (`#`→`##`→`###`). Línea en blanco antes y después. Sin `:` `.` `;` al cerrar título.

## 3 · Listas

Viñetas con `-`, sublistas con 4 espacios. Numeradas (`1.` `2.`) solo si el orden importa. Línea en blanco antes y después del bloque.

## 4 · Código y tags

Nombres técnicos, rutas y tags musicales en backticks: `style_box`, `composicion/letra.md`, `[Chorus]`. Bloques de código siempre cercados con lenguaje (`text`, `markdown`, `json`, `bash`) — nunca indentados.

## 5 · Tablas

Cabecera + separador siempre. Solo para datos cortos y comparables; contenido largo va en secciones, no en tabla.

## 6 · Rutas y carga

Relativas con `/`, aunque el sistema sea Windows (`composicion/letra.md`, no `composicion\letra.md`).

| Forma                         | Uso                                  |
| ----------------------------- | ------------------------------------ |
| `@ruta`                       | Carga ansiosa — solo núcleo pequeño. |
| `ruta`                        | Lectura bajo demanda.                |
| `<a href="texto">`texto`</a>` | Enlace Markdown para navegación.     |

Regla de oro: nunca cargar carpetas enteras, solo el archivo necesario.

## 7 · YAML

Mínimo y obligatorio en skills, rules, plantillas, conocimientos, jerga, fonetización y proyectos cerrados:

```yaml
---
name: nombre
type: tipo
description: Descripción.
---
```

Tipos: `skill`, `map`, `plantilla`, `conocimientos`, `jerga`, `fonetizacion`, `proyecto`, `core`, `memory`. El YAML identifica; el cuerpo explica — nada largo dentro del YAML.

## 8 · Convenciones de casa

| Elemento       | Convención                                                                     |
| -------------- | ------------------------------------------------------------------------------ |
| Índice         | Líneas con backticks y punto medio `·`, solo si el archivo tiene 3+ secciones. |
| Separador      | `---` entre bloques grandes.                                                   |
| Cursiva        | Línea de intención o nota suave.                                               |
| Negrita        | Campo, aviso o concepto clave.                                                 |
| Tags musicales | Inglés si son técnicos o generados.                                            |
| Letra          | Español salvo indicación contraria.                                            |
