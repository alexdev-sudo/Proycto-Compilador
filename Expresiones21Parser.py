# Generated from Expresiones21.g4 by ANTLR 4.13.2
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
        4,1,36,171,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,0,1,0,1,0,1,1,1,1,5,1,48,8,1,10,1,12,1,51,9,1,1,1,1,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,64,8,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,3,3,74,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,8,1,8,1,9,1,9,1,9,5,9,109,8,9,10,9,12,9,112,9,9,1,10,1,10,
        1,10,5,10,117,8,10,10,10,12,10,120,9,10,1,11,1,11,1,11,5,11,125,
        8,11,10,11,12,11,128,9,11,1,12,1,12,1,12,5,12,133,8,12,10,12,12,
        12,136,9,12,1,13,1,13,1,13,5,13,141,8,13,10,13,12,13,144,9,13,1,
        14,1,14,1,14,5,14,149,8,14,10,14,12,14,152,9,14,1,15,1,15,1,15,3,
        15,157,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,
        16,169,8,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,0,4,1,0,26,28,1,0,22,25,1,0,18,19,1,0,20,21,175,0,37,1,0,0,
        0,2,45,1,0,0,0,4,63,1,0,0,0,6,73,1,0,0,0,8,75,1,0,0,0,10,79,1,0,
        0,0,12,87,1,0,0,0,14,93,1,0,0,0,16,103,1,0,0,0,18,105,1,0,0,0,20,
        113,1,0,0,0,22,121,1,0,0,0,24,129,1,0,0,0,26,137,1,0,0,0,28,145,
        1,0,0,0,30,156,1,0,0,0,32,168,1,0,0,0,34,36,5,1,0,0,35,34,1,0,0,
        0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,
        1,0,0,0,40,41,5,2,0,0,41,42,3,2,1,0,42,43,5,3,0,0,43,44,5,0,0,1,
        44,1,1,0,0,0,45,49,5,2,0,0,46,48,3,4,2,0,47,46,1,0,0,0,48,51,1,0,
        0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,
        5,3,0,0,53,3,1,0,0,0,54,55,3,6,3,0,55,56,5,16,0,0,56,64,1,0,0,0,
        57,58,3,8,4,0,58,59,5,16,0,0,59,64,1,0,0,0,60,64,3,10,5,0,61,64,
        3,12,6,0,62,64,3,14,7,0,63,54,1,0,0,0,63,57,1,0,0,0,63,60,1,0,0,
        0,63,61,1,0,0,0,63,62,1,0,0,0,64,5,1,0,0,0,65,66,5,6,0,0,66,74,5,
        32,0,0,67,68,5,7,0,0,68,74,5,32,0,0,69,70,5,8,0,0,70,74,5,32,0,0,
        71,72,5,9,0,0,72,74,5,32,0,0,73,65,1,0,0,0,73,67,1,0,0,0,73,69,1,
        0,0,0,73,71,1,0,0,0,74,7,1,0,0,0,75,76,5,32,0,0,76,77,5,17,0,0,77,
        78,3,16,8,0,78,9,1,0,0,0,79,80,5,4,0,0,80,81,5,14,0,0,81,82,3,16,
        8,0,82,83,5,15,0,0,83,84,3,2,1,0,84,85,5,5,0,0,85,86,3,2,1,0,86,
        11,1,0,0,0,87,88,5,11,0,0,88,89,5,14,0,0,89,90,3,16,8,0,90,91,5,
        15,0,0,91,92,3,2,1,0,92,13,1,0,0,0,93,94,5,13,0,0,94,95,5,14,0,0,
        95,96,3,8,4,0,96,97,5,16,0,0,97,98,3,16,8,0,98,99,5,16,0,0,99,100,
        3,8,4,0,100,101,5,15,0,0,101,102,3,2,1,0,102,15,1,0,0,0,103,104,
        3,18,9,0,104,17,1,0,0,0,105,110,3,20,10,0,106,107,5,30,0,0,107,109,
        3,20,10,0,108,106,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,
        1,0,0,0,111,19,1,0,0,0,112,110,1,0,0,0,113,118,3,22,11,0,114,115,
        5,29,0,0,115,117,3,22,11,0,116,114,1,0,0,0,117,120,1,0,0,0,118,116,
        1,0,0,0,118,119,1,0,0,0,119,21,1,0,0,0,120,118,1,0,0,0,121,126,3,
        24,12,0,122,123,7,0,0,0,123,125,3,24,12,0,124,122,1,0,0,0,125,128,
        1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,23,1,0,0,0,128,126,1,
        0,0,0,129,134,3,26,13,0,130,131,7,1,0,0,131,133,3,26,13,0,132,130,
        1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,25,1,
        0,0,0,136,134,1,0,0,0,137,142,3,28,14,0,138,139,7,2,0,0,139,141,
        3,28,14,0,140,138,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,
        1,0,0,0,143,27,1,0,0,0,144,142,1,0,0,0,145,150,3,30,15,0,146,147,
        7,3,0,0,147,149,3,30,15,0,148,146,1,0,0,0,149,152,1,0,0,0,150,148,
        1,0,0,0,150,151,1,0,0,0,151,29,1,0,0,0,152,150,1,0,0,0,153,154,5,
        31,0,0,154,157,3,30,15,0,155,157,3,32,16,0,156,153,1,0,0,0,156,155,
        1,0,0,0,157,31,1,0,0,0,158,169,5,33,0,0,159,169,5,34,0,0,160,169,
        5,35,0,0,161,169,5,10,0,0,162,169,5,12,0,0,163,169,5,32,0,0,164,
        165,5,14,0,0,165,166,3,16,8,0,166,167,5,15,0,0,167,169,1,0,0,0,168,
        158,1,0,0,0,168,159,1,0,0,0,168,160,1,0,0,0,168,161,1,0,0,0,168,
        162,1,0,0,0,168,163,1,0,0,0,168,164,1,0,0,0,169,33,1,0,0,0,12,37,
        49,63,73,110,118,126,134,142,150,156,168
    ]

