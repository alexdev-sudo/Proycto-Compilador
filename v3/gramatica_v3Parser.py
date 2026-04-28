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
        4,1,46,300,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,1,0,1,0,1,0,3,0,67,8,0,
        1,1,1,1,1,1,1,2,1,2,5,2,74,8,2,10,2,12,2,77,9,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,105,8,3,1,4,1,4,1,4,1,4,3,4,111,8,4,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,126,8,6,
        10,6,12,6,129,9,6,3,6,131,8,6,1,6,3,6,134,8,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,150,8,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,162,8,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,5,13,179,
        8,13,10,13,12,13,182,9,13,1,14,1,14,1,14,1,14,3,14,188,8,14,1,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,
        1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,5,19,212,8,19,10,19,12,19,
        215,9,19,3,19,217,8,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,
        21,1,21,1,22,1,22,1,22,5,22,232,8,22,10,22,12,22,235,9,22,1,23,1,
        23,1,23,5,23,240,8,23,10,23,12,23,243,9,23,1,24,1,24,1,24,5,24,248,
        8,24,10,24,12,24,251,9,24,1,25,1,25,1,25,5,25,256,8,25,10,25,12,
        25,259,9,25,1,26,1,26,1,26,5,26,264,8,26,10,26,12,26,267,9,26,1,
        27,1,27,1,27,5,27,272,8,27,10,27,12,27,275,9,27,1,28,1,28,1,28,3,
        28,280,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,1,29,1,29,1,29,3,29,298,8,29,1,29,0,0,30,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
        54,56,58,0,6,1,0,12,15,1,0,12,16,1,0,36,38,1,0,32,35,1,0,27,28,1,
        0,29,31,309,0,66,1,0,0,0,2,68,1,0,0,0,4,71,1,0,0,0,6,104,1,0,0,0,
        8,106,1,0,0,0,10,112,1,0,0,0,12,116,1,0,0,0,14,135,1,0,0,0,16,142,
        1,0,0,0,18,151,1,0,0,0,20,157,1,0,0,0,22,170,1,0,0,0,24,172,1,0,
        0,0,26,175,1,0,0,0,28,183,1,0,0,0,30,192,1,0,0,0,32,196,1,0,0,0,
        34,199,1,0,0,0,36,202,1,0,0,0,38,206,1,0,0,0,40,220,1,0,0,0,42,226,
        1,0,0,0,44,228,1,0,0,0,46,236,1,0,0,0,48,244,1,0,0,0,50,252,1,0,
        0,0,52,260,1,0,0,0,54,268,1,0,0,0,56,279,1,0,0,0,58,297,1,0,0,0,
        60,61,3,42,21,0,61,62,5,0,0,1,62,67,1,0,0,0,63,64,3,2,1,0,64,65,
        5,0,0,1,65,67,1,0,0,0,66,60,1,0,0,0,66,63,1,0,0,0,67,1,1,0,0,0,68,
        69,5,1,0,0,69,70,3,4,2,0,70,3,1,0,0,0,71,75,5,2,0,0,72,74,3,6,3,
        0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,
        1,0,0,0,77,75,1,0,0,0,78,79,5,3,0,0,79,5,1,0,0,0,80,81,3,8,4,0,81,
        82,5,25,0,0,82,105,1,0,0,0,83,84,3,12,6,0,84,85,5,25,0,0,85,105,
        1,0,0,0,86,87,3,10,5,0,87,88,5,25,0,0,88,105,1,0,0,0,89,90,3,14,
        7,0,90,91,5,25,0,0,91,105,1,0,0,0,92,105,3,16,8,0,93,105,3,18,9,
        0,94,105,3,20,10,0,95,105,3,30,15,0,96,97,3,38,19,0,97,98,5,25,0,
        0,98,105,1,0,0,0,99,105,3,40,20,0,100,105,3,28,14,0,101,105,3,32,
        16,0,102,105,3,34,17,0,103,105,3,36,18,0,104,80,1,0,0,0,104,83,1,
        0,0,0,104,86,1,0,0,0,104,89,1,0,0,0,104,92,1,0,0,0,104,93,1,0,0,
        0,104,94,1,0,0,0,104,95,1,0,0,0,104,96,1,0,0,0,104,99,1,0,0,0,104,
        100,1,0,0,0,104,101,1,0,0,0,104,102,1,0,0,0,104,103,1,0,0,0,105,
        7,1,0,0,0,106,107,7,0,0,0,107,110,5,42,0,0,108,109,5,26,0,0,109,
        111,3,42,21,0,110,108,1,0,0,0,110,111,1,0,0,0,111,9,1,0,0,0,112,
        113,5,42,0,0,113,114,5,26,0,0,114,115,3,42,21,0,115,11,1,0,0,0,116,
        117,7,0,0,0,117,118,5,21,0,0,118,119,5,22,0,0,119,133,5,42,0,0,120,
        121,5,26,0,0,121,130,5,21,0,0,122,127,3,42,21,0,123,124,5,20,0,0,
        124,126,3,42,21,0,125,123,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,
        0,127,128,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,130,122,1,0,0,
        0,130,131,1,0,0,0,131,132,1,0,0,0,132,134,5,22,0,0,133,120,1,0,0,
        0,133,134,1,0,0,0,134,13,1,0,0,0,135,136,5,42,0,0,136,137,5,21,0,
        0,137,138,3,42,21,0,138,139,5,22,0,0,139,140,5,26,0,0,140,141,3,
        42,21,0,141,15,1,0,0,0,142,143,5,4,0,0,143,144,5,23,0,0,144,145,
        3,42,21,0,145,146,5,24,0,0,146,149,3,4,2,0,147,148,5,5,0,0,148,150,
        3,4,2,0,149,147,1,0,0,0,149,150,1,0,0,0,150,17,1,0,0,0,151,152,5,
        6,0,0,152,153,5,23,0,0,153,154,3,42,21,0,154,155,5,24,0,0,155,156,
        3,4,2,0,156,19,1,0,0,0,157,158,5,7,0,0,158,161,5,23,0,0,159,162,
        3,8,4,0,160,162,3,10,5,0,161,159,1,0,0,0,161,160,1,0,0,0,162,163,
        1,0,0,0,163,164,5,25,0,0,164,165,3,42,21,0,165,166,5,25,0,0,166,
        167,3,10,5,0,167,168,5,24,0,0,168,169,3,4,2,0,169,21,1,0,0,0,170,
        171,7,1,0,0,171,23,1,0,0,0,172,173,3,22,11,0,173,174,5,42,0,0,174,
        25,1,0,0,0,175,180,3,24,12,0,176,177,5,20,0,0,177,179,3,24,12,0,
        178,176,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,
        181,27,1,0,0,0,182,180,1,0,0,0,183,184,3,22,11,0,184,185,5,42,0,
        0,185,187,5,23,0,0,186,188,3,26,13,0,187,186,1,0,0,0,187,188,1,0,
        0,0,188,189,1,0,0,0,189,190,5,24,0,0,190,191,3,4,2,0,191,29,1,0,
        0,0,192,193,5,8,0,0,193,194,3,42,21,0,194,195,5,25,0,0,195,31,1,
        0,0,0,196,197,5,9,0,0,197,198,5,25,0,0,198,33,1,0,0,0,199,200,5,
        10,0,0,200,201,5,25,0,0,201,35,1,0,0,0,202,203,5,11,0,0,203,204,
        5,42,0,0,204,205,5,25,0,0,205,37,1,0,0,0,206,207,5,42,0,0,207,216,
        5,23,0,0,208,213,3,42,21,0,209,210,5,20,0,0,210,212,3,42,21,0,211,
        209,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,
        217,1,0,0,0,215,213,1,0,0,0,216,208,1,0,0,0,216,217,1,0,0,0,217,
        218,1,0,0,0,218,219,5,24,0,0,219,39,1,0,0,0,220,221,5,19,0,0,221,
        222,5,23,0,0,222,223,3,42,21,0,223,224,5,24,0,0,224,225,5,25,0,0,
        225,41,1,0,0,0,226,227,3,44,22,0,227,43,1,0,0,0,228,233,3,46,23,
        0,229,230,5,40,0,0,230,232,3,46,23,0,231,229,1,0,0,0,232,235,1,0,
        0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,45,1,0,0,0,235,233,1,0,0,
        0,236,241,3,48,24,0,237,238,5,39,0,0,238,240,3,48,24,0,239,237,1,
        0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,47,1,0,
        0,0,243,241,1,0,0,0,244,249,3,50,25,0,245,246,7,2,0,0,246,248,3,
        50,25,0,247,245,1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,0,249,250,
        1,0,0,0,250,49,1,0,0,0,251,249,1,0,0,0,252,257,3,52,26,0,253,254,
        7,3,0,0,254,256,3,52,26,0,255,253,1,0,0,0,256,259,1,0,0,0,257,255,
        1,0,0,0,257,258,1,0,0,0,258,51,1,0,0,0,259,257,1,0,0,0,260,265,3,
        54,27,0,261,262,7,4,0,0,262,264,3,54,27,0,263,261,1,0,0,0,264,267,
        1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,266,53,1,0,0,0,267,265,1,
        0,0,0,268,273,3,56,28,0,269,270,7,5,0,0,270,272,3,56,28,0,271,269,
        1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,55,1,
        0,0,0,275,273,1,0,0,0,276,277,5,41,0,0,277,280,3,56,28,0,278,280,
        3,58,29,0,279,276,1,0,0,0,279,278,1,0,0,0,280,57,1,0,0,0,281,298,
        3,38,19,0,282,283,5,42,0,0,283,284,5,21,0,0,284,285,3,42,21,0,285,
        286,5,22,0,0,286,298,1,0,0,0,287,298,5,17,0,0,288,298,5,18,0,0,289,
        298,5,42,0,0,290,298,5,43,0,0,291,298,5,44,0,0,292,298,5,45,0,0,
        293,294,5,23,0,0,294,295,3,42,21,0,295,296,5,24,0,0,296,298,1,0,
        0,0,297,281,1,0,0,0,297,282,1,0,0,0,297,287,1,0,0,0,297,288,1,0,
        0,0,297,289,1,0,0,0,297,290,1,0,0,0,297,291,1,0,0,0,297,292,1,0,
        0,0,297,293,1,0,0,0,298,59,1,0,0,0,21,66,75,104,110,127,130,133,
        149,161,180,187,213,216,233,241,249,257,265,273,279,297
    ]

