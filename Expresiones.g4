grammar ExpresionesS;

// Regla inicial
root : expr EOF ;

// Expresiones con precedencia
expr
    : expr SUM expr      # Suma
    | expr RES expr      # Resta
    | expr MUL expr      # Multi
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