---
name: proyecto
type: skill
description: Orquestador del ciclo de vida creativo de la obra y gestor de operaciones mecánicas de almacenamiento.
---

# proyecto

## 1 · Propósito

Gestiona la infraestructura de archivos del sistema. Opera en dos niveles estrictos: 

1. **Ciclo de vida:** Orquesta el nacimiento, desarrollo y finalización canónica de una obra musical.
2. **Operaciones mecánicas:** Ejecuta comandos transaccionales de lectura, escritura, copia y eliminación sobre el sistema de archivos.

## 2 · Nivel A: Ciclo de Vida del Proyecto

Comandos que alteran el estado creativo y la ubicación canónica de la obra.

- `crear`: Inicializa el proyecto. Genera el archivo `_hojas_sucias/<slug>.md` (utilizando *snake_case* estricto). Aplica el contenido de `chuletas/plantilla_hoja_sucia.md` como guía estructural flexible. Inicia la recopilación de datos interactuando con el usuario.
- `retomar`: Restaura el contexto de un proyecto existente. 
    - Desde `_hojas_sucias/`: Lee el borrador actual y expone un resumen de estado para continuar la iteración.
    - Desde `proyectos/<slug>/`: Clona el contenido del proyecto terminado hacia `_hojas_sucias/<slug>.md` y prepara el entorno para su modificación.
- `aprobar`: Finaliza la obra satisfactoriamente. Transfiere el contenido depurado a `proyectos/<slug>/<slug>.md` aplicando rigurosamente `chuletas/plantilla_proyecto.md`. Registra la nueva entrada en el catálogo `PROYECTOS.md`. Acto seguido, evalúa la obra e invoca la skill `retrospectiva` si detecta hallazgos técnicos de alto valor.

## 3 · Nivel B: Operaciones Mecánicas

Comandos transaccionales que no alteran la narrativa creativa de la obra.

- `guardar`: Ejecuta un volcado de seguridad. Genera un clon exacto del estado actual bajo la nomenclatura `_hojas_sucias/<slug>_NN.md`.
- `listar`: Ejecuta una lectura de directorio. Devuelve el índice de archivos activos en `_hojas_sucias/` o el registro histórico de `PROYECTOS.md` según el parámetro solicitado.
- `cerrar`: Libera la memoria de trabajo del proyecto en curso y retorna el sistema al Modo Conversacional, manteniendo los archivos intactos.
- `cancelar`: Detiene la ejecución del proceso interactivo actual, manteniendo el proyecto abierto en la ventana de contexto.
- `eliminar`: Ejecuta el borrado total. Suprime el archivo de trabajo, las copias de seguridad asociadas y purga el contexto activo del modelo.

## 4 · Mapa del Almacenamiento

| Capa Lógica                 | Ruta Física                        | Función Estructural                                  |
| --------------------------- | ---------------------------------- | ---------------------------------------------------- |
| Trabajo en curso            | `_hojas_sucias/<slug>.md`          | Borrador dinámico de sobrescritura continua.         |
| Obras aprobadas             | `proyectos/<slug>/<slug>.md`       | Archivo final y canónico de la obra terminada.       |
| Catálogo Global             | `PROYECTOS.md`                     | Índice relacional de todas las obras aprobadas.      |
| Plantilla de inicialización | `chuletas/plantilla_hoja_sucia.md` | Esquema conceptual para la fase de ideación.         |
| Plantilla de consolidación  | `chuletas/plantilla_proyecto.md`   | Esquema canónico para el formateo del archivo final. |

## 5 · Entradas y Salidas

- **Entrada Estándar:** Un comando de ejecución explícito (`crear`, `aprobar`, `guardar`, etc.) seguido del `<slug>` objetivo.
- **Salida Estándar:** Confirmación de la operación sobre el sistema de archivos y exposición del estado resultante para continuar la interacción.
