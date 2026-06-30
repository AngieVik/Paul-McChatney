# Paul McChatney

Sistema de composición musical asistida por IA para crear canciones, prompts, style_box, lyrics_box, exclude_box y documentación de proyectos musicales.

## Estructura

- `system_prompt/`: identidad y comportamiento principal.
- `.claude/`: memoria y reglas de carga.
- `chupilista/`: biblioteca de tags para Suno.
- `composicion/`: reglas de escritura, estructura y producción.
- `conocimientos/`: documentos técnicos y retrospectivas.
- `proyectos/`: canciones terminadas.
- `_hojas_sucias/`: ideas o trabajos en curso.

## Regla principal

No cargar carpetas enteras. Usar los índices y abrir solo el archivo necesario.