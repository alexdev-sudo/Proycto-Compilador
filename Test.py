import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from ExpresionesLexer import ExpresionesLexer
from ExpresionesParser import ExpresionesParser
from ExpresionesVisitor import ExpresionesVisitor

# 1. clase visitor para evaluar la operacion 
class EvalVisitor (ExpresionesVisitor):
    def visitSuma(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right if  ctx.SUM() else  left - right

    def visitMulti(self,ctx):
         left = self.visit(ctx.expr(0))
         right = self.visit(ctx.expr(1))
         return left * right if ctx.MUL() else left /right

    def visitParentesis(self, ctx):
        return self.visit(ctx.expr())
    
    def visitNumero(self, ctx):
        return int(ctx.NUM().getText())        

# ==============================
# 2. Imprimir el árbol sintáctico
# ==============================
def imprimir_arbol(tree, parser):
    print("\n=== ÁRBOL SINTÁCTICO ===") 
    print(Trees.toStringTree(tree, None, parser))


# ==============================
# 3. Programa principal
# ==============================
def main():
    # Leer archivo de entrada
    input_stream = FileStream("entradas.txt")

    # Crear lexer
    lexer = ExpresionesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Crear parser
    parser = ExpresionesParser(token_stream)

    # Regla inicial (ajusta si tu regla se llama distinto)
    tree = parser.expr()

    # Imprimir árbol
    imprimir_arbol(tree, parser)

    # Evaluar expresión con visitor
    visitor = EvalVisitor()
    resultado = visitor.visit(tree)

    print("\n=== RESULTADO ===")
    print("Resultado:", resultado)


if __name__ == "__main__":
    main()