---
name: fonetizar
description: Use when el usuario pide adaptar la pronunciación cantada de una obra, un párrafo o una frase a un acento o idioma concreto.
---

# fonetizar

- *Reescribe texto cantable para que suene con un acento o idioma concreto. La fonetización va en la letra cantable, nunca en el `style_box`.*

---

## Activación

- **En `produccion`:** se aplica después de `letra` en Fase 3 cuando se solicita un acento o idioma.
- **En modo conversacional:** se activa de forma independiente sobre lo que indique el usuario —una obra completa, un párrafo o una sola frase, proporcionada o señalada por él— con un acento o idioma objetivo.

---

## Fuentes de Consulta

- *No abras guías a ciegas: entra por el mapa, que decide qué archivo abrir.*
    - **Mapa:** `.agents/maps/fonetizar.md`
    - **Biblioteca:** `fonetizar/` (abre solo la guía del acento/idioma objetivo, un archivo).

---

## Parámetros de Entrada

- **Texto objetivo:** obra completa, párrafo o frase suelta, proporcionada o indicada por el usuario.
- **Acento / idioma objetivo:** el sistema fonológico a aplicar.

---

## Flujo de Ejecución

- **Resolver guía:** identifica el acento/idioma y localiza su guía vía `.agents/maps/fonetizar.md`; abre solo ese archivo.
- **Calibrar evidencia:** trata las guías sin fuentes o pruebas registradas como heurísticas artísticas, no como reglas universales sobre una población.
- **Aplicar transformaciones:** conserva la grafía original por defecto y aplica únicamente las transformaciones pedidas, aprobadas o necesarias por un problema de pronunciación observado.
- **Entregar:** devuelve el texto fonetizado (`composicion/formato.md §2`); nunca toca el `style_box`.

---

## Principios clave

- La fonetización puede cambiar pronunciación, timbre y emoción; el resultado concreto se comprueba en la generación.
- `jerga` puede complementar el personaje cuando la intención lo justifique; no la añadas automáticamente.

---

## Relación con otras skills

- Se aplica después de `letra` en Fase 3 cuando se pide acento/idioma; también puede usarse sobre una letra ya escrita.
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
