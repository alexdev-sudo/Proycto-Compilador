# Generador de codigo intermedio (TAC)

from turtle import left
from antlr.v3.gramatica_v3Visitor import gramatica_v3Visitor
from src.tabla_simbolos import TablaSibolos

# Clase que recorre el árbol sintáctico (AST) y genera código intermedio (TAC)
class TACGenerator(gramatica_v3Visitor):
    def __init__(self):
        # Lista donde se almacena el código TAC generado
        self.code = []
        self.temp_count = 0
        self.label_count = 0

# Manejo de valores constantes (enteros, floats, strings, booleanos)
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
 # Evalúa expresiones multiplicativas generando temporales
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
   # Genera código TAC para comparaciones relacionales 
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

   # Manejo de asignaciones y declaracion de variables 
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



    # Implementacion del ciclo while usando etiquetas de inicio y fin
    def visitWhilestm(self, ctx):

        Lstart = self.new_label()
        Lend = self.new_label()

        self.code.append(f"{Lstart}:")

        cond = self.visit(ctx.expr())
        self.code.append(f"ifFalse {cond} goto {Lend}")

        self.visit(ctx.bloque())

        self.code.append(f"goto {Lstart}")
        self.code.append(f"{Lend}:")    

    # Manejo de ciclo while con etiquetas de inicio y fin
    def visitWhilestm(self, ctx):

        Lstart = self.new_label()
        Lend = self.new_label()

        self.code.append(f"{Lstart}:")

        cond = self.visit(ctx.expr())
        self.code.append(f"ifFalse {cond} goto {Lend}")

        self.visit(ctx.bloque())

        self.code.append(f"goto {Lstart}")
        self.code.append(f"{Lend}:")   

  # Genera una nueva variable temporal  
    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"
    
# Genera una nueva etiqueta
    def new_label(self):
        self.label_count += 1
        return f"l{self.label_count}"
    
  # Maneja operaciones + y - usando temporales  
    def visitSuma(self, ctx):
        left = self.visit(ctx.producto(0))

        for i in range(1, len(ctx.producto())):
            right = self.visit(ctx.producto(i))
            temp = self.new_temp()

            op = "+" if ctx.SUM(i-1) else "-"
            self.code.append(f"{temp} = {left} {op} {right}")
            left = temp

        return left
    
    # Manejo de estructura condicional if-else  
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

   # Validación de operadores de igualdad ==, !=     
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

# Retorna el código TAC completo como string  
    def get_code(self):
        return "\n".join(self.code)
