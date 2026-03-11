# Generated from Expresiones_2.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,132,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,0,1,1,1,1,5,1,37,8,1,10,1,12,1,40,9,1,1,
        1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,51,8,2,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,67,8,5,1,6,1,6,1,7,1,7,1,
        7,5,7,74,8,7,10,7,12,7,77,9,7,1,8,1,8,1,8,5,8,82,8,8,10,8,12,8,85,
        9,8,1,9,1,9,1,9,5,9,90,8,9,10,9,12,9,93,9,9,1,10,1,10,1,10,5,10,
        98,8,10,10,10,12,10,101,9,10,1,11,1,11,1,11,5,11,106,8,11,10,11,
        12,11,109,9,11,1,12,1,12,1,12,5,12,114,8,12,10,12,12,12,117,9,12,
        1,13,1,13,1,13,3,13,122,8,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,
        130,8,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,4,
        1,0,19,21,1,0,15,18,1,0,11,12,1,0,13,14,129,0,30,1,0,0,0,2,34,1,
        0,0,0,4,50,1,0,0,0,6,52,1,0,0,0,8,55,1,0,0,0,10,59,1,0,0,0,12,68,
        1,0,0,0,14,70,1,0,0,0,16,78,1,0,0,0,18,86,1,0,0,0,20,94,1,0,0,0,
        22,102,1,0,0,0,24,110,1,0,0,0,26,121,1,0,0,0,28,129,1,0,0,0,30,31,
        5,1,0,0,31,32,3,2,1,0,32,33,5,0,0,1,33,1,1,0,0,0,34,38,5,7,0,0,35,
        37,3,4,2,0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,
        0,39,41,1,0,0,0,40,38,1,0,0,0,41,42,5,8,0,0,42,3,1,0,0,0,43,44,3,
        6,3,0,44,45,5,9,0,0,45,51,1,0,0,0,46,47,3,8,4,0,47,48,5,9,0,0,48,
        51,1,0,0,0,49,51,3,10,5,0,50,43,1,0,0,0,50,46,1,0,0,0,50,49,1,0,
        0,0,51,5,1,0,0,0,52,53,5,4,0,0,53,54,5,25,0,0,54,7,1,0,0,0,55,56,
        5,25,0,0,56,57,5,10,0,0,57,58,3,12,6,0,58,9,1,0,0,0,59,60,5,2,0,
        0,60,61,5,5,0,0,61,62,3,12,6,0,62,63,5,6,0,0,63,66,3,2,1,0,64,65,
        5,3,0,0,65,67,3,2,1,0,66,64,1,0,0,0,66,67,1,0,0,0,67,11,1,0,0,0,
        68,69,3,14,7,0,69,13,1,0,0,0,70,75,3,16,8,0,71,72,5,23,0,0,72,74,
        3,16,8,0,73,71,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,
        76,15,1,0,0,0,77,75,1,0,0,0,78,83,3,18,9,0,79,80,5,22,0,0,80,82,
        3,18,9,0,81,79,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,
        84,17,1,0,0,0,85,83,1,0,0,0,86,91,3,20,10,0,87,88,7,0,0,0,88,90,
        3,20,10,0,89,87,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,
        0,92,19,1,0,0,0,93,91,1,0,0,0,94,99,3,22,11,0,95,96,7,1,0,0,96,98,
        3,22,11,0,97,95,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,
        0,0,100,21,1,0,0,0,101,99,1,0,0,0,102,107,3,24,12,0,103,104,7,2,
        0,0,104,106,3,24,12,0,105,103,1,0,0,0,106,109,1,0,0,0,107,105,1,
        0,0,0,107,108,1,0,0,0,108,23,1,0,0,0,109,107,1,0,0,0,110,115,3,26,
        13,0,111,112,7,3,0,0,112,114,3,26,13,0,113,111,1,0,0,0,114,117,1,
        0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,25,1,0,0,0,117,115,1,0,
        0,0,118,119,5,24,0,0,119,122,3,26,13,0,120,122,3,28,14,0,121,118,
        1,0,0,0,121,120,1,0,0,0,122,27,1,0,0,0,123,130,5,26,0,0,124,130,
        5,25,0,0,125,126,5,5,0,0,126,127,3,12,6,0,127,128,5,6,0,0,128,130,
        1,0,0,0,129,123,1,0,0,0,129,124,1,0,0,0,129,125,1,0,0,0,130,29,1,
        0,0,0,11,38,50,66,75,83,91,99,107,115,121,129
    ]

