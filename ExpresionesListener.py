# Generated from Expresiones.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by ExpresionesParser#Div.
    def enterDiv(self, ctx:ExpresionesParser.DivContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Div.
    def exitDiv(self, ctx:ExpresionesParser.DivContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Numero.
    def enterNumero(self, ctx:ExpresionesParser.NumeroContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Numero.
    def exitNumero(self, ctx:ExpresionesParser.NumeroContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Suma.
    def enterSuma(self, ctx:ExpresionesParser.SumaContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Suma.
    def exitSuma(self, ctx:ExpresionesParser.SumaContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Parentesis.
    def enterParentesis(self, ctx:ExpresionesParser.ParentesisContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Parentesis.
    def exitParentesis(self, ctx:ExpresionesParser.ParentesisContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Multi.
    def enterMulti(self, ctx:ExpresionesParser.MultiContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Multi.
    def exitMulti(self, ctx:ExpresionesParser.MultiContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#Resta.
    def enterResta(self, ctx:ExpresionesParser.RestaContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#Resta.
    def exitResta(self, ctx:ExpresionesParser.RestaContext):
        pass



del ExpresionesParser