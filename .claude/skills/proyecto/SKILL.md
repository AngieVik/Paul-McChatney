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

- `crear`: Inicializa el proyecto. Genera el archivo `_hojas_sucias/<slug>.md` (utilizando *snake_case* estricto). Aplica el contenido de `chuletas/plantilla_hoja_sucia.md` como guía estructural flexible. Inicia la recopilación de datos interactuando con el usuario. **Colisión:** si ya existe `_hojas_sucias/<slug>.md`, aborta y pide confirmación antes de sobrescribirlo; nunca lo pisa en silencio.
- `retomar`: Restaura el contexto de un proyecto existente.
    - Desde `_hojas_sucias/`: Lee el borrador actual y expone un resumen de estado para continuar la iteración.
    - Desde `proyectos/<slug>/`: Clona el contenido del proyecto terminado hacia `_hojas_sucias/<slug>.md` y prepara el entorno para su modificación. **Colisión:** si el borrador de destino `_hojas_sucias/<slug>.md` ya existe, aborta y pide confirmación antes de sobrescribirlo.
- `aprobar`: Finaliza la obra satisfactoriamente. Transfiere el contenido depurado a `proyectos/<slug>/<slug>.md` aplicando rigurosamente `chuletas/plantilla_proyecto.md`. Registra la obra en el catálogo `PROYECTOS.md` localizándola por ruta o slug: si ya existe una fila para esa obra, actualiza esa fila en lugar de añadir una nueva (evita duplicados por reaprobación). Al terminar, solo sugiere al usuario si quiere hacer una retrospectiva de cierre; no analiza la obra ni propone aprendizajes automáticamente.

## 3 · Nivel B: Operaciones Mecánicas

Comandos transaccionales que no alteran la narrativa creativa de la obra.

- `guardar`: Ejecuta un volcado de seguridad. Genera un clon exacto del estado actual bajo la nomenclatura `_hojas_sucias/<slug>_NN.md`, donde `NN` es el mayor índice existente más uno (dos dígitos, p. ej. `01`, `02`); nunca sobrescribe una copia previa.
- `listar`: Ejecuta una lectura de directorio. Devuelve el índice de archivos activos en `_hojas_sucias/` o el registro histórico de `PROYECTOS.md` según el parámetro solicitado.
- `cerrar`: Termina la sesión y libera el contexto de la obra.
- `cancelar`: Cancela únicamente la operación actual; la obra sigue activa.
- `eliminar`: Ejecuta el borrado total. **Antes de suprimir nada exige una confirmación destructiva explícita que incluya el `<slug>`** (p. ej. `eliminar <slug>` confirmado); sin esa confirmación no borra el archivo de trabajo, sus copias de seguridad `_NN` ni purga el contexto activo del modelo.

## 4 · Mapa del Almacenamiento

| Capa Lógica                 | Ruta Física                        | Función Estructural                                  |
| --------------------------- | ---------------------------------- | ---------------------------------------------------- |
| Trabajo en curso            | `_hojas_sucias/<slug>.md`          | Borrador dinámico de sobrescritura continua.         |
| Obras aprobadas             | `proyectos/<slug>/<slug>.md`       | Archivo final y canónico de la obra terminada.       |
| Catálogo Global             | `PROYECTOS.md`                     | Índice relacional de todas las obras aprobadas.      |
| Plantilla de inicialización | `chuletas/plantilla_hoja_sucia.md` | Esquema conceptual para la fase de ideación.         |
| Plantilla de consolidación  | `chuletas/plantilla_proyecto.md`   | Esquema canónico para el formateo del archivo final. |

## 5 · Entradas y Salidas

- **Disponibilidad de herramientas:** confirma una operación de archivo solo después de ejecutarla correctamente. Si el entorno no permite escritura, entrega el contenido y la ruta propuesta sin afirmar que fue creado, movido o eliminado.

- **Entrada Estándar:** Un comando de ejecución explícito (`crear`, `aprobar`, `guardar`, etc.) seguido del `<slug>` objetivo.
- **Salida Estándar:** Confirmación de la operación sobre el sistema de archivos y exposición del estado resultante para continuar la interacción.

## 6 · Regla de Contexto Único (Mentalidad Limpia)

- *Fuente canónica del ciclo de vida (`aprobar` · `cerrar` · `retrospectiva`): el resto de archivos (`system_prompt`, `retrospectiva`, `MEMORY.md`) remiten aquí en vez de repetir la política.*
- Trabaja una sola obra a la vez hasta `aprobar`, `cerrar`, o `eliminar`. Mantén un único contexto activo para conservar versiones limpias y evitar cruces entre obras.
- Ninguna fase de `produccion` cierra la obra por sí sola: hasta `aprobar` sigue siendo un borrador vivo y modificable. Solo `aprobar` finaliza la obra y permite ofrecer una retrospectiva de cierre.
- **Canon no estricto:** el formato canónico de una obra aprobada es una guía viva, no un molde rígido. Una obra terminada puede evolucionar (revisarse, ampliarse o remasterizarse) y las obras históricas pueden no cumplir el canon actual (p. ej. `exclude_box` vacío o `style_box` en prosa); no se reformatean salvo que el usuario lo pida.

## 7 · Ciclo de vida: retrospectiva y aprobación

- *Fuente canónica del ciclo de vida de la obra. Otras skills que necesiten estas reglas enlazan aquí en vez de repetirlas.*
- `retrospectiva` puede ejecutarse en cualquier momento del ciclo, incluso antes de `aprobar`, si el usuario detecta un aprendizaje o pide revisar una decisión.
- `aprobar` no ejecuta retrospectiva automáticamente: solo sugiere al usuario hacer una retrospectiva de cierre.
- Aprobar una obra, aprobar un prompt y aprobar un aprendizaje son acciones independientes.
