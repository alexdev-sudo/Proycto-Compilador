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

    #Lexer 
    lexer = Expresiones21Lexer(input_stream)

    #parser 
    token_stream = CommonTokenStream(lexer)
    parser = Expresiones21Parser(token_stream)

    error_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    tree = parser.root()
    #errores sintacticos
    if error_listener.errors:
        for e in error_listener.errors:
            print(e)
        return
    
    #semantico
    sematic = semanticVisitor()
    sematic.visit(tree)

    if sematic.errors:
        for e in sematic.errors:
            print(e)
        return
    
    #Interpretar
    interpreter = EvalVisitor()
    interpreter.visit(tree)

if __name__ == "__main__":
    main()
    


