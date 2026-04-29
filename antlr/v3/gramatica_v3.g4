grammar gramatica_v3;

//root o regla inicial 
root
      : expr EOF  #exprInput
      | programa EOF #progInput
      ;  

programa: INI bloque #programaRule;

bloque: INILLAVE statement* FIN; 

statement
    : varint SEMI
    | arraydecl SEMI
    | asignacion SEMI
    | arrayasign SEMI
    | ifstm
    | whilestm
    | forstm
    | returnstm
    | llamada SEMI
    | printstm
    | funcion
    | breakstm
    | continuestm
    | importstm
    ;

varint: (INT | FLOAT | STRING | BOOL) VAR (ASSIGN expr)?;
asignacion: VAR ASSIGN expr;

arraydecl: (INT | FLOAT | STRING | BOOL) LBRACKET RBRACKET VAR (ASSIGN LBRACKET (expr (COMMA expr)*)? RBRACKET)?;
arrayasign: VAR LBRACKET expr RBRACKET ASSIGN expr;

ifstm: IF PARENI expr PAREND bloque (ELSE bloque)?;
whilestm: WHILE PARENI expr PAREND bloque;

// FIX ciclos: el init del for acepta varint (declaracion) O asignacion
forstm: FOR PARENI (varint | asignacion) SEMI expr SEMI asignacion PAREND bloque;

tipodato: INT | FLOAT | STRING | BOOL | VOID;

parametro: tipodato VAR;
parametros: parametro (COMMA parametro)*;

funcion: tipodato VAR PARENI parametros? PAREND bloque;

returnstm: RETURN expr SEMI;
breakstm: BREAK SEMI;
continuestm: CONTINUE SEMI;
importstm: IMPORT VAR SEMI;
llamada: VAR PARENI (expr (COMMA expr)*)? PAREND;

printstm: PRINT PARENI expr PAREND SEMI;

expr: logicalOr;
logicalOr: logicalAnd (OR logicalAnd)*;
logicalAnd: igualdad (AND igualdad)*;
igualdad: comparacion ((IGUAL | NOIGUAL | DIFF) comparacion)*;
comparacion: suma ((MAYOR | MENOR | MAYORIGUAL | MENORIGUAL) suma)*;
suma: producto ((SUM | REST) producto)*;
producto: unario ((MUL | DIV | MOD) unario)*;
unario: NOT unario | primario;

// FIX primario: llamada y TRUE/FALSE antes de VAR para evitar ambigüedad
primario
    : llamada
    | VAR LBRACKET expr RBRACKET
    | TRUE
    | FALSE
    | VAR
    | NUM
    | FNUM
    | STRVAL
    | PARENI expr PAREND
    ;


// TOKENS
// FIX: todas las keywords ANTES de VAR para que ANTLR4 las priorice

INI       : 'program';
INILLAVE  : '{';
FIN       : '}';
IF        : 'if';
ELSE      : 'else';
WHILE     : 'while';
FOR       : 'for';
RETURN    : 'return';

INT    : 'int';
FLOAT  : 'float';
STRING : 'string';
BOOL   : 'bool';
VOID   : 'void';

// FIX true/false: tokens explícitos antes de VAR
TRUE  : 'true';
FALSE : 'false';

// FIX print: keyword explícita antes de VAR
PRINT : 'print';

COMMA     : ',';
PARENI    : '(';
PAREND    : ')';
SEMI      : ';';
ASSIGN    : '=';
SUM       : '+';
REST      : '-';
DIV       : '/';
MUL       : '*';
MAYORIGUAL: '>=';
MENORIGUAL: '<=';
MAYOR     : '>';
MENOR     : '<';
IGUAL     : '==';
NOIGUAL   : '<>';
DIFF      : '!=';
AND       : '&&';
OR        : '||';
NOT       : '!';
LBRACKET : '[';
RBRACKET : ']';
MOD: '%';
BREAK    : 'break';
CONTINUE : 'continue';
IMPORT : 'import';

// VAR al final, después de todas las keywords
VAR   : [a-zA-Z][a-zA-Z0-9]*;
NUM   : [0-9]+;
FNUM  : [0-9]+ '.' [0-9]+;
STRVAL: '"' (~["\r\n])* '"';
WS    : [ \t\r\n]+ -> skip;