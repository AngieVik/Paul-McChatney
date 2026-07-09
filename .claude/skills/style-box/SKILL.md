---
name: style-box
type: skill
description: Ensamblador y compilador sintáctico para estructurar tags canónicas y creaciones controladas en los bloques definitivos de Style Box y Exclude Box.
---

# style-box

## 1 · Propósito

Actúa como el motor de compilación y empaquetado técnico del sistema.

Tu función es tomar el diseño acústico teórico dictaminado por la skill fusionar, orquestar la extracción de etiquetas canónicas mediante buscar-tag, integrar las creaciones controladas necesarias y estructurar la información en bloques limpios, coherentes y listos para la generación musical.

style-box no es un juez creativo absoluto.  
style-box compila, ordena y limpia el molde sonoro.

Su autoridad consiste en:

- ordenar el material musical;
- distinguir tags canónicas de tags creadas;
- mantener coherencia acústica y narrativa;
- construir el style_box;
- construir el exclude_box;
- entregar bloques finales claros y utilizables.

## 2 · Parámetros de Entrada

Reconoce e ingiere los insumos provenientes de las etapas previas del flujo:

- **Dictamen de Fusión:** mapa acústico y teórico generado por fusionar. Incluye géneros, tempos, espectro de frecuencias, instrumentación, textura vocal, atmósfera y dirección sonora.
- **Etiquetas Canónicas:** cadenas de texto literales recuperadas y validadas por buscar-tag desde chupilista/.
- **Creaciones Controladas:** tags, fusiones o formulaciones nuevas propuestas por fusionar cuando la CHUPILISTA no contiene una etiqueta exacta para representar la intención artística.
- **Intención de Obra:** emoción núcleo, idioma de la letra, tono narrativo, energía, época, región o cualquier restricción dada por el usuario.

## 3 · Flujo de Ejecución

- **Recepción del Dictamen:** ingiere la fórmula conceptual de fusionar.
    - Identifica género base, fusión principal, energía, tempo o sensación rítmica, instrumentación protagonista, perfil vocal, atmósfera, riesgos de mezcla y elementos que deben excluirse.

- **Extracción Canónica:** parametriza llamadas precisas a buscar-tag para obtener etiquetas existentes en CHUPILISTA.
    - Usa buscar-tag como fuente de canon, no como límite creativo absoluto.
    - Si buscar-tag no localiza una etiqueta exacta, conserva el hueco conceptual para resolverlo mediante creación controlada si fusionar lo justifica.

- **Integración de Creaciones Controladas:** acepta tags creadas por fusionar cuando cumplan estas condiciones:
    - representan una intención artística clara;
    - no contradicen el dictamen acústico;
    - no duplican una tag canónica suficiente;
    - ayudan a fijar una fusión, textura o identidad sonora que CHUPILISTA no cubre literalmente;
    - están redactadas en inglés técnico, compacto y musicalmente útil.
    - **Ejemplo:** [Andalusian Drumstep], [Symphonic Hardtek], [Rustic Industrial Flamenco], [Baroque Gabber Choir], [Dusty Space Rumba].

- **Ensamblaje Jerárquico del Style Box:** ordena el style_box respetando esta jerarquía:
    - género base o fusión principal;
    - idioma o anclaje cultural si procede;
    - atmósfera;
    - instrumentación protagonista;
    - perfil vocal;
    - ritmo, tempo o groove;
    - producción y textura;
    - ghost tag o detalle diferencial.
    - Prioriza claridad, intención y fuerza sonora.
    - Usa 12-20 tags bien elegidas antes que listas largas y débiles.

- **Generación Inversa del Exclude Box:** deduce, a partir del diseño sonoro, los elementos que ensucian, contradicen o debilitan la mezcla.
    - Puede apoyarse en buscar-tag y en composicion/exclude_box.md.
    - El exclude_box debe bloquear géneros no deseados, clichés, timbres incompatibles, errores de mezcla, artefactos digitales, registros vocales opuestos, exceso de brillo, barro, clipping o compresión.
    - Normaliza el formato final según el estándar del proyecto.

- **Compilación Final:** presenta el resultado en bloques limpios, listos para copiar.
    - El style_box debe ser compacto, técnico y musical.
    - El exclude_box debe ser una línea precisa de negativos separados por comas.

## 4 · Reglas de Integridad

- **Canon como ancla:** usa buscar-tag para recuperar vocabulario existente y fiable.
- **Creación controlada permitida:** acepta tags creadas por fusionar cuando cubran una intención artística no representada literalmente en CHUPILISTA.
- **Sin invención decorativa:** toda tag creada debe tener función sonora, narrativa o técnica.
- **Diferenciación interna:** reconoce mentalmente qué tags vienen de CHUPILISTA y cuáles son creación controlada, aunque el bloque final pueda integrarlas de forma natural.
- **Estilo, no artista:** describe el sonido. No uses nombres propios de artistas reales dentro del style_box.
- **Orden ponderado:** coloca al principio lo que más debe dominar el resultado.
- **Menos y mejor:** elimina tags redundantes, flojas o decorativas.
- **Coherencia acústica:** evita mezclar elementos que saturen la misma zona frecuencial sin una razón clara.
- **Precisión negativa:** el exclude_box debe proteger la mezcla, no convertirse en una papelera genérica.
- **Prompteo positivo:** formula instrucciones como acciones útiles. Prioriza lo que la obra debe hacer, sonar y provocar.

## 5 · Salida Estándar

- **Cuando entregue solo style_box y exclude_box:**
    style_box
    [Tag principal], [Tag secundaria], [Instrumento clave], [Perfil vocal], [Ritmo], [Textura], [Producción], [Ghost tag]
    exclude_box
    negative prompt, unwanted genre, muddy mix, clipping, wrong vocal register, generic edm, weak drums, poor separation

- **Cuando use creaciones controladas:**
    style_box
    [Tag canónica], [Creación Controlada], [Tag canónica], [Creación Controlada], [Producción], [Ghost tag]
    Nota interna: las creaciones controladas proceden del dictamen de fusionar y se usan para cubrir huecos no localizados en CHUPILISTA.

- **Cuando no haya canon suficiente:**
    No hay canon suficiente para cubrir todo el concepto.
    Se usan tags canónicas disponibles y creaciones controladas justificadas por fusionar.

## 6 · Relación con Otras Skills

- fusionar diseña la arquitectura sonora y puede proponer creaciones controladas.
- buscar-tag extrae etiquetas canónicas existentes en CHUPILISTA.
- style-box compila canon y creación controlada en un molde sonoro coherente.
- lyrics-box desarrolla estructura, dirección musical, comandos libres e interpretación.
- exclude_box aporta reglas técnicas para limpiar y proteger la mezcla.

style-box no bloquea la creatividad.  
style-box la ordena, la comprime y la convierte en sintaxis útil.
