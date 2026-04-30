from antlr4 import *
from antlr.v3.gramatica_v3Visitor import gramatica_v3Visitor
from antlr.v3.gramatica_v3Parser import gramatica_v3Parser
from src.tabla_simbolos import TablaSibolos

class semanticVisitor(gramatica_v3Visitor):

    def __init__(self):
        self.tabla_simbolos = TablaSibolos()
        self.errors = []
        self.current_function = None

    def error(self, msg, ctx):
        line = ctx.start.line
        col = ctx.start.column
        self.errors.append(f"[Error semántico] en línea {line}, columna {col}: {msg}")

    def visitExprInput(self, ctx):
        return self.visit(ctx.expr())

    def visitProgInput(self, ctx):
        return self.visit(ctx.programa())

    def visitProgramaRule(self, ctx):
        return self.visit(ctx.bloque())

    # ─────────────────────────────────────────
    # BLOQUE
    # ─────────────────────────────────────────
    def visitBloque(self, ctx):
        is_global = isinstance(ctx.parentCtx, gramatica_v3Parser.ProgramaRuleContext)
        if not is_global:
            self.tabla_simbolos.push()
        for stmt in ctx.statement():
            self.visit(stmt)
        if not is_global:
            self.tabla_simbolos.pop()

    # ─────────────────────────────────────────
    # VARIABLES
    # ─────────────────────────────────────────
    def visitVarint(self, ctx):
        name = ctx.VAR().getText()
        tipo = ctx.getChild(0).getText()
        try:
            self.tabla_simbolos.declare(name, tipo)
        except Exception as e:
            self.error(str(e), ctx)
        if ctx.expr():
            expr_type = self.visit(ctx.expr())
            if expr_type != tipo:
                self.error(f"Tipo incompatible: no se puede asignar '{expr_type}' a '{tipo}'", ctx)

    def visitAsignacion(self, ctx):
        name = ctx.VAR().getText()
        expr_type = self.visit(ctx.expr())
        try:
            var_type = self.tabla_simbolos.lookup(name)
            if var_type != expr_type:
                self.error(f"Tipo incompatible: no se puede asignar '{expr_type}' a '{var_type}'", ctx)
        except Exception as e:
            self.error(str(e), ctx)

    # ─────────────────────────────────────────
    # ARREGLOS
    # ─────────────────────────────────────────
    def visitArraydecl(self, ctx):
        name = ctx.VAR().getText()
        tipo = ctx.getChild(0).getText()
        try:
            self.tabla_simbolos.declare(name, f"{tipo}[]")
        except Exception as e:
            self.error(str(e), ctx)
        for e in ctx.expr():
            self.visit(e)

    def visitArrayasign(self, ctx):
        name = ctx.VAR().getText()
        try:
            self.tabla_simbolos.lookup(name)
        except Exception as e:
            self.error(str(e), ctx)
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))

    # ─────────────────────────────────────────
    # CONTROL DE FLUJO
    # ─────────────────────────────────────────
    def visitIfstm(self, ctx):
        self.visit(ctx.expr())
        self.visit(ctx.bloque(0))
        if ctx.ELSE():
            self.visit(ctx.bloque(1))

    def visitWhilestm(self, ctx):
        self.visit(ctx.expr())
        self.visit(ctx.bloque())

    def visitForstm(self, ctx):
        self.visit(ctx.getChild(2))
        self.visit(ctx.expr())
        self.visit(ctx.bloque())
        self.visit(ctx.getChild(6))

    def visitBreakstm(self, ctx):
        pass

    def visitContinuestm(self, ctx):
        pass

    def visitImportstm(self, ctx):
        pass

    # ─────────────────────────────────────────
    # FUNCIONES
    # ─────────────────────────────────────────
    def visitFuncion(self, ctx):
        name = ctx.VAR().getText()
        return_type = ctx.getChild(0).getText()
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

        self.current_function = return_type
        self.tabla_simbolos.push()
        for nombre, tipo in params:
            try:
                self.tabla_simbolos.declare(nombre, tipo)
            except Exception as e:
                self.error(str(e), ctx)
        self.visit(ctx.bloque())
        self.tabla_simbolos.pop()
        self.current_function = None

    def visitReturnstm(self, ctx):
        expr_type = self.visit(ctx.expr())
        if self.current_function and expr_type != self.current_function:
            self.error(f"Tipo de retorno incorrecto: se esperaba '{self.current_function}' pero se obtuvo '{expr_type}'", ctx)
        return expr_type

    def visitLlamada(self, ctx):
        name = ctx.VAR().getText()
        try:
            func = self.tabla_simbolos.get_function(name)
        except Exception as e:
            self.error(str(e), ctx)
            return 'error'
        args = [self.visit(e) for e in ctx.expr()] if ctx.expr() else []
        if len(args) != len(func["params"]):
            self.error("Cantidad incorrecta de argumentos", ctx)
        return func["return_type"]

    # ─────────────────────────────────────────
    # PRINT
    # ─────────────────────────────────────────
    def visitPrintstm(self, ctx):
        return self.visit(ctx.expr())

    # ─────────────────────────────────────────
    # EXPRESIONES
    # ─────────────────────────────────────────
    def visitPrimario(self, ctx):
        if ctx.llamada():
            return self.visit(ctx.llamada())
        if ctx.getChildCount() == 4:
            name = ctx.VAR().getText()
            try:
                tipo = self.tabla_simbolos.lookup(name)
                return tipo.replace("[]", "")
            except Exception as e:
                self.error(str(e), ctx)
                return 'error'
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

    def visitSuma(self, ctx):
        left = self.visit(ctx.producto(0))
        for i in range(1, len(ctx.producto())):
            right = self.visit(ctx.producto(i))
            if left != right:
                self.error(f"Tipos incompatibles en operación: '{left}' y '{right}'", ctx)
        return left

    def visitProducto(self, ctx):
        left = self.visit(ctx.unario(0))
        for i in range(1, len(ctx.unario())):
            right = self.visit(ctx.unario(i))
            if left != right:
                self.error(f"Tipos incompatibles en operación: '{left}' y '{right}'", ctx)
        return left