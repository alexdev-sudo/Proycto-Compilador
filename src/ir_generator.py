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
        global_var = ir.GlobalVariable(self.module, string_type, name=f"str_{len(self.module.globals)}")
        global_var.global_constant = True
        global_var.initializer = ir.Constant(string_type, text_bytes)

        zero = ir.Constant(self.int_type, 0)
        return self.builder.gep(global_var, [zero, zero])    
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
            return self.visit(ctx.expr())

        raise Exception("visitPrimario devolvió None (caso no manejado)")

       
    def visitSuma(self, ctx):
        left = self.visit(ctx.producto(0))

        for i in range(1, len(ctx.producto())):
            right = self.visit(ctx.producto(i))

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
                left = self.buil