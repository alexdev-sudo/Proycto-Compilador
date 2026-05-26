# Generated from gramatica_v4.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gramatica_v4Parser import gramatica_v4Parser
else:
    from gramatica_v4Parser import gramatica_v4Parser

# This class defines a complete generic visitor for a parse tree produced by gramatica_v4Parser.

class gramatica_v4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramatica_v4Parser#exprInput.
    def visitExprInput(self, ctx:gramatica_v4Parser.ExprInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#progInput.
    def visitProgInput(self, ctx:gramatica_v4Parser.ProgInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#programaRule.
    def visitProgramaRule(self, ctx:gramatica_v4Parser.ProgramaRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#bloque.
    def visitBloque(self, ctx:gramatica_v4Parser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#statement.
    def visitStatement(self, ctx:gramatica_v4Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#varint.
    def visitVarint(self, ctx:gramatica_v4Parser.VarintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#asignacion.
    def visitAsignacion(self, ctx:gramatica_v4Parser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#arraydecl.
    def visitArraydecl(self, ctx:gramatica_v4Parser.ArraydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#arrayasign.
    def visitArrayasign(self, ctx:gramatica_v4Parser.ArrayasignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#structdecl.
    def visitStructdecl(self, ctx:gramatica_v4Parser.StructdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#campostruct.
    def visitCampostruct(self, ctx:gramatica_v4Parser.CampostructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#varstruct.
    def visitVarstruct(self, ctx:gramatica_v4Parser.VarstructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#structasign.
    def visitStructasign(self, ctx:gramatica_v4Parser.StructasignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ifstm.
    def visitIfstm(self, ctx:gramatica_v4Parser.IfstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#whilestm.
    def visitWhilestm(self, ctx:gramatica_v4Parser.WhilestmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#forstm.
    def visitForstm(self, ctx:gramatica_v4Parser.ForstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#switchstm.
    def visitSwitchstm(self, ctx:gramatica_v4Parser.SwitchstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#caseclause.
    def visitCaseclause(self, ctx:gramatica_v4Parser.CaseclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#defaultclause.
    def visitDefaultclause(self, ctx:gramatica_v4Parser.DefaultclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#tipodato.
    def visitTipodato(self, ctx:gramatica_v4Parser.TipodatoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#parametro.
    def visitParametro(self, ctx:gramatica_v4Parser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#parametros.
    def visitParametros(self, ctx:gramatica_v4Parser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#funcion.
    def visitFuncion(self, ctx:gramatica_v4Parser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#returnstm.
    def visitReturnstm(self, ctx:gramatica_v4Parser.ReturnstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#breakstm.
    def visitBreakstm(self, ctx:gramatica_v4Parser.BreakstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#continuestm.
    def visitContinuestm(self, ctx:gramatica_v4Parser.ContinuestmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#importstm.
    def visitImportstm(self, ctx:gramatica_v4Parser.ImportstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#llamada.
    def visitLlamada(self, ctx:gramatica_v4Parser.LlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#printstm.
    def visitPrintstm(self, ctx:gramatica_v4Parser.PrintstmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ternario.
    def visitTernario(self, ctx:gramatica_v4Parser.TernarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#exprSimple.
    def visitExprSimple(self, ctx:gramatica_v4Parser.ExprSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#logicalOr.
    def visitLogicalOr(self, ctx:gramatica_v4Parser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#logicalAnd.
    def visitLogicalAnd(self, ctx:gramatica_v4Parser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#igualdad.
    def visitIgualdad(self, ctx:gramatica_v4Parser.IgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#comparacion.
    def visitComparacion(self, ctx:gramatica_v4Parser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#suma.
    def visitSuma(self, ctx:gramatica_v4Parser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#producto.
    def visitProducto(self, ctx:gramatica_v4Parser.ProductoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#unarioNot.
    def visitUnarioNot(self, ctx:gramatica_v4Parser.UnarioNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#unarioCast.
    def visitUnarioCast(self, ctx:gramatica_v4Parser.UnarioCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#unarioPrimario.
    def visitUnarioPrimario(self, ctx:gramatica_v4Parser.UnarioPrimarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#primLlamada.
    def visitPrimLlamada(self, ctx:gramatica_v4Parser.PrimLlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#primArray.
    def visitPrimArray(self, ctx:gramatica_v4Parser.PrimArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#primStructAcceso.
    def visitPrimStructAcceso(self, ctx:gramatica_v4Parser.PrimStructAccesoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#primTrue.
    def visitPrimTrue(self, ctx:gramatica_v4Parser.PrimTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#primFalse.
    def visitPrimFalse(self, ctx:gramatica_v4Parser.PrimFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#primVar.
    def visitPrimVar(self, ctx:gramatica_v4Parser.PrimVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#primNum.
    def visitPrimNum(self, ctx:gramatica_v4Parser.PrimNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#primFnum.
    def visitPrimFnum(self, ctx:gramatica_v4Parser.PrimFnumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#primStr.
    def visitPrimStr(self, ctx:gramatica_v4Parser.PrimStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#primParen.
    def visitPrimParen(self, ctx:gramatica_v4Parser.PrimParenContext):
        return self.visitChildren(ctx)



del gramatica_v4Parser