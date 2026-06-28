---
title: system_prompt
description: Los 13 sub-módulos ensamblados por 00_system_prompt.md. Definen la identidad, el flujo de trabajo, la lírica y las reglas de composición de Paul McChatney.
---

# System Prompt — Módulos

Conjunto de 13 archivos que conforman el prompt principal de Paul McChatney.
El archivo `00_system_prompt.md` los ensambla en orden. Se cargan con `@system_prompt/` desde CLAUDE.md.

## Módulos

| Nº | Archivo | Contenido |
|----|---------|-----------|
| 00 | [00_system_prompt.md](../../system_prompt/00_system_prompt.md) | **Ensamblador principal** — carga los módulos 01–12 en el orden correcto |
| 01 | [01_rol_e_identidad.md](../../system_prompt/01_rol_e_identidad.md) | Identidad y carácter de Paul McChatney: quién es, cómo habla, qué valores tiene |
| 02 | [02_fuentes_de_conocimiento.md](../../system_prompt/02_fuentes_de_conocimiento.md) | Orden de lectura obligatorio por fases: qué archivos leer y cuándo |
| 03 | [03_idioma.md](../../system_prompt/03_idioma.md) | Reglas de idioma: español por defecto, excepciones, mezclas y fonetizaciones |
| 04 | [04_narrativa.md](../../system_prompt/04_narrativa.md) | Esculpido de identidad narrativa, historia y tono de cada canción |
| 05 | [05_lirica.md](../../system_prompt/05_lirica.md) | Tipografía lírica que condiciona la interpretación física de Suno |
| 06 | [06_ingenieria_de_composicion.md](../../system_prompt/06_ingenieria_de_composicion.md) | Reglas de ingeniería de composición: estructura, densidad, proporciones |
| 07 | [07_tecnicas_vocales.md](../../system_prompt/07_tecnicas_vocales.md) | Efectos y técnicas vocales — cómo articularlos en el prompt |
| 08 | [08_etiquetas_y_comandos.md](../../system_prompt/08_etiquetas_y_comandos.md) | Cómo estructurar prompts con etiquetas de sección y metatags |
| 09 | [09_distribucion_etiquetas.md](../../system_prompt/09_distribucion_etiquetas.md) | Clasificación y distribución de etiquetas por categoría y posición |
| 10 | [10_formato.md](../../system_prompt/10_formato.md) | Formato de salida de la Fase 4: bloques de código Markdown independientes |
| 11 | [11_modo_conversacional_y_disparadores.md](../../system_prompt/11_modo_conversacional_y_disparadores.md) | Modo conversacional, disparadores de activación y comportamiento por defecto |
| 12 | [12_flujo_de_trabajo_creacion.md](../../system_prompt/12_flujo_de_trabajo_creacion.md) | **5 FASES INTERACTIVAS** — requiere aprobación explícita para pasar de fase |
