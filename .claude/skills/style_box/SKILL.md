---
name: "style_box"
type: "skill"
description: "Orquestadora del style_box. Coordina fusionar y buscar_tag para compilar el bloque de estilo de la obra. Activable en `produccion` (Fase 2) o en modo conversacional en cualquier momento."
---

# style_box

- *Orquesta la construcción del `style_box` coordinando `fusionar` y `buscar_tag`, siguiendo las instrucciones técnicas de `composicion/style_box.md`.*

---

## Activación

- **En `produccion`:** se activa en Fase 2 de `produccion`, después del dictamen de `fusionar`.
- **En modo conversacional:** se activa de forma independiente y en cualquier momento cuando el usuario pide crear, revisar, corregir o iterar un `style_box`.

---

## Fuentes de Consulta

- *Antes de construir o revisar, consulta el mapa y abre el archivo técnico obligatorio.*
    - **Mapa:** `.claude/rules/style_box.md`
    - **Archivo técnico:** `composicion/style_box.md`
- *Cuando necesites canon de `chupilista`, invoca `buscar_tag`.*
    - Mapa canónico: `.claude/rules/chupilista.md`
    - Biblioteca: `chupilista/`

---

## Parámetros de Entrada

- **Dictamen de Fusión:** mapa acústico y teórico de `fusionar`: géneros, tempos, espectro de frecuencias, instrumentación, textura vocal, atmósfera y dirección sonora.
- **Intención de Obra:** emoción núcleo, idioma de la letra, tono narrativo, energía, época, región o restricción dada por el usuario.
- **Etiquetas Canónicas:** `tags` literales recuperadas y validadas por `buscar_tag`.
- **Creaciones Controladas:** `tags` o fusiones nuevas propuestas por `fusionar` cuando `chupilista` no cubre literalmente la intención artística.
- **Material Existente:** `style_box` ya escrito por el usuario para revisar, limpiar, completar o corregir.

---

## Flujo de Ejecución

- **Resolver modo:** si viene de `produccion`, parte del dictamen de `fusionar`; si se activa sola y falta arquitectura sonora, pide un dictamen a `fusionar` antes de compilar.
- **Abrir referencias:** consulta `.claude/rules/style_box.md` y abre `composicion/style_box.md`.
- **Extraer canon:** usa `buscar_tag` para localizar `tags` existentes en `chupilista`; el canon es ancla fiable, no veto creativo.
- **Compilar `style_box`:** aplica las reglas de `composicion/style_box.md` (orden jerárquico, límite de tags, anclajes y colisiones), integra canon y creaciones controladas, y elimina redundancias. Compila la arquitectura de `fusionar`, no la rediseña.
- **Entregar y parar:** presenta el `style_box` limpio con el formato de `composicion/style_box.md` y espera la revisión del usuario antes de avanzar.

---

## Salida Estándar

- **Bloque `style_box`:** según el orden jerárquico y el formato del archivo técnico, dentro de su límite de tags.
- **Si usa creaciones controladas:** añade una nota interna indicando que proceden del dictamen de `fusionar` y cubren huecos no localizados en `chupilista`.
- **Si el canon es insuficiente:** indícalo; combina las `tags` canónicas disponibles con creaciones controladas justificadas por `fusionar`.

---

## Relación con otras skills

- `produccion` activa `style_box` en Fase 2.
- `fusionar` diseña la arquitectura sonora y propone creaciones controladas; `style_box` la compila y ordena, no la rediseña.
- `buscar_tag` extrae etiquetas canónicas existentes en `chupilista`.
- El `exclude_box` no se compila aquí: se genera íntegro en Fase 5 desde `composicion/exclude_box.md`.

- *`style_box` no bloquea la creatividad: consulta, ordena, compila y entrega sintaxis útil.*
