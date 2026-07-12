---
name: style_box
type: skill
description: Orquestador de style_box y exclude_box. Consulta sus mapas, lee sus archivos técnicos y coordina fusionar y buscar_tag para compilar bloques finales.
---

# style_box

- *Orquesta la construcción del `style_box` y del `exclude_box` siguiendo las instrucciones técnicas que viven en `composicion/style_box.md`.*

---

## 1 · Activación

- **Modo producción:** se activa en Fase 1 de `produccion`, después del dictamen de `fusionar`.
- **Modo independiente:** se activa cuando el usuario pide crear, revisar, corregir o iterar un `style_box`, un `exclude_box` o ambos.

---

## 2 · Fuentes de Consulta

- *Antes de construir o revisar cualquier `style_box`, consulta el mapa y abre el archivo técnico correspondiente.*
    - Mapa: `.claude/rules/style_box.md`
    - Archivo técnico: `composicion/style_box.md`

- *Antes de construir o revisar cualquier `exclude_box`, consulta el mapa y abre el archivo técnico correspondiente.*
    - Mapa: `.claude/rules/exclude_box.md`
    - Archivo técnico: `composicion/exclude_box.md`

- *Cuando necesites canon de `CHUPILISTA`, invoca `buscar_tag`.*
    - Mapa canónico: `.claude/rules/chupilista.md`
    - Biblioteca: `chupilista/`

---

## 3 · Parámetros de Entrada

- **Dictamen de Fusión:** mapa acústico y teórico generado por `fusionar`: géneros, tempos, espectro de frecuencias, instrumentación, textura vocal, atmósfera y dirección sonora.
- **Intención de Obra:** emoción núcleo, idioma de la letra, tono narrativo, energía, época, región o restricción dada por el usuario.
- **Etiquetas Canónicas:** `tags` literales recuperadas y validadas por `buscar_tag`.
- **Creaciones Controladas:** `tags`, fusiones o formulaciones nuevas propuestas por `fusionar` cuando `CHUPILISTA` no cubre literalmente la intención artística.
- **Material Existente:** `style_box` o `exclude_box` ya escritos por el usuario para revisar, limpiar, completar o corregir.

---

## 4 · Flujo de Ejecución

- **Resolver modo de trabajo:** si viene desde `produccion`, recibe el dictamen de `fusionar`; si se activa sola, analiza la petición del usuario y pide a `fusionar` un dictamen cuando falte arquitectura sonora.
- **Abrir referencias:** consulta `.claude/rules/style_box.md` y `composicion/style_box.md`; consulta `.claude/rules/exclude_box.md` y `composicion/exclude_box.md` cuando haya que construir o revisar exclusiones.
- **Extraer canon:** usa `buscar_tag` solo para localizar `tags` existentes en `CHUPILISTA`, manteniendo el canon como referencia y no como veto creativo.
- **Compilar `style_box`:** aplica las reglas de `composicion/style_box.md`, integra canon y creaciones controladas, ordena el molde sonoro y elimina redundancias.
- **Compilar `exclude_box`:** aplica las reglas de `composicion/exclude_box.md`, protege la mezcla y entrega la salida final sin corchetes, como términos separados por comas.
- **Entregar y parar:** presenta los bloques limpios y espera revisión del usuario antes de avanzar.

---

## 5 · Salida Estándar

- **Cuando entregue solo `style_box`:**
    `Tag principal`, `Tag secundaria`, `Instrumento clave`, `Perfil vocal`, `Ritmo`, `Textura`, `Producción`, `Ghost tag`

- **Cuando entregue solo `exclude_box`:**
    `clipping, overcompressed, muddy mix, robotic voice`

- **Cuando entregue ambos:**
    `style_box`
    `Tag principal`, `Tag secundaria`, `Instrumento clave`, `Perfil vocal`, `Ritmo`, `Textura`, `Producción`, `Ghost tag`

    `exclude_box`
    `clipping, overcompressed, muddy mix, robotic voice`

- **Cuando use creaciones controladas:**
    `style_box`
    `Tag canónica`, `Creación Controlada`, `Tag canónica`, `Creación Controlada`, `Producción`, `Ghost tag`

    Nota interna: las creaciones controladas proceden del dictamen de `fusionar` y cubren huecos no localizados en `CHUPILISTA`.

- **Cuando no haya canon suficiente:**
    No hay canon suficiente para cubrir todo el concepto.
    Se usan `tags` canónicas disponibles y creaciones controladas justificadas por `fusionar`.

---

## 6 · Relación con Otras Skills

- `produccion` activa `style_box` en Fase 1 para compilar `style_box` y `exclude_box`.
- `fusionar` diseña la arquitectura sonora y propone creaciones controladas.
- `buscar_tag` extrae etiquetas canónicas existentes en `CHUPILISTA`.
- `lyrics_box` desarrolla estructura, dirección musical, comandos libres e interpretación.
- `exclude_box` vive como archivo técnico en `composicion/exclude_box.md`, no como skill independiente.

`style_box` no bloquea la creatividad.  
`style_box` consulta, ordena, compila y entrega sintaxis útil.
