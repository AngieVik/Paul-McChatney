---
name: lyrics_box
type: skill
description: Orquestadora del lyrics_box. Toma el boceto de letra de Fase 3 y lo desarrolla en Fases 4 y 5 —estructura, dirección de banda, técnica vocal, métrica y efectos— preservando la lírica.
---

# lyrics_box

- *Convierte el boceto de letra limpia en el `lyrics_box` final: le añade estructura, dirección de banda, técnica vocal, comandos temporales y efectos, sin perder la calidad lírica, narrativa, fonética, métrica y poética del original.*

---

## Activación

- **En `produccion`:** recibe el boceto de `letra` (Fase 3) y lo lleva por Fase 4 (estructura y dirección) y Fase 5 (efectos y producción) de `produccion`.
- **En modo conversacional:** se activa de forma independiente cuando el usuario aporta una letra —completa o parcial— y pide estructurarla, dirigirla o convertirla en `lyrics_box`.

---

## Fuentes de Consulta

- *Antes de estructurar, entra por los mapas y abre solo los archivos técnicos que la sección requiera.*
    - **Mapa propio:** `.claude/rules/lyrics_box.md`
    - **Archivo técnico:** `composicion/lyrics_box.md`
    - **Boceto de partida (lírica, narrativa, métrica, fonética, poética):** `.claude/rules/letra.md` → `composicion/letra.md`
    - **Dirección vocal por línea:** `.claude/rules/tecnicas_vocales.md` → `composicion/tecnicas_vocales.md`
    - **Efectos y post-`produccion` (Fase 5):** `.claude/rules/efectos.md` → `composicion/efectos.md`
- *Para canon de secciones, moods, FX o dinámicas, invoca `buscar_tag`.*
    - Mapa canónico: `.claude/rules/chupilista.md`

---

## Parámetros de Entrada

- **Boceto de Letra:** la letra limpia de Fase 3 (sin tags), base de la calidad lírica.
- **Dictamen de Estilo:** el `style_box` compilado en Fase 2, para mantener coherencia sonora.
- **Intención de Sección:** estructura, energía, giros o momentos concretos pedidos por el usuario.
- **Material Existente:** `lyrics_box` ya iniciado para revisar, corregir o iterar.

---

## Flujo de Ejecución

- **Fase 4 · Estructurar:** inserta secciones y comandos temporales según `composicion/lyrics_box.md`; fija la identidad vocal (Persona Stacking) y la dirección de banda; endurece la métrica de la letra (rigidez estructural, `composicion/letra.md §1.2`).
- **Fase 4 · Dirigir voz:** aplica la dirección vocal por línea desde `composicion/tecnicas_vocales.md` (susurros, gritos, duetos, coros, timbre).
- **Fase 5 · Efectos:** inyecta silencios, SFX, glitches, transiciones y comandos de producción temporales desde `composicion/efectos.md`.
- **Preservar la lírica:** en cada pase protege narrativa, fonética, métrica y poética; huye del cliché y de la escritura de IA. Si hace falta reanclar acento, apóyate en `fonetizar`/`jerga`.
- **Entregar y parar:** presenta el `lyrics_box` con el formato de `composicion/lyrics_box.md` (corchetes, columnas), a la espera de revisión del usuario.

---

## Reglas de Integridad

- **La letra manda:** las tags dirigen, no reescriben la historia; el texto cantable conserva su calidad de Fase 3.
- **Un evento, un corchete:** aísla conceptos en columna; tags cortas y contundentes.
- **Canon con criterio:** usa `buscar_tag` para lo canónico; las creaciones se justifican por función.
- **Separación de cajas:** las tags de estilo global viven en el `style_box`; aquí solo van eventos temporales dentro de la letra, el `style_box` compilado en Fase 2 se usa para mantener coherencia sonora.

---

## Relación con otras skills

- `letra` entrega el boceto limpio de Fase 3; `lyrics_box` lo desarrolla, no lo sustituye.
- `tecnicas_vocales` (archivo técnico) aporta la dirección vocal por línea.
- `efectos` (archivo técnico) aporta la capa de post-producción de Fase 5.
- `buscar_tag` extrae canon de secciones, moods, FX y dinámicas.
- `fonetizar` y `jerga` reanclan el acento sobre la letra si se solicita anclaje regional o fonético.

---
