grammar Expresiones21;

//root o relga inicial 
root : INI* INILLAVE funcion* bloque FIN EOF;

bloque: INILLAVE statement* FIN ; 

statement: varint SEMI | asignacion SEMI | ifstm | whilestm | forstm | returnstm | llamada SEMI;

// declaracion de variables 
varint: INT VAR | FLOAT VAR | STRING VAR | BOOL VAR;  //variables tipo int y float
asignacion : VAR ASSIGN expr;  // instruccion de asignacion 

ifstm: IF PARENI expr PAREND bloque(ELSE bloque); // instruccion de if 
whilestm: WHILE PARENI expr PAREND bloque; // instruccion de while
forstm: FOR PARENI asignacion SEMI expr SEMI asignacion PAREND bloque; // regla del for

tipodato: INT | FLOAT | STRING | BOOL | VOID; 

parametro: tipodato VAR;
parametros: parametro (COMMA parametro)*;

funcion: tipodato VAR PARENI parametros? PAREND bloque;

returnstm: RETURN expr SEMI;
llamada: VAR PARENI (expr (COMMA expr)*)? PAREND;

//reglas principales de expresiones 
//definimos que todas las expresiones empiezan evaluando operadores OR.
// para contrololar precedencia de operadores 

expr : logicalOr;

//puede haber muchos OR
logicalOr : logicalAnd( OR logicalAnd)*;

//puede haber muchos &&
logicalAnd: igualdad  (AND igualdad )*;

// expresion de igualdades
igualdad: comparacion ((IGUAL|NOIGUAL|DIFF)comparacion)*;

// expresion de comparadores < > 
comparacion: suma((MAYOR|MENOR|MAYORIGUAL|MENORIGUAL)suma)*;

// expresion de suma
suma: producto((SUM|REST)producto)*;

// expresion de multipicacion 
producto: unario((MUL|DIV)unario)*;

// expresion unario para negar una expresion 
unario: NOT unario | primario;

// expresiones primarios numero variables expresion entre parentesis 
primario: NUM| FNUM | STRVAL | TRUE | FALSE | VAR|PARENI expr PAREND;


// tokens 
INI : 'program {';
INILLAVE : '{';
FIN : '}';
IF : 'if';
ELSE : 'else';
INT : 'int';
FLOAT : 'float';
STRING : 'string';
BOOL : 'bool';
TRUE : 'true';
WHILE : 'while';
FALSE : 'false';
FOR : 'for';
VOID : 'void';
RETURN : 'return';
COMMA : ',';
PARENI: '(';
PAREND: ')';
SEMI: ';';
ASSIGN: '=';
SUM: '+';
REST: '-';
DIV: '/';
MUL: '*';
MAYORIGUAL: '>=';
MENORIGUAL: '<=';
MAYOR: '>';
MENOR: '<';
IGUAL: '==';
NOIGUAL: '<>';
DIFF: '!=';
AND: '&&';
OR: '||';
NOT: '!';


VAR : [a-zA-Z][a-zA-Z0-9]*;
NUM: [0-9]+;
FNUM: [0-9]+ '.' [0-9]+;
STRVAL: '"' (~["\r\n])* '"';
WS : [ \t\r\n]+ -> skip;