"""
ir_manual.py — Módulo de Optimización Manual del IR
Permite aplicar passes de optimización individuales sobre el LLVM IR
y comparar el resultado antes/después mediante un diff textual.

Funciones públicas (requeridas por ui_compilador.py):
    apply_manual_passes(ir_text, passes) -> (str, dict)
    export_manual_ir(ir_text)            -> None
    diff_ir(original, optimized)         -> str
"""

import os
import re
import difflib
import llvmlite.binding as llvm

# ─────────────────────────────────────────────────────────
# INICIALIZACIÓN LLVM (solo una vez al importar el módulo)
# ─────────────────────────────────────────────────────────
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# Ruta de salida del IR manual
_OUTPUT_DIR  = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
_MANUAL_PATH = os.path.join(_OUTPUT_DIR, "output.manual.ll")

# ─────────────────────────────────────────────────────────
# PASSES DISPONIBLES
# Nombres que el usuario puede escribir en la UI → pass real de LLVM
# ─────────────────────────────────────────────────────────
PASSES_DISPONIBLES = {
    "mem2reg":      "mem2reg",
    "instcombine":  "instcombine",
    "simplifycfg":  "simplifycfg",
    "dce":          "dce",
    "inline":       "inline",
    "loop-unroll":  "loop-unroll",
}

# Regex para contar instrucciones (mismo criterio que optimizer.py de Maddie)
_INSTRUCTION_RE = re.compile(
    r"^\s*(?:[%@][\w.$-]+\s*=\s*)?"
    r"(alloca|load|store|add|sub|mul|sdiv|srem|fadd|fsub|fmul|fdiv|"
    r"icmp|fcmp|br|switch|call|ret|getelementptr|select|sitofp|fptosi|"
    r"zext|trunc)\b"
)


def _count_instructions(ir_text: str) -> int:
    """Cuenta instrucciones LLVM en el texto IR."""
    total = 0
    for line in ir_text.splitlines():
        clean = line.strip()
        if clean and not clean.startswith(";") and _INSTRUCTION_RE.match(clean):
            total += 1
    return total


