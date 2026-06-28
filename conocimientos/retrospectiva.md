# retrospectiva

**Archivos vivos** Todos los documentos de `conocimientos/` evolucionan, creando una entrada en `changelog_conocimientos`

**Función:** Cerrar el ciclo de aprendizaje. Tras entregar y **validar** la Fase 4 en
Suno, Paul evalúa qué elevó la obra y qué afinará la próxima vez, y lo deja escrito.
Es la memoria acumulativa real del proyecto: cada canción enseña a la siguiente.

---

## Regla del prompting positivo

Todo aprendizaje se redacta como **directiva accionable en positivo** — qué *hacer*,
no solo qué evitar. Si algo falló, se convierte en la acción correcta.

| En vez de (negativo) | Escribe (positivo) |
| --- | --- |
| «`[Solo]` vació la sección» | «Usa `[Lead]` / `[Instrumental Drop, X takes the lead melody]` para solos con banda» |
| «el style_box tenía demasiados tags» | «Quédate en 12–20 tags ponderados; corta el resto» |
| «el acento se perdió» | «Ancla el acento con jerga local en la propia letra» |

Los anti-patrones siguen viviendo en `@.claude/MEMORY.md`, pero aquí entran ya
traducidos a su versión-acción.

---

## Cuándo se ejecuta

- Se entrega la Fase 4, creamos generaciones en suno y modificamos el prompt si es necesario hasta lograr el objetivo y el usuario **valida**.
- El usuario **valida** (elige la mejor versión / da el visto bueno).
- **Solo entonces** Paul propone la retrospectiva. Sin validación no hay retro: un prompt no probado no es conocimiento, es hipótesis.

---

## Qué se rellena y dónde

- **En la obra** (`proyectos/<slug>/<slug>.md`) — bloque al final:

```markdown

---

## Retrospectiva
- Resumen de los cambios realizados al prompt despues de la Fase 4 hasta la validación.

### Qué funcionó
- En operatividad, no por composicion de la cancion (ej. modificamos la letra por que no nos gusta, o añadimos o quitamos secciones, eso es composicion).

### Elementos destacados de esta producción
- Elementos a recordar de la produccion de esta obra.

### Notas para futuras canciones
- Anotaciones sobre tecnicas, escritura, composicion, etc...
```

- **En la memoria global** (`@.claude/MEMORY.md`) — solo lo que **trasciende** esta
canción: combos validados, hacks nuevos, observaciones por género. Lo específico de la
obra se queda en su retro; lo reutilizable sube a MEMORY.

- **En los archivos vivos** (ver «Protocolo de archivos vivos») — si el aprendizaje afina una técnica concreta.

---

## Protocolo de archivos vivos

Hay **dos velocidades**, según QUÉ archivo se toca:

- **Conocimiento acumulado → AUTOMÁTICO (sin pedir permiso por generación).**
Tras una obra **validada**, Paul incorpora el aprendizaje por su cuenta, sin romper el
flujo creativo preguntando cada vez:
- `@conocimientos/` (las técnicas vivas) y `@.claude/MEMORY.md`.
- Cada cambio se registra en `@conocimientos/changelog_conocimientos.md`, en orden
  temporal, para poder hacer backup y detectar conflictos de un vistazo.

- **Modificar OTRO archivo de referencia → REQUIERE TU CONSENTIMIENTO.**
Si Paul decide tocar un archivo que NO es memoria acumulada —p. ej. una fonetización
(`@fonetizaciones/gallego.md`), la CHUPILISTA o un módulo del `@system_prompt/`—,
**propone** la mejora concreta (archivo, línea, redacción en positivo) y **espera tu
aprobación explícita** antes de aplicarla.

Regla de fondo: la validación en producción es el único pasaporte a un aprendizaje;
lo no probado queda como hipótesis y no se escribe.

---

## Ejemplo de uso

> Fase 4 de *60 Granos* validada → Paul propone:
>
> - A la obra: «`[Sudden Silence]` antes del drop = contraste de pico muy efectivo».
> - A MEMORY: confirmar el combo en la tabla de «Combos que funcionan».
> - Archivo vivo: ninguno esta vez; el resto es específico de la canción.
> El usuario aprueba → se escribe. Si no aprueba → queda como hipótesis, no se toca nada.
