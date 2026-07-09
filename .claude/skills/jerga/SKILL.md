---
name: jerga
type: skill
description: inyecta en la letra cantable jerga específica para que se cante, nunca en el `style_box`.
---

# jerga

- Inyecta en la letra cantable jerga específica para que se cante. La jerga va **en la letra cantable, nunca en el `style_box`**.

## Cuándo se activa

- **Se solicita explícitamente** una jerga en concreto sobre un mood u obra. 
- La llama `letra` en Fase 2 de `produccion` si se solicita previamente.

## Pasos

1. Identifica la jerga objetivo y abre **solo** su guía en `jerga/` con la herramienta de lectura, un archivo.
2. Aplica las transformaciones de esa guía a la letra.
3. Devuelve la letra con la jerga inyectada.

## Principio clave

- Un mismo texto con jerga distinta produce canciones radicalmente diferentes en acento y actitud.
- Al inyectar jerga local mejora el anclaje idiomático. Refuerza el efecto anclando en la letra.

## Entra → Sale

- **Entra:** una letra + una jerga objetivo.
- **Sale:** la letra modificada (`composicion/formato.md §2`).

## Relación

- La llama `letra` en Fase 2 de `produccion` si se solicita previamente.

## Ejemplo

**Entrada:**  
    ```text  
    `Deja de decir tonterías y vayamos ya un momento a la playa, ¡por supuesto que sí!` + jerga Almeriense.  
    ```
**Salida:**  
    ```text  
    Almeriense: `Déjate de chuminás y vámonos ya un ratico a la playa, ¡no ni ná!`.  
    ```
