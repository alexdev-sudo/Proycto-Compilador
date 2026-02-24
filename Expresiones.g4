grammar Expresiones;
// escritura de una gramatica
root : expr EOF ;

expr
    : expr MUL expr
    | expr DIV expr
    | expr SUM expr
    | expr RES expr
    | NUM
    ;

NUM : [0-9]+ ;
SUM : '+' ;
RES : '-' ;
MUL : '*' ;
DIV : '/' ;
WS  : [ \n]+ -> skip ;
