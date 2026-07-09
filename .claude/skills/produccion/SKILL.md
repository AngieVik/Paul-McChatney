---
name: produccion
type: skill
description: Orquesta el flujo completo de creación musical en 5 fases, delegando cada parte en las skills y archivos de referencia adecuados.
---

# produccion

- Activa el **Modo Producción** de Paul McChatney: un flujo guiado, interactivo y por fases para convertir una idea musical en una obra completa, copiable y lista para generar.
- Es la skill central del sistema. No sustituye a las demás skills: las coordina en el momento exacto.

---

## Cuándo se activa

- El usuario pide explícitamente `iniciar una producción`, o `activar el modo producción`.
- El usuario trae una idea musical y quiere desarrollarla paso a paso hasta obra final.
- El usuario quiere trabajar sobre una obra viva usando el ciclo de proyecto.

---

## Antes de empezar

- *Repasa el rol y las reglas* (ya en contexto por `@import`), `system_prompt/system_prompt.md`.
- *Repasa los aprendizajes acumulados*: `.claude/MEMORY.md`.

## Principios de oro

- Una producción no es una respuesta larga: es un **proceso controlado**, cada fase debe dejar una versión más clara, más útil y más generable que la anterior.
- Todo lo producido antes de aprobar es **borrador vivo, conceptual y maleable** .
- La última versión real vive en `_hojas_sucias/<slug>.md`, gestionada por `proyecto`, si el usuario pega una versión consolidada, esa versión pasa a ser la base actual.
- Trabaja sobre una sola obra a la vez, salvo que el usuario pida explícitamente comparar.
-, no saltes fases salvo petición explícita.
- Al terminar cada fase, **para** y espera aprobación, ajuste o instrucción del usuario: Avanzar una fase, Mantener la fase, o retroceder hasta la fase solicitada.
- Usa tu instinto de productor para inyectar tags o instrucciones que disparen la calidad del resultado.


## Pasos

### 0 · Fase 0 Concepto

- Si la idea es vaga, propón 2–3 direcciones fuertes.
- Investiga en web: géneros similares y/o opuestos, géneros subyacentes, tendencias sonoras y referencias de grupos.
- Muestra un pequeño informe; aclara contexto emocional + género.
- Define una hipótesis de producción.
- Crea el **archivo de trabajo** con la skill `proyecto`.

- **PARA.** y entrega: `Borrador título de trabajo o slug provisional creado`, `Borrador concepto emocional`, `Borrador dirección sonora inicial`, `Borrador próxima fase propuesta`.

---

### 1 · Fase 1 Borradores de style_box y exclude_box

- Busca por concepto (grep, solo coincidencias) en el núcleo de `chupilista/` que toque, índice en `.claude/rules/chupilista.md`:
    - Género base.
    - Instrumentos protagonistas.
    - Voz o timbre.
    - Ritmo, BPM o groove.
    - Textura diferencial.
    - Ghost tag si aporta identidad.
- Construye el borrador del `style_box`, combinando canon + instinto + `.claude/rules/style_box.md` (máx ~20 palabras). (Apóyate en las skills `style-box`, `buscar-tag` y `fusionar`).
- Anota exclusiones candidatas, pero no cierres todavía el `exclude_box` final si la obra aún puede cambiar.
- Evita los tags decorativos sin función.

- **PARA.** y entrega: `Borrador del style_box`, `Borrador del exclude_box`

---

### 2 · Fase 2 Borrador de la letra

- Redacta la letra sin tags, foco poético/narrativo; queda abierta a refinarse en fases posteriores. Usa `.claude/rules/letra.md` y la skill `lirica`.
- Solo si se pide **explícitamente** una fonetización o jerga concreta, aplícala con `fonetizar` o `jerga`.
- **PARA.** y entrega: Voz narrativa: `Borrador de la letra limpia`, `Borrador de Quien canta` `Borrador de a quien o a que canta` y `Borrador desde que herida, deseo burla o conflicto canta`.

---

### 3 · Fase 3 Borrador del lyrics_box

- Apóyate en la skill `buscar-tag` y busca las tags concretas por concepto (grep, solo coincidencias) en el núcleo de `chupilista/` que necesites, índice `.claude/rules/chupilista.md`, combinando canon + instinto.  
    **Inyecta las tags de estructura y dirección de banda** de manera magistral en el `lyrics_box`, busca por concepto (grep, solo coincidencias) en `.claude/rules/lyrics_box.md` y `.claude/rules/tecnicas_vocales.md`.  
    **Crea `[MOOD]` y `[PRODUCTION]`.**  
    **Crea la linea cero de identidad vocal** si la obra tiene cantante definido.  
    **Reajusta o modifica la letra** si un tag o un fraseo mejora el resultado.

- **PARA.** y entrega: `Borrador línea cero de identidad vocal (si la obra tiene cantante definido)`, `Borrador [MOOD] y [PRODUCTION]`, `Borrador del lyrics_box`.

---

### 4 · Fase 4 — Masterización.**

- Abre `<razonamiento>`, eleva el impacto y controla el post-procesamiento con `.claude/rules/efectos.md`, apoyate en `buscar-tag`.
- Perfecciona el `exclude_box` con `.claude/rules/exclude_box.md`, apoyate en `buscar-tag`.
- Aplica tecnicas vocales en `lyrics_box` con `.claude/rules/tecnicas_vocales.md`, apoyate en `buscar-tag`.
- Detecta y soluciona errores críticos.
- Instinto de Productor Musical de Élite, no fuerces cambios innecesarios ni añadas efectos superfluos.
- Detecta y soluciona errores críticos. Apóyate en la skill `auditar`.
- **PARA.** y entrega la obra terminada con todos los borradores con el formato expuesto en `composicion/formato.md`.

## Finalizar

- El cierre y la gestión del ciclo se hacen con los **comandos de `proyecto`** (`crear`, `listar`, `retomar`, `cerrar`, `aprobar`, `guardar`, `cancelar`, `eliminar`).
- Al **aprobar** una obra, si contiene hallazgos técnicos o creativos de valor, **sugiere** al usuario iniciar **`retrospectiva`** (`conocimientos/retrospectiva.md`).
- Si hay un **aprendizaje real**, propón archivarlo en `.claude/MEMORY.md` o `composicion/` y espera aprobación.

## Ejemplo

**Entrada:**  
    ```text  
    Usuario: `<inicia la producción, quiero una bulería metalera sobre un herrero gitano>`  
    ```  
    **Salida:**  
    ```text  
    Fase 0: confirmo mood (orgullo/fuego) y fusión (bulería + metal), investigo caló y palmería; pregunto y **paro**.  
    ```
