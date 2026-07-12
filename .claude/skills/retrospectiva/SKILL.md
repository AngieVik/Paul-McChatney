---
name: retrospectiva
type: skill
description: Cierra el ciclo de aprendizaje tras una obra aprobada y propone qué memoria actualizar.
---

# retrospectiva

## Cuándo se activa

- `proyecto` y `produccion` sugieren `retrospectiva` tras aprobar la obra.
- El usuario pide revisar qué se ha aprendido en un proyecto en curso u obra aprobada.

## Pasos

- Al **aprobar** una obra, si contiene hallazgos técnicos o creativos de valor, sugiere al usuario iniciar `retrospectiva` .
- Si hay un **aprendizaje real**, propón archivarlo en `.claude/MEMORY.md` o en un archivo de `.claude/rules/composicion.md/` y espera aprobación.

## Relación

- `proyecto` y `produccion` al finalizar fase 4, sugieren iniciar `retrospectiva` al aprobar la obra para finalizar el ciclo.

## Entra → Sale

- **Entra:**  
    Obra aprobada o proyecto en curso.
- **Sale:**  
    Principio transversal de composición → `.claude/MEMORY.md` y/o Técnica o tag concreto** → su archivo de `composicion/`. Siempre en positivo/accionable.  
    Preguntar: `Añadir`, `Modificar`, `Eliminar` o `No hacer nada`, esperando aprobación antes de tocar archivos.

## Ejemplo

**Entrada:**  
    ```text  
    `proyectos/papas_en_ajopollo/papas_en_ajopollo.md`  
    ```  
**Salida:**  
    ```text  
    Principio transversal de composición → La narrativa manda, antes de tocar un tag, entiende qué historia cuenta la canción y para quién.  
    ¿Quieres `Añadir`, `Modificar`, `Eliminar` o `No hacer nada`? esperando aprobación antes de tocar archivos.  
    ```
