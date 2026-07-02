---
name: fonetizar
description: reescribe la letra cantable para que Suno la cante con un acento o idioma concreto (nunca en el style_box).
---

# fonetizar

Reescribe una letra para que Suno la cante con un acento o idioma concreto. La fonetización va **en la letra cantable, nunca en el style_box**.

## Cuándo se activa

Se pide **explícitamente** un acento o idioma cantado concreto. Se aplica en la Fase 2 (sobre la letra), no antes.

## Pasos

1. Identifica el acento/idioma objetivo y abre **solo** su guía en `fonetizaciones/` (andaluz, americano, gallego, italiano, ruso, caló, ebrio, edad_avanzada…) con la herramienta de lectura — un archivo, no la carpeta. Si no existe, créala desde `chuletas/plantilla_fonetizaciones.md` (con aprobación).
2. Aplica las transformaciones de esa guía a la letra (aspiraciones, elisiones, nasales, dobles consonantes, etc.), respetando la métrica.
3. Para anglicismos dentro de un texto en español, usa el **Hack de Ortografía Fonética** (`system_prompt/system_prompt.md`): escríbelos como suenan (ej. _Beibi_).
4. Devuelve la letra fonetizada; ofrece versión limpia + fonetizada en paralelo si ayuda.

## Principio clave

Un mismo texto con fonetización distinta produce canciones radicalmente diferentes en timbre y emoción. Refuerza el efecto anclando también con jerga local en la letra. Salvo los dialectos de España (andaluz, gallego, euskera…), las guías simulan un acento extranjero cantando en español; si la obra debe cantarse en ese idioma, no fonetices y ancla el idioma en el `style_box`.

## Entra → Sale

- **Entra:** una letra + un acento/idioma objetivo.
- **Sale:** la letra fonetizada (opcional: limpia + fonetizada en paralelo).

## Relación

- La llaman `lirica` y `produccion` (Fase 2). Actúa sobre la letra; nunca toca el `style_box`.

## Ejemplo

> Andaluz: `los perros del puerto` → `loh perroh del puerto`.