class gramatica_v3Parser ( Parser ):

    grammarFileName = "gramatica_v3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'{'", "'}'", "'if'", "'else'", 
                     "'while'", "'for'", "'return'", "'break'", "'continue'", 
                     "'import'", "'int'", "'float'", "'string'", "'bool'", 
                     "'void'", "'true'", "'false'", "'print'", "','", "'['", 
                     "']'", "'('", "')'", "';'", "'='", "'+'", "'-'", "'/'", 
                     "'*'", "'%'", "'>='", "'<='", "'>'", "'<'", "'=='", 
                     "'<>'", "'!='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "INI", "INILLAVE", "FIN", "IF", "ELSE", 
                      "WHILE", "FOR", "RETURN", "BREAK", "CONTINUE", "IMPORT", 
                      "INT", "FLOAT", "STRING", "BOOL", "VOID", "TRUE", 
                      "FALSE", "PRINT", "COMMA", "LBRACKET", "RBRACKET", 
                      "PARENI", "PAREND", "SEMI", "ASSIGN", "SUM", "REST", 
                      "DIV", "MUL", "MOD", "MAYORIGUAL", "MENORIGUAL", "MAYOR", 
                      "MENOR", "IGUAL", "NOIGUAL", "DIFF", "AND", "OR", 
                      "NOT", "VAR", "NUM", "FNUM", "STRVAL", "WS" ]

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
    RULE_importstm = 18
    RULE_llamada = 19
    RULE_printstm = 20
    RULE_expr = 21
    RULE_logicalOr = 22
    RULE_logicalAnd = 23
    RULE_igualdad = 24
    RULE_comparacion = 25
    RULE_suma = 26
    RULE_producto = 27
    RULE_unario = 28
    RULE_primario = 29

    ruleNames =  [ "root", "programa", "bloque", "statement", "varint", 
                   "asignacion", "arraydecl", "arrayasign", "ifstm", "whilestm", 
                   "forstm", "tipodato", "parametro", "parametros", "funcion", 
                   "returnstm", "breakstm", "continuestm", "importstm", 
                   "llamada", "printstm", "expr", "logicalOr", "logicalAnd", 
                   "igualdad", "comparacion", "suma", "producto", "unario", 
                   "primario" ]

    EOF = Token.EOF
    INI=1
    INILLAVE=2
    FIN=3
    IF=4
    ELSE=5
    WHILE=6
    FOR=7
    RETURN=8
    BREAK=9
    CONTINUE=10
    IMPORT=11
    INT=12
    FLOAT=13
    STRING=14
    BOOL=15
    VOID=16
    TRUE=17
    FALSE=18
    PRINT=19
    COMMA=20
    LBRACKET=21
    RBRACKET=22
    PARENI=23
    PAREND=24
    SEMI=25
    ASSIGN=26
    SUM=27
    REST=28
    DIV=29
    MUL=30
    MOD=31
    MAYORIGUAL=32
    MENORIGUAL=33
    MAYOR=34
    MENOR=35
    IGUAL=36
    NOIGUAL=37
    DIFF=38
    AND=39
    OR=40
    NOT=41
    VAR=42
    NUM=43
    FNUM=44
    STRVAL=45
    WS=46

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
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 23, 41, 42, 43, 44, 45]:
                localctx = gramatica_v3Parser.ExprInputContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.expr()
                self.state = 61
                self.match(gramatica_v3Parser.EOF)
                pass
            elif token in [1]:
                localctx = gramatica_v3Parser.ProgInputContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.programa()
                self.state = 64
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
            self.state = 68
            self.match(gramatica_v3Parser.INI)
            self.state = 69
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
            self.state = 71
            self.match(gramatica_v3Parser.INILLAVE)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398047166416) != 0):
                self.state = 72
                self.statement()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
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


        def importstm(self):
            return self.getTypedRuleContext(gramatica_v3Parser.ImportstmContext,0)


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
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.varint()
                self.state = 81
                self.match(gramatica_v3Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.arraydecl()
                self.state = 84
                self.match(gramatica_v3Parser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.asignacion()
                self.state = 87
                self.match(gramatica_v3Parser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.arrayasign()
                self.state = 90
                self.match(gramatica_v3Parser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.ifstm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 93
                self.whilestm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 94
                self.forstm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 95
                self.returnstm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 96
                self.llamada()
                self.state = 97
                self.match(gramatica_v3Parser.SEMI)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 99
                self.printstm()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 100
                self.funcion()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 101
                self.breakstm()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 102
                self.continuestm()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 103
                self.importstm()
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
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 107
            self.match(gramatica_v3Parser.VAR)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 108
                self.match(gramatica_v3Parser.ASSIGN)
                self.state = 109
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
            self.state = 112
            self.match(gramatica_v3Parser.VAR)
            self.state = 113
            self.match(gramatica_v3Parser.ASSIGN)
            self.state = 114
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

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.LBRACKET)
            else:
                return self.getToken(gramatica_v3Parser.LBRACKET, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v3Parser.RBRACKET)
            else:
                return self.getToken(gramatica_v3Parser.RBRACKET, i)

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
            self.state = 116
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 117
            self.match(gramatica_v3Parser.LBRACKET)
            self.state = 118
            self.match(gramatica_v3Parser.RBRACKET)
            self.state = 119
            self.match(gramatica_v3Parser.VAR)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 120
                self.match(gramatica_v3Parser.ASSIGN)
                self.state = 121
                self.match(gramatica_v3Parser.LBRACKET)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68169729703936) != 0):
                    self.state = 122
                    self.expr()
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==20:
                        self.state = 123
                        self.match(gramatica_v3Parser.COMMA)
                        self.state = 124
                        self.expr()
                        self.state = 129
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 132
                self.match(gramatica_v3Parser.RBRACKET)


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
            self.state = 135
            self.match(gramatica_v3Parser.VAR)
            self.state = 136
            self.match(gramatica_v3Parser.LBRACKET)
            self.state = 137
            self.expr()
            self.state = 138
            self.match(gramatica_v3Parser.RBRACKET)
            self.state = 139
            self.match(gramatica_v3Parser.ASSIGN)
            self.state = 140
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
            self.state = 142
            self.match(gramatica_v3Parser.IF)
            self.state = 143
            self.match(gramatica_v3Parser.PARENI)
            self.state = 144
            self.expr()
            self.state = 145
            self.match(gramatica_v3Parser.PAREND)
            self.state = 146
            self.bloque()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 147
                self.match(gramatica_v3Parser.ELSE)
                self.state = 148
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
            self.state = 151
            self.match(gramatica_v3Parser.WHILE)
            self.state = 152
            self.match(gramatica_v3Parser.PARENI)
            self.state = 153
            self.expr()
            self.state = 154
            self.match(gramatica_v3Parser.PAREND)
            self.state = 155
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
            self.state = 157
            self.match(gramatica_v3Parser.FOR)
            self.state = 158
            self.match(gramatica_v3Parser.PARENI)
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14, 15]:
                self.state = 159
                self.varint()
                pass
            elif token in [42]:
                self.state = 160
                self.asignacion()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 163
            self.match(gramatica_v3Parser.SEMI)
            self.state = 164
            self.expr()
            self.state = 165
            self.match(gramatica_v3Parser.SEMI)
            self.state = 166
            self.asignacion()
            self.state = 167
            self.match(gramatica_v3Parser.PAREND)
            self.state = 168
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
            self.state = 170
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0)):
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
            self.state = 172
            self.tipodato()
            self.state = 173
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
            self.state = 175
            self.parametro()
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 176
                self.match(gramatica_v3Parser.COMMA)
                self.state = 177
                self.parametro()
                self.state = 182
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
            self.state = 183
            self.tipodato()
            self.state = 184
            self.match(gramatica_v3Parser.VAR)
            self.state = 185
            self.match(gramatica_v3Parser.PARENI)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0):
                self.state = 186
                self.parametros()


            self.state = 189
            self.match(gramatica_v3Parser.PAREND)
            self.state = 190
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
            self.state = 192
            self.match(gramatica_v3Parser.RETURN)
            self.state = 193
            self.expr()
            self.state = 194
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
            self.state = 196
            self.match(gramatica_v3Parser.BREAK)
            self.state = 197
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
            self.state = 199
            self.match(gramatica_v3Parser.CONTINUE)
            self.state = 200
            self.match(gramatica_v3Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportstmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(gramatica_v3Parser.IMPORT, 0)

        def VAR(self):
            return self.getToken(gramatica_v3Parser.VAR, 0)

        def SEMI(self):
            return self.getToken(gramatica_v3Parser.SEMI, 0)

        def getRuleIndex(self):
            return gramatica_v3Parser.RULE_importstm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportstm" ):
                return visitor.visitImportstm(self)
            else:
                return visitor.visitChildren(self)




    def importstm(self):

        localctx = gramatica_v3Parser.ImportstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_importstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(gramatica_v3Parser.IMPORT)
            self.state = 203
            self.match(gramatica_v3Parser.VAR)
            self.state = 204
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
        self.enterRule(localctx, 38, self.RULE_llamada)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(gramatica_v3Parser.VAR)
            self.state = 207
            self.match(gramatica_v3Parser.PARENI)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68169729703936) != 0):
                self.state = 208
                self.expr()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 209
                    self.match(gramatica_v3Parser.COMMA)
                    self.state = 210
                    self.expr()
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 218
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
        self.enterRule(localctx, 40, self.RULE_printstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(gramatica_v3Parser.PRINT)
            self.state = 221
            self.match(gramatica_v3Parser.PARENI)
            self.state = 222
            self.expr()
            self.state = 223
            self.match(gramatica_v3Parser.PAREND)
            self.state = 224
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
        self.enterRule(localctx, 42, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
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
        self.enterRule(localctx, 44, self.RULE_logicalOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.logicalAnd()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 229
                self.match(gramatica_v3Parser.OR)
                self.state = 230
                self.logicalAnd()
                self.state = 235
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
        self.enterRule(localctx, 46, self.RULE_logicalAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.igualdad()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 237
                self.match(gramatica_v3Parser.AND)
                self.state = 238
                self.igualdad()
                self.state = 243
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
        self.enterRule(localctx, 48, self.RULE_igualdad)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.comparacion()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 481036337152) != 0):
                self.state = 245
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 481036337152) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 246
                self.comparacion()
                self.state = 251
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
        self.enterRule(localctx, 50, self.RULE_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.suma()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 64424509440) != 0):
                self.state = 253
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64424509440) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 254
                self.suma()
                self.state = 259
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
        self.enterRule(localctx, 52, self.RULE_suma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.producto()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 261
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 262
                self.producto()
                self.state = 267
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
        self.enterRule(localctx, 54, self.RULE_producto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.unario()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0):
                self.state = 269
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 270
                self.unario()
                self.state = 275
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
        self.enterRule(localctx, 56, self.RULE_unario)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(gramatica_v3Parser.NOT)
                self.state = 277
                self.unario()
                pass
            elif token in [17, 18, 23, 42, 43, 44, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
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
        self.enterRule(localctx, 58, self.RULE_primario)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.llamada()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(gramatica_v3Parser.VAR)
                self.state = 283
                self.match(gramatica_v3Parser.LBRACKET)
                self.state = 284
                self.expr()
                self.state = 285
                self.match(gramatica_v3Parser.RBRACKET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.match(gramatica_v3Parser.TRUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 288
                self.match(gramatica_v3Parser.FALSE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 289
                self.match(gramatica_v3Parser.VAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 290
                self.match(gramatica_v3Parser.NUM)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 291
                self.match(gramatica_v3Parser.FNUM)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 292
                self.match(gramatica_v3Parser.STRVAL)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 293
                self.match(gramatica_v3Parser.PARENI)
                self.state = 294
                self.expr()
                self.state = 295
                self.match(gramatica_v3Parser.PAREND)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





