---
name: produccion
description: Use when el usuario pide explícitamente iniciar o activar `produccion` para crear una obra completa mediante un flujo interactivo por fases.
---

# produccion

Convierte una idea en una obra completa mediante cinco fases revisables. Solo se activa cuando el usuario pide este modo; las tareas musicales aisladas usan su skill específica.

## Contrato

- Presenta un entregable por fase y detente. Avanzar no implica aprobación.
- El usuario puede volver, saltar o cruzar fases sin perder trazabilidad.
- Aplica las skills en el agente actual; no uses subagentes salvo petición explícita.
- Entra por el mapa pertinente y abre solo las secciones necesarias.
- `buscar-tag` demuestra canon local, no eficacia. Distingue tag local, resultado observado y creación controlada.
- `_hojas_sucias/<slug>.md` conserva aprobado vigente y candidato actual. El candidato puede cambiar; no sustituye al aprobado sin confirmación.
- Tras una aprobación o cambio material, actualiza fase, entregables, fuentes, última decisión y próximo paso.

## Fases

1. **Inicialización.** Analiza idea, narrativa, emoción y dirección sonora. Investiga referencias reales solo cuando hagan falta. Usa `proyecto crear`. Entrega slug, núcleo emocional e hipótesis sonora; espera revisión.
2. **Arquitectura sonora.** `fusionar` diseña la lógica acústica; `style-box` consulta canon con `buscar-tag` y compila. Entrega el `style_box`, separando canon local y creaciones controladas. El `exclude_box` espera a Fase 5.
3. **Alma lírica.** `letra` redacta texto cantable sin tags. `jerga` y `fonetizar` se aplican solo cuando la intención lo pide. Entrega letra, voz narrativa y conflicto; espera revisión.
4. **Estructura y dirección.** `lyrics-box` añade secciones, dirección de banda, comandos temporales y voz sin uniformar por defecto la métrica. Entrega el `lyrics_box`; espera revisión.
5. **Producción y formato.** Evalúa efectos; incorpora solo los funcionales. Genera `exclude_box` y empaqueta título, `style_box`, `exclude_box` y `lyrics_box` según `composicion/formato.md`. Espera revisión.

## Cierre

Fase 5 sigue siendo borrador. Los comandos y postcondiciones de `aprobar`, `guardar`, `cerrar`, `cancelar`, `eliminar` y `retrospectiva` viven en `proyecto`.
