from antlr.v3.gramatica_v3Visitor import gramatica_v3Visitor

class TACGenerator(gramatica_v3Visitor):

    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.label_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def emit(self, instruction):
        self.code.append(instruction)

    def get_code(self):
        return "\n".join(self.code)

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
        for stmt in ctx.statement():
            self.visit(stmt)

    # ─────────────────────────────────────────
    # VARIABLES
    # ─────────────────────────────────────────
    def visitVarint(self, ctx):
        nombre   = ctx.VAR().getText()
        tipo_str = ctx.getChild(0).getText()
        if ctx.expr():
            val = self.visit(ctx.expr())
            self.emit(f"{nombre} = {val}")
        else:
            default = '""' if tipo_str == "string" else "0"
            self.emit(f"{nombre} = {default}")

    def visitAsignacion(self, ctx):
        nombre = ctx.VAR().getText()
        val = self.visit(ctx.expr())
        self.emit(f"{nombre} = {val}")

    # ─────────────────────────────────────────
    # ARREGLOS
    # ─────────────────────────────────────────
    def visitArraydecl(self, ctx):
        nombre = ctx.VAR().getText()
        valores = [self.visit(e) for e in ctx.expr()]
        self.emit(f"{nombre} = [{', '.join(str(v) for v in valores)}]")

    def visitArrayasign(self, ctx):
        nombre = ctx.VAR().getText()
        indice = self.visit(ctx.expr(0))
        valor = self.visit(ctx.expr(1))
        self.emit(f"{nombre}[{indice}] = {valor}")

    # ─────────────────────────────────────────
    # IF
    # ─────────────────────────────────────────
    def visitIfstm(self, ctx):
        cond = self.visit(ctx.expr())
        l_true = self.new_label()
        l_end = self.new_label()

        self.emit(f"if {cond} goto {l_true}")

        if ctx.ELSE():
            self.visit(ctx.bloque(1))

        self.emit(f"goto {l_end}")
        self.emit(f"{l_true}:")
        self.visit(ctx.bloque(0))
        self.emit(f"{l_end}:")

    # ─────────────────────────────────────────
    # WHILE
    # ─────────────────────────────────────────
    def visitWhilestm(self, ctx):
        l_inicio = self.new_label()
        l_fin = self.new_label()

        self.emit(f"{l_inicio}:")
        cond = self.visit(ctx.expr())
        self.emit(f"ifFalse {cond} goto {l_fin}")
        self.visit(ctx.bloque())
        self.emit(f"goto {l_inicio}")
        self.emit(f"{l_fin}:")

    # ─────────────────────────────────────────
    # FOR
    # ─────────────────────────────────────────
    def visitForstm(self, ctx):
        self.visit(ctx.getChild(2))
        l_inicio = self.new_label()
        l_fin = self.new_label()

        self.emit(f"{l_inicio}:")
        cond = self.visit(ctx.expr())
        self.emit(f"ifFalse {cond} goto {l_fin}")
        self.visit(ctx.bloque())
        self.visit(ctx.getChild(6))
        self.emit(f"goto {l_inicio}")
        self.emit(f"{l_fin}:")

    # ─────────────────────────────────────────
    # BREAK / CONTINUE
    # ─────────────────────────────────────────
    def visitBreakstm(self, ctx):
        self.emit("break")

    def visitContinuestm(self, ctx):
        self.emit("continue")

    # ─────────────────────────────────────────
    # IMPORT
    # ─────────────────────────────────────────
    def visitImportstm(self, ctx):
        modulo = ctx.VAR().getText()
        self.emit(f"import {modulo}")

    # ─────────────────────────────────────────
    # FUNCIONES
    # ─────────────────────────────────────────
    def visitFuncion(self, ctx):
        nombre = ctx.VAR().getText()
        self.emit(f"begin_func {nombre}")

        if ctx.parametros():
            for p in ctx.parametros().parametro():
                self.emit(f"param {p.VAR().getText()}")

        self.visit(ctx.bloque())
        self.emit(f"end_func {nombre}")

    def visitReturnstm(self, ctx):
        val = self.visit(ctx.expr())
        self.emit(f"return {val}")

    def visitLlamada(self, ctx):
        nombre = ctx.VAR().getText()
        args = [self.visit(e) for e in ctx.expr()] if ctx.expr() else []
        for arg in args:
            self.emit(f"arg {arg}")
        t = self.new_temp()
        self.emit(f"{t} = call {nombre}, {len(args)}")
        return t

    # ─────────────────────────────────────────
    # PRINT
    # ─────────────────────────────────────────
    def visitPrintstm(self, ctx):
        val = self.visit(ctx.expr())
        self.emit(f"print {val}")

    # ─────────────────────────────────────────
    # EXPRESIONES
    # ─────────────────────────────────────────
    def visitExpr(self, ctx):
        return self.visit(ctx.logicalOr())

    def visitLogicalOr(self, ctx):
        resultado = self.visit(ctx.logicalAnd(0))
        for i in range(1, len(ctx.logicalAnd())):
            right = self.visit(ctx.logicalAnd(i))
            t = self.new_temp()
            self.emit(f"{t} = {resultado} || {right}")
            resultado = t
        return resultado

    def visitLogicalAnd(self, ctx):
        resultado = self.visit(ctx.igualdad(0))
        for i in range(1, len(ctx.igualdad())):
            right = self.visit(ctx.igualdad(i))
            t = self.new_temp()
            self.emit(f"{t} = {resultado} && {right}")
            resultado = t
        return resultado

    def visitIgualdad(self, ctx):
        resultado = self.visit(ctx.comparacion(0))
        for i in range(1, len(ctx.comparacion())):
            right = self.visit(ctx.comparacion(i))
            t = self.new_temp()
            if ctx.IGUAL(i-1):
                self.emit(f"{t} = {resultado} == {right}")
            else:
                self.emit(f"{t} = {resultado} != {right}")
            resultado = t
        return resultado

    def visitComparacion(self, ctx):
        resultado = self.visit(ctx.suma(0))
        for i in range(1, len(ctx.suma())):
            right = self.visit(ctx.suma(i))
            t = self.new_temp()
            op = ctx.getChild(2*i - 1).getText()
            self.emit(f"{t} = {resultado} {op} {right}")
            resultado = t
        return resultado

    def visitSuma(self, ctx):
        resultado = self.visit(ctx.producto(0))
        for i in range(1, len(ctx.producto())):
            right = self.visit(ctx.producto(i))
            t = self.new_temp()
            op = ctx.getChild(2*i - 1).getText()
            self.emit(f"{t} = {resultado} {op} {right}")
            resultado = t
        return resultado

    def visitProducto(self, ctx):
        resultado = self.visit(ctx.unario(0))
        for i in range(1, len(ctx.unario())):
            right = self.visit(ctx.unario(i))
            t = self.new_temp()
            op = ctx.getChild(2*i - 1).getText()
            self.emit(f"{t} = {resultado} {op} {right}")
            resultado = t
        return resultado

    def visitUnario(self, ctx):
        if ctx.NOT():
            val = self.visit(ctx.unario())
            t = self.new_temp()
            self.emit(f"{t} = !{val}")
            return t
        return self.visit(ctx.primario())

    def visitPrimario(self, ctx):
        if ctx.llamada():
            return self.visit(ctx.llamada())
        if ctx.getChildCount() == 4:
            nombre = ctx.VAR().getText()
            indice = self.visit(ctx.expr())
            t = self.new_temp()
            self.emit(f"{t} = {nombre}[{indice}]")
            return t
        if ctx.NUM():
            return ctx.NUM().getText()
        if ctx.FNUM():
            return ctx.FNUM().getText()
        if ctx.STRVAL():
            return ctx.STRVAL().getText()
        if ctx.TRUE():
            return "true"
        if ctx.FALSE():
            return "false"
        if ctx.VAR():
            return ctx.VAR().getText()
        if ctx.expr():
            return self.visit(ctx.expr())