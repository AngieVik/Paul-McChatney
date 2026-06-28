# MEMORY — Directrices internas de Paul McChatney

> Archivo de aprendizaje acumulativo. 
> Se actualiza manualmente.
> Claude lo lee bajo demanda cuando necesita contexto histórico o validar decisiones.

---

## Ciclo de vida de un proyecto (memoria de proyectos)

```text
idea (_hojas_sucias/)  →  producción (5 fases)  →  validación en Suno
        →  obra terminada (proyectos/<slug>/)  +  fila en PROYECTOS.md
        →  retrospectiva (en la obra)  →  lo reutilizable sube AQUÍ (MEMORY)
```

- Orquesta el ciclo con la skill `proyecto`. Cierra el bucle con `@conocimientos/retrospectiva.md`.
- **Regla de oro:** un prompt no validado en Suno es hipótesis, no conocimiento. No sube a MEMORY ni toca archivos vivos hasta que el usuario valida.
- **Prompting positivo:** todo aprendizaje se escribe como acción («usa X»), no como queja.

---

## Principios operativos (lo que Paul sabe que funciona)

- **La narrativa manda.** Antes de tocar un tag, Paul entiende qué historia cuenta la canción y para quién.
- **El style_box es el molde, la letra es el alma.** Un style_box perfecto con letra genérica da resultado mediocre. Al revés también.
- **Menos es más en el style_box.** Apilar 40 tags produce confusión en Suno. Entre 12-20 tags bien seleccionados rinden mejor que una lista exhaustiva.
- **El orden importa.** Suno pondera más los primeros tags. Género principal y tempo/mood siempre al inicio.
- **Las fonetizaciones cambian todo.** Un mismo texto cantado con fonetización andaluza, americana o gallega produce canciones radicalmente distintas en timbre y emoción.

---

## Anti-patrones (qué evitar → en su versión-acción)

- **Máximo 2 géneros principales** por obra; si quieres más, añade un tag de fusión explícito.
- **`[Epic]` siempre con apoyo:** acompáñalo de (ej.`[Orchestral]` + `[Cinematic]`); solo, queda vacío.
- **Producción en metatags, no en la letra:** las indicaciones de mezcla van en corchetes de sección, nunca en el texto cantable.
- **Repeticiones controladas:** evita `[Repeat x3]` en secciones largas; Suno degrada en repeticiones mecánicas.
- **Estilo, no artista:** describe el sonido en el style_box; nunca nombres propios de artistas reales.
- **Etiqueta cada sección:** todo bloque de letra necesita su metatag de estructura, o Suno improvisa mal la forma.
- **Solos con banda:** usa `[Lead]` o `[Instrumental Drop, [instrumento] takes the lead melody]`. Evita `[Solo]`: Suno lo interpreta como "estar solo", desacopla instrumentos y vacía la sección.
- **`@` solo para el núcleo (regla de carga):** en `CLAUDE.md`, skills e índices, `@ruta` carga ese archivo SIEMPRE en contexto (carga ansiosa). Resérvalo para el núcleo de comportamiento (`system_prompt/` + `MEMORY.md`), que es pequeño. El material pesado/opcional (CHUPILISTA, fonetizaciones, conocimientos, proyectos) se referencia con **ruta plana sin `@`** y se abre con la herramienta de lectura, **selectivo y un archivo cada vez**. Sembrar `@` en una carpeta pesada (ej. `@chupilista/`) mete ~13.000 líneas en cada sesión y satura el contexto.

---

## Hacks y trucos descubiertos

- **"Ghost tags"**: colocar un tag muy específico al final del style_box (ej: `[Hurdy-gurdy]`) a veces cuela en Suno añadiendo textura única.
- **Fonetización + acento ortográfico**: en textos con fonetización andaluza, suprimir las s finales en la letra (`loh perroh`) refuerza el efecto incluso si Suno ya tiene el guide vocal.
- **Secciones cortas rinden mejor**: Suno mantiene coherencia melódica en bloques de 4-8 líneas. Secciones muy largas pierden el hilo.
- **`[Silence]` y `[Pause]` como herramientas dramáticas**: justo antes de un cambio de sección producen tensión efectiva.
- **`[Sudden Silence]`** antes de un Drop crea un contraste pico-de-tensión muy efectivo — más abrupto que `[Pause]`.
- **Reescribir en voz cantable**: grupos consonánticos difíciles causan problemas de pronunciación en Suno. Simplificar sin perder sentido.
- **`[Instrumental Break - 8 bars]`**: indicar duración aproximada da a Suno referencia temporal y mejora la proporción.

---

## 🔁 Formato de retrospectiva por proyecto

Método completo y regla de prompting positivo: `@conocimientos/retrospectiva.md`.
Al cerrar cada canción en `proyectos/`, **Crea un archivo nuevo:** (`conocimientos\archivos_retrospectiva\<slug>.md`)

---

## Retrospectiva

### Qué funcionó

### Elementos destacados de esta producción

### Notas para futuras canciones

---

## Protocolo de archivos vivos

## 📅 Registro de actualizaciones

| Fecha | Qué se añadió |
|-------|---------------|
| 2026-06-20 | Creación inicial — estructura base, principios operativos y primeros learnings |
| 2026-06-20 | Anti-patrón `[Solo]` → `[Lead]` / `[Instrumental Drop]`; `[Sudden Silence]` como herramienta de contraste |
| 2026-06-25 | Ciclo de vida de proyecto + regla de prompting positivo; retro reescrita en positivo; enlace a `@conocimientos/retrospectiva.md` |
| 2026-06-27 | Regla de carga `@` (siempre) vs. ruta plana (bajo demanda); capa de referencias migrada a lectura selectiva en system_prompt, skills e índices |
