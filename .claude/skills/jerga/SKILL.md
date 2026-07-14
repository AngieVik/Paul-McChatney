---
name: "jerga"
type: "skill"
description: "Inyecta en el texto cantable jerga específica para que se cante. Nunca en el style_box. Activable en `produccion` (Fase 3) o en modo conversacional sobre una obra, un párrafo o una frase."
---

# jerga

- *Inyecta jerga específica en texto cantable para que se cante. La jerga va en la letra cantable, nunca en el `style_box`.*

---

## Activación

- **En `produccion`:** la invoca `letra` en Fase 3 de `produccion` cuando se solicita una jerga.
- **En modo conversacional:** se activa de forma independiente sobre lo que indique el usuario —una obra completa, un párrafo o una sola frase, proporcionada o señalada por él— con una jerga objetivo.

---

## Fuentes de Consulta

- *No abras guías a ciegas: entra por el mapa, que decide qué archivo abrir.*
    - **Mapa:** `.claude/rules/jerga.md`
    - **Biblioteca:** `jerga/` (abre solo la guía de la jerga objetivo, un archivo).

---

## Parámetros de Entrada

- **Texto objetivo:** obra completa, párrafo o frase suelta, proporcionada o indicada por el usuario.
- **Jerga objetivo:** el repertorio léxico a inyectar.

---

## Flujo de Ejecución

- **Resolver guía:** identifica la jerga y localiza su guía vía `.claude/rules/jerga.md`; abre solo ese archivo.
- **Aplicar transformaciones:** sustituye e inyecta modismos según esa guía en el texto objetivo.
- **Entregar:** devuelve el texto con la jerga inyectada (`composicion/formato.md §2`); nunca toca el `style_box`.

---

## Principios clave

- Un mismo texto con jerga distinta produce resultados radicalmente diferentes en acento y actitud.
- Al inyectar jerga local mejora el anclaje idiomático; refuerza el efecto anclando en la letra.

---

## Relación con otras skills

- `letra` la invoca en Fase 3 cuando se pide jerga; también puede aplicarse después sobre la letra ya escrita.
- `fonetizar` es su gemela (acento/idioma); combinadas, potencian el anclaje regional.

---

## Ejemplo

**Entrada:**

```text
`Deja de decir tonterías y vayamos ya un momento a la playa, ¡por supuesto que sí!` + jerga Almeriense.
```

**Salida:**

```text
Almeriense: `Déjate de chuminás y vámonos ya un ratico a la playa, ¡no ni ná!`.
```
