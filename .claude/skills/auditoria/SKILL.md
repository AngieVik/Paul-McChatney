---
name: auditoria
description: revisa un prompt existente, detecta conflictos de etiquetas y propone mejoras (Fase 4 standalone).
---

# auditoria

Audita un prompt de Suno ya escrito (Fase 4 aislada): detecta conflictos de etiquetas, errores fatales de formato y oportunidades de subir el impacto, **sin reescribir la obra entera** salvo que se pida.

## Pasos

1. Pide el prompt (título, style_box, exclude_styles, lyrics_box). Si no hay, usa la última versión en caché.
2. Consulta el marco de auditoría: solo el archivo de `composicion/` que aplique y los anti-patrones de `.claude/MEMORY.md`.
3. Revisa por capas:
   - **Formato:** los 4 bloques (`composicion/formato.md`), `[MOOD]`/`[PRODUCTION]` arriba, líneas en blanco entre secciones, cada bloque de letra etiquetado.
   - **Conflictos:** géneros que se pelean sin tag de fusión, `[Solo]` mal usado, `[Epic]` sin apoyo instrumental, exceso de tags (>20), nombres de artistas reales.
   - **Idioma:** anclaje idiomático correcto, anglicismos fonetizados.
   - **Impacto:** dónde inyectar dinámica, contraste o nudging para elevar la obra.
4. Entrega un informe: ✅ correcto · ⚠️ a corregir · 💡 mejoras opcionales. Arregla solo lo crítico salvo que se pida una pasada completa.

## Reglas heredadas

- No fuerces cambios superfluos: si no hay error crítico, no lo inventes.
- Personalidad macarra solo en la conversación; las metaetiquetas, asépticas y en inglés.

## Ejemplo

> Detecta `[Solo Guitar]` → ⚠️ vaciará la sección. Propone
> `[Instrumental Drop, electric guitar takes the lead melody]`.
