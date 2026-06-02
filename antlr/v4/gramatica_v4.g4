grammar gramatica_v4;

// ═══════════════════════════════════════════════════════════
// REGLA RAÍZ
// ═══════════════════════════════════════════════════════════

root
    : expr    EOF  #exprInput
    | programa EOF #progInput
    ;

programa: INI bloque #programaRule;

bloque: INILLAVE statement* FIN;

// ═══════════════════════════════════════════════════════════
// STATEMENTS — se agregan: switchstm, structdecl, structasign
// ═══════════════════════════════════════════════════════════

statement
    : varint       SEMI
    | arraydecl    SEMI
    | asignacion   SEMI
    | arrayasign   SEMI
    | structasign  SEMI
    | ifstm
    | whilestm
    | forstm
    | switchstm
    | returnstm
    | llamada      SEMI
    | printstm
    | funcion
    | structdecl
    | varstruct    SEMI
    | breakstm
    | continuestm
    | importstm
    ;

// ═══════════════════════════════════════════════════════════
// VARIABLES Y ARREGLOS (sin cambios respecto a v3)
// ═══════════════════════════════════════════════════════════

varint    : (INT | FLOAT | STRING | BOOL) VAR (ASSIGN expr)?;
asignacion: VAR ASSIGN expr;

arraydecl : (INT | FLOAT | STRING | BOOL) LBRACKET RBRACKET VAR
            (ASSIGN LBRACKET (expr (COMMA expr)*)? RBRACKET)?;
arrayasign: VAR LBRACKET expr RBRACKET ASSIGN expr;

// ═══════════════════════════════════════════════════════════
// STRUCTS  — NUEVO EN v4
// Ejemplo:
//   struct Punto { int x; int y; }
//   Punto p;
//   p.x = 3;
// ═══════════════════════════════════════════════════════════

// Declaración del tipo struct
structdecl: STRUCT VAR INILLAVE campostruct+ FIN;

// Un campo dentro de la definición: tipodato nombre;
campostruct: tipodato VAR SEMI;

// Instanciar un struct: NombreStruct varNombre;
varstruct: VAR VAR;

// Asignación a campo de struct: var.campo = expr
structasign: VAR DOT VAR ASSIGN expr;

// ═══════════════════════════════════════════════════════════
// IF / WHILE / FOR  (sin cambios)
// ═══════════════════════════════════════════════════════════

ifstm   : IF    PARENI expr PAREND bloque (ELSE bloque)?;
whilestm: WHILE PARENI expr PAREND bloque;
forstm  : FOR   PARENI (varint | asignacion) SEMI expr SEMI asignacion PAREND bloque;

// ═══════════════════════════════════════════════════════════
// SWITCH / CASE / DEFAULT  — NUEVO EN v4
// Ejemplo:
//   switch(opcion) {
//       case 1: print("uno"); break;
//       case 2: print("dos"); break;
//       default: print("otro");
//   }
// ═══════════════════════════════════════════════════════════

switchstm  : SWITCH PARENI expr PAREND INILLAVE caseclause* defaultclause? FIN;
caseclause : CASE expr COLON statement*;
defaultclause: DEFAULT COLON statement*;

// ═══════════════════════════════════════════════════════════
// FUNCIONES (sin cambios)
// ═══════════════════════════════════════════════════════════

tipodato  : INT | FLOAT | STRING | BOOL | VOID;
parametro : tipodato VAR;
parametros: parametro (COMMA parametro)*;
funcion   : tipodato VAR PARENI parametros? PAREND bloque;

returnstm : RETURN expr SEMI;
breakstm  : BREAK    SEMI;
continuestm: CONTINUE SEMI;
importstm : IMPORT VAR SEMI;
llamada   : VAR PARENI (expr (COMMA expr)*)? PAREND;
printstm  : PRINT PARENI expr PAREND SEMI;

// ═══════════════════════════════════════════════════════════
// EXPRESIONES
// Se agregan: operador ternario (?:) y casting explícito
// ═══════════════════════════════════════════════════════════

