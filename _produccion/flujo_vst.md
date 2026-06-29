# Flujo de producción en Audacity (para temas de Suno)

> **Patrón para aplicar CUALQUIER efecto de esta guía** (memorízalo, se repite siempre):
>
> 1. Haz **clic en la pista** para seleccionarla.
> 2. Abre el menú **Efectos** y elige el plugin por su nombre.
> 3. Ajusta **solo** las perillas que te indico aquí. Lo demás, no lo toques.
> 4. Pulsa **Aplicar**. (Antes puedes pulsar **Reproducir** dentro del efecto para escuchar cómo queda.)
>
> Trabajas con dos pistas: la **pista de voz** (arriba) y la **pista instrumental** (abajo).

---

## Fase 1 — Pista de voz

Selecciona la **pista de voz**. Aplica los efectos **en este orden** (limpiar → brillo → quitar eses).

### TDR Nova — limpieza  *(OPCIONAL — puedes saltarte este paso al principio)*

Es el mismo plugin que usas en el instrumental, pero con otros ajustes. Aquí **NO actives Threshold** en ninguna banda (son cortes fijos, no dinámicos).

- **HPF (filtro paso alto):** actívalo en **85 Hz**, pendiente **12 dB\oct**. Quita el retumbe y los "pops" de la voz.
- **Una banda → 300 Hz:** baja la ganancia **−3 dB** (deja la Q como viene). Quita el sonido "a caja \ enlatado".
- **Aplicar.**

> Salta este paso si la voz ya suena limpia. Úsalo si notas la voz "embotada", con retumbe o metida en una caja.

### Fresh Air — añade brillo

- **Mid Air:** 10 – 15
- **High Air:** 15 – 20
- **Trim:** −1.0 a −2.0 (bájalo solo lo justo para que no suba el volumen general).
- **Aplicar.**

### Techivation T-De-Esser — quita el exceso de "S"

- **Frequency:** High
- **Intensity \ Threshold:** súbelo hasta que el medidor de reducción marque entre **−3 y −6 dB**, y **solo** cuando suene una "s" o "ch".
- **Sharpness:** 50%
- **Aplicar.**

> **Por qué este orden:** Fresh Air realza agudos y reaviva las eses. Por eso el de-esser va **después**, para domarlas al final.

---

## Fase 2 — Pista instrumental

Selecciona la **pista instrumental**. Un solo efecto:

### TDR Nova — limpia graves y asperezas

- **HPF (filtro paso alto):** actívalo en **30 Hz**, pendiente **18 dB\oct**. Quita el retumbe grave que no se oye pero estorba.
- **Banda 1 → 300 Hz:** activa **Threshold** y ajústala para que baje **−2 dB** cuando los graves suenen embarrados.
- **Banda 4 → 5000 Hz (5 kHz):** activa **Threshold** y ajústala para bajar **−2 a −3 dB** cuando los platillos o los sintes suenen ásperos.
- **Aplicar.**

---

## Fase 3 — Unir las dos pistas en una sola

**Primero, evita que sature.** Reproduce la canción entera y mira el **medidor grande de arriba**: si se pone **rojo (0 dB)**, baja un poco el volumen de las pistas con el **deslizador de ganancia** (el control `– … +` a la izquierda de cada pista) hasta que ya no toque el rojo.

**Cuando ya no toque rojo, une las pistas:**

> **Pistas → Mezclar → Mezclar y generar.**

Esto funde voz e instrumental en **una sola pista**. A partir de aquí, **todos los ajustes los haces sobre esa pista única**.

---

## Fase 4 — Máster (sobre la pista única)

Selecciona la **pista única**. Aplica estos efectos en orden:

### TDR Kotelnikov — compresión de "pegamento" (muy suave)

- **Ratio:** 1.5:1 (máximo 2:1)
- **Attack:** 20 – 30 ms
- **Release:** 150 ms (o el modo **Peak Auto**)
- **Threshold:** bájalo poco a poco hasta que el medidor **Gain Reduction** marque como mucho **−1.5 a −2 dB** en las partes más fuertes.
- **Aplicar.**

### Klanghelm IVGI — calidez (disimula lo "digital" de Suno)

- **Drive:** 2 o 3
- Vigila que **Output** no se ponga rojo ni sature.
- **Aplicar.**

### Volumen final — efecto nativo de Audacity

**Efectos → Volumen y compresión → Normalización de sonoridad**

**Modo:** LUFS (sonoridad percibida)

**Objetivo:** **−14 LUFS**

**Aplicar.**

**Qué hace este paso:** deja tu canción al mismo volumen que las demás en Spotify\YouTube, sin pasarse. Si la quieres con más pegada, prueba **−12 LUFS**; más fuerte que eso empieza a apretar de más.

---

## Fase 5 — Exportar

Antes de exportar, comprueba abajo a la izquierda que la **Frecuencia de proyecto** sea **44100 Hz**.

### Exportar en WAV (calidad máxima, para guardar el original)

**Archivo → Exportar audio → ...** y elige **WAV**.
**Formato:** WAV (Microsoft)
**Codificación:** **PCM de 16 bits con signo**
**Frecuencia:** 44100 Hz
**Canales:** Estéreo

### Exportar en MP3 (para compartir \ subir)

**Archivo → Exportar audio → ...** y elige **MP3**.
**Modo de tasa de bits:** **Constante**
**Calidad:** **320 kbps** (el máximo)
**Canales:** Estéreo (o "Joint Stereo")

> WAV pesa mucho pero no pierde nada: guárdalo como copia maestra. MP3 a 320 kbps pesa poco y suena casi igual: úsalo para enviar o subir.

---

## Configuración útil de Audacity (ajústala una vez)

Cosas que conviene dejar puestas antes de empezar; te ahorran errores.

- **Frecuencia de proyecto a 44100 Hz** — esquina **inferior izquierda**. Que coincida con la exportación.
- **Activar el aviso de saturación:** menú **Ver → Mostrar recortes**. Pinta en **rojo** las zonas que saturan; así las ves de un vistazo sin adivinar.
- **Calidad de trabajo:** **Editar → Preferencias → Calidad → Formato de muestra: 32 bits flotante**. Da margen para que los efectos no saturen mientras trabajas (al exportar en WAV ya bajas a 16 bits).
- **Guarda el proyecto, no solo el audio:** **Archivo → Guardar proyecto** (genera un `.aup3`). Guarda pistas y ajustes para retomar otro día. Exportar (WAV\MP3) es solo el resultado final.

### Atajos que más vas a usar

- **Barra espaciadora** → reproducir \ parar
- **Ctrl + Z** → deshacer (tu mejor amigo)
- **Ctrl + A** → seleccionar toda la pista
- **Inicio \ Fin** → ir al principio \ al final de la canción
- **Ctrl + S** → guardar el proyecto

### Si algo suena mal, mira esto primero

- **¿Satura (rojo)?** Baja el **deslizador de ganancia** de la pista, no subas más efectos.
- **¿Te pasaste con un efecto?** **Ctrl + Z** y vuelve a aplicarlo con valores más suaves.
- **¿Quieres comparar antes\después?** Usa **Reproducir** dentro del efecto antes de pulsar Aplicar.
