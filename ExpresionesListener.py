# Generated from Expresiones.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpresionesParser import ExpresionesParser
else:
    from ExpresionesParser import ExpresionesParser

# This class defines a complete listener for a parse tree produced by ExpresionesParser.
class ExpresionesListener(ParseTreeListener):

    # Enter a parse tree produced by ExpresionesParser#root.
    def enterRoot(self, ctx:ExpresionesParser.RootContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#root.
    def exitRoot(self, ctx:ExpresionesParser.RootContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#block.
    def enterBlock(self, ctx:ExpresionesParser.BlockContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#block.
    def exitBlock(self, ctx:ExpresionesParser.BlockContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#statement.
    def enterStatement(self, ctx:ExpresionesParser.StatementContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#statement.
    def exitStatement(self, ctx:ExpresionesParser.StatementContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Declaracion.
    def enterDeclaracion(self, ctx:ExpresionesParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Declaracion.
    def exitDeclaracion(self, ctx:ExpresionesParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#DeclaracionAsignacion.
    def enterDeclaracionAsignacion(self, ctx:ExpresionesParser.DeclaracionAsignacionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#DeclaracionAsignacion.
    def exitDeclaracionAsignacion(self, ctx:ExpresionesParser.DeclaracionAsignacionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#ifStmt.
    def enterIfStmt(self, ctx:ExpresionesParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#ifStmt.
    def exitIfStmt(self, ctx:ExpresionesParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#expr.
    def enterExpr(self, ctx:ExpresionesParser.ExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#expr.
    def exitExpr(self, ctx:ExpresionesParser.ExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Asignacion.
    def enterAsignacion(self, ctx:ExpresionesParser.AsignacionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Asignacion.
    def exitAsignacion(self, ctx:ExpresionesParser.AsignacionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#ExprBase.
    def enterExprBase(self, ctx:ExpresionesParser.ExprBaseContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#ExprBase.
    def exitExprBase(self, ctx:ExpresionesParser.ExprBaseContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Or.
    def enterOr(self, ctx:ExpresionesParser.OrContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Or.
    def exitOr(self, ctx:ExpresionesParser.OrContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#And.
    def enterAnd(self, ctx:ExpresionesParser.AndContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#And.
    def exitAnd(self, ctx:ExpresionesParser.AndContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Igualdad.
    def enterIgualdad(self, ctx:ExpresionesParser.IgualdadContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Igualdad.
    def exitIgualdad(self, ctx:ExpresionesParser.IgualdadContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Relacional.
    def enterRelacional(self, ctx:ExpresionesParser.RelacionalContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Relacional.
    def exitRelacional(self, ctx:ExpresionesParser.RelacionalContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#SumaResta.
    def enterSumaResta(self, ctx:ExpresionesParser.SumaRestaContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#SumaResta.
    def exitSumaResta(self, ctx:ExpresionesParser.SumaRestaContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#MultiDiv.
    def enterMultiDiv(self, ctx:ExpresionesParser.MultiDivContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#MultiDiv.
    def exitMultiDiv(self, ctx:ExpresionesParser.MultiDivContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Potencia.
    def enterPotencia(self, ctx:ExpresionesParser.PotenciaContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Potencia.
    def exitPotencia(self, ctx:ExpresionesParser.PotenciaContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Not.
    def enterNot(self, ctx:ExpresionesParser.NotContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Not.
    def exitNot(self, ctx:ExpresionesParser.NotContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#UnaryBase.
    def enterUnaryBase(self, ctx:ExpresionesParser.UnaryBaseContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#UnaryBase.
    def exitUnaryBase(self, ctx:ExpresionesParser.UnaryBaseContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Parentesis.
    def enterParentesis(self, ctx:ExpresionesParser.ParentesisContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Parentesis.
    def exitParentesis(self, ctx:ExpresionesParser.ParentesisContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Corchetes.
    def enterCorchetes(self, ctx:ExpresionesParser.CorchetesContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Corchetes.
    def exitCorchetes(self, ctx:ExpresionesParser.CorchetesContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Numero.
    def enterNumero(self, ctx:ExpresionesParser.NumeroContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Numero.
    def exitNumero(self, ctx:ExpresionesParser.NumeroContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Variable.
    def enterVariable(self, ctx:ExpresionesParser.VariableContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Variable.
    def exitVariable(self, ctx:ExpresionesParser.VariableContext):
        pass



del ExpresionesParser