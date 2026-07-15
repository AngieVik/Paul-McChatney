#!/usr/bin/env python3
"""
test_validar_proyecto.py — Pruebas automáticas del validador.

Sin dependencias externas (no requiere pytest): se ejecuta con
`python test_validar_proyecto.py` desde cualquier sitio y devuelve código de
salida 1 si algún caso falla. Cada prueba construye contenido sintético
(válido e inválido) y comprueba que el validador lo clasifica bien, cubriendo
los puntos que motivaron la ampliación: lectura de name/type sin comillas, H1
único, nombres sueltos y ambiguos entre backticks, indexación única por mapa,
tags de chupilista y longitud de description. Así cada ampliación futura del
validador no reintroduce falsos positivos ni puntos ciegos.
"""

import importlib.util
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("validar_proyecto", HERE / "validar_proyecto.py")
V = importlib.util.module_from_spec(spec)
spec.loader.exec_module(V)

FAILURES = []


def check(cond, msg):
    if cond:
        print(f"  ok  {msg}")
    else:
        print(f"FAIL  {msg}")
        FAILURES.append(msg)


def problems_for(fn, text, name="x.md", root=None, **kw):
    probs = []
    root = root or Path("/tmp")
    fn(root / name, text, root, probs, **kw)
    return probs


def has(probs, needle):
    return any(needle in p for p in probs)


# ---------- name/type sin comillas (Hallazgo 1) ----------

def test_frontmatter_value_strips_quotes():
    t = '---\nname: "style_box"\ntype: \'map\'\ndescription: "d"\n---\n\n# style_box\n'
    check(V.frontmatter_value(t, "name") == "style_box", "name entrecomillado se lee sin comillas")
    check(V.frontmatter_value(t, "type") == "map", "type entrecomillado (simples) se lee sin comillas")


def test_plantilla_type_quoted_ok():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "chuletas").mkdir()
        f = root / "chuletas" / "plantilla_x.md"
        f.write_text('---\nname: plantilla_x\ntype: "plantilla"\ndescription: "d"\n---\n\n# plantilla_x\n', encoding="utf-8")
        probs = []
        V.check_plantilla_type(f, f.read_text(encoding="utf-8"), root, probs)
        check(not probs, 'type: "plantilla" (entrecomillado) NO se marca como incorrecto')


def test_plantilla_type_wrong():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "chuletas").mkdir()
        f = root / "chuletas" / "plantilla_x.md"
        f.write_text('---\nname: plantilla_x\ntype: skill\ndescription: "d"\n---\n\n# plantilla_x\n', encoding="utf-8")
        probs = []
        V.check_plantilla_type(f, f.read_text(encoding="utf-8"), root, probs)
        check(has(probs, "type incorrecto"), "type distinto de plantilla se marca")


# ---------- Identidad: exactamente un H1 (Hallazgo 2) ----------

def test_identity_two_h1():
    t = '---\nname: x\ntype: skill\ndescription: "d"\n---\n\n# x\n\n# otro\n'
    p = problems_for(V.check_document_identity, t, name="x.md")
    check(has(p, "H1 múltiple o ausente"), "dos H1 en un documento con identidad se detecta")


def test_identity_zero_h1():
    t = '---\nname: x\ntype: skill\ndescription: "d"\n---\n\nsin encabezado.\n'
    p = problems_for(V.check_document_identity, t, name="x.md")
    check(has(p, "H1 múltiple o ausente"), "cero H1 en un documento con identidad se detecta")


def test_identity_single_h1_ok():
    t = '---\nname: x\ntype: skill\ndescription: "d"\n---\n\n# x\n\n## sub\n'
    p = problems_for(V.check_document_identity, t, name="x.md")
    check(not p, "exactamente un H1 que coincide con name no genera aviso")


# ---------- Nombres sueltos entre backticks (Hallazgo 3) ----------

def test_backtick_bare_missing():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        f = root / "a.md"
        f.write_text("cita a `nope.md` que no existe.\n", encoding="utf-8")
        probs = []
        V.check_backtick_paths(f, f.read_text(encoding="utf-8"), root, probs)
        check(has(probs, "nombre suelto inexistente"), "nombre suelto que no se resuelve se detecta")


def test_backtick_bare_ambiguous():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "sub").mkdir()
        (root / "dup.md").write_text("x", encoding="utf-8")
        (root / "sub" / "dup.md").write_text("x", encoding="utf-8")
        f = root / "sub" / "a.md"
        f.write_text("cita a `dup.md` sin ruta.\n", encoding="utf-8")
        probs = []
        V.check_backtick_paths(f, f.read_text(encoding="utf-8"), root, probs)
        check(has(probs, "ruta ambigua"), "nombre suelto en carpeta y raíz se marca ambiguo")


