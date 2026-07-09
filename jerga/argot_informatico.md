---
name: argot_informatico
type: jerga
description: Argot técnico transversal utilizado por programadores, ingenieros de software, arquitectos de sistemas y perfiles de QA. Es un "tecnolecto" globalizado, forjado en foros (StackOverflow), repositorios (GitHub) y metodologías ágiles. Su propósito es describir conceptos lógicos abstractos con absoluta precisión, aunque frecuentemente deriva en un escudo lingüístico para justificar retrasos, errores o deuda técnica ante perfiles no técnicos (los "muggles" o "clientes").
region: Argot Informático y Desarrollo de Software (Devs)
---

# argot_informatico 

## Perfil Lexical General

Una introducción al "carácter" del vocabulario para entender la mentalidad y el entorno del hablante.

- **Descripción:** Pragmático, cínico y altamente estructurado. Basado en la lógica condicional, a menudo aplica conceptos de programación a situaciones cotidianas de la vida real.
- **Influencias Principales:** Dominio absoluto del inglés técnico (Spanglish inevitable), cultura de internet (memes técnicos), jerga de arquitectura de sistemas (frontend, backend, bases de datos) e ingeniería de prompts para modelos de lenguaje.
- **Rasgo Distintivo:** La transformación sistemática de sustantivos técnicos ingleses en verbos de la primera conjugación castellana (-ar / -ear), creando un híbrido que resulta incomprensible fuera del gremio.

## Glosario de Uso Frecuente (El Núcleo Duro)

Mapeo de las palabras clave esenciales para la supervivencia conversacional en este entorno.

| Término / Expresión        | Significado Estándar                                                                                                  | Registro / Tono         | Ejemplo Práctico (En Contexto)                                                                                        |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Pushear**                | Subir los cambios de código local al repositorio remoto (Git)                                                         | Operativo / Neutro      | *Acabo de pushear mis cambios a la rama principal.* → "He subido mi código al servidor."                              |
| **Deployar / Tirar a Pro** | Desplegar la aplicación en el entorno de producción (hacerla pública)                                                 | Crítico / Tensión       | *El viernes a las 5 no se tira a pro.* → "No se publica código nuevo justo antes del fin de semana."                  |
| **Picar (código)**         | Escribir código de forma manual, continuada y a menudo mecánica                                                       | Cotidiano / Descriptivo | *Llevo seis horas picando componentes.* → "Llevo seis horas programando interfaces."                                  |
| **Refactorizar**           | Reescribir y limpiar el código interno sin alterar su comportamiento externo                                          | Técnico / Necesidad     | *Ese archivo es un espagueti, hay que refactorizarlo.* → "El código es un caos ilegible y necesita ser estructurado." |
| **Debugear**               | Buscar, analizar y eliminar errores (bugs) en el código                                                               | Operativo / Frustración | *Me pasé la tarde debugeando el hook de React.* → "Estuve toda la tarde buscando el error en la función."             |
| **Hardcodear**             | Incrustar datos fijos directamente en el código fuente en lugar de obtenerlos de una base de datos o variable externa | Crítico / Mala práctica | *No hardcodees la URL de Supabase, ponla en el .env.* → "No escribas la dirección fija, usa variables de entorno."    |

- **Nota de intensidad:** Las advertencias de desastre suelen medirse por el entorno afectado. Un error en "Local" (el ordenador del desarrollador) es inofensivo; un error en "Dev/Test" es normal; romper "Producción" (Pro) es un evento catastrófico que paraliza a la empresa.

## Muletillas y Marcadores Discursivos

Las palabras vacías o de apoyo que dan fluidez y naturalidad al discurso, aunque carezcan de significado literal.

| Marcador                        | Función Discursiva                                                                                                                              | Equivalencia Estándar                  |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **"En mi máquina sí funciona"** | Excusatio non petita. El mantra universal para evadir la culpa inicial cuando un código falla en el servidor o en el ordenador de un compañero. | "Yo no he sido", "El código está bien" |
| **"Es un feature, no un bug"**  | Ironía clásica. Convertir un error de programación en una supuesta "característica de diseño" planificada.                                      | "No es un error, es intencionado"      |
| **WIP / ASAP**                  | Acrónimos de chat (Work In Progress / As Soon As Possible). Evitan teclear de más en medio del desarrollo.                                      | "En proceso", "Lo antes posible"       |

- **Regla de oro de la muletilla:** "Por debajo" es la expresión comodín para explicar cualquier magia oscura que ocurre en el servidor o en las librerías sin entrar en detalles. Ej. *"Tailwind por debajo inyecta las clases CSS al compilar"*.

