---
name: fusionar
type: skill
description: Motor conceptual de arquitectura sonora. Analiza el concepto creativo y diseña una mezcla armónica, rítmica y frecuencial viable para que style_box la compile. Activable en producción (Fase 1) o en modo conversacional.
---

# fusionar

- *Diseña la arquitectura sonora de la obra: traduce el concepto creativo en una estructura musical teóricamente viable y entrega un dictamen para `style_box`.*

---

## Activación

- **En producción:** primer paso de Fase 1 de `produccion`; su dictamen alimenta a `style_box`.
- **En modo conversacional:** se activa de forma independiente y en cualquier momento cuando el usuario pide diseñar, revisar o depurar una fusión o arquitectura sonora.

---

## Fuentes de Consulta

- *La técnica de fusión, frecuencias, dinámica y colisión tímbrica vive en el archivo técnico del `style_box`; consúltalo antes de dictaminar.*
    - **Mapa:** `.claude/rules/style_box.md`
    - **Archivo técnico:** `composicion/style_box.md` (§2 Fusión y frecuencias, §3 Dinámicas rítmicas y estructurales, §4 Colisión tímbrica)
- *Para verificar si un ingrediente ya es canon, invoca `buscar_tag`.*

---

## Parámetros de Entrada

- **Concepto Creativo:** idea abstracta, emoción, narrativa o directriz de género que rige la obra en gestación.
- **Restricciones del Usuario:** idioma, época, región, energía o límites dados.

---

## Flujo de Ejecución

- **Análisis estructural:** evalúa el concepto e identifica las necesidades acústicas subyacentes (peso en graves, brillo en agudos, velocidad rítmica, atmósfera).
- **Diseño frecuencial y rítmico:** determina los rangos de BPM viables y cómo deben interactuar los instrumentos para mantener claridad, apoyándote en §2–§4 de `composicion/style_box.md` (p. ej. bajos sintéticos profundos contra percusiones orgánicas de ataque rápido).
- **Formulación conceptual:** construye el dictamen con los ingredientes exactos: género base, subgéneros de apoyo, instrumentación protagonista, diseño de sonido y texturas vocales.
- **Puente de contrastes:** si el concepto exige opuestos extremos (p. ej. clásico + hardtek), diseña el puente conceptual que justifique la integración sin saturar la mezcla.
- **Delegar:** entrega la fórmula estructurada para que `style_box` tome el relevo, invoque `buscar_tag` y ensamble la sintaxis final.

---

## Reglas de Integridad

- **Viabilidad acústica:** toda mezcla propuesta debe ser armónica y rítmicamente coherente.
- **Foco teórico:** mantén el dictamen centrado en teoría musical, producción acústica y psicoacústica.
- **Aislamiento de funciones:** diseña; delega la búsqueda literal de tags en `buscar_tag` y el ensamblaje del bloque final en `style_box`.

---

## Relación con otras skills

- `produccion` activa `fusionar` al inicio de Fase 1.
- `buscar_tag` valida qué ingredientes del dictamen existen como canon en `CHUPILISTA`.
- `style_box` compila el dictamen en el bloque final; `fusionar` no ensambla sintaxis.
