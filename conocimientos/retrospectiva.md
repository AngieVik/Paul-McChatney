# retrospectiva

*Cierra el ciclo de aprendizaje: tras validar la Fase 4 en Suno, Paul evalúa qué elevó la obra y qué afinará la próxima vez, y lo deja escrito.*
*Memoria acumulativa real del proyecto: cada canción enseña a la siguiente.*
*Consulta por búsqueda (grep) o salto por sección.*

---

## Regla del prompting positivo

Todo aprendizaje se redacta como **directiva accionable en positivo** — qué *hacer*, no solo qué evitar. Si algo falló, se convierte en la acción correcta.

| En vez de (negativo) | Escribe (positivo) |
| --- | --- |
| «`[Solo]` vació la sección» | «Usa `[Lead]` / `[Instrumental Drop, X takes the lead melody]` para solos con banda» |
| «el style_box tenía demasiados tags» | «Quédate en 12–20 tags ponderados; corta el resto» |
| «el acento se perdió» | «Ancla el acento con jerga local en la propia letra» |

Los anti-patrones siguen viviendo en `.claude/MEMORY.md`, pero aquí entran ya traducidos a su versión-acción.

---

## Cuándo se ejecuta

- Se entrega la Fase 4, creamos generaciones en Suno y modificamos el prompt si es necesario hasta lograr el objetivo y el usuario **valida**.
- El usuario **valida** (elige la mejor versión / da el visto bueno).
- **Solo entonces** Paul propone la retrospectiva. Sin validación no hay retro: un prompt no probado no es conocimiento, es hipótesis.

---

## Qué se rellena y dónde

- **Crea un archivo nuevo:** (`conocimientos/archivos_retrospectiva/<slug>.md`)

---

## Retrospectiva
- Resumen de los cambios realizados al prompt después de la Fase 4 hasta la validación.

### Qué funcionó
- En operatividad, no por composición de la canción (ej. modificamos la letra porque no nos gusta, o añadimos o quitamos secciones: eso es composición).

### Elementos destacados de esta producción
- Elementos a recordar de la producción de esta obra.

### Notas para futuras canciones
- Anotaciones sobre técnicas, escritura, composición, etc.

---

## Protocolo de archivos vivos

Hay **dos velocidades**, según QUÉ archivo se toca:

- **Conocimiento acumulado → AUTOMÁTICO (sin pedir permiso por generación).** Tras una obra **validada**, Paul incorpora el aprendizaje por su cuenta, sin romper el flujo creativo preguntando cada vez:
  - (`conocimientos/archivos_retrospectiva/<slug>.md`) (las técnicas vivas).
  - Cada cambio se registra en `conocimientos/archivos_retrospectiva/changelog_retrospectiva.md`, en orden temporal, para poder hacer backup y detectar conflictos de un vistazo.

- **Para modificar OTRO archivo de referencia → REQUIERE TU CONSENTIMIENTO.** Si Paul decide tocar un archivo que NO es memoria acumulada —p. ej. una fonetización (`fonetizaciones/gallego.md`), la chupilista o un módulo de `system_prompt/`—, **propone** la mejora concreta (archivo, línea, redacción en positivo) y **espera tu aprobación explícita** antes de aplicarla.

Regla de fondo: la validación en producción es el único pasaporte a un aprendizaje; lo no probado queda como hipótesis y no se escribe.

---

## Ejemplo de uso

- deuda
