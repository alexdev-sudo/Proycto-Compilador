from Expresiones21Visitor import Expresiones21Visitor
from tabla_simbolos import TablaSibolos

class semanticVisitor(Expresiones21Visitor):

    def __init__(self):
        self.tabla_simbolos = TablaSibolos()
        self.errors = []
        self.current_function = None  # Para rastrear el tipo de retorno esperado en funciones

    def error(self, msg, ctx):
        line = ctx.start.line
        col = ctx.start.column
        self.errors.append(f"[Error semántico] en línea {line}, columna {col}: {msg}")


 #variables 

    def visitVarint(self, ctx):
        name = ctx.VAR().getText()  # nombre de la variable
        tipo = ctx.getChild(0).getText()  # tipo de dato (int, float, etc.)

        try: 
            self.tabla_simbolos.declare(name,tipo)
        except Exception as e:
            self.error(str(e), ctx)
          

#Asignaciones 

    def visitAsignacion(self, ctx):
        name = ctx.VAR().getText()
        expr_type = self.visit(ctx.expr())

        try:
            var_type = self.tabla_simbolos.lookup(name)
            if var_type != expr_type:
                self.error(f"Tipo incompatible: no se puede asignar '{expr_type}' a '{var_type}'", ctx)
        except Exception as e:
            self.error(str(e), ctx)

# Expresiones
    def visitPrimario(self, ctx):
        
        if ctx.NUM():
            return 'int'
        if ctx.FNUM():
            return 'float'
        if ctx.STRVAL():
            return 'string'
        if ctx.TRUE() or ctx.FALSE():
            return 'bool'
        if ctx.VAR():
            try:
                return self.tabla_simbolos.lookup(ctx.VAR().getText())
            except Exception as e:
                self.error(str(e), ctx)
                return 'error'  
        return self.visit(ctx.expr())
    # FUNCIONES
    # =========================

    def visitFuncion(self, ctx):

        name = ctx.VAR().getText()
        return_type = ctx.getChild(0).getText()  # tipo de retorno (int, float, etc.)

        params = []
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                tipo = p.tipodato().getText()
                nombre = p.VAR().getText()
                params.append((nombre, tipo))

        try:
            self.tabla_simbolos.declare_function(name, return_type, params, ctx.bloque())
        except Exception as e:
            self.error(str(e), ctx)
        #Validar el cuerpo de la función
        # Validar el cuerpo de la función
        self.current_function = return_type

        self.tabla_simbolos.push()   # ← NUEVO scope para parámetros

        # declarar parámetros en el scope
        for nombre, tipo in params:
            try:
                self.tabla_simbolos.declare(nombre, tipo)
            except Exception as e:
                self.error(str(e), ctx)

        self.visit(ctx.bloque())

        self.tabla_simbolos.pop()    # ← salir del scope

        self.current_function = None    

    # SCOPES
    # =========================

    def visitBloque(self, ctx):
        # solo crea un nuevo scope si No es el global (root)
        is_global = len(self.tabla_simbolos.Scopes) == 1

        if not is_global:
            self.tabla_simbolos.push()

        for stmt in ctx.statement():
            self.visit(stmt)

        if not is_global:
            self.tabla_simbolos.pop()    
     # llamadas  y Reterno 

    def visitLlamada(self, ctx):
        name = ctx.VAR().getText()

        try:
            func = self.tabla_simbolos.get_function(name)
        except Exception as e:
            self.error(str(e), ctx)
            return 'error'

        args = []
        if ctx.expr():
            args = [self.visit(e) for e in ctx.expr()]

        if len(args) != len(func["params"]):
            self.error("Cantidad incorrecta de argumentos", ctx)

        return func["return"]
    def visitReturnstm(self, ctx):
        expr_type = self.visit(ctx.expr())
        if self.current_function and expr_type != self.current_function:
            self.error(f"Tipo de retorno incorrecto: se esperaba '{self.current_function}' pero se obtuvo '{expr_type}'", ctx)
            
        return expr_type