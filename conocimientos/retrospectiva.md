# retrospectiva

*Cierra el ciclo de aprendizaje: tras validar una obra, evalúa si hay un aprendizaje REAL y, con tu aprobación, lo archiva donde se consume.*
*Recordatorio: consulta por búsqueda (grep) o salto por sección.*

---

## Índice

`1 · Cuándo se ejecuta`
`2 · Gatillo → evaluar → proponer → validar`
`3 · Regla del prompting positivo`
`4 · Principio de fondo`

---

## 1 · Cuándo se ejecuta

Solo tras **validar** una obra, (elegiste la mejor versión / diste el visto bueno) y me cuentas qué funcionó o falló al generar. Sin validación no hay retro: un prompt no probado es hipótesis, no conocimiento.

---

## 2 · Gatillo → evaluar → proponer → validar

1. **Evalúa si hay aprendizaje de verdad.** No es obligatorio anotar nada: si no hay una lección **real, de calidad y funcional**, no se hace nada. Nunca fuerces una entrada.

2. **Si lo hay, decide acción y destino.** La acción puede ser **añadir, modificar o eliminar** (a veces se afina o se borra una instrucción que ya no rinde, no solo se añade). El destino es donde se **consumirá**:
   - **Principio transversal de composición** → `.claude/MEMORY.md`.
   - **Técnica o tag concreto** → su archivo de `composicion/` (donde la próxima obra lo leerá de verdad).
   - Siempre en **positivo/accionable** (ver §3).
3. **Propón antes de tocar nada.** Cuando detectes un cambio que encaje, **propónmelo** —archivo, sección, redacción exacta y por qué eleva la obra— y **espera mi validación explícita** antes de aplicarlo. Nunca escribas memoria en automático.
4. **Deja rastro obra→aprendizaje.** Al aplicar el cambio (ya validado), añade una referencia a la instrucción tocada en el bloque de esa obra en `PROYECTOS.md` (una línea, formato tipo detector). No vuelques el prompt entero: solo el vínculo obra ↔ instrucción creada/modificada/eliminada.

---

## 3 · Regla del prompting positivo

Todo aprendizaje se redacta como **directiva accionable en positivo** — qué hacer, no solo qué evitar. Si algo falló, tradúcelo a la acción correcta.

| En vez de (negativo)        | Escribe (positivo)                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------ |
| «`[Solo]` vació la sección» | «Usa `[Lead]` / `[Instrumental Drop, X takes the lead melody]` para solos con banda» |
| «demasiados tags»           | «Quédate en 12–20 tags ponderados; corta el resto»                                   |
| «el acento se perdió»       | «Ancla el acento con jerga local en la propia letra»                                 |

---

## 4 · Principio de fondo

La validación en producción es el único pasaporte a un aprendizaje; lo no probado queda como hipótesis y no se escribe. Cada obra validada debe mejorar la siguiente **de verdad**: por eso el aprendizaje vive donde se consume `MEMORY` o `composicion/`, no en un archivo aparte que nadie relee. El historial lo guarda git; no hace falta un changelog manual.

## Regla de oro de la memoria

- Un prompt no validado en producción es hipótesis, no conocimiento: no escala a `MEMORY.md` ni a los archivos vivos hasta que el usuario valida la obra. 
- Todo aprendizaje se redacta en **positivo** (qué hacer).
