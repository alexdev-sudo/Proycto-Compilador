import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from antlr.v3.gramatica_v3Lexer import gramatica_v3Lexer
from antlr.v3.gramatica_v3Parser import gramatica_v3Parser
from src.custom_errors import CustomErrorListener, LexerErrorListener
from src.visitador_semantico import semanticVisitor
from src.visitador_interprete import EvalVisitor

def fase(nombre, numero):
    print(f"\n{'='*50}")
    print(f"  FASE {numero}: {nombre}")
    print(f"{'='*50}")

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/test_ok.src"
    input_stream = FileStream(input_file, encoding='utf-8')

    resultados = []

    # ─────────────────────────────────────────
    # FASE 1 — LÉXICO
    # ─────────────────────────────────────────
    fase("LÉXICO", 1)
    t_inicio = time.time()

    lexer = gramatica_v3Lexer(input_stream)
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
        print("\n  Pipeline detenido en fase léxica.")
        return

    print(f"  Estado: OK | Tiempo: {t_lexico:.2f}ms")
    resultados.append(("Léxico", "OK", t_lexico))

    # ─────────────────────────────────────────
    # FASE 2 — SINTÁCTICO
    # ─────────────────────────────────────────
    fase("SINTÁCTICO", 2)
    t_inicio = time.time()

    parser = gramatica_v3Parser(token_stream)
    parser_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_listener)

    tree = parser.root()

    t_sintactico = (time.time() - t_inicio) * 1000

    if parser_listener.errors:
        for e in parser_listener.errors:
            print(e)
        print(f"\n  Estado: ERROR | Tiempo: {t_sintactico:.2f}ms")
        print("\n  Pipeline detenido en fase sintáctica.")
        return

    print(f"  Estado: OK | Tiempo: {t_sintactico:.2f}ms")
    resultados.append(("Sintáctico", "OK", t_sintactico))

    # ─────────────────────────────────────────
    # FASE 3 — SEMÁNTICO
    # ─────────────────────────────────────────
    fase("SEMÁNTICO", 3)
    t_inicio = time.time()

    semantico = semanticVisitor()
    semantico.visit(tree)

    t_semantico = (time.time() - t_inicio) * 1000

    if semantico.errors:
        for e in semantico.errors:
            print(e)
        print(f"\n  Estado: ERROR | Tiempo: {t_semantico:.2f}ms")
        print("\n  Pipeline detenido en fase semántica.")
        return

    print(f"  Estado: OK | Tiempo: {t_semantico:.2f}ms")
    resultados.append(("Semántico", "OK", t_semantico))

    # ─────────────────────────────────────────
    # FASE 4 — GENERACIÓN TAC
    # ─────────────────────────────────────────
    fase("GENERACIÓN TAC", 4)
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
        print(tac_output)
        print(f"  Estado: OK | Tiempo: {t_tac:.2f}ms")
        resultados.append(("TAC", "OK", t_tac))

    except Exception as e:
        t_tac = (time.time() - t_inicio) * 1000
        print(f"  Error TAC: {e}")
        print(f"  Estado: ERROR | Tiempo: {t_tac:.2f}ms")
        resultados.append(("TAC", "ERROR", t_tac))

    # ─────────────────────────────────────────
    # FASE 5 — GENERACIÓN LLVM IR
    # ─────────────────────────────────────────
    fase("GENERACIÓN LLVM IR", 5)
    t_inicio = time.time()

    try:
        from src.ir_generator import IRGenerator
        ir = IRGenerator()
        ir.visit(tree)
        ir_output = ir.get_ir()

        with open("outputs/output.ll", "w", encoding="utf-8") as f:
            f.write(ir_output)

        t_ir = (time.time() - t_inicio) * 1000
        print(ir_output)
        print(f"  Estado: OK | Tiempo: {t_ir:.2f}ms")
        resultados.append(("LLVM IR", "OK", t_ir))

    except Exception as e:
        t_ir = (time.time() - t_inicio) * 1000
        print(f"  Error IR: {e}")
        print(f"  Estado: ERROR | Tiempo: {t_ir:.2f}ms")
        resultados.append(("LLVM IR", "ERROR", t_ir))

    # ─────────────────────────────────────────
    # FASE 6 — EJECUCIÓN / INTÉRPRETE
    # ─────────────────────────────────────────
    fase("EJECUCIÓN", 6)
    t_inicio = time.time()

    try:
        interpreter = EvalVisitor()
        interpreter.visit(tree)
        t_interprete = (time.time() - t_inicio) * 1000
        print(f"  Estado: OK | Tiempo: {t_interprete:.2f}ms")
        resultados.append(("Ejecución", "OK", t_interprete))

    except Exception as e:
        t_interprete = (time.time() - t_inicio) * 1000
        print(f"  Error ejecución: {e}")
        print(f"  Estado: ERROR | Tiempo: {t_interprete:.2f}ms")
        resultados.append(("Ejecución", "ERROR", t_interprete))

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