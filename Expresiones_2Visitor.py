# Generated from Expresiones_2.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Expresiones_2Parser import Expresiones_2Parser
else:
    from Expresiones_2Parser import Expresiones_2Parser

# This class defines a complete generic visitor for a parse tree produced by Expresiones_2Parser.

class Expresiones_2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Expresiones_2Parser#root.
    def visitRoot(self, ctx:Expresiones_2Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#bloque.
    def visitBloque(self, ctx:Expresiones_2Parser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#statement.
    def visitStatement(self, ctx:Expresiones_2Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#varint.
    def visitVarint(self, ctx:Expresiones_2Parser.VarintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#asignacion.
    def visitAsignacion(self, ctx:Expresiones_2Parser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#ifstm.
    def visitIfstm(self, ctx:Expresiones_2Parser.IfstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#expr.
    def visitExpr(self, ctx:Expresiones_2Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#logicalOr.
    def visitLogicalOr(self, ctx:Expresiones_2Parser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#logicalAnd.
    def visitLogicalAnd(self, ctx:Expresiones_2Parser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#igualdad.
    def visitIgualdad(self, ctx:Expresiones_2Parser.IgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#comparacion.
    def visitComparacion(self, ctx:Expresiones_2Parser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#suma.
    def visitSuma(self, ctx:Expresiones_2Parser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#producto.
    def visitProducto(self, ctx:Expresiones_2Parser.ProductoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#unario.
    def visitUnario(self, ctx:Expresiones_2Parser.UnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones_2Parser#primario.
    def visitPrimario(self, ctx:Expresiones_2Parser.PrimarioContext):
        return self.visitChildren(ctx)



del Expresiones_2Parser