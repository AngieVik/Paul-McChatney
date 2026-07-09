---
name: style-box
type: skill
description: Ensamblador y compilador sintáctico para estructurar las etiquetas recuperadas en los bloques definitivos de Style Box y Exclude Box.
---

# style-box

## 1 · Propósito

Actúa como el motor de compilación y empaquetado técnico del sistema. Tu función es tomar el diseño acústico teórico dictaminado por la skill `fusionar`, orquestar la extracción de datos literales mediante `buscar-tag`, y estructurar la información en bloques de código con formato estricto, listos para la generación musical.

## 2 · Parámetros de Entrada

Reconoce e ingiere los insumos provenientes de las etapas previas del flujo:

- **Dictamen de Fusión:** El mapa acústico y teórico generado por la skill `fusionar` (géneros, tempos, espectro de frecuencias).
- **Etiquetas Crudas:** Las cadenas de texto literales (tags) recuperadas y validadas por la skill `buscar-tag` desde los directorios canónicos.

## 3 · Flujo de Ejecución

1. **Recepción y Orquestación:** Ingiere la fórmula conceptual de `fusionar` y parametriza llamadas precisas a `buscar-tag` para obtener los corchetes exactos necesarios para representar dicha fórmula.
2. **Ensamblaje Jerárquico (Style Box):** Ordena las etiquetas recuperadas respetando la jerarquía algorítmica de la composición (Género Base, Atmósfera, Instrumentación, Perfil Vocal, Ritmo/Estructura, Efectos de Producción).
3. **Generación Inversa (Exclude Box):** Deduce, a partir del diseño sonoro, los elementos acústicos, frecuencias, subgéneros o timbres vocales que chocarían o ensuciarían la mezcla. Formula un bloque de exclusión (*negative prompt*) parametrizando nuevamente a `buscar-tag` en los módulos de exclusión.
4. **Compilación Final:** Presenta el resultado como bloques de texto preformateado (código Markdown), asegurando que la sintaxis sea impecable y esté lista para el motor de audio.

## 4 · Lista de Control y Reglas de Integridad

- **Linter de Compilación:** Asegura que todas las etiquetas integradas en los bloques finales cuenten con su apertura y cierre de corchetes intactos. Separa los tags mediante comas y espacios uniformes.
- **Cero Improvisación:** Construye el bloque final utilizando estrictamente las etiquetas suministradas por `buscar-tag`. Omite la creación, alteración o inyección de tags no verificados en la base de datos canónica.
- **Precisión Negativa:** Garantiza que el Exclude Box contenga directrices técnicas precisas y enfocadas en la limpieza de la mezcla frecuencial (ej. bloqueando bombos saturados si la fusión requiere precisión sinfónica).
