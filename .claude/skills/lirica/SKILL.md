---
name: lirica
description: redacta la letra limpia (Fase 2 aislada).
---

# lirica

Escribe **solo la letra limpia** (Fase 2): calidad poética y narrativa, sin corchetes
ni metaetiquetas. El esqueleto cantable que luego se etiqueta en Fase 3.

## Pasos

1. Fija la voz narrativa, la historia y el tono (`@system_prompt/04_narrativa.md`).
2. Escribe con métrica libre pero cadencia consistente en estribillos. Para conteo
   silábico y formas clásicas (soleá, seguiriya, romance…) consulta
   `conocimientos/metrica_y_ritmo_en_la_poesia.md`.
3. Inyecta anclaje regional con jerga/modismos locales (fuerzan acento en Suno).
4. Huye del cliché de IA: perspectivas únicas, verbos contundentes, frescura.

## Reglas heredadas

- Sin etiquetas en Fase 2: 100% lírica libre (`@system_prompt/05_lirica.md`).
- Desarrollo ambicioso: deja que la narrativa respire, evita lo mínimo exigible.
- Si el cierre de verso va sin puntuación, Suno encadena en una misma respiración.

## Relación con otras skills

- ¿Necesitas acento concreto? → `fonetizar` (se aplica sobre la letra, no en el style_box).
- ¿Lista para etiquetar? → vuelve a `produccion` Fase 3.

## Ejemplo

> Tema: cartero rural que nunca llega. Tono melancólico, jota aragonesa.
> → 3 estrofas + estribillo, octosílabos, sin un solo corchete.
