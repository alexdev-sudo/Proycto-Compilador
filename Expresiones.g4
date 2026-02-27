grammar Expresiones;

// Regla inicial
root : expr EOF ;

// Expresiones con precedencia
expr
    : expr MUL expr      # Multi
    | expr RES expr      # Resta
    | expr SUM expr      # Suma
    | expr DIV expr      # Div
    | '(' expr ')'       # Parentesis
    | NUM                # Numero
    ;

// Tokens
NUM : [0-9]+ ;
SUM : '+' ;
RES : '-' ;
MUL : '*' ;
DIV : '/' ;
WS  : [ \t\r\n]+ -> skip ;