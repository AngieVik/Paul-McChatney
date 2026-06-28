# Auditoría de estructura — Paul McChatney

> Todos los hallazgos han sido solucionados.
> Fecha: 2026-06-27 · Alcance: capa de configuración (`.claude/`, `system_prompt/`, `rules/`, índices `PROYECTOS.md` / `folder-structure.md`). No se auditó el contenido lírico de los ~76 proyectos.
> Severidad: 🔴 crítico (rompe carga/links) · 🟠 alto (desinformación operativa) · 🟡 medio/pulido.

---

## 🔴 CRÍTICO

### 1. CLAUDE.md carga el monolito congelado en vez de la fuente de verdad

- **`.claude/CLAUDE.md:5`** → `@system_prompt/00_system_prompt_BUILD.md`
- El propio BUILD lo desaconseja: **`system_prompt/00_system_prompt_BUILD.md:1-6`** dice *"Archivo GENERADO. No editar a mano… Dentro de Claude Code/Cowork se usa `00_system_prompt.md` (puro @import)."*
- **Consecuencia:** cualquier edición a los módulos `01–12` NO llega a Claude hasta regenerar BUILD a mano. Hoy editas el módulo y el sistema sigue leyendo la copia vieja. Source-of-truth roto.
- **Fix:** cambiar la línea 5 a `@system_prompt/00_system_prompt.md`. Reservar el BUILD solo para copiar-pegar fuera (Suno/ChatGPT).

### 2. Import roto por espacio

- **`.claude/CLAUDE.md:13`** → `- Proyectos completados: @ proyectos/`
- El espacio tras `@` invalida el import; además la carpeta es `proyectos/` (sin espacio inicial).
- Mismo patrón cosmético en **`.claude/rules/rules.md:32`** (`└──  proyectos/`) y **`.claude/MEMORY.md:13`**.

### 3. Skills fuera de la carpeta que Claude descubre

- Las 9 skills están en **`.claude/<skill>/SKILL.md`** (`auditoria`, `buscar-tag`, `cover-art`, `fonetizar`, `fusionar`, `lirica`, `produccion`, `proyecto`, `style-box`).
- La convención de Claude Code/Cowork es **`.claude/skills/<skill>/SKILL.md`**. Tal como están, lo más probable es que **no se carguen como skills**.
- **Fix:** mover todas a `.claude/skills/`. Verificar después que aparecen en el listado de skills.

### 4. PROYECTOS.md — los 76 enlaces están rotos (triple fallo)

- **Espacio inicial en la URL:** `(proyectos/60_granos.md)` en **`PROYECTOS.md:12`** (y todas las filas).
- **Ruta plana vs. anidada:** el archivo real es `proyectos/60_granos/60_granos.md`, no `proyectos/60_granos.md`. Todos los proyectos viven en subcarpeta.
- **Slugs que no coinciden** con la carpeta real, p. ej.:
  - `PROYECTOS.md:77` `la_marcha_de_los_rebeldes.md` → real `arre_borriquito_la_marcha_de_los_rebeldes_villancico/`
  - `PROYECTOS.md:17` `frutilla_lunar.md` → real `frutilla_lunar_merengue_hardcore_v1/`
  - `PROYECTOS.md:63` `exploding_ice_cream.md` → real `bakuhatsu_ice_cream_exploding_ice_cream/`
  - `PROYECTOS.md:54` `nina_de_salitre.md` → real `la_nina_de_salitre/`
  - (afecta a la mayoría de filas)
- **Enlace partido en dos líneas → markdown roto:** **`PROYECTOS.md:120-121`** (`…no_me_creyeron` ⏎ `.md`).
- **Fix:** regenerar el catálogo con un pequeño script que recorra `proyectos/*/` y construya `proyectos/<slug>/<slug>.md`.

---

## 🟠 ALTO — desinformación operativa

### 5. Las Fases apuntan a documentos que ya no existen (paradigma ChatGPT)

- **`system_prompt/02_fuentes_de_conocimiento.md:8-10`** y su gemelo en **`system_prompt/00_system_prompt_BUILD.md:26-28, 238, 275, 282`** mencionan:
  - *"hoja de cálculo CHUPILISTA"* → hoy son 15 archivos `.md`, no una hoja de cálculo.
  - *"Documentos adjuntos Paul-TeoriaMusical"* → **no existe** ningún archivo con ese nombre (el conocimiento está en `conocimientos/`).
  - *"Documentos adjuntos Paul-Suno"* → **no existe** (la auditoría es ahora la skill `auditoria`).
  - *"herramienta de lectura de archivos adjuntos"* → terminología del entorno antiguo.
- **Consecuencia:** en Fase 1/3/4 Paul busca recursos inexistentes con esos nombres.
- **Fix:** remapear a rutas reales: `@chupilista/`, `@conocimientos/` (TeoríaMusical/métrica/efectos), skill/`auditoria` (Paul-Suno).

### 6. folder-structure.md totalmente obsoleto