// El ternario va en el nivel más alto de expr para que sea de baja
// precedencia y no choque con operadores binarios internos.
// Forma: condicion ? valorSiVerdad : valorSiFalso
expr
    : logicalOr QUESTION expr COLON expr  #ternario
    | logicalOr                            #exprSimple
    ;

logicalOr : logicalAnd (OR  logicalAnd)*;
logicalAnd: igualdad   (AND igualdad)*;

igualdad  : comparacion ((IGUAL | NOIGUAL | DIFF) comparacion)*;
comparacion: suma ((MAYOR | MENOR | MAYORIGUAL | MENORIGUAL) suma)*;

suma    : producto ((SUM  | REST) producto)*;
producto: unario   ((MUL  | DIV  | MOD)  unario)*;

// Unario: negación lógica y casting explícito  — NUEVO EN v4
// Casting: (int) expr,  (float) expr,  (bool) expr,  (string) expr
unario
    : NOT unario                        #unarioNot
    | REST unario                       #unarioNeg
    | PARENI tipodato PAREND unario     #unarioCast
    | primario                          #unarioPrimario
    ;

// Primario: se agrega acceso a campo de struct (var.campo)
primario
    : llamada                           #primLlamada
    | VAR LBRACKET expr RBRACKET        #primArray
    | VAR DOT VAR                       #primStructAcceso
    | TRUE                              #primTrue
    | FALSE                             #primFalse
    | VAR                               #primVar
    | NUM                               #primNum
    | FNUM                              #primFnum
    | STRVAL                            #primStr
    | PARENI expr PAREND                #primParen
    ;

// ═══════════════════════════════════════════════════════════
// TOKENS
// REGLA: todas las keywords ANTES de VAR
// ═══════════════════════════════════════════════════════════

// ── Estructura del programa ──────────────────────────────
INI       : 'program';
INILLAVE  : '{';
FIN       : '}';

// ── Control de flujo ─────────────────────────────────────
IF        : 'if';
ELSE      : 'else';
WHILE     : 'while';
FOR       : 'for';
RETURN    : 'return';
BREAK     : 'break';
CONTINUE  : 'continue';
IMPORT    : 'import';

// ── Switch / case  (NUEVO v4) ────────────────────────────
SWITCH    : 'switch';
CASE      : 'case';
DEFAULT   : 'default';

// ── Tipos de dato ─────────────────────────────────────────
INT       : 'int';
FLOAT     : 'float';
STRING    : 'string';
BOOL      : 'bool';
VOID      : 'void';

// ── Structs (NUEVO v4) ────────────────────────────────────
STRUCT    : 'struct';

// ── Literales booleanos ───────────────────────────────────
TRUE      : 'true';
FALSE     : 'false';

// ── I/O ──────────────────────────────────────────────────
PRINT     : 'print';

// ── Puntuación ────────────────────────────────────────────
LBRACKET  : '[';
RBRACKET  : ']';
COMMA     : ',';
PARENI    : '(';
PAREND    : ')';
SEMI      : ';';
COLON     : ':';        // Necesario para case: y ternario ?:
DOT       : '.';        // Acceso a campo de struct: p.x

// ── Operadores aritméticos ───────────────────────────────
ASSIGN    : '=';
SUM       : '+';
REST      : '-';
DIV       : '/';
MUL       : '*';
MOD       : '%';

// ── Operadores relacionales ───────────────────────────────
MAYORIGUAL: '>=';
MENORIGUAL: '<=';
MAYOR     : '>';
MENOR     : '<';
IGUAL     : '==';
NOIGUAL   : '<>';
DIFF      : '!=';

// ── Operadores lógicos ────────────────────────────────────
AND       : '&&';
OR        : '||';
NOT       : '!';

// ── Operador ternario (NUEVO v4) ──────────────────────────
QUESTION  : '?';

// ── Identificadores y literales ──────────────────────────
// VAR siempre al final para que las keywords tengan prioridad
VAR    : [a-zA-Z_][a-zA-Z0-9_]*;
NUM    : [0-9]+;
FNUM   : [0-9]+ '.' [0-9]+;
STRVAL : '"' (~["\r\n])* '"';

// ── Comentarios y espacios ────────────────────────────────
LINE_COMMENT : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
WS           : [ \t\r\n]+ -> skip;
