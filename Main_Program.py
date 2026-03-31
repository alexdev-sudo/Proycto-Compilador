import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from Expresiones21Lexer import Expresiones21Lexer
from Expresiones21Parser import Expresiones21Parser
from Expresiones21Visitor import Expresiones21Visitor


# ==============================
# Visitor para evaluar programa
# ==============================
class EvalVisitor(Expresiones21Visitor):

    def __init__(self):
        self.memory = {}


# ==============================
# PROGRAMA
# ==============================

    def visitRoot(self, ctx):
        return self.visit(ctx.bloque())


    def visitBloque(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)


    def visitStatement(self, ctx):

        if ctx.varint():
            return self.visit(ctx.varint())

        if ctx.asignacion():
            return self.visit(ctx.asignacion())

        if ctx.ifstm():
            return self.visit(ctx.ifstm())


# ==============================
# VARIABLES
# ==============================

    def visitVarint(self, ctx):

        nombre = ctx.VAR().getText()

        if nombre not in self.memory:
            self.memory[nombre] = 0


    def visitAsignacion(self, ctx):

        nombre = ctx.VAR().getText()

        valor = self.visit(ctx.expr())

        self.memory[nombre] = valor

        return valor


# ==============================
# IF
# ==============================

    def visitIfstm(self, ctx):

        condicion = self.visit(ctx.expr())

        if condicion:
            self.visit(ctx.bloque(0))
        else:
            if ctx.ELSE():
                self.visit(ctx.bloque(1))


# ==============================
# EXPRESIONES LOGICAS
# ==============================

    def visitLogicalOr(self, ctx):

        resultado = self.visit(ctx.logicalAnd(0))

        for i in range(1, len(ctx.logicalAnd())):
            resultado = resultado or self.visit(ctx.logicalAnd(i))

        return resultado


    def visitLogicalAnd(self, ctx):

        resultado = self.visit(ctx.igualdad(0))

        for i in range(1, len(ctx.igualdad())):
            resultado = resultado and self.visit(ctx.igualdad(i))

        return resultado


# ==============================
# IGUALDAD
# ==============================

    def visitIgualdad(self, ctx):

        left = self.visit(ctx.comparacion(0))

        for i in range(1, len(ctx.comparacion())):

            right = self.visit(ctx.comparacion(i))

            if ctx.IGUAL(i-1):
                left = left == right

            elif ctx.NOIGUAL(i-1) or ctx.DIFF(i-1):
                left = left != right

        return left


# ==============================
# COMPARACIONES
# ==============================

    def visitComparacion(self, ctx):

        left = self.visit(ctx.suma(0))

        for i in range(1, len(ctx.suma())):

            right = self.visit(ctx.suma(i))

            if ctx.MAYOR(i-1):
                left = left > right

            elif ctx.MENOR(i-1):
                left = left < right

            elif ctx.MAYORIGUAL(i-1):
                left = left >= right

            elif ctx.MENORIGUAL(i-1):
                left = left <= right

        return left


# ==============================
# SUMA
# ==============================

    def visitSuma(self, ctx):

        resultado = self.visit(ctx.producto(0))

        for i in range(1, len(ctx.producto())):

            right = self.visit(ctx.producto(i))

            if ctx.SUM(i-1):
                resultado += right
            else:
                resultado -= right

        return resultado


# ==============================
# PRODUCTO
# ==============================

    def visitProducto(self, ctx):

        resultado = self.visit(ctx.unario(0))

        for i in range(1, len(ctx.unario())):

            right = self.visit(ctx.unario(i))

            if ctx.MUL(i-1):
                resultado *= right
            else:
                resultado /= right

        return resultado


# ==============================
# UNARIO
# ==============================

    def visitUnario(self, ctx):

        if ctx.NOT():
            return not self.visit(ctx.unario())

        return self.visit(ctx.primario())


# ==============================
# PRIMARIO
# ==============================

    def visitPrimario(self, ctx):

        if ctx.NUM():
            return int(ctx.NUM().getText())

        if ctx.VAR():
            nombre = ctx.VAR().getText()
            return self.memory.get(nombre, 0)

        if ctx.expr():
            return self.visit(ctx.expr())


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

    input_stream = FileStream("entradas Expr.txt")

    lexer = Expresiones21Lexer(input_stream)

    token_stream = CommonTokenStream(lexer)

    parser = Expresiones21Parser(token_stream)

    tree = parser.root()

    imprimir_arbol(tree, parser)

    visitor = EvalVisitor()

    visitor.visit(tree)

    print("\n=== MEMORIA FINAL ===")

    for var, val in visitor.memory.items():
        print(var, "=", val)


if __name__ == "__main__":
    main()