## Modificaciones Morfológicas y Gramaticales

Cómo la jerga altera la estructura de las palabras regulares del idioma.

- **Anglicismos Castellanizados Frecuentes:** 
    - *Mockear:* Crear datos falsos de prueba (*mock data*) para simular una interfaz antes de conectar la base de datos real.
    - *Renderizar:* Procesar código para mostrar la interfaz gráfica final al usuario.
    - *Componentizar:* Dividir una interfaz de usuario grande en fragmentos de código pequeños y reutilizables.
    - *Parsear:* Analizar y convertir una cadena de texto (como un JSON) en un objeto manejable por el lenguaje.
- **El uso de siglas como entidades vivas:** Las siglas asumen el rol de sujetos activos en la frase. Ej. "La API se ha caído", "La UI no responde", "El PR (Pull Request) está bloqueado", "El LLM está alucinando".

## "Falsos Amigos" Lexicales y Palabras Tabú

Advertencias críticas sobre términos del español estándar que en esta jerga tienen un significado completamente distinto (y demuestran si alguien es técnico o no).

- **Librería (Library):** 
    - *Significado normal:* Tienda donde se compran libros.
    - *Significado en la jerga:* Biblioteca de código preescrito que los programadores usan para no reinventar la rueda (Ej. React, shadcn/ui).
    - *Nivel de peligro:* Bajo, pero decir "biblioteca" en lugar de "librería" delatará inmediatamente que no eres del sector, a pesar de ser gramaticalmente correcto en español.
- **Promesa (Promise):**
    - *Significado normal:* Ofrecimiento solemne de cumplir algo.
    - *Significado en la jerga:* Un objeto que representa la terminación o el fracaso eventual de una operación asíncrona (como pedir datos a un servidor). 
    - *Nivel de peligro:* Bajo.
- **Prompt:**
    - *Significado normal:* Relativo a la prontitud o rapidez (arcaico/desuso en español general).
    - *Significado en la jerga:* La cadena de texto estructurada, las directrices y el contexto que se inyectan en un modelo de Inteligencia Artificial para condicionar su respuesta ("Prompt Engineering").
    - *Nivel de peligro:* Medio (Confundirlo en entornos modernos de desarrollo denota obsolescencia técnica).

## Casos Prácticos de Aplicación (Diálogo Decodificado)

Disección de frases completas aplicando el vocabulario y las reglas anteriores.

### Frase de Ejemplo 1: Resolviendo un problema de Frontend

- **Original en Jerga:** `El componente no está renderizando bien porque el hook no trae el JSON de Supabase. Por ahora mockea los datos, métele un div con unas clases provisorias de Tailwind y abre el PR, que luego lo refactorizamos.`
    - *Desglose Lexical:* "Componente" es una pieza de la interfaz. "Renderizando" es mostrándose visualmente. "Hook" es una función especial de React. "JSON" es el formato de los datos. "Supabase" es el servicio de base de datos en la nube. "Mockea" indica usar datos falsos. "Div" es un contenedor HTML. "Tailwind" es un framework de estilos CSS. "Abre el PR" significa enviar el código para revisión. "Refactorizamos" promete mejorarlo en el futuro.
    - *Traducción Estándar:* **"La pieza de la interfaz gráfica no se visualiza correctamente porque la función interna no logra descargar los datos del servidor. De momento, utiliza datos inventados de prueba, aplícale unos estilos visuales rápidos y envía la petición de revisión de código, ya lo reescribiremos correctamente más adelante."**

### Frase de Ejemplo 2: Aclaración de Arquitectura y Estructura

- **Original en Jerga:** `He estado pusheando el core de U24Core, pero tened claro algo para la arquitectura: filiación no es, ni ha sido, ni será nunca un módulo principal, así que no lo integréis en el root ni lo hardcodeéis en el navbar de la UI.`
    - *Desglose Lexical:* "Pusheando" es subir el código. "Core" es el núcleo del sistema. "U24Core" es el nombre del proyecto. "Módulo principal" es una pieza clave e independiente de la arquitectura. "Root" es la raíz del proyecto o nivel más alto del directorio. "Hardcodeéis" es escribir la ruta de forma fija y manual. "Navbar" es la barra de navegación. "UI" es la interfaz de usuario.
    - *Traducción Estándar:* **"He estado subiendo al servidor el núcleo de nuestra aplicación médica, pero entended esta regla de diseño estructural: la gestión de datos de pacientes (filiación) es estrictamente secundaria. Por tanto, no la coloquéis en la carpeta raíz del proyecto ni programéis su acceso directo de forma manual en la barra de navegación visual."**