def test_backtick_bare_label_skipped():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "jerga").mkdir()
        (root / "jerga" / "calo.md").write_text("x", encoding="utf-8")
        f = root / "map.md"
        # la ruta completa aparece en el mismo archivo: el nombre suelto es etiqueta
        f.write_text("índice `jerga/calo.md` etiqueta `calo.md`.\n", encoding="utf-8")
        probs = []
        V.check_backtick_paths(f, f.read_text(encoding="utf-8"), root, probs)
        check(not probs, "nombre suelto con su ruta completa en el mismo archivo NO se marca")


def test_backtick_canonical_ok():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / ".claude").mkdir()
        (root / ".claude" / "MEMORY.md").write_text("x", encoding="utf-8")
        f = root / "a.md"
        f.write_text("ver `MEMORY.md`.\n", encoding="utf-8")
        probs = []
        V.check_backtick_paths(f, f.read_text(encoding="utf-8"), root, probs)
        check(not probs, "nombre canónico suelto (MEMORY.md) que existe en el repo NO se marca")


# ---------- Longitud de description (Hallazgo descriptions) ----------

def test_description_length():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "composicion").mkdir()
        f = root / "composicion" / "foo.md"
        longd = "a" * 260
        f.write_text(f'---\nname: foo\ntype: composicion\ndescription: "{longd}"\n---\n\n# foo\n', encoding="utf-8")
        probs = []
        V.check_description_length(f, f.read_text(encoding="utf-8"), root, probs)
        check(has(probs, "description larga"), "description de 260 caracteres se detecta")


def test_description_length_ok():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "composicion").mkdir()
        f = root / "composicion" / "foo.md"
        f.write_text('---\nname: foo\ntype: composicion\ndescription: "corta y clara."\n---\n\n# foo\n', encoding="utf-8")
        probs = []
        V.check_description_length(f, f.read_text(encoding="utf-8"), root, probs)
        check(not probs, "description corta no genera aviso")


# ---------- Indexación única por mapa (Mejora) ----------

def test_library_indexing_orphan_and_dup():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "jerga").mkdir()
        (root / ".claude" / "rules").mkdir(parents=True)
        (root / "jerga" / "a.md").write_text("x", encoding="utf-8")
        (root / "jerga" / "b.md").write_text("x", encoding="utf-8")
        # el mapa referencia a.md dos veces (duplicado) y omite b.md (huérfano)
        (root / ".claude" / "rules" / "jerga.md").write_text(
            "índice\njerga/a.md\njerga/a.md\n", encoding="utf-8")
        probs = []
        V.check_library_indexing(root, probs)
        check(has(probs, "archivo sin indexar") and "jerga/b.md" in " ".join(probs),
              "archivo de biblioteca no indexado (huérfano) se detecta")
        check(has(probs, "archivo indexado por duplicado"),
              "archivo de biblioteca indexado dos veces se detecta")


def test_library_indexing_clean():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "jerga").mkdir()
        (root / ".claude" / "rules").mkdir(parents=True)
        (root / "jerga" / "a.md").write_text("x", encoding="utf-8")
        (root / ".claude" / "rules" / "jerga.md").write_text("índice jerga/a.md\n", encoding="utf-8")
        probs = []
        V.check_library_indexing(root, probs)
        check(not probs, "cada archivo indexado exactamente una vez no genera aviso")


# ---------- Tags de chupilista (Mejora) ----------

def _chup(text):
    root = Path("/tmp")
    probs = []
    warns = []
    V.check_chupilista_tags(root / "chupilista" / "m.md", text, root, probs, warns)
    return probs, warns


def test_chupilista_malformed():
    probs, warns = _chup("[Bien]\n[Mal\n")
    check(has(probs, "tag mal formada"), "tag con corchete sin cerrar se detecta (error)")


def test_chupilista_exact_duplicate():
    probs, warns = _chup("[Uno]\n[Dos]\n[Uno]\n")
    check(has(probs, "tag duplicada"), "tag duplicada exacta en el archivo se detecta (error)")


def test_chupilista_near_duplicate_is_warning():
    probs, warns = _chup("[Neo Soul]\n[Neo-soul]\n")
    check(not has(probs, "posible duplicado") and has(warns, "posible duplicado"),
          "casi-duplicado (guion/mayúsculas) es ADVERTENCIA, no error")