# ─────────────────────────────────────────────────────────
# FUNCIÓN PRINCIPAL
# ─────────────────────────────────────────────────────────
def apply_manual_passes(ir_text: str, passes: list) -> tuple:
    """
    Aplica una lista de passes de optimización sobre el IR recibido.

    Parámetros:
        ir_text (str) : texto del LLVM IR original (contenido de output.ll)
        passes  (list): lista de strings con los nombres de passes a aplicar,
                        por ejemplo ["mem2reg", "dce", "simplifycfg"]

    Retorna:
        (optimized_ir, info)
        - optimized_ir (str) : texto del IR resultante
        - info (dict)        : métricas y passes aplicados/ignorados
            {
              "applied":     [...],   # passes que se aplicaron
              "skipped":     [...],   # passes no reconocidos (ignorados)
              "before":      int,     # instrucciones antes
              "after":       int,     # instrucciones después
              "reduction":   float,   # porcentaje de reducción
            }
    """
    # Separar passes válidos de desconocidos
    applied = []
    skipped = []
    for p in passes:
        nombre = p.strip().lower()
        if nombre in PASSES_DISPONIBLES:
            applied.append(PASSES_DISPONIBLES[nombre])
        else:
            skipped.append(p)

    before = _count_instructions(ir_text)

    # Si no hay passes válidos, devolver el IR sin cambios
    if not applied:
        return ir_text, {
            "applied":   [],
            "skipped":   skipped,
            "before":    before,
            "after":     before,
            "reduction": 0.0,
        }

    # Parsear y verificar el módulo
    module = llvm.parse_assembly(ir_text)
    module.verify()

    # Construir el pipeline de passes manualmente.
    # Usamos speed_level=0 para NO activar O3 automáticamente;
    # solo los passes que el usuario seleccionó se aplican.
    target = llvm.Target.from_default_triple()
    tm     = target.create_target_machine()
    pto    = llvm.PipelineTuningOptions(speed_level=0, size_level=0)
    pb     = llvm.create_pass_builder(tm, pto)

    # Mapa: nombre pass → acción sobre FunctionPassManager
    FPM_MAP = {
        "mem2reg":     lambda m: m.add_sroa_pass(),
        "instcombine": lambda m: m.add_instruction_combine_pass(),
        "simplifycfg": lambda m: m.add_simplify_cfg_pass(),
        "dce":         lambda m: m.add_dead_code_elimination_pass(),
        "loop-unroll": lambda m: m.add_loop_unroll_pass(),
    }

    # Mapa: nombre pass → acción sobre ModulePassManager
    MPM_MAP = {
        "mem2reg":     lambda m: m.add_sroa_pass(),
        "instcombine": lambda m: m.add_instruction_combine_pass(),
        "simplifycfg": lambda m: m.add_simplify_cfg_pass(),
        "dce":         lambda m: m.add_dead_code_elimination_pass(),
        "inline":      lambda m: m.add_always_inliner_pass(),
        "loop-unroll": lambda m: m.add_loop_unroll_pass(),
    }

    fpm = pb.getFunctionPassManager()
    mpm = pb.getModulePassManager()

    for p in applied:
        if p in FPM_MAP:
            FPM_MAP[p](fpm)
        if p in MPM_MAP:
            MPM_MAP[p](mpm)

    # Aplicar a nivel función primero, luego a nivel módulo
    for fn in module.functions:
        if not fn.is_declaration:
            fpm.run(fn, pb)

    mpm.run(module, pb)

    optimized = str(module)
    after     = _count_instructions(optimized)
    reduction = ((before - after) / before * 100.0) if before else 0.0

    return optimized, {
        "applied":   applied,
        "skipped":   skipped,
        "before":    before,
        "after":     after,
        "reduction": round(reduction, 2),
    }


# ─────────────────────────────────────────────────────────
# EXPORTAR IR MANUAL
# ─────────────────────────────────────────────────────────
def export_manual_ir(ir_text: str) -> None:
    """
    Guarda el IR resultante de la optimización manual en
    outputs/output.manual.ll

    Parámetros:
        ir_text (str): texto del IR optimizado manualmente
    """
    os.makedirs(_OUTPUT_DIR, exist_ok=True)
    with open(_MANUAL_PATH, "w", encoding="utf-8") as f:
        f.write(ir_text)


# ─────────────────────────────────────────────────────────
# DIFF ENTRE IR ORIGINAL Y OPTIMIZADO
# ─────────────────────────────────────────────────────────
def diff_ir(original: str, optimized: str) -> str:
    """
    Genera un diff unificado entre el IR original y el optimizado.
    Las líneas con + son instrucciones añadidas o modificadas,
    las líneas con - son las eliminadas/reemplazadas.

    Parámetros:
        original  (str): IR antes de los passes
        optimized (str): IR después de los passes

    Retorna:
        str con el diff formateado, listo para mostrar en consola Rich.
        Si no hay diferencias, retorna un mensaje indicándolo.
    """
    lineas_orig = original.splitlines(keepends=True)
    lineas_opt  = optimized.splitlines(keepends=True)

    diff = list(difflib.unified_diff(
        lineas_orig,
        lineas_opt,
        fromfile="IR original (output.ll)",
        tofile="IR manual   (output.manual.ll)",
        lineterm="",
    ))

    if not diff:
        return "Sin diferencias: los passes seleccionados no modificaron el IR.\n(El programa no ofrece oportunidades para estas transformaciones.)"

    # Limitar a 120 líneas para que no desborde la consola
    MAX_LINEAS = 120
    resultado  = "".join(diff[:MAX_LINEAS])
    if len(diff) > MAX_LINEAS:
        omitidas = len(diff) - MAX_LINEAS
        resultado += f"\n... ({omitidas} líneas omitidas — ver output.manual.ll para el diff completo)"

    return resultado