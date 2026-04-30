from turtle import left
from antlr.v3.gramatica_v3Visitor import gramatica_v3Visitor
from src.tabla_simbolos import TablaSibolos

class TACGenerator(gramatica_v3Visitor):
    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.label_count = 0


    def visitPrimario(self, ctx):

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

        # array acceso
        if ctx.VAR() and ctx.LBRACKET():
            name = ctx.VAR().getText()
            index = self.visit(ctx.expr())
            temp = self.new_temp()
            self.code.append(f"{temp} = {name}[{index}]")
            return temp

        if ctx.VAR():
            return ctx.VAR().getText()

        if ctx.expr():
            return self.visit(ctx.expr())    
    def visitProducto(self, ctx):

        left = self.visit(ctx.unario(0))

        for i in range(1, len(ctx.unario())):
            right = self.visit(ctx.unario(i))
            temp = self.new_temp()

            if ctx.MUL(i-1):
                op = "*"
            elif ctx.DIV(i-1):
                op = "/"
            elif ctx.MOD(i-1):
                op = "%"

            self.code.append(f"{temp} = {left} {op} {right}")
            left = temp

        return left    
    def visitComparacion(self, ctx):

        left = self.visit(ctx.suma(0))

        for i in range(1, len(ctx.suma())):
            right = self.visit(ctx.suma(i))
            temp = self.new_temp()

            if ctx.MAYOR(i-1):
                op = ">"
            elif ctx.MENOR(i-1):
                op = "<"
            elif ctx.MAYORIGUAL(i-1):
                op = ">="
            elif ctx.MENORIGUAL(i-1):
                op = "<="

            self.code.append(f"{temp} = {left} {op} {right}")
            left = temp

        return left

    
    def visitAsignacion(self, ctx):

        name = ctx.VAR().getText()
        value = self.visit(ctx.expr())

        self.code.append(f"{name} = {value}")
        return name
    
    def visitVarint(self, ctx):

        name = ctx.VAR().getText()

        if ctx.expr():
            value = self.visit(ctx.expr())
        else:
            value = "0"

        self.code.append(f"{name} = {value}")
        

    def visitWhilestm(self, ctx):

        Lstart = self.new_label()
        Lend = self.new_label()

        self.code.append(f"{Lstart}:")

        cond = self.visit(ctx.expr())
        self.code.append(f"ifFalse {cond} goto {Lend}")

        self.visit(ctx.bloque())

        self.code.append(f"goto {Lstart}")
        self.code.append(f"{Lend}:")    

    def visitWhilestm(self, ctx):

        Lstart = self.new_label()
        Lend = self.new_label()

        self.code.append(f"{Lstart}:")

        cond = self.visit(ctx.expr())
        self.code.append(f"ifFalse {cond} goto {Lend}")

        self.visit(ctx.bloque())

        self.code.append(f"goto {Lstart}")
        self.code.append(f"{Lend}:")   
    
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"l{self.label_count}"
    
    def visitSuma(self, ctx):
        left = self.visit(ctx.producto(0))

        for i in range(1, len(ctx.producto())):
            right = self.visit(ctx.producto(i))
            temp = self.new_temp()

            op = "+" if ctx.SUM(i-1) else "-"
            self.code.append(f"{temp} = {left} {op} {right}")
            left = temp

        return left
    
    def visitIfstm(self, ctx):
        cond = self.visit(ctx.expr())

        L1 = self.new_label()
        L2 = self.new_label()

        self.code.append(f"ifFalse {cond} goto {L1}")
        self.visit(ctx.bloque(0))
        self.code.append(f"goto {L2}")
        self.code.append(f"{L1}:")

        if ctx.ELSE():
            self.visit(ctx.bloque(1))

        self.code.append(f"{L2}:")
        
    def visitIgualdad(self, ctx):

        left = self.visit(ctx.comparacion(0))

        for i in range(1, len(ctx.comparacion())):
            right = self.visit(ctx.comparacion(i))
            temp = self.new_temp()

            if ctx.IGUAL(i-1):
                op = "=="
            elif ctx.NOIGUAL(i-1) or ctx.DIFF(i-1):
                op = "!="

            self.code.append(f"{temp} = {left} {op} {right}")
            left = temp

        return left