def test_chupilista_clean():
    probs, warns = _chup("[Alpha]\n[Beta]\n[Gamma Delta]\n")
    check(not probs and not warns, "lista de tags limpia no genera avisos")


# ---------- YAML ----------

def test_yaml_valid():
    t = '---\nname: x\ntype: skill\ndescription: "Foo: con dos puntos, pero entrecomillado."\n---\n\n# x\n'
    p = problems_for(V.check_yaml_frontmatter_shape, t)
    check(not p, "YAML válido (descripción con ':' entrecomillada) no genera avisos")


def test_yaml_unquoted_colon():
    t = '---\nname: x\ntype: skill\ndescription: Foo: bar sin comillas\n---\n'
    p = problems_for(V.check_yaml_frontmatter_shape, t)
    check(has(p, "YAML"), "valor sin comillas con ':' se detecta")


def test_yaml_missing_space():
    t = '---\nname:x\ntype: skill\ndescription: ok\n---\n'
    p = problems_for(V.check_yaml_frontmatter_shape, t)
    check(has(p, "falta un espacio"), "clave:valor sin espacio se detecta")


def test_yaml_punct_after_quote():
    t = '---\nname: x\ntype: skill\ndescription: "Foo".\n---\n'
    p = problems_for(V.check_yaml_frontmatter_shape, t)
    check(has(p, "fuera de las comillas"), "puntuación tras la comilla de cierre se detecta")


def test_yaml_unclosed_quote():
    t = '---\nname: x\ntype: skill\ndescription: "Foo sin cerrar\n---\n'
    p = problems_for(V.check_yaml_frontmatter_shape, t)
    check(has(p, "sin cerrar"), "comilla sin cerrar se detecta")


# ---------- Control chars / NUL ----------

def test_control_nul():
    t = "# x\n\ncontenido\x00con nulo\n"
    p = problems_for(V.check_control_chars, t)
    check(has(p, "byte de control"), "byte NUL (\\x00) se detecta")


def test_control_clean():
    t = "# x\n\nlínea con tab\ty salto\n"
    p = problems_for(V.check_control_chars, t)
    check(not p, "tab/salto de línea NO se marcan como control")


# ---------- Fences 0 / 3 / 4 espacios ----------

def test_fence_0_closed():
    t = "# x\n\n```text\nhola\n```\n"
    p = problems_for(V.check_unclosed_fences, t)
    check(not p, "fence 0 espacios bien cerrado no genera aviso")


def test_fence_0_unclosed():
    t = "# x\n\n```text\nhola\n"
    p = problems_for(V.check_unclosed_fences, t)
    check(has(p, "fence sin cerrar"), "fence 0 espacios sin cerrar se detecta")


def test_fence_3_closed():
    t = "# x\n\n   ```text\n   hola\n   ```\n"
    p = problems_for(V.check_unclosed_fences, t)
    check(not p, "fence con 3 espacios de sangría cuenta como fence válido")


def test_fence_4_not_a_fence():
    t = "# x\n\n```text\nreal sin cerrar\n\n    ```text\n    indentado\n    ```\n"
    p = problems_for(V.check_unclosed_fences, t)
    check(has(p, "fence sin cerrar"), "fences de 4 espacios se ignoran; se detecta el real de 0 espacios")


def test_fence_4_only_no_false_positive():
    t = "# x\n\n    ```text\n    indentado\n    ```\n"
    p = problems_for(V.check_unclosed_fences, t)
    check(not p, "dos ``` con 4 espacios no se cuentan como fence (sin falso positivo)")


# ---------- Frontmatter exigido por ruta ----------

def test_frontmatter_required_missing():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "composicion").mkdir()
        f = root / "composicion" / "foo.md"
        f.write_text("# foo\n\nsin frontmatter.\n", encoding="utf-8")
        probs = []
        V.check_frontmatter_and_truncation(f, f.read_text(encoding="utf-8"), root, probs)
        check(has(probs, "frontmatter ausente"), "composicion/ sin frontmatter se marca [frontmatter ausente]")


def test_frontmatter_not_required_proyectos():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "proyectos" / "obra").mkdir(parents=True)
        f = root / "proyectos" / "obra" / "obra.md"
        f.write_text("# obra\n\nletra sin frontmatter.\n", encoding="utf-8")
        probs = []
        V.check_frontmatter_and_truncation(f, f.read_text(encoding="utf-8"), root, probs)
        check(not has(probs, "frontmatter ausente"), "proyectos/ sin frontmatter NO se marca (exento)")


