---
name: jerga
description: Use when el usuario pide adaptar texto cantable con la jerga o los modismos de una región, oficio o comunidad concreta.
---

# jerga

- *Inyecta jerga específica en texto cantable para que se cante. La jerga va en la letra cantable, nunca en el `style_box`.*

---

## Activación

- **En `produccion`:** se aplica después de `letra` en Fase 3 cuando se solicita una jerga.
- **En modo conversacional:** se activa de forma independiente sobre lo que indique el usuario —una obra completa, un párrafo o una sola frase, proporcionada o señalada por él— con una jerga objetivo.

---

## Fuentes de Consulta

- *No abras guías a ciegas: entra por el mapa, que decide qué archivo abrir.*
    - **Mapa:** `.agents/maps/jerga.md`
    - **Biblioteca:** `jerga/` (abre solo la guía de la jerga objetivo, un archivo).

---

## Parámetros de Entrada

- **Texto objetivo:** obra completa, párrafo o frase suelta, proporcionada o indicada por el usuario.
- **Jerga objetivo:** el repertorio léxico a inyectar.

---

## Flujo de Ejecución

- **Resolver guía:** identifica la jerga y localiza su guía vía `.agents/maps/jerga.md`; abre solo ese archivo.
- **Calibrar evidencia:** trata la guía como repertorio contextual; no atribuyas sus rasgos de forma uniforme a toda una región, oficio o comunidad.
- **Aplicar transformaciones:** conserva el registro original por defecto e incorpora solo los modismos pedidos o aprobados que encajen con personaje, época e intención.
- **Entregar:** devuelve el texto con la jerga inyectada (`composicion/formato.md §2`); nunca toca el `style_box`.

---

## Principios clave

- La jerga puede modificar la voz narrativa, la época percibida y la actitud; su efecto se evalúa en contexto.
- No conviertas una guía en una caricatura ni acumules modismos para demostrar procedencia.

---

## Relación con otras skills

- Se aplica después de `letra` en Fase 3 cuando se pide jerga; también puede usarse sobre una letra ya escrita.
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
