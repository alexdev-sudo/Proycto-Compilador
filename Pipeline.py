import sys
from antlr4 import *

from Expresiones21Lexer import Expresiones21Lexer
from Expresiones21Parser import Expresiones21Parser

from custom_errors import CustomErrorListener
from visitador_semantico import semanticVisitor
from visitador_interprete import EvalVisitor

def main():

    input_file = sys.argv[1] if len(sys.argv) > 1 else "entradas Expr.txt"
    input_stream = FileStream(input_file)
    print("\n ----- Analisis lexico---------")

    #Lexer--------------------------------- 

    lexer = Expresiones21Lexer(input_stream)
    # Error lexico
    error_listener = CustomErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)  

    
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    if error_listener.errors:
        for e in error_listener.errors:
            print(e)
        print("\n Error en Fase Lexica, Pipeline detendo ")    
        return
    print("Lexico correcto, iniciando fase sintactica")

    #Parser-----------------------------------
    parser = Expresiones21Parser(token_stream)
    # error_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    tree = parser.root()

    #errores sintacticos
    if error_listener.errors:
        for e in error_listener.errors:
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
    


