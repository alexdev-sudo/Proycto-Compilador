# Generated from gramatica_v3.g4 by ANTLR 4.13.2
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
        4,1,45,293,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,1,0,1,0,1,0,3,0,65,8,0,1,1,1,1,1,
        1,1,2,1,2,5,2,72,8,2,10,2,12,2,75,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,3,3,102,8,3,1,4,1,4,1,4,1,4,3,4,108,8,4,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,123,8,6,10,6,12,6,126,
        9,6,3,6,128,8,6,1,6,3,6,131,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,3,8,147,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,3,10,159,8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,5,13,176,8,13,10,13,12,13,
        179,9,13,1,14,1,14,1,14,1,14,3,14,185,8,14,1,14,1,14,1,14,1,15,1,
        15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,
        18,5,18,205,8,18,10,18,12,18,208,9,18,3,18,210,8,18,1,18,1,18,1,
        19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,21,1,21,1,21,5,21,225,8,
        21,10,21,12,21,228,9,21,1,22,1,22,1,22,5,22,233,8,22,10,22,12,22,
        236,9,22,1,23,1,23,1,23,5,23,241,8,23,10,23,12,23,244,9,23,1,24,
        1,24,1,24,5,24,249,8,24,10,24,12,24,252,9,24,1,25,1,25,1,25,5,25,
        257,8,25,10,25,12,25,260,9,25,1,26,1,26,1,26,5,26,265,8,26,10,26,
        12,26,268,9,26,1,27,1,27,1,27,3,27,273,8,27,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,
        291,8,28,1,28,0,0,29,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,0,6,1,0,9,12,1,0,9,13,1,0,
        30,32,1,0,26,29,1,0,22,23,2,0,24,25,38,38,302,0,64,1,0,0,0,2,66,
        1,0,0,0,4,69,1,0,0,0,6,101,1,0,0,0,8,103,1,0,0,0,10,109,1,0,0,0,
        12,113,1,0,0,0,14,132,1,0,0,0,16,139,1,0,0,0,18,148,1,0,0,0,20,154,
        1,0,0,0,22,167,1,0,0,0,24,169,1,0,0,0,26,172,1,0,0,0,28,180,1,0,
        0,0,30,189,1,0,0,0,32,193,1,0,0,0,34,196,1,0,0,0,36,199,1,0,0,0,
        38,213,1,0,0,0,40,219,1,0,0,0,42,221,1,0,0,0,44,229,1,0,0,0,46,237,
        1,0,0,0,48,245,1,0,0,0,50,253,1,0,0,0,52,261,1,0,0,0,54,272,1,0,
        0,0,56,290,1,0,0,0,58,59,3,40,20,0,59,60,5,0,0,1,60,65,1,0,0,0,61,
        62,3,2,1,0,62,63,5,0,0,1,63,65,1,0,0,0,64,58,1,0,0,0,64,61,1,0,0,
        0,65,1,1,0,0,0,66,67,5,1,0,0,67,68,3,4,2,0,68,3,1,0,0,0,69,73,5,
        2,0,0,70,72,3,6,3,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,
        74,1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,77,5,3,0,0,77,5,1,0,0,
        0,78,79,3,8,4,0,79,80,5,20,0,0,80,102,1,0,0,0,81,82,3,12,6,0,82,
        83,5,20,0,0,83,102,1,0,0,0,84,85,3,10,5,0,85,86,5,20,0,0,86,102,
        1,0,0,0,87,88,3,14,7,0,88,89,5,20,0,0,89,102,1,0,0,0,90,102,3,16,
        8,0,91,102,3,18,9,0,92,102,3,20,10,0,93,102,3,30,15,0,94,95,3,36,
        18,0,95,96,5,20,0,0,96,102,1,0,0,0,97,102,3,38,19,0,98,102,3,28,
        14,0,99,102,3,32,16,0,100,102,3,34,17,0,101,78,1,0,0,0,101,81,1,
        0,0,0,101,84,1,0,0,0,101,87,1,0,0,0,101,90,1,0,0,0,101,91,1,0,0,
        0,101,92,1,0,0,0,101,93,1,0,0,0,101,94,1,0,0,0,101,97,1,0,0,0,101,
        98,1,0,0,0,101,99,1,0,0,0,101,100,1,0,0,0,102,7,1,0,0,0,103,104,
        7,0,0,0,104,107,5,41,0,0,105,106,5,21,0,0,106,108,3,40,20,0,107,
        105,1,0,0,0,107,108,1,0,0,0,108,9,1,0,0,0,109,110,5,41,0,0,110,111,
        5,21,0,0,111,112,3,40,20,0,112,11,1,0,0,0,113,114,7,0,0,0,114,115,
        5,36,0,0,115,116,5,37,0,0,116,130,5,41,0,0,117,118,5,21,0,0,118,
        127,5,2,0,0,119,124,3,40,20,0,120,121,5,17,0,0,121,123,3,40,20,0,
        122,120,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,
        125,128,1,0,0,0,126,124,1,0,0,0,127,119,1,0,0,0,127,128,1,0,0,0,
        128,129,1,0,0,0,129,131,5,3,0,0,130,117,1,0,0,0,130,131,1,0,0,0,
        131,13,1,0,0,0,132,133,5,41,0,0,133,134,5,36,0,0,134,135,3,40,20,
        0,135,136,5,37,0,0,136,137,5,21,0,0,137,138,3,40,20,0,138,15,1,0,
        0,0,139,140,5,4,0,0,140,141,5,18,0,0,141,142,3,40,20,0,142,143,5,
        19,0,0,143,146,3,4,2,0,144,145,5,5,0,0,145,147,3,4,2,0,146,144,1,
        0,0,0,146,147,1,0,0,0,147,17,1,0,0,0,148,149,5,6,0,0,149,150,5,18,
        0,0,150,151,3,40,20,0,151,152,5,19,0,0,152,153,3,4,2,0,153,19,1,
        0,0,0,154,155,5,7,0,0,155,158,5,18,0,0,156,159,3,8,4,0,157,159,3,
        10,5,0,158,156,1,0,0,0,158,157,1,0,0,0,159,160,1,0,0,0,160,161,5,
        20,0,0,161,162,3,40,20,0,162,163,5,20,0,0,163,164,3,10,5,0,164,165,
        5,19,0,0,165,166,3,4,2,0,166,21,1,0,0,0,167,168,7,1,0,0,168,23,1,
        0,0,0,169,170,3,22,11,0,170,171,5,41,0,0,171,25,1,0,0,0,172,177,
        3,24,12,0,173,174,5,17,0,0,174,176,3,24,12,0,175,173,1,0,0,0,176,
        179,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,27,1,0,0,0,179,177,
        1,0,0,0,180,181,3,22,11,0,181,182,5,41,0,0,182,184,5,18,0,0,183,
        185,3,26,13,0,184,183,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,
        187,5,19,0,0,187,188,3,4,2,0,188,29,1,0,0,0,189,190,5,8,0,0,190,
        191,3,40,20,0,191,192,5,20,0,0,192,31,1,0,0,0,193,194,5,39,0,0,194,
        195,5,20,0,0,195,33,1,0,0,0,196,197,5,40,0,0,197,198,5,20,0,0,198,
        35,1,0,0,0,199,200,5,41,0,0,200,209,5,18,0,0,201,206,3,40,20,0,202,
        203,5,17,0,0,203,205,3,40,20,0,204,202,1,0,0,0,205,208,1,0,0,0,206,
        204,1,0,0,0,206,207,1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,209,
        201,1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,212,5,19,0,0,212,
        37,1,0,0,0,213,214,5,16,0,0,214,215,5,18,0,0,215,216,3,40,20,0,216,
        217,5,19,0,0,217,218,5,20,0,0,218,39,1,0,0,0,219,220,3,42,21,0,220,
        41,1,0,0,0,221,226,3,44,22,0,222,223,5,34,0,0,223,225,3,44,22,0,
        224,222,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,
        227,43,1,0,0,0,228,226,1,0,0,0,229,234,3,46,23,0,230,231,5,33,0,
        0,231,233,3,46,23,0,232,230,1,0,0,0,233,236,1,0,0,0,234,232,1,0,
        0,0,234,235,1,0,0,0,235,45,1,0,0,0,236,234,1,0,0,0,237,242,3,48,
        24,0,238,239,7,2,0,0,239,241,3,48,24,0,240,238,1,0,0,0,241,244,1,
        0,0,0,242,240,1,0,0,0,242,243,1,0,0,0,243,47,1,0,0,0,244,242,1,0,
        0,0,245,250,3,50,25,0,246,247,7,3,0,0,247,249,3,50,25,0,248,246,
        1,0,0,0,249,252,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,49,1,
        0,0,0,252,250,1,0,0,0,253,258,3,52,26,0,254,255,7,4,0,0,255,257,
        3,52,26,0,256,254,1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,0,258,259,
        1,0,0,0,259,51,1,0,0,0,260,258,1,0,0,0,261,266,3,54,27,0,262,263,
        7,5,0,0,263,265,3,54,27,0,264,262,1,0,0,0,265,268,1,0,0,0,266,264,
        1,0,0,0,266,267,1,0,0,0,267,53,1,0,0,0,268,266,1,0,0,0,269,270,5,
        35,0,0,270,273,3,54,27,0,271,273,3,56,28,0,272,269,1,0,0,0,272,271,
        1,0,0,0,273,55,1,0,0,0,274,291,3,36,18,0,275,276,5,41,0,0,276,277,
        5,36,0,0,277,278,3,40,20,0,278,279,5,37,0,0,279,291,1,0,0,0,280,
        291,5,14,0,0,281,291,5,15,0,0,282,291,5,41,0,0,283,291,5,42,0,0,
        284,291,5,43,0,0,285,291,5,44,0,0,286,287,5,18,0,0,287,288,3,40,
        20,0,288,289,5,19,0,0,289,291,1,0,0,0,290,274,1,0,0,0,290,275,1,
        0,0,0,290,280,1,0,0,0,290,281,1,0,0,0,290,282,1,0,0,0,290,283,1,
        0,0,0,290,284,1,0,0,0,290,285,1,0,0,0,290,286,1,0,0,0,291,57,1,0,
        0,0,21,64,73,101,107,124,127,130,146,158,177,184,206,209,226,234,
        242,250,258,266,272,290
    ]

