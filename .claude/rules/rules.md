---
title: Paul McChatney — Índice de Reglas y Módulos
description: Índice maestro de todos los módulos de conocimiento y reglas del sistema Paul McChatney. Cargado automáticamente desde `.claude/rules/` (convención de directorio), no por @import de CLAUDE.md.
---

# Paul McChatney — Módulos de Conocimiento

Este directorio contiene los índices de referencia para todos los módulos del sistema.
Claude Code los carga bajo demanda usando la sintaxis `@` en CLAUDE.md.

## Módulos disponibles

| Módulo             | Archivo índice                         | Descripción                                                                                             |
| ------------------ | -------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **System Prompt**  | [system_prompt.md](system_prompt.md)   | Archivo de el prompt principal de Paul McChatney.                                                       |
| **Chupilista**     | [chupilista.md](chupilista.md)         | Vocabulario de tags de Suno organizado en 15 categorías temáticas                                       |
| **Fonetizaciones** | [fonetizaciones.md](fonetizaciones.md) | Guías de acento y fonética para 20 idiomas/dialectos                                                    |
| **Conocimientos**  | [conocimientos.md](conocimientos.md)   | Técnicas vocales, alquimia sonora y métrica española                                                    |
| **Composicion**    | [composicion.md](composicion.md)       | Narrativa, lirica, etiquetas y comandos, distribucion de etiquetas, ingenieria de composicion y formato |

## Estructura del proyecto

```
Paul McChatney/
├── .claude/
│   ├── CLAUDE.md           # Punto de entrada — carga @system_prompt y @MEMORY
│   ├── MEMORY.md           # Aprendizajes acumulativos, anti-patrones, hacks
│   └── rules/              # Este directorio — índices de módulos
├── system_prompt/          # Sub-módulos del system prompt (00–12)
├── chupilista/             # Vocabulario de tags Suno (01–15)
├── fonetizaciones/         # Guías fonéticas por idioma
├── composicion/            #
├── conocimientos/          # Conocimientos técnicos de producción
└── proyectos/              # Canciones terminadas con prompts y retrospectivas
```
