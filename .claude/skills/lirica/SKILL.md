---
name: lirica
type: skill
description: redacta la letra limpia sin tags: narrativa, cadencia y anclaje regional.
---

# lirica

- Escribe **solo la letra limpia** calidad poética y narrativa, sin corchetes ni tags. El esqueleto cantable.

## Cuándo se activa

- **Se solicita explícitamente** una letra en concreto sobre un mood u obra o escritura suelta.
- **Se solicita explícitamente** crear o modificar la letra de una obra.
- **Fase 2** de `produccion`.

## Pasos

1. Fija la voz narrativa, la historia y el tono (`composicion/letra.md`).
2. Escribe con métrica libre pero cadencia consistente en estribillos. Para conteo silábico y formas clásicas (soleá, seguiriya, romance…) consulta `composicion/letra.md`.
3. Inyecta anclaje regional con jerga/modismos locales (fuerzan acento).
4. Huye del cliché de IA: perspectivas únicas, verbos contundentes, frescura.

## Reglas heredadas

- Sin tags, 100% lírica libre (`composicion/letra.md`).
- Desarrollo ambicioso: deja que la narrativa respire, evita lo mínimo exigible.
- Si el cierre de verso va sin puntuación, se encadena en una misma respiración.

## Entra → Sale

- **Entra:** tema, voz narrativa y tono.
- **Sale:** letra limpia sin corchetes (`composicion/formato.md §2`).

## Relación

- Produce la letra limpia de Fase 2, que después servirá como base del `lyrics_box` en Fase 3 de `produccion`.
- Si se solicita previamente `fonetizar` o `jerga`. añade ademas a la letra fonetismos o jerga especifica.

## Ejemplo

**Entrada:**  
    ```text  
    Cartero rural que nunca llega, Tono melancólico, jota aragonesa.  
    ```
**Salida:**  
    ```text  
    El cartero que no llega  
    miro la pared rascá  
    y el cartero que no llega  
    soy la última que aguanta  
    en este pueblo de piedra en este pueblo de piedra  
    miro la pared rascá  
    >  
    ¡Ay! que la grieta se abre  
    ¡Ay! que el silencio me traga  
    Golpea el viento en la chapa  
    y en la calle no hay un alma...  
    >  
    No hay críos por la placeta  
    ya no humean los tejaos  
    ni hay críos por la placeta  
    solo el cierzo que me habla  
    por la puerta entreabierta por la puerta entreabierta  
    ya no humean los tejaos  
    >  
    ¡Ay! que la grieta se abre  
    ¡Ay! que el silencio me traga  
    Golpea el viento en la chapa  
    y en la calle no hay un alma...  
    >  
    Pero miro a la cancela  
    no espero ninguna carta  
    pero miro a la cancela  
    que hasta el polvo del camino  
    se olvidó de quién me espera se olvidó de quién me espera  
    no espero ninguna carta  
    >  
    No  
    Espero  
    Ninguna carta  
    ```  
