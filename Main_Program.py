import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from Expresiones21Lexer import Expresiones21Lexer
from Expresiones21Parser import Expresiones21Parser
from visitador_interprete import EvalVisitor




# ==============================
# IMPRIMIR ARBOL
# ==============================

def imprimir_arbol(tree, parser):

    print("\n=== ÁRBOL SINTÁCTICO ===")
    print(Trees.toStringTree(tree, None, parser))


# ==============================
# MAIN
# ==============================

def main():

    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = FileStream("entradas Programa.txt")


     # lexer
    lexer = Expresiones21Lexer(input_stream)

    # Parser 
    token_stream = CommonTokenStream(lexer)

    parser = Expresiones21Parser(token_stream)

    tree = parser.root()

    imprimir_arbol(tree, parser)
    #Interpretar
    visitor = EvalVisitor()

    visitor.visit(tree)

    print("\n=== MEMORIA FINAL ===")

    for var, val in visitor.memory.items():
        print(var, "=", val)


if __name__ == "__main__":
    main()