---
name: retrospectiva
type: skill
description: Cierra el ciclo de aprendizaje tras una obra: detecta hallazgos reales, decide dónde archivarlos y actualiza memoria y manuales bajo aprobación. Skill autónoma generadora de conocimiento.
---

# retrospectiva

- *Convierte la experiencia de una obra en conocimiento reutilizable: destila principios, confirma o descarta corazonadas y propone dónde guardarlos, siempre con aprobación del usuario.*

---

## Activación

- **Al aprobar una obra:** `proyecto` y `produccion`, (comando `aprobar`) sugieren iniciar `retrospectiva`. La solicita el usuario.
- **En modo conversacional:** el usuario pide revisar qué se ha aprendido en un proyecto en curso o en una obra ya aprobada.

---

## Fuentes de Consulta

- *Para decidir dónde vive cada aprendizaje, consulta los mapas antes de tocar archivos.*
    - **Principios transversales:** `.claude/MEMORY.md`.
    - **Técnica o tag concreto:** su archivo en `composicion/`, localizado por el mapa correspondiente en `.claude/rules/` (índice `.claude/rules/composicion.md`).
    - **Corazonadas `⚗️`:** viven marcadas dentro de los archivos de `composicion/`; la retrospectiva las asciende, degrada o elimina.

---

## Protocolo de adquisición de aprendizaje

1. **Detectar hallazgo real:** revisa la obra buscando algo que haya funcionado (o fallado) de forma no obvia: una técnica nueva, un principio creativo, una corrección de mezcla, un cliché evitado. Descarta lo ya documentado o lo trivial.
2. **Clasificar el destino:**
    - **Principio transversal** (aplica a cualquier obra) → candidato a `.claude/MEMORY.md`.
    - **Técnica o tag concreto** (pertenece a una caja) → candidato a su `composicion/<archivo>.md`, entrando por su mapa en `.claude/rules/`.
    - **Corazonada `⚗️`** puesta a prueba en la obra → **ascender** (quitar la marca `⚗️` si se confirmó), **degradar** (mantener marca y matizar) o **eliminar** (si se refutó).
3. **Formular en positivo/accionable:** redacta el aprendizaje como instrucción útil, nunca como anécdota ni reproche.
4. **Proponer y esperar aprobación:** presenta el cambio y pregunta `Añadir`, `Modificar`, `Eliminar` o `No hacer nada`. No toques ningún archivo hasta recibir el visto bueno.
5. **Aplicar y confirmar:** ejecutado el cambio aprobado, confirma qué archivo se actualizó.

---

## Reglas de Integridad

- **Nunca escribe sin aprobación:** toda propuesta pasa por el usuario antes de tocar archivos.
- **Un aprendizaje, un destino:** transversal → `MEMORY`; concreto → su `composicion/`. No dupliques.
- **Positivo y accionable:** el conocimiento se guarda como regla utilizable.

---

## Relación con otras skills

- `proyecto` y `produccion` la sugieren al aprobar la obra, cerrando el ciclo.
- Escribe en `.claude/MEMORY.md` (principios) y en los `composicion/*.md` (técnicas), enrutando por sus mapas `.claude/rules/`.

---

## Ejemplo

**Entrada:**
    ```text
    `proyectos/papas_en_ajopollo/papas_en_ajopollo.md`
    ```
**Salida:**
    ```text
    Principio transversal → La narrativa manda: antes de tocar un tag, entiende qué historia cuenta la canción y para quién. (→ .claude/MEMORY.md)
    Corazonada confirmada → el "3D Room Dynamics" de efectos §1.5 funcionó: propongo ascenderlo (quitar ⚗️). (→ composicion/efectos.md)
    ¿`Añadir`, `Modificar`, `Eliminar` o `No hacer nada`?
    ```