# ---------- Plantillas ----------

def test_plantilla_without_frontmatter_skeleton():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "chuletas").mkdir()
        f = root / "chuletas" / "plantilla_foo.md"
        f.write_text(
            "---\nname: plantilla_foo\ntype: plantilla\ndescription: \"d\"\n---\n\n"
            "# plantilla_foo\n\n## Esqueleto\n\n```markdown\n---\nname: <slug>\n"
            "type: x\nregion: <A: b sin comillas>\n---\n\n# <slug>\n```\n",
            encoding="utf-8")
        probs = []
        V.check_plantilla_skeletons(f, f.read_text(encoding="utf-8"), root, probs)
        check(has(probs, "YAML"), "esqueleto de plantilla con YAML inválido se detecta")


def test_plantilla_no_skeleton():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "chuletas").mkdir()
        f = root / "chuletas" / "plantilla_bar.md"
        f.write_text("---\nname: plantilla_bar\ntype: plantilla\ndescription: \"d\"\n---\n\n# plantilla_bar\n\nsin bloque copiable.\n", encoding="utf-8")
        probs = []
        V.check_plantilla_skeletons(f, f.read_text(encoding="utf-8"), root, probs)
        check(has(probs, "plantilla sin esqueleto"), "plantilla sin bloque de código se detecta")


# ---------- Encabezados dentro / fuera de bloques de código ----------

def test_heading_inside_codeblock_ignored():
    t = "# x\n\n```markdown\n### encabezado dentro del bloque\n```\n\n## fuera\n"
    p = problems_for(V.check_heading_style, t)
    check(not p, "encabezado dentro de un bloque cercado NO se valida (ni salto ni cierre)")


def test_heading_ending_inside_codeblock_ignored():
    t = "# x\n\n```text\n## titulo con dos puntos:\n```\n"
    p = problems_for(V.check_heading_style, t)
    check(not p, "encabezado terminado en ':' dentro de bloque de código no se marca")


def test_heading_jump_outside_codeblock_flagged():
    t = "# x\n\n### salto real fuera del bloque\n"
    p = problems_for(V.check_heading_style, t)
    check(has(p, "salto de nivel"), "salto de nivel en prosa real (fuera de bloque) sí se detecta")


# ---------- Claves YAML: comentadas / anidadas no cuentan ----------

def _fm_probs(root, folder, name, body):
    (root / folder).mkdir(parents=True, exist_ok=True)
    f = root / folder / name
    f.write_text(body, encoding="utf-8")
    probs = []
    V.check_frontmatter_and_truncation(f, f.read_text(encoding="utf-8"), root, probs)
    return probs


def test_frontmatter_commented_key_not_counted():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        body = "---\n# name: no soy la clave real\ntype: composicion\ndescription: ok\n---\n\n# foo\n"
        probs = _fm_probs(root, "composicion", "foo.md", body)
        check(any("incompleto" in p and "name" in p for p in probs),
              "clave comentada '# name:' NO cuenta como la clave real (se marca faltante)")


def test_frontmatter_nested_key_not_toplevel():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        body = "---\nmeta:\n  name: anidado\ntype: composicion\ndescription: ok\n---\n\n# bar\n"
        probs = _fm_probs(root, "composicion", "bar.md", body)
        check(any("incompleto" in p and "name" in p for p in probs),
              "clave anidada 'meta.name' NO cuenta como name de nivel superior")


def test_frontmatter_real_keys_ok():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        body = "---\nname: ok\ntype: composicion\ndescription: d\n---\n\n# ok\n"
        probs = _fm_probs(root, "composicion", "ok.md", body)
        check(not any("incompleto" in p for p in probs),
              "las tres claves reales de nivel superior no se marcan como faltantes")


# ---------- Agrupación del reporte (Hallazgo 4) ----------

def test_group_by_category():
    items = ["[a] uno", "[b] dos", "[a] tres", "sin prefijo"]
    g = V.group_by_category(items)
    check(len(g.get("a", [])) == 2 and len(g.get("b", [])) == 1 and "(sin categoría)" in g,
          "los problemas se agrupan por su prefijo entre corchetes")


def main():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    print(f"Ejecutando {len(tests)} pruebas del validador...\n")
    for t in tests:
        print(f"[{t.__name__}]")
        t()
    print()
    if FAILURES:
        print(f"{len(FAILURES)} fallo(s).")
        return 1
    print(f"Todas las pruebas pasaron ({len(tests)} casos).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
