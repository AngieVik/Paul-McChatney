---
name: buscar-tag
description: Use when una tarea necesita buscar, verificar, citar o reutilizar tags literales de Suno en la `chupilista` local.
---

# buscar-tag

Localiza tags literales en `chupilista/`. Confirma existencia, grafía y ubicación dentro del canon local; no garantiza una eficacia concreta en Suno.

## Fuentes

- Entra por `.agents/maps/chupilista.md` y abre solo los módulos necesarios.
- Usa primero `rg` con el concepto, sus raíces y sinónimos razonables.

## Flujo

1. Resuelve el módulo probable mediante el mapa, salvo que la tarea ya indique una ruta.
2. Busca el concepto y variantes útiles.
3. Extrae únicamente coincidencias literales; conserva idioma, mayúsculas y grafía.
4. Comprueba `[`, contenido no vacío y `]`.
5. Entrega cada resultado como `[Tag Exacta]` · `archivo:línea` · caja recomendada · nota mínima.

Si no hay coincidencia, dilo tras buscar sinónimos. Una skill creativa puede proponer después una creación controlada, pero no la presentes como canon.

## Integridad

- Distingue siempre: tag documentada en el repositorio, comportamiento observado en una prueba y propuesta experimental.
- Una coincidencia demuestra canon local, no eficacia ni aprobación artística.
- Si una tag útil está mal formada, informa de la incidencia y no la valides.
- `buscar-tag` extrae y cita; `fusionar`, `style-box`, `lyrics-box` o la skill consumidora deciden cómo integrarla.
