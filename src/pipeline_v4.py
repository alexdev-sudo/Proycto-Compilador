import sys
import os
import time
import argparse
import subprocess

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from antlr.v4.gramatica_v4Lexer import gramatica_v4Lexer
from antlr.v4.gramatica_v4Parser import gramatica_v4Parser

from src.custom_errors import CustomErrorListener, LexerErrorListener
from src.visitador_semantico import semanticVisitor
from src.visitador_interprete import EvalVisitor
from src.tac_generator import TACGenerator
from src.ir_generator import IRGenerator
from src.optimizer import optimize_o3

def fase(nombre, numero):
    print(f"\n{'='*50}")
    print(f"  FASE {numero}: {nombre}")
    print(f"{'='*50}")

TARGET_TRIPLES = {
    "linux": "x86_64-pc-linux-gnu",
    "windows": "x86_64-w64-windows-gnu",
}


def parse_args():
    parser = argparse.ArgumentParser(description="Pipeline v4 del compilador")
    parser.add_argument("input_file", nargs="?", default="inputs/test_ok.src")
    parser.add_argument("--target", choices=["linux", "windows", "both"], default="linux")
    return parser.parse_args()


def sanitize_ir_for_clang(ir_text: str) -> str:
    """
    LlvmLite puede emitir IR valido para su version interna de LLVM,
    pero no siempre compatible con el clang instalado en el sistema.

    output.opt.ll conserva el IR optimizado real.
    output.native.ll es una copia saneada solo para que clang pueda generar binario.
    """

    # LLVM nuevo puede emitir:
    #   getelementptr inbounds nuw ...
    # Algunos clang antiguos esperan:
    #   getelementptr inbounds ...
    ir_text = ir_text.replace("getelementptr inbounds nuw ", "getelementptr inbounds ")
    ir_text = ir_text.replace("getelementptr nuw ", "getelementptr ")

    # LLVM nuevo puede emitir:
    #   icmp samesign ult ...
    # Algunos clang antiguos esperan:
    #   icmp ult ...
    ir_text = ir_text.replace("icmp samesign ", "icmp ")

    # LLVM nuevo puede emitir:
    #   zext nneg ...
    # Si tu clang no lo soporta, se deja como zext normal.
    ir_text = ir_text.replace("zext nneg ", "zext ")
    ir_text = ir_text.replace("sext nneg ", "sext ")
    ir_text = ir_text.replace("trunc nneg ", "trunc ")

    return ir_text


def build_native(ir_path: str, platform: str) -> str:
    os.makedirs("outputs", exist_ok=True)

    if platform == "linux":
        output_path = "outputs/program_linux"
        cmd = ["clang", ir_path, "-O3", "-o", output_path]

    elif platform == "windows":
        output_path = "outputs/program_windows.exe"
        cmd = [
            "clang",
            "-target",
            "x86_64-w64-windows-gnu",
            ir_path,
            "-O3",
            "-o",
            output_path,
        ]

    else:
        raise ValueError(f"Plataforma no soportada: {platform}")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return output_path    

