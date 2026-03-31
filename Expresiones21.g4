grammar Expresiones21;

//root o relga inicial 
root : INI* INILLAVE bloque FIN EOF;

bloque: INILLAVE statement* FIN ; 

statement: varint SEMI | asignacion SEMI|ifstm;

// declaracion de variables 
varint: INT VAR | FLOAT VAR;  //variables tipo int y float
asignacion : VAR ASSIGN expr;  // instruccion de asignacion 

ifstm: IF PARENI expr PAREND bloque(ELSE bloque); // instruccion de if 

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
primario: NUM| FNUM | VAR|PARENI expr PAREND;


// tokens 
INI : 'program {';
INILLAVE : '{';
FIN : '}';
IF : 'if';
ELSE : 'else';
INT : 'int';
FLOAT : 'float';

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
WS : [ \t\r\n]+ -> skip;