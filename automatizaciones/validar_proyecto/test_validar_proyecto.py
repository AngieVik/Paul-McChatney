#!/usr/bin/env python3
"""
test_validar_proyecto.py — Pruebas automáticas del validador.

Sin dependencias externas (no requiere pytest): se ejecuta con
`python test_validar_proyecto.py` desde cualquier sitio y devuelve código de
salida 1 si algún caso falla. Cada prueba construye contenido sintético
(válido e inválido) y comprueba que el validador lo clasifica bien, cubriendo
los puntos ciegos que motivaron la ampliación: YAML inválido, bytes nulos,
fences con 0/3/4 espacios, mapas y skills desincronizados, y plantillas sin
frontmatter. Así cada ampliación futura del validador no reintroduce falsos
positivos ni puntos ciegos.
"""

import importlib.util
import os
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
    """Ejecuta un chequeo sobre texto sintético y devuelve la lista de avisos."""
    probs = []
    root = root or Path("/tmp")
    fn(root / name, text, root, probs, **kw)
    return probs


def has(probs, needle):
    return any(needle in p for p in probs)


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
    # Dos marcas ``` con 4 espacios NO deben contar como fence (CommonMark);
    # combinadas con un fence real de 0 espacios sin cerrar, el conteo real es
    # impar (1) y debe detectarse; las de 4 espacios no descuadran nada.
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


# ---------- Bidireccionalidad mapa <-> skill ----------

def _scaffold(root):
    (root / ".claude" / "rules").mkdir(parents=True)
    (root / ".claude" / "skills").mkdir(parents=True)


def _mk_map(root, name, consumido):
    (root / ".claude" / "rules" / f"{name}.md").write_text(
        f"---\nname: {name}\ntype: map\ndescription: \"m\"\n---\n\n# {name}\n\n- **Consumido por:** {consumido}\n",
        encoding="utf-8")


def _mk_skill(root, name, body=""):
    d = root / ".claude" / "skills" / name
    d.mkdir(parents=True, exist_ok=True)
    (d / "SKILL.md").write_text(
        f"---\nname: {name}\ntype: skill\ndescription: \"s\"\n---\n\n# {name}\n\n{body}\n",
        encoding="utf-8")


def test_forward_desync():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        _scaffold(root)
        _mk_map(root, "style_box", "`otra` (skill)")           # NO menciona a la skill que lo cita
        _mk_skill(root, "style_box", "Uso `.claude/rules/style_box.md`.")
        maps = V.collect_maps_consumido(root)
        probs = []
        sk = root / ".claude" / "skills" / "style_box" / "SKILL.md"
        V.check_map_skill_bidirectional(sk, sk.read_text(encoding="utf-8"), root, maps, probs)
        check(has(probs, "bidireccionalidad rota"),
              "skill cita mapa que no la lista en Consumido por -> flag (skill->mapa)")


def test_reverse_desync():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        _scaffold(root)
        _mk_map(root, "style_box", "`style_box` (skill), `produccion` (Fase 2)")
        _mk_skill(root, "style_box", "no cita su mapa")         # dueña que NO cita de vuelta
        maps = V.collect_maps_consumido(root)
        probs = []
        V.check_map_owner_reciprocity(root, maps, probs)
        check(has(probs, "bidireccionalidad incompleta"),
              "skill dueña que no cita su mapa -> flag (mapa->skill)")


def test_reverse_produccion_exception():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        _scaffold(root)
        _mk_map(root, "efectos", "`produccion` (Fase 5)")
        _mk_skill(root, "produccion", "orquesta sin citar efectos")
        maps = V.collect_maps_consumido(root)
        probs = []
        V.check_map_owner_reciprocity(root, maps, probs)
        check(not probs, "produccion es excepción declarada -> sin flag")


def test_reverse_conceptual_consumer():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        _scaffold(root)
        # `letra` aparece SIN anotación (skill) y no existe skill homónima aquí:
        _mk_map(root, "chupilista", "`exclude_box`, `letra`")
        maps = V.collect_maps_consumido(root)
        probs = []
        V.check_map_owner_reciprocity(root, maps, probs)
        check(not probs, "consumidor conceptual (no (skill), sin skill real) -> sin flag")


# ---------- Plantillas ----------

def test_plantilla_without_frontmatter_skeleton():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "chuletas").mkdir()
        f = root / "chuletas" / "plantilla_foo.md"
        # esqueleto con region: <A: b> -> YAML inválido dentro del esqueleto
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


def main():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    print(f"Ejecutando {len(tests)} pruebas del validador...\n")
    for t in tests:
        print(f"[{t.__name__}]")
        t()
    print()
    if FAILURES:
        print(f"❌ {len(FAILURES)} fallo(s).")
        return 1
    print(f"✅ Todas las pruebas pasaron ({len(tests)} casos).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