class Expresiones21Parser ( Parser ):

    grammarFileName = "Expresiones21.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program {'", "'{'", "'}'", "'if'", "'else'", 
                     "'int'", "'float'", "'string'", "'bool'", "'true'", 
                     "'while'", "'false'", "'for'", "'('", "')'", "';'", 
                     "'='", "'+'", "'-'", "'/'", "'*'", "'>='", "'<='", 
                     "'>'", "'<'", "'=='", "'<>'", "'!='", "'&&'", "'||'", 
                     "'!'" ]

    symbolicNames = [ "<INVALID>", "INI", "INILLAVE", "FIN", "IF", "ELSE", 
                      "INT", "FLOAT", "STRING", "BOOL", "TRUE", "WHILE", 
                      "FALSE", "FOR", "PARENI", "PAREND", "SEMI", "ASSIGN", 
                      "SUM", "REST", "DIV", "MUL", "MAYORIGUAL", "MENORIGUAL", 
                      "MAYOR", "MENOR", "IGUAL", "NOIGUAL", "DIFF", "AND", 
                      "OR", "NOT", "VAR", "NUM", "FNUM", "STRVAL", "WS" ]

    RULE_root = 0
    RULE_bloque = 1
    RULE_statement = 2
    RULE_varint = 3
    RULE_asignacion = 4
    RULE_ifstm = 5
    RULE_whilestm = 6
    RULE_forstm = 7
    RULE_expr = 8
    RULE_logicalOr = 9
    RULE_logicalAnd = 10
    RULE_igualdad = 11
    RULE_comparacion = 12
    RULE_suma = 13
    RULE_producto = 14
    RULE_unario = 15
    RULE_primario = 16

    ruleNames =  [ "root", "bloque", "statement", "varint", "asignacion", 
                   "ifstm", "whilestm", "forstm", "expr", "logicalOr", "logicalAnd", 
                   "igualdad", "comparacion", "suma", "producto", "unario", 
                   "primario" ]

    EOF = Token.EOF
    INI=1
    INILLAVE=2
    FIN=3
    IF=4
    ELSE=5
    INT=6
    FLOAT=7
    STRING=8
    BOOL=9
    TRUE=10
    WHILE=11
    FALSE=12
    FOR=13
    PARENI=14
    PAREND=15
    SEMI=16
    ASSIGN=17
    SUM=18
    REST=19
    DIV=20
    MUL=21
    MAYORIGUAL=22
    MENORIGUAL=23
    MAYOR=24
    MENOR=25
    IGUAL=26
    NOIGUAL=27
    DIFF=28
    AND=29
    OR=30
    NOT=31
    VAR=32
    NUM=33
    FNUM=34
    STRVAL=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INILLAVE(self):
            return self.getToken(Expresiones21Parser.INILLAVE, 0)

        def bloque(self):
            return self.getTypedRuleContext(Expresiones21Parser.BloqueContext,0)


        def FIN(self):
            return self.getToken(Expresiones21Parser.FIN, 0)

        def EOF(self):
            return self.getToken(Expresiones21Parser.EOF, 0)

        def INI(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.INI)
            else:
                return self.getToken(Expresiones21Parser.INI, i)

        def getRuleIndex(self):
            return Expresiones21Parser.RULE_root

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

        localctx = Expresiones21Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 34
                self.match(Expresiones21Parser.INI)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(Expresiones21Parser.INILLAVE)
            self.state = 41
            self.bloque()
            self.state = 42
            self.match(Expresiones21Parser.FIN)
            self.state = 43
            self.match(Expresiones21Parser.EOF)
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

        def INILLAVE(self):
            return self.getToken(Expresiones21Parser.INILLAVE, 0)

        def FIN(self):
            return self.getToken(Expresiones21Parser.FIN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expresiones21Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Expresiones21Parser.StatementContext,i)


        def getRuleIndex(self):
            return Expresiones21Parser.RULE_bloque

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

        localctx = Expresiones21Parser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(Expresiones21Parser.INILLAVE)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4294978512) != 0):
                self.state = 46
                self.statement()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(Expresiones21Parser.FIN)
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
            return self.getTypedRuleContext(Expresiones21Parser.VarintContext,0)


        def SEMI(self):
            return self.getToken(Expresiones21Parser.SEMI, 0)

        def asignacion(self):
            return self.getTypedRuleContext(Expresiones21Parser.AsignacionContext,0)


        def ifstm(self):
            return self.getTypedRuleContext(Expresiones21Parser.IfstmContext,0)


        def whilestm(self):
            return self.getTypedRuleContext(Expresiones21Parser.WhilestmContext,0)


        def forstm(self):
            return self.getTypedRuleContext(Expresiones21Parser.ForstmContext,0)


        def getRuleIndex(self):
            return Expresiones21Parser.RULE_statement

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

        localctx = Expresiones21Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.varint()
                self.state = 55
                self.match(Expresiones21Parser.SEMI)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.asignacion()
                self.state = 58
                self.match(Expresiones21Parser.SEMI)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.ifstm()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.whilestm()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 62
                self.forstm()
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
            return self.getToken(Expresiones21Parser.INT, 0)

        def VAR(self):
            return self.getToken(Expresiones21Parser.VAR, 0)

        def FLOAT(self):
            return self.getToken(Expresiones21Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(Expresiones21Parser.STRING, 0)

        def BOOL(self):
            return self.getToken(Expresiones21Parser.BOOL, 0)

        def getRuleIndex(self):
            return Expresiones21Parser.RULE_varint

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

        localctx = Expresiones21Parser.VarintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varint)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(Expresiones21Parser.INT)
                self.state = 66
                self.match(Expresiones21Parser.VAR)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(Expresiones21Parser.FLOAT)
                self.state = 68
                self.match(Expresiones21Parser.VAR)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.match(Expresiones21Parser.STRING)
                self.state = 70
                self.match(Expresiones21Parser.VAR)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.match(Expresiones21Parser.BOOL)
                self.state = 72
                self.match(Expresiones21Parser.VAR)
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


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(Expresiones21Parser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(Expresiones21Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(Expresiones21Parser.ExprContext,0)


        def getRuleIndex(self):
            return Expresiones21Parser.RULE_asignacion

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

        localctx = Expresiones21Parser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(Expresiones21Parser.VAR)
            self.state = 76
            self.match(Expresiones21Parser.ASSIGN)
            self.state = 77
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
            return self.getToken(Expresiones21Parser.IF, 0)

        def PARENI(self):
            return self.getToken(Expresiones21Parser.PARENI, 0)

        def expr(self):
            return self.getTypedRuleContext(Expresiones21Parser.ExprContext,0)


        def PAREND(self):
            return self.getToken(Expresiones21Parser.PAREND, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expresiones21Parser.BloqueContext)
            else:
                return self.getTypedRuleContext(Expresiones21Parser.BloqueContext,i)


        def ELSE(self):
            return self.getToken(Expresiones21Parser.ELSE, 0)

        def getRuleIndex(self):
            return Expresiones21Parser.RULE_ifstm

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

        localctx = Expresiones21Parser.IfstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(Expresiones21Parser.IF)
            self.state = 80
            self.match(Expresiones21Parser.PARENI)
            self.state = 81
            self.expr()
            self.state = 82
            self.match(Expresiones21Parser.PAREND)
            self.state = 83
            self.bloque()

            self.state = 84
            self.match(Expresiones21Parser.ELSE)
            self.state = 85
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(Expresiones21Parser.WHILE, 0)

        def PARENI(self):
            return self.getToken(Expresiones21Parser.PARENI, 0)

        def expr(self):
            return self.getTypedRuleContext(Expresiones21Parser.ExprContext,0)


        def PAREND(self):
            return self.getToken(Expresiones21Parser.PAREND, 0)

        def bloque(self):
            return self.getTypedRuleContext(Expresiones21Parser.BloqueContext,0)


        def getRuleIndex(self):
            return Expresiones21Parser.RULE_whilestm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhilestm" ):
                listener.enterWhilestm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhilestm" ):
                listener.exitWhilestm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestm" ):
                return visitor.visitWhilestm(self)
            else:
                return visitor.visitChildren(self)




    def whilestm(self):

        localctx = Expresiones21Parser.WhilestmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whilestm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(Expresiones21Parser.WHILE)
            self.state = 88
            self.match(Expresiones21Parser.PARENI)
            self.state = 89
            self.expr()
            self.state = 90
            self.match(Expresiones21Parser.PAREND)
            self.state = 91
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Expresiones21Parser.FOR, 0)

        def PARENI(self):
            return self.getToken(Expresiones21Parser.PARENI, 0)

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expresiones21Parser.AsignacionContext)
            else:
                return self.getTypedRuleContext(Expresiones21Parser.AsignacionContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.SEMI)
            else:
                return self.getToken(Expresiones21Parser.SEMI, i)

        def expr(self):
            return self.getTypedRuleContext(Expresiones21Parser.ExprContext,0)


        def PAREND(self):
            return self.getToken(Expresiones21Parser.PAREND, 0)

        def bloque(self):
            return self.getTypedRuleContext(Expresiones21Parser.BloqueContext,0)


        def getRuleIndex(self):
            return Expresiones21Parser.RULE_forstm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForstm" ):
                listener.enterForstm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForstm" ):
                listener.exitForstm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstm" ):
                return visitor.visitForstm(self)
            else:
                return visitor.visitChildren(self)




    def forstm(self):

        localctx = Expresiones21Parser.ForstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(Expresiones21Parser.FOR)
            self.state = 94
            self.match(Expresiones21Parser.PARENI)
            self.state = 95
            self.asignacion()
            self.state = 96
            self.match(Expresiones21Parser.SEMI)
            self.state = 97
            self.expr()
            self.state = 98
            self.match(Expresiones21Parser.SEMI)
            self.state = 99
            self.asignacion()
            self.state = 100
            self.match(Expresiones21Parser.PAREND)
            self.state = 101
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
            return self.getTypedRuleContext(Expresiones21Parser.LogicalOrContext,0)


        def getRuleIndex(self):
            return Expresiones21Parser.RULE_expr

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

        localctx = Expresiones21Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
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
                return self.getTypedRuleContexts(Expresiones21Parser.LogicalAndContext)
            else:
                return self.getTypedRuleContext(Expresiones21Parser.LogicalAndContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.OR)
            else:
                return self.getToken(Expresiones21Parser.OR, i)

        def getRuleIndex(self):
            return Expresiones21Parser.RULE_logicalOr

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

        localctx = Expresiones21Parser.LogicalOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_logicalOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.logicalAnd()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 106
                self.match(Expresiones21Parser.OR)
                self.state = 107
                self.logicalAnd()
                self.state = 112
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
                return self.getTypedRuleContexts(Expresiones21Parser.IgualdadContext)
            else:
                return self.getTypedRuleContext(Expresiones21Parser.IgualdadContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.AND)
            else:
                return self.getToken(Expresiones21Parser.AND, i)

        def getRuleIndex(self):
            return Expresiones21Parser.RULE_logicalAnd

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

        localctx = Expresiones21Parser.LogicalAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_logicalAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.igualdad()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 114
                self.match(Expresiones21Parser.AND)
                self.state = 115
                self.igualdad()
                self.state = 120
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
                return self.getTypedRuleContexts(Expresiones21Parser.ComparacionContext)
            else:
                return self.getTypedRuleContext(Expresiones21Parser.ComparacionContext,i)


        def IGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.IGUAL)
            else:
                return self.getToken(Expresiones21Parser.IGUAL, i)

        def NOIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.NOIGUAL)
            else:
                return self.getToken(Expresiones21Parser.NOIGUAL, i)

        def DIFF(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.DIFF)
            else:
                return self.getToken(Expresiones21Parser.DIFF, i)

        def getRuleIndex(self):
            return Expresiones21Parser.RULE_igualdad

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

        localctx = Expresiones21Parser.IgualdadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_igualdad)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.comparacion()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0):
                self.state = 122
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 123
                self.comparacion()
                self.state = 128
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
                return self.getTypedRuleContexts(Expresiones21Parser.SumaContext)
            else:
                return self.getTypedRuleContext(Expresiones21Parser.SumaContext,i)


        def MAYOR(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.MAYOR)
            else:
                return self.getToken(Expresiones21Parser.MAYOR, i)

        def MENOR(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.MENOR)
            else:
                return self.getToken(Expresiones21Parser.MENOR, i)

        def MAYORIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.MAYORIGUAL)
            else:
                return self.getToken(Expresiones21Parser.MAYORIGUAL, i)

        def MENORIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.MENORIGUAL)
            else:
                return self.getToken(Expresiones21Parser.MENORIGUAL, i)

        def getRuleIndex(self):
            return Expresiones21Parser.RULE_comparacion

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

        localctx = Expresiones21Parser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.suma()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0):
                self.state = 130
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 131
                self.suma()
                self.state = 136
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
                return self.getTypedRuleContexts(Expresiones21Parser.ProductoContext)
            else:
                return self.getTypedRuleContext(Expresiones21Parser.ProductoContext,i)


        def SUM(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.SUM)
            else:
                return self.getToken(Expresiones21Parser.SUM, i)

        def REST(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.REST)
            else:
                return self.getToken(Expresiones21Parser.REST, i)

        def getRuleIndex(self):
            return Expresiones21Parser.RULE_suma

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

        localctx = Expresiones21Parser.SumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_suma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.producto()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 138
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 139
                self.producto()
                self.state = 144
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
                return self.getTypedRuleContexts(Expresiones21Parser.UnarioContext)
            else:
                return self.getTypedRuleContext(Expresiones21Parser.UnarioContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.MUL)
            else:
                return self.getToken(Expresiones21Parser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(Expresiones21Parser.DIV)
            else:
                return self.getToken(Expresiones21Parser.DIV, i)

        def getRuleIndex(self):
            return Expresiones21Parser.RULE_producto

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

        localctx = Expresiones21Parser.ProductoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_producto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.unario()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 146
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 147
                self.unario()
                self.state = 152
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
            return self.getToken(Expresiones21Parser.NOT, 0)

        def unario(self):
            return self.getTypedRuleContext(Expresiones21Parser.UnarioContext,0)


        def primario(self):
            return self.getTypedRuleContext(Expresiones21Parser.PrimarioContext,0)


        def getRuleIndex(self):
            return Expresiones21Parser.RULE_unario

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

        localctx = Expresiones21Parser.UnarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_unario)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(Expresiones21Parser.NOT)
                self.state = 154
                self.unario()
                pass
            elif token in [10, 12, 14, 32, 33, 34, 35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
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
            return self.getToken(Expresiones21Parser.NUM, 0)

        def FNUM(self):
            return self.getToken(Expresiones21Parser.FNUM, 0)

        def STRVAL(self):
            return self.getToken(Expresiones21Parser.STRVAL, 0)

        def TRUE(self):
            return self.getToken(Expresiones21Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(Expresiones21Parser.FALSE, 0)

        def VAR(self):
            return self.getToken(Expresiones21Parser.VAR, 0)

        def PARENI(self):
            return self.getToken(Expresiones21Parser.PARENI, 0)

        def expr(self):
            return self.getTypedRuleContext(Expresiones21Parser.ExprContext,0)


        def PAREND(self):
            return self.getToken(Expresiones21Parser.PAREND, 0)

        def getRuleIndex(self):
            return Expresiones21Parser.RULE_primario

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

        localctx = Expresiones21Parser.PrimarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_primario)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(Expresiones21Parser.NUM)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(Expresiones21Parser.FNUM)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.match(Expresiones21Parser.STRVAL)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.match(Expresiones21Parser.TRUE)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                self.match(Expresiones21Parser.FALSE)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 6)
                self.state = 163
                self.match(Expresiones21Parser.VAR)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 164
                self.match(Expresiones21Parser.PARENI)
                self.state = 165
                self.expr()
                self.state = 166
                self.match(Expresiones21Parser.PAREND)
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





