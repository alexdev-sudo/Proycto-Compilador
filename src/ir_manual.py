import difflib
import subprocess
import tempfile
from pathlib import Path

# Mapeo entre los nombres de optimizaciones soportadas
# y los nombres de pases utilizados por LLVM.
PASS_MAP = {
    "mem2reg": "mem2reg",
    "instcombine": "instcombine",
    "simplifycfg": "simplifycfg",
    "dce": "dce",
    "inline": "inline",
    "loop-unroll": "loop-unroll",
}

def apply_manual_passes(ir_text, selected_passes):
    passes = []

     # Valida que todos los pases solicitados existan
    # dentro de la lista de pases soportados.

    for p in selected_passes:
        name = p.strip()

        if name not in PASS_MAP:
            validos = ", ".join(PASS_MAP.keys())
            raise ValueError(f"Pass no soportado: {name}. Validos: {validos}")

        passes.append(PASS_MAP[name])

# Si no se seleccionó ningún pase,
    # devuelve el código original sin modificaciones.

    if not passes:
        return ir_text, {"passes": [], "changed": False}

 # Crea archivos temporales para almacenar
    # el IR de entrada y el resultado optimizado.

    with tempfile.TemporaryDirectory() as tmp:
        in_path = Path(tmp) / "input.ll"
        out_path = Path(tmp) / "output.ll"

        # Guarda el código IR original.
        in_path.write_text(ir_text, encoding="utf-8")
        # Construye el pipeline de optimización.
        # Ejemplo: mem2reg,instcombine,dce

                # Une la lista de pases en una cadena separada por comas
        pipeline = ",".join(passes)

        # Construye el comando para ejecutar la herramienta opt de LLVM
        cmd = ["opt", f"-passes={pipeline}", "-S", str(in_path), "-o", str(out_path)]

        # Ejecuta el comando de optimizacion como un subproceso
        result = subprocess.run(cmd, capture_output=True, text=True)


        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        optimized = out_path.read_text(encoding="utf-8")

    return optimized, {
        "passes": selected_passes,
        "changed": optimized != ir_text,
    }

def diff_ir(before, after):
    return "\n".join(
        difflib.unified_diff(
            before.splitlines(),
            after.splitlines(),
            fromfile="original.ll",
            tofile="manual.ll",
            lineterm="",
        )
    )

def export_manual_ir(ir_text, path="outputs/output.manual.ll"):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(ir_text, encoding="utf-8")
    return path

def run_ir(ir_path):
    result = subprocess.run(["lli", ir_path], capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout