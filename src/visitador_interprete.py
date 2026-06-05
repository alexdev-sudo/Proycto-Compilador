from antlr4 import *
from antlr.v4.gramatica_v4Visitor import gramatica_v4Visitor
from antlr.v4.gramatica_v4Parser import gramatica_v4Parser

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value
        

class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass

class EvalVisitor(gramatica_v4Visitor):

    def __init__(self):
        self.scopes = [{}]
        self.functions = {}
        self.struct_defs = {}

    # ─────────────────────────────────────────
    # PROGRAMA
    # ─────────────────────────────────────────
    def visitProgInput(self, ctx):
        return self.visit(ctx.programa())

    def visitExprInput(self, ctx):
        return self.visit(ctx.expr())

    def visitProgramaRule(self, ctx):
        return self.visit(ctx.bloque())

    def visitBloque(self, ctx):
        is_global = isinstance(ctx.parentCtx, gramatica_v4Parser.ProgramaRuleContext)
        if not is_global:
            self.push()
        for stmt in ctx.statement():
            self.visit(stmt)
        if not is_global:
            self.pop()

    # ─────────────────────────────────────────
    # VARIABLES
    # ─────────────────────────────────────────
    def visitVarint(self, ctx):
        nombre = ctx.VAR().getText()
        tipo = ctx.getChild(0).getText()

        if tipo == "int":
            valor = 0
        elif tipo == "float":
            valor = 0.0
        elif tipo == "string":
            valor = ""
        elif tipo == "bool":
            valor = False

        if ctx.expr():
            valor = self.visit(ctx.expr())

        self.scopes[-1][nombre] = valor

    def visitAsignacion(self, ctx):
        nombre = ctx.VAR().getText()
        valor = self.visit(ctx.expr())
        self.set_var(nombre, valor)
        return valor

    # ─────────────────────────────────────────
    # ARREGLOS
    # ─────────────────────────────────────────
    def visitArraydecl(self, ctx):
        nombre = ctx.VAR().getText()
        valores = [self.visit(e) for e in ctx.expr()]
        self.scopes[-1][nombre] = valores

    def visitArrayasign(self, ctx):
        nombre = ctx.VAR().getText()
        indice = self.visit(ctx.expr(0))
        valor  = self.visit(ctx.expr(1))
        arr = self.get_var(nombre)
        arr[indice] = valor

    # ─────────────────────────────────────────
    # IF
    # ─────────────────────────────────────────
    def visitIfstm(self, ctx):
        condicion = self.visit(ctx.expr())
        if condicion:
            self.visit(ctx.bloque(0))
        else:
            if ctx.ELSE():
                self.visit(ctx.bloque(1))

    # ─────────────────────────────────────────
    # WHILE
    # ─────────────────────────────────────────
    def visitWhilestm(self, ctx):
        while self.visit(ctx.expr()):
            try:
                self.visit(ctx.bloque())
            except BreakException:
                break
            except ContinueException:
                continue

    # ─────────────────────────────────────────
    # FOR
    # ─────────────────────────────────────────
    def visitForstm(self, ctx):
        self.visit(ctx.getChild(2))
        while self.visit(ctx.expr()):
            try:
                self.visit(ctx.bloque())
            except BreakException:
                break
            except ContinueException:
                pass
            self.visit(ctx.getChild(6))

    # ─────────────────────────────────────────
    # BREAK / CONTINUE / IMPORT
    # ─────────────────────────────────────────
    def visitBreakstm(self, ctx):
        raise BreakException()

    def visitContinuestm(self, ctx):
        raise ContinueException()

    def visitImportstm(self, ctx):
        pass

    # ─────────────────────────────────────────
    # FUNCIONES
    # ─────────────────────────────────────────
    def visitFuncion(self, ctx):
        name = ctx.VAR().getText()
        self.functions[name] = ctx

    def visitReturnstm(self, ctx):
        value = self.visit(ctx.expr())
        raise ReturnValue(value)

    def visitLlamada(self, ctx):
        name = ctx.VAR().getText()
        if name not in self.functions:
            raise Exception(f"Función '{name}' no definida")

        func_ctx = self.functions[name]
        self.push()

        args   = [self.visit(e) for e in ctx.expr()] if ctx.expr() else []
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

    # ─────────────────────────────────────────
    # PRINT
    # ─────────────────────────────────────────
    def visitPrintstm(self, ctx):
        valor = self.visit(ctx.expr())
        print(valor)

    # ─────────────────────────────────────────
    # EXPRESIONES
    # ─────────────────────────────────────────
    def visitExprSimple(self, ctx):
        return self.visit(ctx.logicalOr())

    def visitUnarioNot(self, ctx):
        return not self.visit(ctx.unario())

    def visitUnarioPrimario(self, ctx):
        return self.visit(ctx.primario())

    def visitPrimLlamada(self, ctx):
        return self.visit(ctx.llamada())

    def visitPrimArray(self, ctx):
        nombre = ctx.VAR().getText()
        indice = self.visit(ctx.expr())
        arr = self.get_var(nombre)
        return arr[indice]

    def visitPrimTrue(self, ctx):
        return True

    def visitPrimFalse(self, ctx):
        return False

    def visitPrimVar(self, ctx):
        return self.get_var(ctx.VAR().getText())

    def visitPrimNum(self, ctx):
        return int(ctx.NUM().getText())

    def visitPrimFnum(self, ctx):
        return float(ctx.FNUM().getText())

    def visitPrimStr(self, ctx):
        return ctx.STRVAL().getText()[1:-1]

    def visitPrimParen(self, ctx):
        return self.visit(ctx.expr())


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

    def visitIgualdad(self, ctx):
        left = self.visit(ctx.comparacion(0))
        for i in range(1, len(ctx.comparacion())):
            right = self.visit(ctx.comparacion(i))
            if ctx.IGUAL(i-1):
                left = left == right
            elif ctx.NOIGUAL(i-1) or ctx.DIFF(i-1):
                left = left != right
        return left

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

    def visitSuma(self, ctx):
        resultado = self.visit(ctx.producto(0))
        for i in range(1, len(ctx.producto())):
            right = self.visit(ctx.producto(i))
            op = ctx.getChild(2*i - 1).getText()
            if op == "+":
                resultado += right
            else:
                resultado -= right
        return resultado

    def visitProducto(self, ctx):
        resultado = self.visit(ctx.unario(0))
        for i in range(1, len(ctx.unario())):
            right = self.visit(ctx.unario(i))
            op = ctx.getChild(2*i - 1).getText()
            if op == "*":
                resultado *= right
            elif op == "/":
                resultado /= right
            elif op == "%":
                resultado %= right
        return resultado

    def visitUnario(self, ctx):
        if ctx.NOT():
            return not self.visit(ctx.unario())
        return self.visit(ctx.primario())

    def visitPrimario(self, ctx):
        if ctx.llamada():
            return self.visit(ctx.llamada())
        if ctx.getChildCount() == 4:
            nombre = ctx.VAR().getText()
            indice = self.visit(ctx.expr())
            arr = self.get_var(nombre)
            return arr[indice]
        if ctx.NUM():
            return int(ctx.NUM().getText())
        if ctx.FNUM():
            return float(ctx.FNUM().getText())
        if ctx.STRVAL():
            return ctx.STRVAL().getText()[1:-1]
        if ctx.TRUE():
            return True
        if ctx.FALSE():
            return False
        if ctx.VAR():
            return self.get_var(ctx.VAR().getText())
        if ctx.expr():
            return self.visit(ctx.expr())

    # ─────────────────────────────────────────
    # SCOPES
    # ─────────────────────────────────────────
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
    
    def visitUnarioCast(self,ctx):
        tipo_destino = ctx.tipodato().getText()
        valor = self.visit(ctx.unario())
        if tipo_destino == "int": 
            return int(valor)
        if tipo_destino == "float":
            return float(valor)
        if tipo_destino == "string": 
            return str(valor)
        if tipo_destino == "bool":
            return bool(valor)
        return  valor 
    
    def visitTernario(self,ctx):
        condicion = self.visit(ctx.logicalOr())
        if condicion: 
            return self.visit(ctx.expr(0))
        return self.visit(ctx.expr(1))

    def visitStructdecl(self,ctx):
        nombre = ctx.VAR().getText()
        campos = {}
        for campo in ctx.campostruct():
            campos[
                campo.VAR().getText()
            ] = None
        self.struct_defs[nombre] = campos

    def visitVarstruct(self,ctx):
        tipo = ctx.VAR(0).getText()
        nombre = ctx.VAR(1).getText()
        self.scopes[-1][nombre] = dict(
            self.struct_defs[tipo]
        )
    def visitStructasign(self,ctx):
        variable = ctx.VAR(0).getText()
        campo = ctx.VAR(1).getText()
        valor = self.visit(ctx.expr())
        self.get_var(variable)[campo] = valor

    def visitPrimStructAcceso(self,ctx):
        variable = ctx.VAR(0).getText()
        campo = ctx.VAR(1).getText()
        return self.get_var(variable)[campo]
    
    def visitSwitchstm(self,ctx):
        valor = self.visit(ctx.expr())
        ejecutado = False
        for case in ctx.caseclause():
            case_valor = self.visit(
                case.expr()
            )
            if valor == case_valor:
                ejecutado = True
                try:
                    for stmt in case.statement():
                        self.visit(stmt)
                except BreakException:
                    return
        if not ejecutado and ctx.defaultclause():
            for stmt in ctx.defaultclause().statement():
                self.visit(stmt)
    def visitUnarioNeg(self, ctx):
        return -self.visit(ctx.unario())            