- **`folder-structure.md:100`** "Total Files: 75" — reales: ~476 (≈200 `.md`).
- **`folder-structure.md:23`** lista `Mozart.md` y **`:28`** `plantilla_proyecto.md` dentro de `_hojas_sucias/` — `Mozart.md` no existe; `plantilla_proyecto.md` está en `chuletas/`.
- Faltan en `_hojas_sucias/`: `clasificacion_proyectos.md`, `sliders.md`, `taxonomia_integral_de_la_musica_rave_2025.md` (sí existen).
- **`folder-structure.md:5`** lista `_docs/` — no existe (está en `.gitignore`).
- **`folder-structure.md:69`** `fonetizaciones/plantilla.md` — el archivo real es `chuletas/plantilla_fonetizaciones.md`.
- No lista `chuletas/`, las skills de `.claude/`, ni `_temp/extraer_metadata/`.
- **`folder-structure.md:107-184`** la sección "Ignored Files" usa slugs que no concuerdan con las carpetas reales.
- **Fix:** regenerar automáticamente o borrar (es un artefacto generado que envejece mal).

### 7. rules/fonetizaciones.md — enlace roto, tabla malformada y conteo desfasado

- **`.claude/rules/fonetizaciones.md:32`** enlaza `../../fonetizaciones/plantilla_fonetizaciones.md` → ese archivo está en `chuletas/`, no en `fonetizaciones/`. **Link roto.**
- **`:3`** y **`:17`** (en rules.md) dicen "13 idiomas/dialectos", pero la tabla lista **20** entradas (se añadieron `calo`, `ebrio`, `edad_avanzada`, `hombre_gay`, `infancia_temprana`, `pueblo_peninsular`, `rural_profundo`).
- **`:33-40`** filas sin las columnas Idioma/Notas → tabla markdown malformada.
- **`:28` y `:38`** `italiano.md` aparece **duplicado**.

### 8. PROYECTOS.md desactualizado de conteo

- **`PROYECTOS.md:161`** "74 proyectos · última actualización 2026-06-20". Hay **76** carpetas de proyecto y faltan entradas en el catálogo (p. ej. `jindama_de_plomo`, `la_via_del_oxido`, `la_tregua_que_no_firmamos`, `miopia_balistica`, `poyekhali_el_guaguanco_de_la_vostok`, `rito_da_fraga`, `la_letra_pequena_v2`).

### 9. Skill `proyecto` apunta a una carpeta inexistente

- **`.claude/proyecto/SKILL.md:2`** describe gestionar ideas en `proyectos_e_ideas/` — esa carpeta no existe.
- **`.claude/MEMORY.md:12`** dice que las ideas viven en `_hojas_sucias/`. **Conflicto de ruta** entre la skill y la memoria.

### 10. rules/*.md se anuncian como auto-cargadas pero CLAUDE.md no las importa

- **`.claude/rules/rules.md:3`** (frontmatter) afirma *"Cargado automáticamente por CLAUDE.md"*, pero **`CLAUDE.md`** solo importa `00_system_prompt_BUILD.md` y `MEMORY.md`. Bajo resolución `@import` pura, las `rules/` quedan huérfanas (solo se cargan si Cowork las incluye por convención de directorio). Verificar y, si procede, añadir el import o corregir la afirmación.

---

## 🟡 MEDIO / pulido

### 11. rules/conocimientos.md — etiqueta copy-paste

- **`.claude/rules/conocimientos.md:17`** la fila de `changelog_conocimientos.md` está descrita como **"Retrospectiva"** (heredado de la fila de arriba); debería decir "Changelog". Además el texto del enlace es `conocimientos.md` cuando apunta a `changelog_conocimientos.md`.

### 12. rules/chupilista.md — textos de enlace que no casan con el target (cosmético)

- **`.claude/rules/chupilista.md:15`** texto `01_genres_subgenres.md` vs target real `01_core_genres_and_subgenres.md`.
- **`:20`** texto `06_song structure & sections.md` (con espacios y `&`) vs target `06_song_structure_and_sections.md`. Los targets resuelven; solo desentona el texto visible.

### 13. Typos / detalles de redacción

- **`.claude/MEMORY.md:84`** "en orde temporal" → "orden".
- **`system_prompt/12_flujo_de_trabajo_creacion.md:5`** "5 FASES" es correcto (0–4 = 5) pero conviene aclarar la numeración 0-based para evitar lecturas de "faltan fases".

### 14. .gitignore — verificar intención sobre carátulas

- **`.gitignore:15`** `*.png` + **`:20-23`** `proyectos/**` con whitelist solo de `*.md`: las carátulas (`cover_art.png`, `*_adjunt.jpg`) que generan `folder-structure`/skill `cover-art` **nunca se versionan**. Coherente con "el repo solo versiona texto", pero confírmalo si esperabas conservar las portadas en git.

---

## Resumen de prioridades

1. **CLAUDE.md:5** → cargar `00_system_prompt.md` (no el BUILD). *Mayor impacto, 1 línea.*
2. **CLAUDE.md:13** → quitar el espacio de `@ proyectos/`.
3. **Mover `.claude/<skill>/` → `.claude/skills/<skill>/`.**
4. **Regenerar `PROYECTOS.md`** (rutas anidadas + slugs reales) con script.
5. **Reescribir `02_fuentes_de_conocimiento.md`** para apuntar a `chupilista/`, `conocimientos/` y skill `auditoria` en vez de "Paul-Suno/Paul-TeoriaMusical/hoja de cálculo".
6. **Regenerar o eliminar `folder-structure.md`.**
7. Corregir `rules/fonetizaciones.md` (link plantilla, conteo 20, duplicado italiano, tabla).
8. Alinear skill `proyecto` (`proyectos_e_ideas/` → `_hojas_sucias/`).
