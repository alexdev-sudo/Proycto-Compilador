from antlr4 import *
from antlr.v4.gramatica_v4Visitor import gramatica_v4Visitor
from antlr.v4.gramatica_v4Parser import gramatica_v4Parser
from src.tabla_simbolos import TablaSibolos

class semanticVisitor(gramatica_v4Visitor):


    def __init__(self):
        self.tabla_simbolos = TablaSibolos()
        self.errors = []
        self.current_function = None

    def error(self, msg, ctx):
        line = ctx.start.line
        col = ctx.start.column
        self.errors.append(f"[Error Semántico] Línea {line}, Columna {col}: {msg}")

    def compatible(self, expected, received):
        if expected == received:
            return True
        if expected == "float" and received == "int":
            return True
        return False    

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
        is_global = isinstance(ctx.parentCtx, gramatica_v4Parser.ProgramaRuleContext)
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
            if not self.compatible(tipo, expr_type):
                self.error(f"Tipo incompatible: no se puede asignar '{expr_type}' a '{tipo}'", ctx)

    def visitAsignacion(self, ctx):
        name = ctx.VAR().getText()
        expr_type = self.visit(ctx.expr())
        try:
            var_type = self.tabla_simbolos.lookup(name)
            if not self.compatible(var_type, expr_type):
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

        for expr in ctx.expr():
            expr_type = self.visit(expr)
            if expr_type != tipo:
                self.error(f"Elemento de arreglo incompatible: se esperaba '{tipo}' pero se obtuvo '{expr_type}'", expr)

    def visitArrayasign(self, ctx):
        name = ctx.VAR().getText()
        index_type = self.visit(ctx.expr(0))
        value_type = self.visit(ctx.expr(1))
        if index_type != "int":
            self.error(f"El índice del arreglo debe ser int, recibió '{index_type}'", ctx)
        try:
            array_type = self.tabla_simbolos.lookup(name)
            if not array_type.endswith("[]"):
                self.error(f"'{name}' no es un arreglo", ctx)
                return
            element_type = array_type.replace("[]", "")
            if element_type != value_type:
                self.error(f"Tipo incompatible: no se puede asignar '{value_type}' a '{element_type}'", ctx)
        except Exception as e:
            self.error(str(e), ctx)


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
        else:
            for i in range(len(args)):
                esperado = func["params"][i][1]
                recibido = args[i]
                if esperado != recibido: 
                    self.error(
                        f"argumento {i+1}: se esperaba '{esperado}' pero se recibio '{recibido}'",
                        ctx)
        
        
        return func["return_type"]

    # ─────────────────────────────────────────
    # PRINT
    # ─────────────────────────────────────────
    def visitPrintstm(self, ctx):
        return self.visit(ctx.expr())

    # ─────────────────────────────────────────
    # EXPRESIONES
    # ─────────────────────────────────────────
    def visitExprSimple(self, ctx):
        return self.visit(ctx.logicalOr())

    def visitLogicalOr(self, ctx):
        left = self.visit(ctx.logicalAnd(0))
        for i in range(1, len(ctx.logicalAnd())):
            right = self.visit(ctx.logicalAnd(i))
            if left != "bool" or right != "bool":
                self.error(f"Operador || requiere bool y bool, recibió '{left}' y '{right}'", ctx)
            left = "bool"
        return left

    def visitLogicalAnd(self, ctx):
        left = self.visit(ctx.igualdad(0))
        for i in range(1, len(ctx.igualdad())):
            right = self.visit(ctx.igualdad(i))
            if left != "bool" or right != "bool":
                self.error(f"Operador && requiere bool y bool, recibió '{left}' y '{right}'", ctx)
            left = "bool"
        return left

    def visitIgualdad(self, ctx):
        left = self.visit(ctx.comparacion(0))
        for i in range(1, len(ctx.comparacion())):
            right = self.visit(ctx.comparacion(i))
            if left != right:
                self.error(f"Tipos incompatibles en comparación: '{left}' y '{right}'", ctx)
            left = "bool"
        return left

    def visitComparacion(self, ctx):
        left = self.visit(ctx.suma(0))
        for i in range(1, len(ctx.suma())):
            right = self.visit(ctx.suma(i))
            if left not in ("int", "float") or right not in ("int", "float"):
                self.error(f"Comparación relacional requiere números, recibió '{left}' y '{right}'", ctx)
            left = "bool"
        return left

    def visitSuma(self, ctx):
        left = self.visit(ctx.producto(0))

        for i in range(1, len(ctx.producto())):
            right = self.visit(ctx.producto(i))

            if left == right:
                continue

            if left in ("int", "float") and right in ("int", "float"):
                left = "float"
                continue

            self.error(f"Tipos incompatibles en operación: '{left}' y '{right}'", ctx)

        return left

    def visitProducto(self, ctx):
        left = self.visit(ctx.unario(0))

        for i in range(1, len(ctx.unario())):
            right = self.visit(ctx.unario(i))

            if left == right:
                continue

            if left in ("int", "float") and right in ("int", "float"):
                left = "float"
                continue

            self.error(f"Tipos incompatibles en operación: '{left}' y '{right}'", ctx)

        return left

    def visitUnarioNot(self, ctx):
        tipo = self.visit(ctx.unario())
        if tipo != "bool":
            self.error(f"El operador ! requiere bool, recibió '{tipo}'", ctx)
        return "bool"

    def visitUnarioNeg(self, ctx):
        tipo = self.visit(ctx.unario())
        if tipo not in ("int", "float"):
            self.error(f"El operador - requiere int o float, recibió '{tipo}'", ctx)
        return tipo

    def visitUnarioCast(self, ctx):
        tipo_destino = ctx.tipodato().getText()
        self.visit(ctx.unario())
        return tipo_destino

    def visitUnarioPrimario(self, ctx):
        return self.visit(ctx.primario())

    def visitTernario(self, ctx):
        condicion = self.visit(ctx.logicalOr())
        tipo_true = self.visit(ctx.expr(0))
        tipo_false = self.visit(ctx.expr(1))

        if condicion != "bool":
            self.error(f"La condición del ternario debe ser bool, recibió '{condicion}'", ctx)

        if tipo_true != tipo_false:
            self.error("Ambas ramas del ternario deben ser del mismo tipo", ctx)

        return tipo_true

    def visitPrimLlamada(self, ctx):
        return self.visit(ctx.llamada())

    def visitPrimArray(self, ctx):
        name = ctx.VAR().getText()
        index_type = self.visit(ctx.expr())

        if index_type != "int":
            self.error(f"El índice del arreglo debe ser int, recibió '{index_type}'", ctx)

        try:
            tipo = self.tabla_simbolos.lookup(name)
            if not tipo.endswith("[]"):
                self.error(f"'{name}' no es un arreglo", ctx)
                return "error"
            return tipo.replace("[]", "")
        except Exception as e:
            self.error(str(e), ctx)
            return "error"

    def visitPrimStructAcceso(self, ctx):
        variable = ctx.VAR(0).getText()
        campo = ctx.VAR(1).getText()

        try:
            tipo_var = self.tabla_simbolos.lookup(variable)

            if not tipo_var.startswith("struct:"):
                self.error(f"'{variable}' no es struct", ctx)
                return "error"

            nombre_struct = tipo_var.split(":", 1)[1]
            campos = self.tabla_simbolos.get_struct(nombre_struct)

            if campo not in campos:
                self.error(f"Campo '{campo}' inexistente", ctx)
                return "error"

            return campos[campo]

        except Exception as e:
            self.error(str(e), ctx)
            return "error"

    def visitPrimTrue(self, ctx):
        return "bool"

    def visitPrimFalse(self, ctx):
        return "bool"

    def visitPrimVar(self, ctx):
        try:
            return self.tabla_simbolos.lookup(ctx.VAR().getText())
        except Exception as e:
            self.error(str(e), ctx)
            return "error"

    def visitPrimNum(self, ctx):
        return "int"

    def visitPrimFnum(self, ctx):
        return "float"

    def visitPrimStr(self, ctx):
        return "string"

    def visitPrimParen(self, ctx):
        return self.visit(ctx.expr()) 
        
    def visitStructdecl(self,ctx):

        nombre = ctx.VAR().getText()

        campos = {}

        for campo in ctx.campostruct():

            tipo = campo.tipodato().getText()

            nombre_campo = campo.VAR().getText()

            campos[nombre_campo] = tipo

        try:
            self.tabla_simbolos.declare_struct(
                nombre,
                campos
            )
        except Exception as e:
            self.error(str(e),ctx)
        #intanciacion de la estructura, acepetara ejemplo punto p ; p.x
    def visitVarstruct(self,ctx):
        tipo_struct = ctx.VAR(0).getText()
        variable = ctx.VAR(1).getText()
        try:
            self.tabla_simbolos.get_struct(
                tipo_struct
            )
            self.tabla_simbolos.declare(
                variable,
                f"struct:{tipo_struct}"
            )
        except Exception as e:
            self.error(str(e),ctx)    

            #asignacion a campos de la estructura ejemplo p.x =5 
    def visitStructasign(self,ctx):
        variable = ctx.VAR(0).getText()
        campo = ctx.VAR(1).getText()
        valor_tipo = self.visit(
            ctx.expr()
        )
        try:
            tipo_var = self.tabla_simbolos.lookup(
                variable
            )
            if not tipo_var.startswith("struct:"):
                self.error(
                    "No es struct",
                    ctx
                )
                return
            nombre_struct = tipo_var.split(":")[1]
            campos = self.tabla_simbolos.get_struct(
                nombre_struct
            )
            if campo not in campos:
                self.error(
                    f"Campo '{campo}' inexistente",
                    ctx
                )
            elif not self.compatible(campos[campo], valor_tipo):
                self.error(
                    "Tipo incompatible",
                    ctx
                )
        except Exception as e:
            self.error(str(e),ctx)

