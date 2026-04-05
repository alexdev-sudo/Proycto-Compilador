from Expresiones21Parser import Expresiones21Parser
from Expresiones21Visitor import Expresiones21Visitor
# ==============================
# Visitor para evaluar programa
# ==============================
class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class EvalVisitor(Expresiones21Visitor):

    def visitProgInput(self, ctx):
        programa_ctx = ctx.getChild(0)  # asumiendo que el programa es el primer hijo
        return self.visit(programa_ctx)

    def visitExprInput(self, ctx):
        return self.visit(ctx.expr())
    
    
    

    def __init__(self):
        self.scopes = [{}]
        self.functions = {}


# ==============================
# PROGRAMA
# ==============================
   
    
    def visitProgramaRule(self, ctx):
       
        return self.visit(ctx.bloque())
        


    def visitBloque(self, ctx):
       

        is_program_block = isinstance(ctx.parentCtx, Expresiones21Parser.ProgramaContext)


        if not is_program_block:
            self.push()

        for stmt in ctx.statement():
            self.visit(stmt)

        if not is_program_block:
            self.pop()
    


# ==============================
# VARIABLES
# ==============================

    def visitVarint(self, ctx):

        nombre = ctx.VAR().getText()

        if ctx.INT():
            self.scopes[-1][nombre] = 0
        elif ctx.FLOAT():
            self.scopes[-1][nombre] = 0.0
        elif ctx.STRING():
            self.scopes[-1][nombre] = ""
        elif ctx.BOOL():
            self.scopes[-1][nombre] = False


    def visitAsignacion(self, ctx):

        nombre = ctx.VAR().getText()

        valor = self.visit(ctx.expr())

        self.set_var(nombre, valor)

        return valor


# ==============================
# IF
# ==============================

    def visitIfstm(self, ctx):

        condicion = self.visit(ctx.expr())

        if condicion:
            self.visit(ctx.bloque(0))
        else:
            if ctx.ELSE():
                self.visit(ctx.bloque(1))


# ==============================
# WHILE
# ==============================

    def visitWhilestm(self, ctx):

        while self.visit(ctx.expr()):
            self.visit(ctx.bloque())


# ==============================
# FOR
# ==============================

    def visitForstm(self, ctx):

        self.visit(ctx.asignacion(0))

        while self.visit(ctx.expr()):
            self.visit(ctx.bloque())
            self.visit(ctx.asignacion(1))


# ==============================
# PRINT
# ==============================

    def visitPrintstm(self, ctx):
           
        valor = self.visit(ctx.expr())
        print(valor)


# ==============================
# EXPRESIONES LOGICAS
# ==============================

    def visitLogicalOr(self, ctx):

        resultado = self.visit(ctx.logicalAnd(0))

        for i in range(1, len(ctx.logicalAnd())):
            resultado = resultado or self.visit(ctx.logicalAnd(i))

        return resultado


    def visitLogicalAnd(self, ctx):

        resultado = self.visit(ctx.igualdad(0))

        for i in range(1, len(ctx.igualdad())):
            resultado = resultado and self.visit(ctx.igualdad(i))

        return resultado


# ==============================
# IGUALDAD
# ==============================

    def visitIgualdad(self, ctx):

        left = self.visit(ctx.comparacion(0))

        for i in range(1, len(ctx.comparacion())):

            right = self.visit(ctx.comparacion(i))

            if ctx.IGUAL(i-1):
                left = left == right

            elif ctx.NOIGUAL(i-1) or ctx.DIFF(i-1):
                left = left != right

        return left


# ==============================
# COMPARACIONES
# ==============================

    def visitComparacion(self, ctx):

        left = self.visit(ctx.suma(0))

        for i in range(1, len(ctx.suma())):

            right = self.visit(ctx.suma(i))

            if ctx.MAYOR(i-1):
                left = left > right

            elif ctx.MENOR(i-1):
                left = left < right

            elif ctx.MAYORIGUAL(i-1):
                left = left >= right

            elif ctx.MENORIGUAL(i-1):
                left = left <= right

        return left


# ==============================
# SUMA
# ==============================

    def visitSuma(self, ctx):

        resultado = self.visit(ctx.producto(0))

        for i in range(1, len(ctx.producto())):

            right = self.visit(ctx.producto(i))

            if ctx.SUM(i-1):
                resultado += right
            else:
                resultado -= right

        return resultado


# ==============================
# PRODUCTO
# ==============================

    def visitProducto(self, ctx):

        resultado = self.visit(ctx.unario(0))

        for i in range(1, len(ctx.unario())):

            right = self.visit(ctx.unario(i))

            if ctx.MUL(i-1):
                resultado *= right
            else:
                resultado /= right

        return resultado


# ==============================
# UNARIO
# ==============================

    def visitUnario(self, ctx):

        if ctx.NOT():
            return not self.visit(ctx.unario())

        return self.visit(ctx.primario())


# ==============================
# PRIMARIO
# ==============================

    def visitPrimario(self, ctx):
         
        if ctx.llamada():
            return self.visit(ctx.llamada())
        if ctx.NUM():
            return int(ctx.NUM().getText())

        if ctx.FNUM():
            return float(ctx.FNUM().getText())

        if ctx.STRVAL():
            return ctx.STRVAL().getText()[1:-1]  # quita las comillas

        if ctx.TRUE():
            return True

        if ctx.FALSE():
            return False

        if ctx.VAR():
            nombre = ctx.VAR().getText()
            return self.get_var(nombre)

        if ctx.expr():
            return self.visit(ctx.expr())
   # ==============================
# SCOPES
# ==============================

    def push(self):
        self.scopes.append({})

    def pop(self):
        self.scopes.pop()

    def set_var(self, name, value):
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name] = value
                return
        self.scopes[-1][name] = value

    def get_var(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Variable '{name}' no definida")
    
    def visitReturnstm(self, ctx):
        value = self.visit(ctx.expr())
        raise ReturnValue(value) 
    
    def visitFuncion(self, ctx):
        name = ctx.VAR().getText()
        self.functions[name] = ctx 

    def visitLlamada(self, ctx):

        name = ctx.VAR().getText()

        if name not in self.functions:
            raise Exception(f"Función '{name}' no definida")

        func_ctx = self.functions[name]

        # nuevo scope
        self.push()

        args = [self.visit(e) for e in ctx.expr()] if ctx.expr() else []
        params = func_ctx.parametros().parametro() if func_ctx.parametros() else []

        for i in range(len(params)):
            param_name = params[i].VAR().getText()
            self.scopes[-1][param_name] = args[i]

        try:
            self.visit(func_ctx.bloque())
        except ReturnValue as rv:
            self.pop()
            return rv.value

        self.pop()

        


