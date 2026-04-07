from Expresiones21Visitor import Expresiones21Visitor
from tabla_simbolos import TablaSibolos
from Expresiones21Parser import Expresiones21Parser
class semanticVisitor(Expresiones21Visitor):
    def visitExprInput(self, ctx):
        return self.visit(ctx.expr())

    def visitProgInput(self, ctx):
        return self.visit(ctx.programa())

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
        name = ctx.VAR().getText()
        tipo = ctx.getChild(0).getText()

        try:
            self.tabla_simbolos.declare(name, tipo)
        except Exception as e:
            self.error(str(e), ctx)

        # Valida asignacion si existe
        if ctx.expr():
            expr_type = self.visit(ctx.expr())

            if expr_type != tipo:
                self.error(f"Tipo incompatible: no se puede asignar '{expr_type}' a '{tipo}'", ctx)
          

#Asignaciones 
    # Verifica que la variable exista y que el tipo de la expresión sea compatible con el declarado
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
        
        if ctx.llamada():
            return self.visit(ctx.llamada())
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
    # Registra la función en la tabla de símbolos y valida su cuerpo en un nuevo scope
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
    # Crea un nuevo scope al entrar a un bloque, excepto en el bloque global del programa
    def visitBloque(self, ctx):
        # verifica si el padre es ''programa'' para no crear un scope global adicional
        is_global = isinstance(ctx.parentCtx, Expresiones21Parser.ProgramaContext)

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

        return func["return_type"]
    def visitReturnstm(self, ctx):
        expr_type = self.visit(ctx.expr())
        if self.current_function and expr_type != self.current_function:
            self.error(f"Tipo de retorno incorrecto: se esperaba '{self.current_function}' pero se obtuvo '{expr_type}'", ctx)
            
        return expr_type
    
    def visitPrintstm(self, ctx):
        return self.visit(ctx.expr())
    
    def visitSuma(self, ctx):
        left = self.visit(ctx.producto(0))

        for i in range(1, len(ctx.producto())):
            right = self.visit(ctx.producto(i))
            if left != right:
                self.error(f"Tipos incompatibles en operacion arimetica: '{left}' y '{right}'", ctx)
        return left
