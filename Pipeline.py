import sys
from antlr4 import *

from Expresiones21Lexer import Expresiones21Lexer
from Expresiones21Parser import Expresiones21Parser

from custom_errors import CustomErrorListener
from visitador_semantico import semanticVisitor
from visitador_interprete import EvalVisitor
from custom_errors import LexerErrorListener

def main():
    # Se lee el archivo de entrada proporcionado como argumento o se usa el archivo por defecto
    input_file = sys.argv[1] if len(sys.argv) > 1 else "entradas Expr.txt"
    input_stream = FileStream(input_file, encoding='utf-8')
    print("\n ----- Analisis lexico---------")

    #Lexer--------------------------------- 
    # Se inicializa el parser con el flujo de tokens generado por el analizador léxico
    lexer = Expresiones21Lexer(input_stream)
    lexer_listener = LexerErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_listener)
    
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    if lexer_listener.errors:
        for e in lexer_listener.errors:
            print(e)
        print("\n Error en Fase Lexica, Pipeline detendo ")    
        return
    print("Lexico correcto, iniciando fase sintactica")

    # Fase sintacitca Parser-----------------------------
    
    parser = Expresiones21Parser(token_stream)
    parser_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_listener)
    
    tree = parser.root()

    #errores sintacticos
    if parser_listener.errors:
        for e in parser_listener.errors:
            print(e)
        print("\n Error en Fase Sintactica, Pipeline detendo ")    
        return
    print("Sintaxis correcta, iniciando fase semantica")

    #semantico--------------------------------

    sematic = semanticVisitor()
    sematic.visit(tree)

    if sematic.errors:
        for e in sematic.errors:
            print(e)
        print("\n Error en Fase Semantica, Pipeline detenido ")    
        return
    print("Semantica correcta, iniciando fase de ejecucion")

    #Interpretar--------------------------------

    interpreter = EvalVisitor()
    print("\n=== iniciando interpretación ===")
    interpreter.visit(tree)

    print("\n=== interpretación finalizada ===")

if __name__ == "__main__":
    main()
    