class Expresiones_2Parser ( Parser ):

    grammarFileName = "Expresiones_2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'if'", "'else'", "'int'", 
                     "'('", "')'", "'{'", "'}'", "';'", "'='", "'+'", "'-'", 
                     "'/'", "'*'", "'>='", "'<='", "'>'", "'<'", "'=='", 
                     "'<>'", "'!='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "IF", "ELSE", "INT", "PARENI", 
                      "PAREND", "LLAVEI", "LLAVED", "SEMI", "ASSIGN", "SUM", 
                      "REST", "DIV", "MUL", "MAYORIGUAL", "MENORIGUAL", 
                      "MAYOR", "MENOR", "IGUAL", "NOIGUAL", "DIFF", "AND", 
                      "OR", "NOT", "VAR", "NUM", "WS" ]

    RULE_root = 0
    RULE_bloque = 1
    RULE_statement = 2
    RULE_varint = 3
    RULE_asignacion = 4
    RULE_ifstm = 5
    RULE_expr = 6
    RULE_logicalOr = 7
    RULE_logicalAnd = 8
    RULE_igualdad = 9
    RULE_comparacion = 10
    RULE_suma = 11
    RULE_producto = 12
    RULE_unario = 13
    RULE_primario = 14

    ruleNames =  [ "root", "bloque", "statement", "varint", "asignacion", 
                   "ifstm", "expr", "logicalOr", "logicalAnd", "igualdad", 
                   "comparacion", "suma", "producto", "unario", "primario" ]

    EOF = Token.EOF
    PROGRAM=1
    IF=2
    ELSE=3
    INT=4
    PARENI=5
    PAREND=6
    LLAVEI=7
    LLAVED=8
    SEMI=9
    ASSIGN=10
    SUM=11
    REST=12
    DIV=13
    MUL=14
    MAYORIGUAL=15
    MENORIGUAL=16
    MAYOR=17
    MENOR=18
    IGUAL=19
    NOIGUAL=20
    DIFF=21
    AND=22
    OR=23
    NOT=24
    VAR=25
    NUM=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(Expresiones_2Parser.PROGRAM, 0)

        def bloque(self):
            return self.getTypedRuleContext(Expresiones_2Parser.BloqueContext,0)


        def EOF(self):
            return self.getToken(Expresiones_2Parser.EOF, 0)

        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = Expresiones_2Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(Expresiones_2Parser.PROGRAM)
            self.state = 31
            self.bloque()
            self.state = 32
            self.match(Expresiones_2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVEI(self):
            return self.getToken(Expresiones_2Parser.LLAVEI, 0)

        def LLAVED(self):
            return self.getToken(Expresiones_2Parser.LLAVED, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expresiones_2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Expresiones_2Parser.StatementContext,i)


        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = Expresiones_2Parser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(Expresiones_2Parser.LLAVEI)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33554452) != 0):
                self.state = 35
                self.statement()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(Expresiones_2Parser.LLAVED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varint(self):
            return self.getTypedRuleContext(Expresiones_2Parser.VarintContext,0)


        def SEMI(self):
            return self.getToken(Expresiones_2Parser.SEMI, 0)

        def asignacion(self):
            return self.getTypedRuleContext(Expresiones_2Parser.AsignacionContext,0)


        def ifstm(self):
            return self.getTypedRuleContext(Expresiones_2Parser.IfstmContext,0)


        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = Expresiones_2Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.varint()
                self.state = 44
                self.match(Expresiones_2Parser.SEMI)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.asignacion()
                self.state = 47
                self.match(Expresiones_2Parser.SEMI)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.ifstm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(Expresiones_2Parser.INT, 0)

        def VAR(self):
            return self.getToken(Expresiones_2Parser.VAR, 0)

        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_varint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarint" ):
                listener.enterVarint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarint" ):
                listener.exitVarint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarint" ):
                return visitor.visitVarint(self)
            else:
                return visitor.visitChildren(self)




    def varint(self):

        localctx = Expresiones_2Parser.VarintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(Expresiones_2Parser.INT)
            self.state = 53
            self.match(Expresiones_2Parser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(Expresiones_2Parser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(Expresiones_2Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(Expresiones_2Parser.ExprContext,0)


        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = Expresiones_2Parser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(Expresiones_2Parser.VAR)
            self.state = 56
            self.match(Expresiones_2Parser.ASSIGN)
            self.state = 57
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Expresiones_2Parser.IF, 0)

        def PARENI(self):
            return self.getToken(Expresiones_2Parser.PARENI, 0)

        def expr(self):
            return self.getTypedRuleContext(Expresiones_2Parser.ExprContext,0)


        def PAREND(self):
            return self.getToken(Expresiones_2Parser.PAREND, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expresiones_2Parser.BloqueContext)
            else:
                return self.getTypedRuleContext(Expresiones_2Parser.BloqueContext,i)


        def ELSE(self):
            return self.getToken(Expresiones_2Parser.ELSE, 0)

        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_ifstm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstm" ):
                listener.enterIfstm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstm" ):
                listener.exitIfstm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstm" ):
                return visitor.visitIfstm(self)
            else:
                return visitor.visitChildren(self)




    def ifstm(self):

        localctx = Expresiones_2Parser.IfstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifstm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(Expresiones_2Parser.IF)
            self.state = 60
            self.match(Expresiones_2Parser.PARENI)
            self.state = 61
            self.expr()
            self.state = 62
            self.match(Expresiones_2Parser.PAREND)
            self.state = 63
            self.bloque()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 64
                self.match(Expresiones_2Parser.ELSE)
                self.state = 65
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOr(self):
            return self.getTypedRuleContext(Expresiones_2Parser.LogicalOrContext,0)


        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = Expresiones_2Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.logicalOr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expresiones_2Parser.LogicalAndContext)
            else:
                return self.getTypedRuleContext(Expresiones_2Parser.LogicalAndContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.OR)
            else:
                return self.getToken(Expresiones_2Parser.OR, i)

        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_logicalOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOr" ):
                listener.enterLogicalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOr" ):
                listener.exitLogicalOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
            else:
                return visitor.visitChildren(self)




    def logicalOr(self):

        localctx = Expresiones_2Parser.LogicalOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_logicalOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.logicalAnd()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 71
                self.match(Expresiones_2Parser.OR)
                self.state = 72
                self.logicalAnd()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def igualdad(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expresiones_2Parser.IgualdadContext)
            else:
                return self.getTypedRuleContext(Expresiones_2Parser.IgualdadContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.AND)
            else:
                return self.getToken(Expresiones_2Parser.AND, i)

        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_logicalAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAnd" ):
                listener.enterLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAnd" ):
                listener.exitLogicalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)




    def logicalAnd(self):

        localctx = Expresiones_2Parser.LogicalAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_logicalAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.igualdad()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 79
                self.match(Expresiones_2Parser.AND)
                self.state = 80
                self.igualdad()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgualdadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expresiones_2Parser.ComparacionContext)
            else:
                return self.getTypedRuleContext(Expresiones_2Parser.ComparacionContext,i)


        def IGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.IGUAL)
            else:
                return self.getToken(Expresiones_2Parser.IGUAL, i)

        def NOIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.NOIGUAL)
            else:
                return self.getToken(Expresiones_2Parser.NOIGUAL, i)

        def DIFF(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.DIFF)
            else:
                return self.getToken(Expresiones_2Parser.DIFF, i)

        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_igualdad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgualdad" ):
                listener.enterIgualdad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgualdad" ):
                listener.exitIgualdad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgualdad" ):
                return visitor.visitIgualdad(self)
            else:
                return visitor.visitChildren(self)




    def igualdad(self):

        localctx = Expresiones_2Parser.IgualdadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_igualdad)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.comparacion()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0):
                self.state = 87
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 88
                self.comparacion()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def suma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expresiones_2Parser.SumaContext)
            else:
                return self.getTypedRuleContext(Expresiones_2Parser.SumaContext,i)


        def MAYOR(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.MAYOR)
            else:
                return self.getToken(Expresiones_2Parser.MAYOR, i)

        def MENOR(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.MENOR)
            else:
                return self.getToken(Expresiones_2Parser.MENOR, i)

        def MAYORIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.MAYORIGUAL)
            else:
                return self.getToken(Expresiones_2Parser.MAYORIGUAL, i)

        def MENORIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.MENORIGUAL)
            else:
                return self.getToken(Expresiones_2Parser.MENORIGUAL, i)

        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_comparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)




    def comparacion(self):

        localctx = Expresiones_2Parser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.suma()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0):
                self.state = 95
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 96
                self.suma()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def producto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expresiones_2Parser.ProductoContext)
            else:
                return self.getTypedRuleContext(Expresiones_2Parser.ProductoContext,i)


        def SUM(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.SUM)
            else:
                return self.getToken(Expresiones_2Parser.SUM, i)

        def REST(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.REST)
            else:
                return self.getToken(Expresiones_2Parser.REST, i)

        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_suma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)




    def suma(self):

        localctx = Expresiones_2Parser.SumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_suma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.producto()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==12:
                self.state = 103
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 104
                self.producto()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProductoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expresiones_2Parser.UnarioContext)
            else:
                return self.getTypedRuleContext(Expresiones_2Parser.UnarioContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.MUL)
            else:
                return self.getToken(Expresiones_2Parser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones_2Parser.DIV)
            else:
                return self.getToken(Expresiones_2Parser.DIV, i)

        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_producto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProducto" ):
                listener.enterProducto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProducto" ):
                listener.exitProducto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProducto" ):
                return visitor.visitProducto(self)
            else:
                return visitor.visitChildren(self)




    def producto(self):

        localctx = Expresiones_2Parser.ProductoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_producto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.unario()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 111
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 112
                self.unario()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(Expresiones_2Parser.NOT, 0)

        def unario(self):
            return self.getTypedRuleContext(Expresiones_2Parser.UnarioContext,0)


        def primario(self):
            return self.getTypedRuleContext(Expresiones_2Parser.PrimarioContext,0)


        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_unario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnario" ):
                listener.enterUnario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnario" ):
                listener.exitUnario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnario" ):
                return visitor.visitUnario(self)
            else:
                return visitor.visitChildren(self)




    def unario(self):

        localctx = Expresiones_2Parser.UnarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_unario)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(Expresiones_2Parser.NOT)
                self.state = 119
                self.unario()
                pass
            elif token in [5, 25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.primario()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(Expresiones_2Parser.NUM, 0)

        def VAR(self):
            return self.getToken(Expresiones_2Parser.VAR, 0)

        def PARENI(self):
            return self.getToken(Expresiones_2Parser.PARENI, 0)

        def expr(self):
            return self.getTypedRuleContext(Expresiones_2Parser.ExprContext,0)


        def PAREND(self):
            return self.getToken(Expresiones_2Parser.PAREND, 0)

        def getRuleIndex(self):
            return Expresiones_2Parser.RULE_primario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimario" ):
                listener.enterPrimario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimario" ):
                listener.exitPrimario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimario" ):
                return visitor.visitPrimario(self)
            else:
                return visitor.visitChildren(self)




    def primario(self):

        localctx = Expresiones_2Parser.PrimarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primario)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(Expresiones_2Parser.NUM)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(Expresiones_2Parser.VAR)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.match(Expresiones_2Parser.PARENI)
                self.state = 126
                self.expr()
                self.state = 127
                self.match(Expresiones_2Parser.PAREND)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





