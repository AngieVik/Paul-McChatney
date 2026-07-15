---
name: buscar_tag
type: skill
description: Extractor canónico de etiquetas chupilista. Localiza, valida y entrega tags existentes como referencia fiable para cualquier skill y en cualquier fase. Activable en `produccion` o en modo conversacional.
---

# buscar_tag

- *Extractor canónico: localiza, valida y entrega etiquetas sintácticas exactas `[Tag]` desde `chupilista/` como material fiable de referencia. La decisión creativa final pertenece a la skill consumidora.*

---

## Activación

- **En `produccion`:** invocado por `style_box` (Fase 2), por `letra`/`lyrics_box` o por cualquier fase que necesite canon.
- **En modo conversacional:** invocable en cualquier momento, por el usuario o por otra skill, siempre que se necesiten tags canónicas.

---

## Fuentes de Consulta

- **Mapa canónico:** `.claude/rules/chupilista.md`
- **Biblioteca:** `chupilista/` (abre solo el/los módulos necesarios, contexto mínimo y preciso).

---

## Parámetros de Entrada

- **Concepto Objetivo:** requerimiento acústico, rítmico, vocal, temporal, estructural o conceptual buscado.
    - **Ejemplo:** percusión distorsionada, coro barroco, voz rasgada, drop silencioso.
- **Rutas Objetivo (opcional):** módulos `.md` concretos de `chupilista/` donde focalizar la búsqueda.
- **Caja Destino (opcional):** contexto de uso esperado: `style_box`, `lyrics_box`, `exclude_box`, mood, production u otro bloque definido por la skill consumidora.

---

## Flujo de Ejecución

- **Resolución de índice:** si la consumidora omite las rutas objetivo, consulta `.claude/rules/chupilista.md` para mapear el concepto al módulo probable; carga solo los módulos necesarios.
- **Búsqueda selectiva:** busca el concepto dentro del módulo elegido por raíz, variantes y sinónimos razonables.
    - **Ejemplo:** para voz rasgada, busca también raspy, gritty, hoarse, distorted vocal, vocal fry, si el módulo lo justifica.
- **Extracción literal:** extrae únicamente etiquetas que existan literalmente; conserva la grafía y el idioma de origen.
- **Validación sintáctica:** verifica corchete de apertura, contenido no vacío y corchete de cierre; reporta como incidencia cualquier tag útil pero mal formada.
- **Entrega:** devuelve las coincidencias útiles en formato compacto (tag exacta · archivo de origen · caja recomendada · nota mínima).

---

## Reglas de Integridad

- **Canon, no veto:** si una etiqueta no existe, informa de que no hay coincidencia canónica; la consumidora conserva libertad para crear una tag controlada si la intención artística lo justifica.
- **Autoridad delimitada:** evalúa existencia, origen y sintaxis; la viabilidad artística queda en `fusionar`, `style_box`, `lyrics_box` o la consumidora.
- **Extracción pura:** entrega tags existentes; la creación de tags corresponde a las skills creativas.
- **Fidelidad léxica:** conserva las tags exactamente como aparecen en origen.
- **Búsqueda ampliable:** si no hay resultado directo, reintenta con sinónimos antes de declarar ausencia canónica.

---

## Formato de salida

- **Con coincidencias:**
    `[Tag Exacta]` · `chupilista/NN_archivo.md` · caja recomendada · nota mínima de uso
- **Sin coincidencia:**
    Concepto no localizado en la base canónica. La skill consumidora puede crear una tag controlada si la intención artística lo justifica.
- **Con etiqueta mal formada:**
    Incidencia sintáctica localizada: <línea o fragmento>. Revisar corchetes antes de validar como tag.

---

## Relación con otras skills

- `fusionar` propone conceptos, fusiones y creaciones controladas; `buscar_tag` confirma qué es canon.
- `style_box` combina tags canónicas de `buscar_tag` con creaciones controladas de `fusionar`.
- `lyrics_box` usa tags canónicas, comandos libres y dirección musical no presente en `chupilista`.
- `exclude_box` (Fase 5) puede pedir tags canónicas y normalizarlas sin corchetes según su formato.

- *`buscar_tag` entrega materia prima canónica fiable; la consumidora decide cómo integrarla.*
