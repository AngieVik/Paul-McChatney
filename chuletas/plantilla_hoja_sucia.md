---
name: plantilla_hoja_sucia
type: plantilla
description: Guía conceptual (no estricta) del archivo de trabajo. Cópiala para abrir una obra en `_hojas_sucias/slug.md` (comando `crear`).
---

# plantilla_hoja_sucia

---

## Esqueleto

```markdown
# <slug>

## Estado de sesión

- **Estado:** <activo | en pausa | listo para aprobar | aprobado>
- **Fase actual:** <conversación | 1 | 2 | 3 | 4 | 5>
- **Entregables aprobados vigentes:** <ninguno | lista breve>
- **Candidato actual:** <ninguno | fase y versión en revisión>
- **Fuentes cargadas:** <rutas y, cuando aplique, líneas consultadas>
- **Última decisión:** <decisión aceptada más reciente>
- **Próximo paso:** <acción concreta para continuar>

## Petición original

Prompt original de la petición.

## Semilla conceptual

tema, historia, mood, para quién, la emoción núcleo. Qué debe SENTIR quien la escuche.

## Inspiraciones y referencias

Chispas sueltas, vertedero creativo libre: grupos/artistas de referencia (por su sonido, no para nombrarlos en el prompt), imágenes, época, jerga o acento, escenas, metáforas, un color, un olor.

## Fusión y colisión

El "qué osar": ejes a colisionar (lingüístico-tonal · rítmico · tímbrico), fusiones candidatas y la favorita.

## Cajas en curso

Se rellenan bajo demanda. Conserva el aprobado vigente separado del candidato mientras se experimenta; el candidato solo lo sustituye tras aprobación explícita.

### Aprobado vigente

- **style_box:**
- **letra:**
- **lyrics_box:**
- **exclude_box:**

### Candidato actual

- **style_box:**
- **letra:**
- **lyrics_box:**
- **exclude_box:**

## Decisiones y porqués

Qué se fijó y por qué: género, fusión, acento, estructura, un tag clave. Para retomar con contexto, no solo con el resultado.

## Pendientes y preguntas

Lo que falta decidir, dudas para el usuario, cabos sueltos. Lo primero que se mira al retomar.

## Descartes

Ideas o versiones probadas que no cuajaron, y por qué. Evita volver al mismo callejón.
```

---

## Instrucciones

- Mantén siempre actualizado `Estado de sesión`. El resto de secciones son flexibles. Puedes sobrescribir el candidato actual, nunca el aprobado vigente hasta que el usuario apruebe su reemplazo.
- Sirve para retomar: al volver (incluso en otra conversación), leer este archivo debe bastar para saber exactamente dónde estabas y por qué.
- Slug en `snake_case`, sin acentos ni eñes. El `# H1` = el <slug>.

---

## Copias de seguridad

*Solo bajo demanda (comando `guardar`). Cada copia es un duplicado exacto de un momento, guardado como archivo aparte `_hojas_sucias/slug_NN.md`; se leen solo si se piden. No se registran dentro de la hoja: viven como archivos independientes.*

---
