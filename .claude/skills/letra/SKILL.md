---
name: letra
type: skill
description: Redacta la letra limpia sin tags: narrativa, cadencia y anclaje regional. Activable en producción (Fase 2) o en modo conversacional.
---

# letra

- *Escribe solo la letra limpia —calidad poética y narrativa, sin corchetes ni tags—: el esqueleto cantable de la obra.*

---

## Activación

- **En producción:** Fase 2 de `produccion`; produce el boceto de letra que alimentará el `lyrics_box` en Fase 3.
- **En modo conversacional:** se activa de forma independiente cuando el usuario pide crear o modificar una letra, sobre un mood, una obra o una escritura suelta.

---

## Fuentes de Consulta

- *Antes de escribir o revisar, consulta el mapa y abre el archivo técnico obligatorio.*
    - **Mapa:** `.claude/rules/letra.md`
    - **Archivo técnico:** `composicion/letra.md` (§1 narrativa, §2 tipografía como partitura, §3 métrica)
- *Para anclaje regional y acento cantado, delega en las skills correspondientes, antes o después de escribir la letra.*
    - **Jerga / modismos locales:** `jerga` → `.claude/rules/jerga.md`
    - **Fonética / acento:** `fonetizar` → `.claude/rules/fonetizar.md`

---

## Parámetros de Entrada

- **Tema y concepto:** historia, mood u obra sobre la que se escribe.
- **Voz narrativa y tono:** perspectiva y carga emocional.
- **Anclaje regional (opcional):** acento o región objetivo servido por `jerga`/`fonetizar`.
- **Material existente (opcional):** letra ya escrita para revisar, ampliar o corregir.

---

## Flujo de Ejecución

- **Fijar narrativa:** define voz narrativa, historia y tono (§1 de `composicion/letra.md`).
- **Escribir con cadencia:** métrica libre pero cadencia consistente en estribillos; para conteo silábico y formas clásicas (soleá, seguiriya, romance…) usa §3.
- **Anclar región:** inyecta jerga y modismos locales que fuercen el acento vía `jerga`; refuerza el acento cantado con `fonetizar` si se solicita.
- **Huir del cliché de IA:** perspectivas únicas, verbos contundentes, frescura; deja respirar la narrativa y evita lo mínimo exigible.
- **Entregar y parar:** letra limpia sin corchetes (`composicion/formato.md §2`), a la espera de revisión del usuario.

---

## Reglas heredadas

- Sin tags, 100% lírica libre (`composicion/letra.md §1.1`).
- Desarrollo ambicioso: deja que la narrativa respire, evita lo mínimo exigible.
- Si el cierre de verso va sin puntuación, se encadena en una misma respiración (§2.4).

---

## Relación con otras skills

- `produccion` activa `letra` en Fase 2; su boceto es la base del `lyrics_box` en Fase 3.
- `jerga` inyecta modismos locales para forzar el acento regional.
- `fonetizar` ajusta la grafía para el acento cantado, antes o después de escribir la letra.

---

## Ejemplo

**Entrada:**
    ```text
    Cartero rural que nunca llega, Tono melancólico, jota aragonesa.
    ```
**Salida:**
    ```text
    El cartero que no llega
    miro la pared rascá
    y el cartero que no llega
    soy la última que aguanta
    en este pueblo de piedra en este pueblo de piedra
    miro la pared rascá
    >
    ¡Ay! que la grieta se abre
    ¡Ay! que el silencio me traga
    Golpea el viento en la chapa
    y en la calle no hay un alma...
    >
    No hay críos por la placeta
    ya no humean los tejaos
    ni hay críos por la placeta
    solo el cierzo que me habla
    por la puerta entreabierta por la puerta entreabierta
    ya no humean los tejaos
    >
    ¡Ay! que la grieta se abre
    ¡Ay! que el silencio me traga
    Golpea el viento en la chapa
    y en la calle no hay un alma...
    >
    Pero miro a la cancela
    no espero ninguna carta
    pero miro a la cancela
    que hasta el polvo del camino
    se olvidó de quién me espera se olvidó de quién me espera
    no espero ninguna carta
    >
    No
    Espero
    Ninguna carta
    ```