def main():
    args = parse_args()
    input_file = args.input_file
    target = args.target

    input_stream = FileStream(input_file, encoding="utf-8")
    resultados = []

    # ─────────────────────────────────────────
    # FASE 1 — LEXICO
    # ─────────────────────────────────────────
    fase("LEXICO", 1)
    t_inicio = time.time()

    lexer = gramatica_v4Lexer(input_stream)
    lexer_listener = LexerErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_listener)

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    t_lexico = (time.time() - t_inicio) * 1000

    if lexer_listener.errors:
        for e in lexer_listener.errors:
            print(e)
        print(f"\n  Estado: ERROR | Tiempo: {t_lexico:.2f}ms")
        print("\n  Pipeline detenido en fase lexica.")
        return

    print(f"  Estado: OK | Tiempo: {t_lexico:.2f}ms")
    resultados.append(("Lexico", "OK", t_lexico))

    # ─────────────────────────────────────────
    # FASE 2 — SINTACTICO
    # ─────────────────────────────────────────
    fase("SINTACTICO", 2)
    t_inicio = time.time()

    parser = gramatica_v4Parser(token_stream)
    parser_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_listener)

    tree = parser.root()

    t_sintactico = (time.time() - t_inicio) * 1000

    if parser_listener.errors:
        for e in parser_listener.errors:
            print(e)
        print(f"\n  Estado: ERROR | Tiempo: {t_sintactico:.2f}ms")
        print("\n  Pipeline detenido en fase sintactica.")
        return

    print(f"  Estado: OK | Tiempo: {t_sintactico:.2f}ms")
    resultados.append(("Sintactico", "OK", t_sintactico))

    # ─────────────────────────────────────────
    # FASE 3 — SEMANTICO
    # ─────────────────────────────────────────
    fase("SEMANTICO", 3)
    t_inicio = time.time()

    semantico = semanticVisitor()
    semantico.visit(tree)

    t_semantico = (time.time() - t_inicio) * 1000

    if semantico.errors:
        for e in semantico.errors:
            print(e)
        print(f"\n  Estado: ERROR | Tiempo: {t_semantico:.2f}ms")
        print("\n  Pipeline detenido en fase semantica.")
        return

    print(f"  Estado: OK | Tiempo: {t_semantico:.2f}ms")
    resultados.append(("Semantico", "OK", t_semantico))

    # ─────────────────────────────────────────
    # FASE 4 — GENERACION TAC
    # ─────────────────────────────────────────
    fase("GENERACION TAC", 4)
    t_inicio = time.time()

    try:
        from src.tac_generator import TACGenerator
        tac = TACGenerator()
        tac.visit(tree)
        tac_output = tac.get_code()

        os.makedirs("outputs", exist_ok=True)
        with open("outputs/output.tac", "w", encoding="utf-8") as f:
            f.write(tac_output)

        t_tac = (time.time() - t_inicio) * 1000
        print(f"  Estado: OK | Tiempo: {t_tac:.2f}ms")
        resultados.append(("TAC", "OK", t_tac))

    except Exception as e:
        t_tac = (time.time() - t_inicio) * 1000
        print(f"  Error TAC: {e}")
        print(f"  Estado: ERROR | Tiempo: {t_tac:.2f}ms")
        resultados.append(("TAC", "ERROR", t_tac))

    # ─────────────────────────────────────────
    # FASE 5 — GENERACION LLVM IR
    # ─────────────────────────────────────────
    fase("GENERACION LLVM IR", 5)
    t_inicio = time.time()

    try:
        from src.ir_generator import IRGenerator
        triple = TARGET_TRIPLES["windows"] if target == "windows" else TARGET_TRIPLES["linux"]

        ir = IRGenerator(target_triple=triple)
        ir.visit(tree)
        ir_output = ir.get_ir()

        with open("outputs/output.ll", "w", encoding="utf-8") as f:
            f.write(ir_output)

        t_ir = (time.time() - t_inicio) * 1000
        print(f"  Estado: OK | Tiempo: {t_ir:.2f}ms")
        resultados.append(("LLVM IR", "OK", t_ir))

    except Exception as e:
        t_ir = (time.time() - t_inicio) * 1000
        print(f"  Error IR: {e}")
        print(f"  Estado: ERROR | Tiempo: {t_ir:.2f}ms")
        resultados.append(("LLVM IR", "ERROR", t_ir))

    # ─────────────────────────────────────────
    # FASE 6 — EJECUCION / INTERPRETE
    # ─────────────────────────────────────────
    fase("EJECUCION", 6)
    t_inicio = time.time()

    try:
        interpreter = EvalVisitor()
        interpreter.visit(tree)
        t_interprete = (time.time() - t_inicio) * 1000
        print(f"  Estado: OK | Tiempo: {t_interprete:.2f}ms")
        resultados.append(("Ejecucion", "OK", t_interprete))

    except Exception as e:
        t_interprete = (time.time() - t_inicio) * 1000
        print(f"  Error ejecucion: {e}")
        print(f"  Estado: ERROR | Tiempo: {t_interprete:.2f}ms")
        resultados.append(("Ejecucion", "ERROR", t_interprete))
        # ─────────────────────────────────────────
    # FASE 7 — OPTIMIZACION O3
    # ─────────────────────────────────────────
    fase("OPTIMIZACION O3", 7)
    t_inicio = time.time()

    try:
        ir_optimizado, metricas = optimize_o3(ir_output)

        with open("outputs/output.opt.ll", "w", encoding="utf-8") as f:
            f.write(ir_optimizado)

        t_o3 = (time.time() - t_inicio) * 1000

        print(f"  Estado: OK | Tiempo: {t_o3:.2f}ms")
        print(f"  Instrucciones antes: {metricas['instructions_before']}")
        print(f"  Instrucciones despues: {metricas['instructions_after']}")
        print(f"  Reduccion: {metricas['reduction_percent']:.2f}%")

        resultados.append(("Optimizacion O3", "OK", t_o3))

    except Exception as e:
        t_o3 = (time.time() - t_inicio) * 1000

        print(f"  Error O3: {e}")
        print(f"  Estado: ERROR | Tiempo: {t_o3:.2f}ms")

        resultados.append(("Optimizacion O3", "ERROR", t_o3))

        ir_optimizado = ir_output

        with open("outputs/output.opt.ll", "w", encoding="utf-8") as f:
            f.write(ir_optimizado)

        # ─────────────────────────────────────────
    # FASE 8 — GENERACION BINARIO NATIVO
    # ─────────────────────────────────────────
    fase("GENERACION BINARIO NATIVO", 8)
    t_inicio = time.time()

    try:
        native_ir = sanitize_ir_for_clang(ir_optimizado)

        with open("outputs/output.native.ll", "w", encoding="utf-8") as f:
            f.write(native_ir)

        platforms = ["linux", "windows"] if target == "both" else [target]

        for platform in platforms:
            binary_path = build_native("outputs/output.native.ll", platform)
            print(f"  {platform}: {binary_path}")

        t_bin = (time.time() - t_inicio) * 1000

        print(f"  Estado: OK | Tiempo: {t_bin:.2f}ms")
        resultados.append(("Binario nativo", "OK", t_bin))

    except Exception as e:
        t_bin = (time.time() - t_inicio) * 1000

        print(f"  Error binario: {e}")
        print(f"  Estado: ERROR | Tiempo: {t_bin:.2f}ms")

        resultados.append(("Binario nativo", "ERROR", t_bin))        
    # ─────────────────────────────────────────
    # RESUMEN FINAL
    # ─────────────────────────────────────────
    print(f"\n{'='*50}")
    print("  RESUMEN DEL PIPELINE")
    print(f"{'='*50}")
    for nombre, estado, tiempo in resultados:
        print(f"  {nombre:<20} {estado:<8} {tiempo:.2f}ms")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    main()