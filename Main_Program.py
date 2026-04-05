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
    DEBUG = False # cambiamos a false para quitar los prints de debug

    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = FileStream("entradas Expr.txt")


     # lexer
    lexer = Expresiones21Lexer(input_stream)

    # Parser 
    token_stream = CommonTokenStream(lexer)

    parser = Expresiones21Parser(token_stream)

    tree = parser.root()
    if DEBUG:
        imprimir_arbol(tree, parser)
    #Interpretar
    visitor = EvalVisitor()

    visitor.visitProgInput(tree)

    if DEBUG:
        print("scopes:", visitor.scopes)


    if DEBUG:

        print("\n=== MEMORIA FINAL ===")
    #imprimir solo el scope global
        for var, val in visitor.scopes[0].items():
            print(var, "=", val)


if __name__ == "__main__":
    main()