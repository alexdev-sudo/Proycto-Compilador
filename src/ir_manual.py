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
# ─────────────────────────────────────────────────────────
PASS_MAP = {
    "mem2reg":     "mem2reg",
    "instcombine": "instcombine",
    "simplifycfg": "simplifycfg",
    "dce":         "dce",
    "inline":      "inline",
    "loop-unroll": "loop-unroll",
}

# Regex para contar instrucciones (mismo criterio que optimizer.py)
_INSTRUCTION_RE = re.compile(
    r"^\s*(?:[%@][\w.$-]+\s*=\s*)?"
    r"(alloca|load|store|add|sub|mul|sdiv|srem|fadd|fsub|fmul|fdiv|"
    r"icmp|fcmp|br|switch|call|ret|getelementptr|select|sitofp|fptosi|"
    r"zext|trunc)\b"
)

def _count_instructions(ir_text: str) -> int:
    total = 0
    for line in ir_text.splitlines():
        clean = line.strip()
        if clean and not clean.startswith(";") and _INSTRUCTION_RE.match(clean):
            total += 1
    return total


# ─────────────────────────────────────────────────────────
# FUNCIÓN PRINCIPAL
# ─────────────────────────────────────────────────────────
def apply_manual_passes(ir_text: str, selected_passes: list) -> tuple:
    """
    Aplica passes de optimización individuales sobre el IR.

    Parámetros:
        ir_text         (str)  : texto del LLVM IR original
        selected_passes (list) : nombres de passes a aplicar

    Retorna:
        (optimized_ir, info)
        - optimized_ir (str)
        - info (dict): { applied, skipped, before, after, reduction_percent, changed }
    """
    applied = []
    skipped = []
    for p in selected_passes:
        name = p.strip().lower()
        if name in PASS_MAP:
            applied.append(name)
        else:
            skipped.append(p)

    before = _count_instructions(ir_text)

    if not applied:
        return ir_text, {
            "passes":             [],
            "applied":            [],
            "skipped":            skipped,
            "changed":            False,
            "before":             before,
            "after":              before,
            "reduction_percent":  0.0,
        }

    module = llvm.parse_assembly(ir_text)
    module.verify()

    target = llvm.Target.from_default_triple()
    tm     = target.create_target_machine()
    pto    = llvm.PipelineTuningOptions(speed_level=0, size_level=0)
    pb     = llvm.create_pass_builder(tm, pto)

    FPM_MAP = {
        "mem2reg":     lambda m: m.add_sroa_pass(),
        "instcombine": lambda m: m.add_instruction_combine_pass(),
        "simplifycfg": lambda m: m.add_simplify_cfg_pass(),
        "dce":         lambda m: m.add_dead_code_elimination_pass(),
        "loop-unroll": lambda m: m.add_loop_unroll_pass(),
    }
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

    for fn in module.functions:
        if not fn.is_declaration:
            fpm.run(fn, pb)
    mpm.run(module, pb)

    optimized  = str(module)
    after      = _count_instructions(optimized)
    reduction  = ((before - after) / before * 100.0) if before else 0.0

    return optimized, {
        "passes":            applied,
        "applied":           applied,
        "skipped":           skipped,
        "changed":           optimized != ir_text,
        "before":            before,
        "after":             after,
        "reduction_percent": round(reduction, 2),
    }


# ─────────────────────────────────────────────────────────
# EXPORTAR IR MANUAL
# ─────────────────────────────────────────────────────────
def export_manual_ir(ir_text: str, path: str = None) -> str:
    target_path = path or _MANUAL_PATH
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(ir_text)
    return target_path


# ─────────────────────────────────────────────────────────
# DIFF ENTRE IR ORIGINAL Y OPTIMIZADO
# ─────────────────────────────────────────────────────────
def diff_ir(original: str, optimized: str) -> str:
    lineas_orig = original.splitlines(keepends=True)
    lineas_opt  = optimized.splitlines(keepends=True)

    diff = list(difflib.unified_diff(
        lineas_orig,
        lineas_opt,
        fromfile="original.ll",
        tofile="manual.ll",
        lineterm="",
    ))

    if not diff:
        return "Sin diferencias: los passes seleccionados no modificaron el IR."

    MAX_LINEAS = 120
    resultado  = "".join(diff[:MAX_LINEAS])
    if len(diff) > MAX_LINEAS:
        resultado += f"\n... ({len(diff) - MAX_LINEAS} líneas omitidas)"
    return resultado


# ─────────────────────────────────────────────────────────
# RE-EJECUCIÓN DEL IR (requerido por el enunciado)
# ─────────────────────────────────────────────────────────
def run_ir(ir_path: str) -> str:
    """Ejecuta el IR con llvmlite JIT y retorna la salida."""
    with open(ir_path, "r", encoding="utf-8") as f:
        ir_text = f.read()

    module   = llvm.parse_assembly(ir_text)
    target   = llvm.Target.from_default_triple()
    tm       = target.create_target_machine()
    engine   = llvm.create_mcjit_compiler(module, tm)
    engine.finalize_object()
    engine.run_static_constructors()

    main_ptr = engine.get_function_address("main")
    import ctypes
    cfunc = ctypes.CFUNCTYPE(ctypes.c_int)(main_ptr)
    cfunc()
    return ""