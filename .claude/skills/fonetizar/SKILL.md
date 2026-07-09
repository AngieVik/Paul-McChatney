---
name: fonetizar
type: skill
description: reescribe la letra cantable, para que se cante con un acento o idioma concreto, nunca en el `style_box`.
---

# fonetizar

- Reescribe la letra cantable, para que se cante con un acento o idioma concreto. La fonetización va **en la letra cantable, nunca en el `style_box`**.

## Cuándo se activa

- **Se solicita explícitamente** un acento o idioma concreto sobre un mood u obra.
- La llama `letra` en Fase 2 de `produccion` si se solicita previamente.

## Pasos

1. Identifica el acento/idioma objetivo y abre **solo** su guía en `fonetizar/` con la herramienta de lectura, un archivo.
2. Aplica las transformaciones de esa guía a la letra.
3. Devuelve la letra fonetizada.

## Principios clave

- Un mismo texto con fonetización distinta produce canciones radicalmente diferentes en timbre y emoción.
- Refuerza el efecto anclando también con jerga local en la letra.

## Entra → Sale

- **Entra:** Letra + Acento/idioma objetivo.
- **Sale:** la letra fonetizada (`composicion/formato.md §2`).

## Relación

- La llama `letra` en Fase 2 de `produccion` si se solicita previamente.

## Ejemplo

**Entrada:**  
    ```text  
    `los perros del puerto` + Acento Andaluz.  
    ```
**Salida:**  
    ```text  
    Letra fonetizada Andaluz: `loh perroh del puerto`.  
    ```
