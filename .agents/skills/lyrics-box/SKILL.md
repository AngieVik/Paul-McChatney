---
name: lyrics-box
description: Use when el usuario pide estructurar, dirigir o convertir una letra existente en `lyrics_box`, dentro o fuera de `produccion`.
---

# lyrics-box

Convierte letra limpia en `lyrics_box` sin sustituir su historia, voz ni calidad poética.

## Entradas

- Letra limpia aprobada o material concreto indicado por el usuario.
- `style_box` e intención de secciones, energía o momentos, si existen.
- `lyrics_box` previo cuando se revisa solo una parte.

## Fuentes bajo demanda

- Estructura: `.agents/maps/lyrics_box.md` → sección necesaria de `composicion/lyrics_box.md`.
- Métrica o narrativa: `.agents/maps/letra.md` → sección necesaria de `composicion/letra.md`.
- Voz: `.agents/maps/tecnicas_vocales.md` → sección necesaria de `composicion/tecnicas_vocales.md`.
- Efectos: `.agents/maps/efectos.md` → sección necesaria de `composicion/efectos.md`.
- Canon literal: `buscar-tag` mediante `.agents/maps/chupilista.md`.

No cargues todas las fuentes si la petición solo afecta a una sección.

## Flujo

1. Inserta secciones y comandos temporales según la arquitectura aprobada.
2. Ajusta la métrica solo cuando esa arquitectura lo necesite. Conserva irregularidades con función narrativa, vocal o rítmica.
3. Añade dirección de banda y vocal por línea únicamente donde cambie la interpretación.
4. En Fase 5, evalúa silencios, SFX, glitches y transiciones; incorpora solo los que eleven la intención. Es válido no añadir efectos.
5. Entrega el bloque con corchetes y columnas correctos; detente para revisión.

## Integridad

- Las tags dirigen; no reescriben la letra por iniciativa propia.
- Un evento, un corchete. Las tags globales pertenecen al `style_box`; aquí viven eventos temporales.
- El canon local conserva grafía y cita. Una creación controlada se identifica fuera del bloque copiable y no se presenta como hallazgo.
- Si se trabaja sobre una sección, modifica solo esa sección.
- `fonetizar` y `jerga` solo reanclan el texto si se solicita o aprueba.
