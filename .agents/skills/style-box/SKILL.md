---
name: style-box
description: Use when el usuario pide crear, revisar, corregir o iterar un `style_box`, dentro o fuera de `produccion`.
---

# style-box

- *Construye el `style_box` aplicando `fusionar` y `buscar-tag`, siguiendo las instrucciones técnicas de `composicion/style_box.md`.*

---

## Activación

- **En `produccion`:** se activa en Fase 2 de `produccion`, después del dictamen de `fusionar`.
- **En modo conversacional:** se activa de forma independiente y en cualquier momento cuando el usuario pide crear, revisar, corregir o iterar un `style_box`.

---

## Fuentes de Consulta

- *Antes de construir o revisar, consulta el mapa y abre el archivo técnico obligatorio.*
    - **Mapa:** `.agents/maps/style_box.md`
    - **Archivo técnico:** `composicion/style_box.md`
- *Cuando necesites canon de `chupilista`, aplica `buscar-tag`.*
    - Mapa canónico: `.agents/maps/chupilista.md`
    - Biblioteca: `chupilista/`

---

## Parámetros de Entrada

- **Dictamen de Fusión:** mapa acústico y teórico de `fusionar`: géneros, tempos, espectro de frecuencias, instrumentación, textura vocal, atmósfera y dirección sonora.
- **Intención de Obra:** emoción núcleo, idioma de la letra, tono narrativo, energía, época, región o restricción dada por el usuario.
- **Etiquetas Canónicas:** `tags` literales recuperadas y validadas por `buscar-tag`.
- **Creaciones Controladas:** `tags` o fusiones nuevas propuestas por `fusionar` cuando `chupilista` no cubre literalmente la intención artística.
- **Material Existente:** `style_box` ya escrito por el usuario para revisar, limpiar, completar o corregir.

---

## Flujo de Ejecución

- **Resolver modo:** si viene de `produccion`, parte del dictamen de `fusionar`; si se activa sola y falta arquitectura sonora, pide un dictamen a `fusionar` antes de compilar.
- **Abrir referencias:** consulta `.agents/maps/style_box.md` y abre `composicion/style_box.md`.
- **Extraer canon:** usa `buscar-tag` para localizar `tags` existentes en `chupilista`; el canon es ancla documental, no prueba de eficacia ni veto creativo.
- **Compilar `style_box`:** aplica las reglas de `composicion/style_box.md` (orden jerárquico, límite de tags, anclajes y colisiones), integra canon y creaciones controladas, y elimina redundancias. Compila la arquitectura de `fusionar`, no la rediseña.
- **Entregar y parar:** presenta el `style_box` limpio con el formato de `composicion/style_box.md` y espera la revisión del usuario antes de avanzar.

---

## Salida Estándar

- **Bloque `style_box`:** según el orden jerárquico y el formato del archivo técnico, dentro de su límite de tags.
- **Si usa creaciones controladas:** indícalo fuera del bloque copiable; nunca mezcles notas de trazabilidad con la sintaxis que recibirá Suno.
- **Si el canon es insuficiente:** indícalo; combina las `tags` canónicas disponibles con creaciones controladas justificadas por `fusionar`.

---

## Relación con otras skills

- `produccion` activa `style-box` en Fase 2.
- `fusionar` diseña la arquitectura sonora y propone creaciones controladas; `style-box` la compila y ordena, no la rediseña.
- `buscar-tag` extrae etiquetas canónicas existentes en `chupilista`.
- El `exclude_box` no se compila aquí: se genera íntegro en Fase 5 desde `composicion/exclude_box.md`.

- *`style-box` no bloquea la creatividad: consulta, ordena, compila y entrega sintaxis útil.*
