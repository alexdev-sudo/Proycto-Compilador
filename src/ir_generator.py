from llvmlite import ir
from antlr.v3.gramatica_v3Visitor import gramatica_v3Visitor
from src.tabla_simbolos import TablaSibolos
class IRGenerator(gramatica_v3Visitor):

    def __init__(self):
        self.module = ir.Module(name="programa")
        self.loop_stack = []

        # tipos
        self.int_type = ir.IntType(32)
        self.float_type = ir.DoubleType()
        self.bool_type = ir.IntType(1)

        # funcion main
        func_type = ir.FunctionType(ir.VoidType(), [])
        self.main_func = ir.Function(self.module, func_type, name="main")

        block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        # tabla de variables
        self.scopes = [{}]

        self.printf = ir.Function(
        self.module,
        ir.FunctionType(ir.IntType(32), [ir.IntType(8).as_pointer()], var_arg=True),
        name="printf")

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        self.scopes.pop()

    def declare_var(self, name, ptr):
        if name in self.scopes[-1]:
            raise Exception(f"Variable '{name}' ya declarada en este scope")
        self.scopes[-1][name] = ptr

    def get_var(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Variable '{name}' no definida")   

    def create_string(self, text):
        text_bytes = bytearray(text.encode("utf8")) + b"\00"

        string_type = ir.ArrayType(ir.IntType(8), len(text_bytes))
        global_var = ir.GlobalVariable(
            self.module,
            string_type,
            name=f"str_{len(self.module.globals)}"
        )
        global_var.global_constant = True
        global_var.initializer = ir.Constant(string_type, text_bytes)

        zero = ir.Constant(self.int_type, 0)
        ptr = self.builder.gep(global_var, [zero, zero])

        #
        ptr.string_value = text

        return ptr
    def visitProgramaRule(self, ctx):
        self.visit(ctx.bloque())
        self.builder.ret_void()
        return self.module
    
    def visitVarint(self, ctx):
        name = ctx.VAR().getText()

        value = self.visit(ctx.expr()) if ctx.expr() else None

        if value is None:
            value = ir.Constant(self.int_type, 0)

        with self.builder.goto_entry_block():
            ptr = self.builder.alloca(value.type, name=name)

        self.builder.store(value, ptr)

        self.declare_var(name, ptr)
    def visitPrimario(self, ctx):
        if ctx.NUM():
            return ir.Constant(self.int_type, int(ctx.NUM().getText()))
        if ctx.STRVAL():
            text = ctx.STRVAL().getText().strip('"')
            return self.create_string(text)

        if ctx.VAR() and ctx.LBRACKET():
            name = ctx.VAR().getText()
            index = self.visit(ctx.expr())
            ptr = self.get_var(name)
            gep = self.builder.gep(ptr, [ir.Constant(self.int_type, 0), index])
            return self.builder.load(gep)

        if ctx.VAR():
            ptr = self.get_var(ctx.VAR().getText())
            if ptr is None:
                raise Exception(f"Variable {ctx.VAR().getText()} no definida en IR")
            return self.builder.load(ptr)

        if ctx.expr():
            val = self.visit(ctx.expr())
            if val is None:
                raise Exception("visitPrimario: visit(ctx.expr()) devolvió None")
            return val

        

       
    def visitSuma(self, ctx):
        left = self.visit(ctx.producto(0))

        for i in range(1, len(ctx.producto())):
            right = self.visit(ctx.producto(i))

           
            #concatenacion de strings
            # ─────────────────────────────
            if hasattr(left, "string_value") and hasattr(right, "string_value"):
                new_str = left.string_value + right.string_value
                return self.create_string(new_str)
           
            # enteros
            # ─────────────────────────────
            if ctx.SUM(i-1):
                left = self.builder.add(left, right)
            else:
                left = self.builder.sub(left, right)

        return left
    
    def visitComparacion(self, ctx):
        left = self.visit(ctx.suma(0))

        for i in range(1, len(ctx.suma())):
            right = self.visit(ctx.suma(i)) 

            if ctx.MENOR(i-1):
                left = self.builder.icmp_signed('<', left, right)
            elif ctx.MAYOR(i-1):
                left = self.builder.icmp_signed('>', left, right)
            elif ctx.MENORIGUAL(i-1):
                left = self.builder.icmp_signed('<=', left, right)
            elif ctx.MAYORIGUAL(i-1):
                left = self.builder.icmp_signed('>=', left, right)

        return left
    #Implementacion de acceso a arrays y declaración de arrays
    def visitArraydecl(self, ctx):
        name = ctx.VAR().getText()
        values = [self.visit(e) for e in ctx.expr()]

        array_type = ir.ArrayType(self.int_type, len(values))

        with self.builder.goto_entry_block():
            ptr = self.builder.alloca(array_type, name=name)

        for i, val in enumerate(values):
            gep = self.builder.gep(ptr, [ir.Constant(self.int_type, 0),
                                        ir.Constant(self.int_type, i)])
            self.builder.store(val, gep)

        self.declare_var(name, ptr)
    
    def visitPrintstm(self, ctx):
        value = self.visit(ctx.expr())

        if isinstance(value.type, ir.IntType):
            fmt = self.create_string("%d\n")
            self.builder.call(self.printf, [fmt, value])
        else:
            fmt = self.create_string("%s\n")
            self.builder.call(self.printf, [fmt, value])

    def visitProducto(self, ctx):
        left = self.visit(ctx.unario(0))

        for i in range(1, len(ctx.unario())):
            right = self.visit(ctx.unario(i))

            if left is None or right is None:
                raise Exception("Error: operación con valor None en producto")

            if ctx.MUL(i-1):
                left = self.builder.mul(left, right)
            elif ctx.DIV(i-1):
                left = self.builder.sdiv(left, right)
            elif ctx.MOD(i-1):
                left = self.builder.srem(left, right)

        return left
    def get_ir(self):
        return str(self.module)
    def visitIfstm(self, ctx):
        cond = self.visit(ctx.expr()) 
        if isinstance(cond.type, ir.IntType) and cond.type.width != 1:
            cond = self.builder.icmp_signed("!=", cond, ir.Constant(cond.type, 0))

        then_block = self.builder.append_basic_block("if_then")
        else_block = self.builder.append_basic_block("if_else")
        end_block = self.builder.append_basic_block("if_end")
        

        self.builder.cbranch(cond, then_block, else_block)

        # THEN
        self.builder.position_at_start(then_block)
        self.visit(ctx.bloque(0))
        if not self.builder.block.is_terminated:
            self.builder.branch(end_block)

        # ELSE
        self.builder.position_at_start(else_block)
        if ctx.ELSE():
            self.visit(ctx.bloque(1))
        if not self.builder.block.is_terminated:
            self.builder.branch(end_block)

        # END
        self.builder.position_at_start(end_block)

    def visitWhilestm(self, ctx):
        loop_cond = self.builder.append_basic_block("while_cond")
        loop_body = self.builder.append_basic_block("while_body")
        loop_end = self.builder.append_basic_block("while_end")

        # guardar destino de break
        self.loop_stack.append(loop_end)

        #conectar flujo actual al while
        self.builder.branch(loop_cond)

        # ─────────────
        # CONDICIÓN
     
        self.builder.position_at_start(loop_cond)
        cond = self.visit(ctx.expr())

        if isinstance(cond.type, ir.IntType) and cond.type.width != 1:
            cond = self.builder.icmp_signed("!=", cond, ir.Constant(cond.type, 0))
        self.builder.cbranch(cond, loop_body, loop_end)

        # CUERPO
  
        self.builder.position_at_start(loop_body)
        self.visit(ctx.bloque())

        # volver a evaluar condición
        if not self.builder.block.is_terminated:
            self.builder.branch(loop_cond)

       
        # FIN
       
        self.builder.position_at_start(loop_end)

        self.loop_stack.pop()

    def visitBreakstm(self, ctx):
        if not self.loop_stack:
            raise Exception("break fuera de loop")

        self.builder.branch(self.loop_stack[-1]) 

    def visitAsignacion(self, ctx):
        name = ctx.VAR().getText()
        value = self.visit(ctx.expr())

        ptr = self.get_var(name)
        self.builder.store(value, ptr)

        return value    
    
