grammar Expresiones21;

//root o relga inicial 
root : 'program' bloque EOF;

// regla sintactica (parser rule) 
// el bloque esta formado por 0 o mas instrucciones

bloque: LLAVEI  statement* LLAVED; 
statement: varint SEMI | asignacion SEMI|ifstm;


varint: INT VAR;
asignacion : VAR ASSIGN expr;
ifstm: IF PARENI expr PAREND bloque(ELSE bloque)?;

expr : logicalOr;
logicalOr : logicalAnd( OR logicalAnd)*;
logicalAnd: igualdad  (AND igualdad )*;
igualdad: comparacion ((IGUAL|NOIGUAL|DIFF)comparacion)*;
comparacion: suma((MAYOR|MENOR|MAYORIGUAL|MENORIGUAL)suma)*;
suma: producto((SUM|REST)producto)*;
producto: unario((MUL|DIV)unario)*;
unario: NOT unario | primario;
primario: NUM|VAR|PARENI expr PAREND;


// tokens 

IF : 'if';
ELSE : 'else';
INT : 'int';
PARENI: '(';
PAREND: ')';
LLAVEI: '{';
LLAVED: '}';
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
