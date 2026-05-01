grammar Expresiones21;

//root o relga inicial 
root : 'program' bloque EOF;

// regla sintactica (parser rule) 
// el bloque esta formado por 0 o mas instrucciones
bloque: '{'  statement* '}'; 

// regla de las intrucciones 
// tipos de intrucciones, se definimos el tipo de instrucciones en el lenguaje
statement: varint SEMI | asignacion SEMI|ifstm;

// declaracion de variables 
varint: INT VAR;  //variables tipo int 
asignacion : VAR ASSIGN expr;  // instruccion de asignacion 

ifstm: IF PARENI expr PAREND bloque(ELSE bloque)?; // instruccion de if 

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
primario: NUM|VAR|PARENI expr PAREND;


// tokens 

IF : 'if';
ELSE : 'else';
INT : 'int';
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
WS : [ \t\r\n]+ -> skip;
