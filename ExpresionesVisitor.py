# Generated from Expresiones.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExpresionesParser import ExpresionesParser
else:
    from ExpresionesParser import ExpresionesParser

# This class defines a complete generic visitor for a parse tree produced by ExpresionesParser.

class ExpresionesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpresionesParser#root.
    def visitRoot(self, ctx:ExpresionesParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#Div.
    def visitDiv(self, ctx:ExpresionesParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#Numero.
    def visitNumero(self, ctx:ExpresionesParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#Suma.
    def visitSuma(self, ctx:ExpresionesParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#Parentesis.
    def visitParentesis(self, ctx:ExpresionesParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#Multi.
    def visitMulti(self, ctx:ExpresionesParser.MultiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#Resta.
    def visitResta(self, ctx:ExpresionesParser.RestaContext):
        return self.visitChildren(ctx)



del ExpresionesParser