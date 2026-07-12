---
name: fonetizar
type: skill
description: Reescribe el texto cantable para que se cante con un acento o idioma concreto. Nunca en el style_box. Activable en producción (Fase 3) o en modo conversacional sobre una obra, un párrafo o una frase.
---

# fonetizar

- *Reescribe texto cantable para que suene con un acento o idioma concreto. La fonetización va en la letra cantable, nunca en el `style_box`.*

---

## Activación

- **En producción:** la invoca `letra` en Fase 3 de `produccion` cuando se solicita un acento o idioma.
- **En modo conversacional:** se activa de forma independiente sobre lo que indique el usuario —una obra completa, un párrafo o una sola frase, proporcionada o señalada por él— con un acento o idioma objetivo.

---

## Fuentes de Consulta

- *No abras guías a ciegas: entra por el mapa, que decide qué archivo abrir.*
    - **Mapa:** `.claude/rules/fonetizar.md`
    - **Biblioteca:** `fonetizar/` (abre solo la guía del acento/idioma objetivo, un archivo).

---

## Parámetros de Entrada

- **Texto objetivo:** obra completa, párrafo o frase suelta, proporcionada o indicada por el usuario.
- **Acento / idioma objetivo:** el sistema fonológico a aplicar.

---

## Flujo de Ejecución

- **Resolver guía:** identifica el acento/idioma y localiza su guía vía `.claude/rules/fonetizar.md`; abre solo ese archivo.
- **Aplicar transformaciones:** aplica las reglas de esa guía al texto objetivo.
- **Entregar:** devuelve el texto fonetizado (`composicion/formato.md §2`); nunca toca el `style_box`.

---

## Principios clave

- Un mismo texto con fonetización distinta produce resultados radicalmente diferentes en timbre y emoción.
- Refuerza el efecto anclando también con `jerga` local en la letra.

---

## Relación con otras skills

- `letra` la invoca en Fase 3 cuando se pide acento/idioma; también puede aplicarse después sobre la letra ya escrita.
- `jerga` es su gemela (modismos locales); combinadas, potencian el anclaje regional.

---

## Ejemplo

**Entrada:**
    ```text
    `los perros del puerto` + Acento Andaluz.
    ```
**Salida:**
    ```text
    Letra fonetizada Andaluz: `loh perroh del puerto`.
    ```