class gramatica_v3Parser ( Parser ):

    grammarFileName = "gramatica_v3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'{'", "'}'", "'if'", "'else'", 
                     "'while'", "'for'", "'return'", "'int'", "'float'", 
                     "'string'", "'bool'", "'void'", "'true'", "'false'", 
                     "'print'", "','", "'('", "')'", "';'", "'='", "'+'", 
                     "'-'", "'/'", "'*'", "'>='", "'<='", "'>'", "'<'", 
                     "'=='", "'<>'", "'!='", "'&&'", "'||'", "'!'", "'['", 
                     "']'", "'%'", "'break'", "'continue'" ]

    symbolicNames = [ "<INVALID>", "INI", "INILLAVE", "FIN", "IF", "ELSE", 
                      "WHILE", "FOR", "RETURN", "INT", "FLOAT", "STRING", 
                      "BOOL", "VOID", "TRUE", "FALSE", "PRINT", "COMMA", 
                      "PARENI", "PAREND", "SEMI", "ASSIGN", "SUM", "REST", 
                      "DIV", "MUL", "MAYORIGUAL", "MENORIGUAL", "MAYOR", 
                      "MENOR", "IGUAL", "NOIGUAL", "DIFF", "AND", "OR", 
                      "NOT", "LBRACKET", "RBRACKET", "MOD", "BREAK", "CONTINUE", 
                      "VAR", "NUM", "FNUM", "STRVAL", "WS" ]

    RULE_root = 0
    RULE_programa = 1
    RULE_bloque = 2
    RULE_statement = 3
    RULE_varint = 4
    RULE_asignacion = 5
    RULE_arraydecl = 6
    RULE_arrayasign = 7
    RULE_ifstm = 8
    RULE_whilestm = 9
    RULE_forstm = 10
    RULE_tipodato = 11
    RULE_parametro = 12
    RULE_parametros = 13
    RULE_funcion = 14
    RULE_returnstm = 15
    RULE_breakstm = 16
    RULE_continuestm = 17
    RULE_llamada = 18
    RULE_printstm = 19
    RULE_expr = 20
    RULE_logicalOr = 21
    RULE_logicalAnd = 22
    RULE_igualdad = 23
    RULE_comparacion = 24
    RULE_suma = 25
    RULE_producto = 26
    RULE_unario = 27
    RULE_primario = 28

    ruleNames =  [ "root", "programa", "bloque", "statement", "varint", 
                   "asignacion", "arraydecl", "arrayasign", "ifstm", "whilestm", 
                   "forstm", "tipodato", "parametro", "parametros", "funcion", 
                   "returnstm", "breakstm", "continuestm", "llamada", "printstm", 
                   "expr", "logicalOr", "logicalAnd", "igualdad", "comparacion", 
                   "suma", "producto", "unario", "primario" ]

    EOF = Token.EOF
    INI=1
    INILLAVE=2
    FIN=3
    IF=4
    ELSE=5
    WHILE=6
    FOR=7
    RETURN=8
    INT=9
    FLOAT=10
    STRING=11
    BOOL=12
    VOID=13
    TRUE=14
    FALSE=15
    PRINT=16
    COMMA=17
    PARENI=18
    PAREND=19
    SEMI=20
    ASSIGN=21
    SUM=22
    REST=23
    DIV=24
    MUL=25
    MAYORIGUAL=26
    MENORIGUAL=27
    MAYOR=28
    MENOR=29
    IGUAL=30
    NOIGUAL=31
    DIFF=32
    AND=33
    OR=34
    NOT=35
    LBRACKET=36
    RBRACKET=37
    MOD=38
    BREAK=39
    CONTINUE=40
    VAR=41
    NUM=42
    FNUM=43
    STRVAL=44
    WS=45

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


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_root

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprInputContext(RootContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.RootContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)

        def EOF(self):
            return self.getToken(gramatica_v3Parser.EOF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprInput" ):
                return visitor.visitExprInput(self)
            else:
                return visitor.visitChildren(self)


    class ProgInputContext(RootContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.RootContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def programa(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ProgramaContext,0)

        def EOF(self):
            return self.getToken(gramatica_v3Parser.EOF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgInput" ):
                return visitor.visitProgInput(self)
            else:
                return visitor.visitChildren(self)



    def root(self):

        localctx = gramatica_v3Parser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 18, 35, 41, 42, 43, 44]:
                localctx = gramatica_v3Parser.ExprInputContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.expr()
                self.state = 59
                self.match(gramatica_v3Parser.EOF)
                pass
            elif token in [1]:
                localctx = gramatica_v3Parser.ProgInputContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.programa()
                self.state = 62
                self.match(gramatica_v3Parser.EOF)
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


    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_programa

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramaRuleContext(ProgramaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v3Parser.ProgramaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INI(self):
            return self.getToken(gramatica_v3Parser.INI, 0)
        def bloque(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BloqueContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramaRule" ):
                return visitor.visitProgramaRule(self)
            else:
                return visitor.visitChildren(self)



    def programa(self):

        localctx = gramatica_v3Parser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programa)
        try:
            localctx = gramatica_v3Parser.ProgramaRuleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(gramatica_v3Parser.INI)
            self.state = 67
            self.bloque()
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
            return self.getToken(gramatica_v3Parser.INILLAVE, 0)

        def FIN(self):
            return self.getToken(gramatica_v3Parser.FIN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.StatementContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.StatementContext,i)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_bloque

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = gramatica_v3Parser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(gramatica_v3Parser.INILLAVE)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3848290779088) != 0):
                self.state = 70
                self.statement()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(gramatica_v3Parser.FIN)
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
            return self.getTypedRuleContext(gramatica_v3Parser.VarintContext,0)


        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def arraydecl(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ArraydeclContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(gramatica_v3Parser.AsignacionContext,0)


        def arrayasign(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ArrayasignContext,0)


        def ifstm(self):
            return self.getTypedRuleContext(gramatica_v3Parser.IfstmContext,0)


        def whilestm(self):
            return self.getTypedRuleContext(gramatica_v3Parser.WhilestmContext,0)


        def forstm(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ForstmContext,0)


        def returnstm(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ReturnstmContext,0)


        def llamada(self):
            return self.getTypedRuleContext(gramatica_v3Parser.LlamadaContext,0)


        def printstm(self):
            return self.getTypedRuleContext(gramatica_v3Parser.PrintstmContext,0)


        def funcion(self):
            return self.getTypedRuleContext(gramatica_v3Parser.FuncionContext,0)


        def breakstm(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BreakstmContext,0)


        def continuestm(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ContinuestmContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gramatica_v3Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.varint()
                self.state = 79
                self.match(gramatica_v3Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.arraydecl()
                self.state = 82
                self.match(gramatica_v3Parser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.asignacion()
                self.state = 85
                self.match(gramatica_v3Parser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.arrayasign()
                self.state = 88
                self.match(gramatica_v3Parser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 90
                self.ifstm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 91
                self.whilestm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 92
                self.forstm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 93
                self.returnstm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 94
                self.llamada()
                self.state = 95
                self.match(gramatica_v3Parser.SEMI)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 97
                self.printstm()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 98
                self.funcion()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 99
                self.breakstm()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 100
                self.continuestm()
                pass


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

        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def INT(self):
            return self.getToken(gramatica_v3Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(gramatica_v3Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(gramatica_v3Parser.STRING, 0)

        def BOOL(self):
            return self.getToken(gramatica_v3Parser.BOOL, 0)

        def ASSIGN(self):
            return self.getToken(gramatica_v3Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_varint

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarint" ):
                return visitor.visitVarint(self)
            else:
                return visitor.visitChildren(self)




    def varint(self):

        localctx = gramatica_v3Parser.VarintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 104
            self.match(gramatica_v3Parser.VAR)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 105
                self.match(gramatica_v3Parser.ASSIGN)
                self.state = 106
                self.expr()


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
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(gramatica_v3Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_asignacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = gramatica_v3Parser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(gramatica_v3Parser.VAR)
            self.state = 110
            self.match(gramatica_v3Parser.ASSIGN)
            self.state = 111
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(gramatica_v3Parser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(gramatica_v3Parser.RBRACKET, 0)

        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def INT(self):
            return self.getToken(gramatica_v3Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(gramatica_v3Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(gramatica_v3Parser.STRING, 0)

        def BOOL(self):
            return self.getToken(gramatica_v3Parser.BOOL, 0)

        def ASSIGN(self):
            return self.getToken(gramatica_v3Parser.ASSIGN, 0)

        def INILLAVE(self):
            return self.getToken(gramatica_v3Parser.INILLAVE, 0)

        def FIN(self):
            return self.getToken(gramatica_v3Parser.FIN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.COMMA)
            else:
                return self.getToken(gramatica_v3Parser.COMMA, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = gramatica_v3Parser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arraydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 114
            self.match(gramatica_v3Parser.LBRACKET)
            self.state = 115
            self.match(gramatica_v3Parser.RBRACKET)
            self.state = 116
            self.match(gramatica_v3Parser.VAR)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 117
                self.match(gramatica_v3Parser.ASSIGN)
                self.state = 118
                self.match(gramatica_v3Parser.INILLAVE)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 33019708882944) != 0):
                    self.state = 119
                    self.expr()
                    self.state = 124
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==17:
                        self.state = 120
                        self.match(gramatica_v3Parser.COMMA)
                        self.state = 121
                        self.expr()
                        self.state = 126
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 129
                self.match(gramatica_v3Parser.FIN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayasignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def LBRACKET(self):
            return self.getToken(gramatica_v3Parser.LBRACKET, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)


        def RBRACKET(self):
            return self.getToken(gramatica_v3Parser.RBRACKET, 0)

        def ASSIGN(self):
            return self.getToken(gramatica_v3Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_arrayasign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayasign" ):
                return visitor.visitArrayasign(self)
            else:
                return visitor.visitChildren(self)




    def arrayasign(self):

        localctx = gramatica_v3Parser.ArrayasignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrayasign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(gramatica_v3Parser.VAR)
            self.state = 133
            self.match(gramatica_v3Parser.LBRACKET)
            self.state = 134
            self.expr()
            self.state = 135
            self.match(gramatica_v3Parser.RBRACKET)
            self.state = 136
            self.match(gramatica_v3Parser.ASSIGN)
            self.state = 137
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
            return self.getToken(gramatica_v3Parser.IF, 0)

        def PARENI(self):
            return self.getToken(gramatica_v3Parser.PARENI, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def PAREND(self):
            return self.getToken(gramatica_v3Parser.PAREND, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.BloqueContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.BloqueContext,i)


        def ELSE(self):
            return self.getToken(gramatica_v3Parser.ELSE, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_ifstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstm" ):
                return visitor.visitIfstm(self)
            else:
                return visitor.visitChildren(self)




    def ifstm(self):

        localctx = gramatica_v3Parser.IfstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifstm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(gramatica_v3Parser.IF)
            self.state = 140
            self.match(gramatica_v3Parser.PARENI)
            self.state = 141
            self.expr()
            self.state = 142
            self.match(gramatica_v3Parser.PAREND)
            self.state = 143
            self.bloque()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 144
                self.match(gramatica_v3Parser.ELSE)
                self.state = 145
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
            return self.getToken(gramatica_v3Parser.WHILE, 0)

        def PARENI(self):
            return self.getToken(gramatica_v3Parser.PARENI, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def PAREND(self):
            return self.getToken(gramatica_v3Parser.PAREND, 0)

        def bloque(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BloqueContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_whilestm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestm" ):
                return visitor.visitWhilestm(self)
            else:
                return visitor.visitChildren(self)




    def whilestm(self):

        localctx = gramatica_v3Parser.WhilestmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whilestm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(gramatica_v3Parser.WHILE)
            self.state = 149
            self.match(gramatica_v3Parser.PARENI)
            self.state = 150
            self.expr()
            self.state = 151
            self.match(gramatica_v3Parser.PAREND)
            self.state = 152
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
            return self.getToken(gramatica_v3Parser.FOR, 0)

        def PARENI(self):
            return self.getToken(gramatica_v3Parser.PARENI, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.SEMI)
            else:
                return self.getToken(gramatica_v3Parser.SEMI, i)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.AsignacionContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.AsignacionContext,i)


        def PAREND(self):
            return self.getToken(gramatica_v3Parser.PAREND, 0)

        def bloque(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BloqueContext,0)


        def varint(self):
            return self.getTypedRuleContext(gramatica_v3Parser.VarintContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_forstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstm" ):
                return visitor.visitForstm(self)
            else:
                return visitor.visitChildren(self)




    def forstm(self):

        localctx = gramatica_v3Parser.ForstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(gramatica_v3Parser.FOR)
            self.state = 155
            self.match(gramatica_v3Parser.PARENI)
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12]:
                self.state = 156
                self.varint()
                pass
            elif token in [41]:
                self.state = 157
                self.asignacion()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 160
            self.match(gramatica_v3Parser.SEMI)
            self.state = 161
            self.expr()
            self.state = 162
            self.match(gramatica_v3Parser.SEMI)
            self.state = 163
            self.asignacion()
            self.state = 164
            self.match(gramatica_v3Parser.PAREND)
            self.state = 165
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipodatoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(gramatica_v3Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(gramatica_v3Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(gramatica_v3Parser.STRING, 0)

        def BOOL(self):
            return self.getToken(gramatica_v3Parser.BOOL, 0)

        def VOID(self):
            return self.getToken(gramatica_v3Parser.VOID, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_tipodato

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipodato" ):
                return visitor.visitTipodato(self)
            else:
                return visitor.visitChildren(self)




    def tipodato(self):

        localctx = gramatica_v3Parser.TipodatoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tipodato)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15872) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipodato(self):
            return self.getTypedRuleContext(gramatica_v3Parser.TipodatoContext,0)


        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_parametro

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = gramatica_v3Parser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.tipodato()
            self.state = 170
            self.match(gramatica_v3Parser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ParametroContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ParametroContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.COMMA)
            else:
                return self.getToken(gramatica_v3Parser.COMMA, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_parametros

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = gramatica_v3Parser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.parametro()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 173
                self.match(gramatica_v3Parser.COMMA)
                self.state = 174
                self.parametro()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipodato(self):
            return self.getTypedRuleContext(gramatica_v3Parser.TipodatoContext,0)


        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def PARENI(self):
            return self.getToken(gramatica_v3Parser.PARENI, 0)

        def PAREND(self):
            return self.getToken(gramatica_v3Parser.PAREND, 0)

        def bloque(self):
            return self.getTypedRuleContext(gramatica_v3Parser.BloqueContext,0)


        def parametros(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ParametrosContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_funcion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = gramatica_v3Parser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.tipodato()
            self.state = 181
            self.match(gramatica_v3Parser.VAR)
            self.state = 182
            self.match(gramatica_v3Parser.PARENI)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15872) != 0):
                self.state = 183
                self.parametros()


            self.state = 186
            self.match(gramatica_v3Parser.PAREND)
            self.state = 187
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(gramatica_v3Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_returnstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstm" ):
                return visitor.visitReturnstm(self)
            else:
                return visitor.visitChildren(self)




    def returnstm(self):

        localctx = gramatica_v3Parser.ReturnstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(gramatica_v3Parser.RETURN)
            self.state = 190
            self.expr()
            self.state = 191
            self.match(gramatica_v3Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(gramatica_v3Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_breakstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstm" ):
                return visitor.visitBreakstm(self)
            else:
                return visitor.visitChildren(self)




    def breakstm(self):

        localctx = gramatica_v3Parser.BreakstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_breakstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(gramatica_v3Parser.BREAK)
            self.state = 194
            self.match(gramatica_v3Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(gramatica_v3Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_continuestm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestm" ):
                return visitor.visitContinuestm(self)
            else:
                return visitor.visitChildren(self)




    def continuestm(self):

        localctx = gramatica_v3Parser.ContinuestmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_continuestm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(gramatica_v3Parser.CONTINUE)
            self.state = 197
            self.match(gramatica_v3Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def PARENI(self):
            return self.getToken(gramatica_v3Parser.PARENI, 0)

        def PAREND(self):
            return self.getToken(gramatica_v3Parser.PAREND, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.COMMA)
            else:
                return self.getToken(gramatica_v3Parser.COMMA, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_llamada

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada" ):
                return visitor.visitLlamada(self)
            else:
                return visitor.visitChildren(self)




    def llamada(self):

        localctx = gramatica_v3Parser.LlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_llamada)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(gramatica_v3Parser.VAR)
            self.state = 200
            self.match(gramatica_v3Parser.PARENI)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 33019708882944) != 0):
                self.state = 201
                self.expr()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 202
                    self.match(gramatica_v3Parser.COMMA)
                    self.state = 203
                    self.expr()
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 211
            self.match(gramatica_v3Parser.PAREND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(gramatica_v3Parser.PRINT, 0)

        def PARENI(self):
            return self.getToken(gramatica_v3Parser.PARENI, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def PAREND(self):
            return self.getToken(gramatica_v3Parser.PAREND, 0)

        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_printstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintstm" ):
                return visitor.visitPrintstm(self)
            else:
                return visitor.visitChildren(self)




    def printstm(self):

        localctx = gramatica_v3Parser.PrintstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_printstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(gramatica_v3Parser.PRINT)
            self.state = 214
            self.match(gramatica_v3Parser.PARENI)
            self.state = 215
            self.expr()
            self.state = 216
            self.match(gramatica_v3Parser.PAREND)
            self.state = 217
            self.match(gramatica_v3Parser.SEMI)
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
            return self.getTypedRuleContext(gramatica_v3Parser.LogicalOrContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = gramatica_v3Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
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
                return self.getTypedRuleContexts(gramatica_v3Parser.LogicalAndContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.LogicalAndContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.OR)
            else:
                return self.getToken(gramatica_v3Parser.OR, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_logicalOr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
            else:
                return visitor.visitChildren(self)




    def logicalOr(self):

        localctx = gramatica_v3Parser.LogicalOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_logicalOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.logicalAnd()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 222
                self.match(gramatica_v3Parser.OR)
                self.state = 223
                self.logicalAnd()
                self.state = 228
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
                return self.getTypedRuleContexts(gramatica_v3Parser.IgualdadContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.IgualdadContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.AND)
            else:
                return self.getToken(gramatica_v3Parser.AND, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_logicalAnd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)




    def logicalAnd(self):

        localctx = gramatica_v3Parser.LogicalAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_logicalAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.igualdad()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 230
                self.match(gramatica_v3Parser.AND)
                self.state = 231
                self.igualdad()
                self.state = 236
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
                return self.getTypedRuleContexts(gramatica_v3Parser.ComparacionContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ComparacionContext,i)


        def IGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.IGUAL)
            else:
                return self.getToken(gramatica_v3Parser.IGUAL, i)

        def NOIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.NOIGUAL)
            else:
                return self.getToken(gramatica_v3Parser.NOIGUAL, i)

        def DIFF(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.DIFF)
            else:
                return self.getToken(gramatica_v3Parser.DIFF, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_igualdad

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgualdad" ):
                return visitor.visitIgualdad(self)
            else:
                return visitor.visitChildren(self)




    def igualdad(self):

        localctx = gramatica_v3Parser.IgualdadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_igualdad)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.comparacion()
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0):
                self.state = 238
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 239
                self.comparacion()
                self.state = 244
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
                return self.getTypedRuleContexts(gramatica_v3Parser.SumaContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.SumaContext,i)


        def MAYOR(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.MAYOR)
            else:
                return self.getToken(gramatica_v3Parser.MAYOR, i)

        def MENOR(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.MENOR)
            else:
                return self.getToken(gramatica_v3Parser.MENOR, i)

        def MAYORIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.MAYORIGUAL)
            else:
                return self.getToken(gramatica_v3Parser.MAYORIGUAL, i)

        def MENORIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.MENORIGUAL)
            else:
                return self.getToken(gramatica_v3Parser.MENORIGUAL, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_comparacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)




    def comparacion(self):

        localctx = gramatica_v3Parser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.suma()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0):
                self.state = 246
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 247
                self.suma()
                self.state = 252
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
                return self.getTypedRuleContexts(gramatica_v3Parser.ProductoContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.ProductoContext,i)


        def SUM(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.SUM)
            else:
                return self.getToken(gramatica_v3Parser.SUM, i)

        def REST(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.REST)
            else:
                return self.getToken(gramatica_v3Parser.REST, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_suma

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)




    def suma(self):

        localctx = gramatica_v3Parser.SumaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_suma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.producto()
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 254
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 255
                self.producto()
                self.state = 260
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
                return self.getTypedRuleContexts(gramatica_v3Parser.UnarioContext)
            else:
                return self.getTypedRuleContext(gramatica_v3Parser.UnarioContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.MUL)
            else:
                return self.getToken(gramatica_v3Parser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.DIV)
            else:
                return self.getToken(gramatica_v3Parser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.MOD)
            else:
                return self.getToken(gramatica_v3Parser.MOD, i)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_producto

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProducto" ):
                return visitor.visitProducto(self)
            else:
                return visitor.visitChildren(self)




    def producto(self):

        localctx = gramatica_v3Parser.ProductoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_producto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.unario()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 274928238592) != 0):
                self.state = 262
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 274928238592) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 263
                self.unario()
                self.state = 268
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
            return self.getToken(gramatica_v3Parser.NOT, 0)

        def unario(self):
            return self.getTypedRuleContext(gramatica_v3Parser.UnarioContext,0)


        def primario(self):
            return self.getTypedRuleContext(gramatica_v3Parser.PrimarioContext,0)


        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_unario

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnario" ):
                return visitor.visitUnario(self)
            else:
                return visitor.visitChildren(self)




    def unario(self):

        localctx = gramatica_v3Parser.UnarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_unario)
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(gramatica_v3Parser.NOT)
                self.state = 270
                self.unario()
                pass
            elif token in [14, 15, 18, 41, 42, 43, 44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
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

        def llamada(self):
            return self.getTypedRuleContext(gramatica_v3Parser.LlamadaContext,0)


        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def LBRACKET(self):
            return self.getToken(gramatica_v3Parser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(gramatica_v3Parser.RBRACKET, 0)

        def TRUE(self):
            return self.getToken(gramatica_v3Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(gramatica_v3Parser.FALSE, 0)

        def NUM(self):
            return self.getToken(gramatica_v3Parser.NUM, 0)

        def FNUM(self):
            return self.getToken(gramatica_v3Parser.FNUM, 0)

        def STRVAL(self):
            return self.getToken(gramatica_v3Parser.STRVAL, 0)

        def PARENI(self):
            return self.getToken(gramatica_v3Parser.PARENI, 0)

        def PAREND(self):
            return self.getToken(gramatica_v3Parser.PAREND, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_primario

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimario" ):
                return visitor.visitPrimario(self)
            else:
                return visitor.visitChildren(self)




    def primario(self):

        localctx = gramatica_v3Parser.PrimarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_primario)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.llamada()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.match(gramatica_v3Parser.VAR)
                self.state = 276
                self.match(gramatica_v3Parser.LBRACKET)
                self.state = 277
                self.expr()
                self.state = 278
                self.match(gramatica_v3Parser.RBRACKET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.match(gramatica_v3Parser.TRUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 281
                self.match(gramatica_v3Parser.FALSE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 282
                self.match(gramatica_v3Parser.VAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 283
                self.match(gramatica_v3Parser.NUM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 284
                self.match(gramatica_v3Parser.FNUM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 285
                self.match(gramatica_v3Parser.STRVAL)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 286
                self.match(gramatica_v3Parser.PARENI)
                self.state = 287
                self.expr()
                self.state = 288
                self.match(gramatica_v3Parser.PAREND)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





