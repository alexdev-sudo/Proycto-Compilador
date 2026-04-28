# Generated from gramatica_v3.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramatica_v3Parser import gramatica_v3Parser
else:
    from gramatica_v3Parser import gramatica_v3Parser

# This class defines a complete generic visitor for a parse tree produced by gramatica_v3Parser.

class gramatica_v3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramatica_v3Parser#exprInput.
    def visitExprInput(self, ctx:gramatica_v3Parser.ExprInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#progInput.
    def visitProgInput(self, ctx:gramatica_v3Parser.ProgInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#programaRule.
    def visitProgramaRule(self, ctx:gramatica_v3Parser.ProgramaRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#bloque.
    def visitBloque(self, ctx:gramatica_v3Parser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#statement.
    def visitStatement(self, ctx:gramatica_v3Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#varint.
    def visitVarint(self, ctx:gramatica_v3Parser.VarintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#asignacion.
    def visitAsignacion(self, ctx:gramatica_v3Parser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#arraydecl.
    def visitArraydecl(self, ctx:gramatica_v3Parser.ArraydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#arrayasign.
    def visitArrayasign(self, ctx:gramatica_v3Parser.ArrayasignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#ifstm.
    def visitIfstm(self, ctx:gramatica_v3Parser.IfstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#whilestm.
    def visitWhilestm(self, ctx:gramatica_v3Parser.WhilestmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#forstm.
    def visitForstm(self, ctx:gramatica_v3Parser.ForstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#tipodato.
    def visitTipodato(self, ctx:gramatica_v3Parser.TipodatoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#parametro.
    def visitParametro(self, ctx:gramatica_v3Parser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#parametros.
    def visitParametros(self, ctx:gramatica_v3Parser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#funcion.
    def visitFuncion(self, ctx:gramatica_v3Parser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#returnstm.
    def visitReturnstm(self, ctx:gramatica_v3Parser.ReturnstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#llamada.
    def visitLlamada(self, ctx:gramatica_v3Parser.LlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#printstm.
    def visitPrintstm(self, ctx:gramatica_v3Parser.PrintstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#expr.
    def visitExpr(self, ctx:gramatica_v3Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#logicalOr.
    def visitLogicalOr(self, ctx:gramatica_v3Parser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#logicalAnd.
    def visitLogicalAnd(self, ctx:gramatica_v3Parser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#igualdad.
    def visitIgualdad(self, ctx:gramatica_v3Parser.IgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#comparacion.
    def visitComparacion(self, ctx:gramatica_v3Parser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#suma.
    def visitSuma(self, ctx:gramatica_v3Parser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#producto.
    def visitProducto(self, ctx:gramatica_v3Parser.ProductoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#unario.
    def visitUnario(self, ctx:gramatica_v3Parser.UnarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v3Parser#primario.
    def visitPrimario(self, ctx:gramatica_v3Parser.PrimarioContext):
        return self.visitChildren(ctx)



del gramatica_v3Parser