---
name: retrospectiva
type: skill
description: Gestiona el ciclo de aprendizaje del sistema: detecta hallazgos reales en cualquier momento del proceso, decide dónde archivarlos y actualiza memoria o manuales solo bajo aprobación explícita del usuario.
---

# retrospectiva

- *Convierte aprendizajes detectados durante el trabajo en conocimiento reutilizable: destila principios, confirma o descarta corazonadas y propone dónde guardarlos, siempre con aprobación explícita del usuario.*

---

## Activación

- **En cualquier momento:** puede activarse durante una obra abierta, una fase, una corrección, una prueba técnica, una instrucción del usuario, una lógica nueva, una función nueva de Suno o una obra ya aprobada; no requiere que la obra esté terminada.
- **Tras `aprobar` una obra:** `proyecto` solo sugiere si el usuario quiere hacer una retrospectiva.
    - **Si la respuesta es positiva** analiza y propone aprendizajes reales si existen.
- **Condición para escribir:** ningún aprendizaje se archiva en `MEMORY.md`, `composicion/` o `PROYECTOS.md` sin aprobación explícita del usuario.

---

## Fuentes de Consulta

- *Para decidir dónde vive cada aprendizaje, consulta los mapas antes de tocar archivos.*
    - **Principios transversales:** `.claude/MEMORY.md`.
    - **Técnica o tag concreto:** su archivo en `composicion/`, localizado por el mapa correspondiente en `.claude/rules/` (índice `.claude/rules/composicion.md`).
    - **Corazonadas `⚗️`:** viven marcadas dentro de los archivos de `composicion/`; la retrospectiva las asciende, degrada o elimina.

---

## Protocolo de adquisición de aprendizaje

1. **Detectar hallazgo real:** revisa la obra o texto indicado buscando algo que haya funcionado (o fallado) de forma no obvia: una técnica nueva, un principio creativo, una corrección de mezcla, un cliché evitado. Descarta lo ya documentado o lo trivial.
2. **Distinguir fuente y aprendizaje:** la fuente puede ser un prompt, una instrucción del usuario, una prueba, una salida de Suno, una corrección o una decisión durante `produccion`. La fuente no es conocimiento por sí sola.
3. **Validar utilidad:** conserva solo aprendizajes reutilizables; descarta ocurrencias aisladas, gustos pasajeros o resultados no comprobados.
4. **Clasificar el destino:**
    - **Principio transversal** (aplica a cualquier obra) → candidato a `.claude/MEMORY.md`.
    - **Técnica o tag concreto** (pertenece a una caja) → candidato a su `composicion/<archivo>.md`, entrando por su mapa en `.claude/rules/`.
    - **Corazonada `⚗️`** puesta a prueba en la obra → **ascender** (quitar la marca `⚗️` si se confirmó), **degradar** (mantener marca y matizar) o **eliminar** (si se refutó).
5. **Formular en positivo/accionable:** redacta el aprendizaje como instrucción útil, nunca como anécdota ni reproche.
6. **Proponer y esperar aprobación:** presenta el cambio y pregunta `Añadir`, `Modificar`, `Eliminar` o `No hacer nada`. No toques ningún archivo hasta recibir el visto bueno.
7. **Aplicar y confirmar:** ejecutado el cambio aprobado, confirma qué archivo se actualizó.

---

## Reglas de Integridad

- **Un aprendizaje, un destino:** transversal → `MEMORY`; concreto → su `composicion/`. No dupliques.
- **Positivo y accionable:** el conocimiento se guarda como regla utilizable.
- **Una instrucción validada sí puede ser aprendizaje:** si el usuario corrige, confirma o aprueba una regla reutilizable, puede archivarse aunque la obra siga abierta.
- **La obra y el aprendizaje son entidades separadas:** aprobar una obra, aprobar un prompt y aprobar un aprendizaje no son lo mismo.
- **Mismo proceso siempre:** no hay retrospectiva provisional/canónica separada; hay un único proceso de detección, formulación, aprobación y escritura.
- **Nunca escribas sin aprobación:** todo cambio en `MEMORY.md`, `composicion/` o `PROYECTOS.md` requiere confirmación explícita.

---

## Relación con otras skills

- Puede ejecutarse en cualquier momento que el usuario detecte o pida revisar un aprendizaje; no requiere que la obra esté cerrada.
- `proyecto` solo la sugiere tras `aprobar` (retrospectiva de cierre), sin ejecutarla automáticamente; solo `aprobar` finaliza la obra.
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
