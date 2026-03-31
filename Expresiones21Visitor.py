# Generated from Expresiones21.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Expresiones21Parser import Expresiones21Parser
else:
    from Expresiones21Parser import Expresiones21Parser

# This class defines a complete generic visitor for a parse tree produced by Expresiones21Parser.

class Expresiones21Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Expresiones21Parser#root.
    def visitRoot(self, ctx:Expresiones21Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#bloque.
    def visitBloque(self, ctx:Expresiones21Parser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#statement.
    def visitStatement(self, ctx:Expresiones21Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#varint.
    def visitVarint(self, ctx:Expresiones21Parser.VarintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#asignacion.
    def visitAsignacion(self, ctx:Expresiones21Parser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#ifstm.
    def visitIfstm(self, ctx:Expresiones21Parser.IfstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#whilestm.
    def visitWhilestm(self, ctx:Expresiones21Parser.WhilestmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#forstm.
    def visitForstm(self, ctx:Expresiones21Parser.ForstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#expr.
    def visitExpr(self, ctx:Expresiones21Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#logicalOr.
    def visitLogicalOr(self, ctx:Expresiones21Parser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#logicalAnd.
    def visitLogicalAnd(self, ctx:Expresiones21Parser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#igualdad.
    def visitIgualdad(self, ctx:Expresiones21Parser.IgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#comparacion.
    def visitComparacion(self, ctx:Expresiones21Parser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#suma.
    def visitSuma(self, ctx:Expresiones21Parser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#producto.
    def visitProducto(self, ctx:Expresiones21Parser.ProductoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#unario.
    def visitUnario(self, ctx:Expresiones21Parser.UnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expresiones21Parser#primario.
    def visitPrimario(self, ctx:Expresiones21Parser.PrimarioContext):
        return self.visitChildren(ctx)



del Expresiones21Parser