#acceso a campos de la estructura ejemplo p.x permite p.x dentro de expresiones 
    def visitPrimStructAcceso(self,ctx):
        variable = ctx.VAR(0).getText()
        campo = ctx.VAR(1).getText()
        try:
            tipo_var = self.tabla_simbolos.lookup(
                variable
            )
            nombre_struct = tipo_var.split(":")[1]

            campos = self.tabla_simbolos.get_struct(
                nombre_struct
            )
            return campos[campo]
        except Exception as e:
            self.error(str(e),ctx)
            return "error"
    
     # funcion switch case permite switch(expr){ case valor: bloque; break; default: bloque}
    def visitSwitchstm(self, ctx):
        # 1. Obtenemos el tipo de la expresión principal del switch
        tipo_switch = self.visit(ctx.expr())
        
        # 2. Visitamos cada case pasando el tipo_switch para que se valide dentro
        for case in ctx.caseclause():
            # Le pasamos el tipo_switch como un argumento personalizado al método del case
            self.visitCaseclause_con_tipo(case, tipo_switch)
            
        if ctx.defaultclause():
            self.visit(ctx.defaultclause())

    # Método intermedio para poder pasarle el tipo del switch al case
    def visitCaseclause_con_tipo(self, ctx, tipo_switch):
        # 1. Obtenemos el tipo del valor del case actual (ej: "hola" -> string, 5 -> int)
        tipo_case = self.visit(ctx.expr())

        # 2. Validamos si ambos tipos son compatibles
        if tipo_case != tipo_switch:
            self.error(
                f"Tipo incompatible en el case. El switch espera '{tipo_switch}' pero recibió '{tipo_case}'.", 
                ctx
            )

        # 3. Continuamos con la visita de las instrucciones dentro del case
        for stmt in ctx.statement():
            self.visit(stmt)

    # Dejamos el método original por si ANTLR lo llama automáticamente en otra parte
    def visitCaseclause(self, ctx):
        # Si entra por aquí de forma general, solo visita sin validar tipo
        self.visit(ctx.expr())
        for stmt in ctx.statement():
            self.visit(stmt)
    def visitDefaultclause(self,ctx):

        for stmt in ctx.statement():
            self.visit(stmt)
