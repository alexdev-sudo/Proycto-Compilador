from llvmlite import ir
from antlr.v3.gramatica_v3Visitor import gramatica_v3Visitor

class IRGenerator(gramatica_v3Visitor):

    def __init__(self):
        self.module = ir.Module(name="programa")
        self.builder = None
        self.func = None
        self.variables = {}
        self.functions = {}
        self.loop_stack = []

        # Tipos base
        self.int_type   = ir.IntType(32)
        self.float_type = ir.DoubleType()
        self.bool_type  = ir.IntType(1)
        self.void_type  = ir.VoidType()

        # Declarar printf externo
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty  = ir.FunctionType(self.int_type, [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

        # Función main
        main_ty   = ir.FunctionType(self.int_type, [])
        self.func = ir.Function(self.module, main_ty, name="main")
        block     = self.func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def get_ir(self):
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.int_type, 0))
        return str(self.module)

    def get_type(self, tipo_str):
        if tipo_str == "int":
            return self.int_type
        elif tipo_str == "float":
            return self.float_type
        elif tipo_str == "bool":
            return self.bool_type
        else:
            return self.int_type

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
        nombre = ctx.VAR().getText()
        tipo_str = ctx.getChild(0).getText()
        llvm_type = self.get_type(tipo_str)

        ptr = self.builder.alloca(llvm_type, name=nombre)
        self.variables[nombre] = (ptr, llvm_type)

        if ctx.expr():
            val = self.visit(ctx.expr())
            val = self._cast(val, llvm_type)
            self.builder.store(val, ptr)
        else:
            self.builder.store(ir.Constant(llvm_type, 0), ptr)

    def visitAsignacion(self, ctx):
        nombre = ctx.VAR().getText()
        val = self.visit(ctx.expr())
        if nombre in self.variables:
            ptr, llvm_type = self.variables[nombre]
            val = self._cast(val, llvm_type)
            self.builder.store(val, ptr)

    # ─────────────────────────────────────────
    # ARREGLOS
    # ─────────────────────────────────────────
    def visitArraydecl(self, ctx):
        nombre = ctx.VAR().getText()
        tipo_str = ctx.getChild(0).getText()
        llvm_type = self.get_type(tipo_str)
        valores = [self.visit(e) for e in ctx.expr()]
        n = len(valores)

        arr_type = ir.ArrayType(llvm_type, n)
        ptr = self.builder.alloca(arr_type, name=nombre)
        self.variables[nombre] = (ptr, llvm_type, n)

        for i, val in enumerate(valores):
            idx = [ir.Constant(self.int_type, 0), ir.Constant(self.int_type, i)]
            elem_ptr = self.builder.gep(ptr, idx, inbounds=True)
            self.builder.store(self._cast(val, llvm_type), elem_ptr)

    def visitArrayasign(self, ctx):
        nombre = ctx.VAR().getText()
        indice = self.visit(ctx.expr(0))
        valor  = self.visit(ctx.expr(1))
        if nombre in self.variables:
            ptr, llvm_type, _ = self.variables[nombre]
            idx = [ir.Constant(self.int_type, 0), indice]
            elem_ptr = self.builder.gep(ptr, idx, inbounds=True)
            self.builder.store(self._cast(valor, llvm_type), elem_ptr)

    # ─────────────────────────────────────────
    # IF
    # ─────────────────────────────────────────
    def visitIfstm(self, ctx):
        cond = self.visit(ctx.expr())
        cond = self._to_bool(cond)

        then_block = self.func.append_basic_block("then")
        else_block = self.func.append_basic_block("else")
        end_block  = self.func.append_basic_block("endif")

        self.builder.cbranch(cond, then_block, else_block)

        self.builder = ir.IRBuilder(then_block)
        self.visit(ctx.bloque(0))
        if not self.builder.block.is_terminated:
            self.builder.branch(end_block)

        self.builder = ir.IRBuilder(else_block)
        if ctx.ELSE():
            self.visit(ctx.bloque(1))
        if not self.builder.block.is_terminated:
            self.builder.branch(end_block)

        self.builder = ir.IRBuilder(end_block)

    # ─────────────────────────────────────────
    # WHILE
    # ─────────────────────────────────────────
    def visitWhilestm(self, ctx):
        cond_block = self.func.append_basic_block("while_cond")
        body_block = self.func.append_basic_block("while_body")
        end_block  = self.func.append_basic_block("while_end")

        self.loop_stack.append(end_block)
        self.builder.branch(cond_block)

        self.builder = ir.IRBuilder(cond_block)
        cond = self.visit(ctx.expr())
        cond = self._to_bool(cond)
        self.builder.cbranch(cond, body_block, end_block)

        self.builder = ir.IRBuilder(body_block)
        self.visit(ctx.bloque())
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)

        self.builder = ir.IRBuilder(end_block)
        self.loop_stack.pop()

    # ─────────────────────────────────────────
    # FOR
    # ─────────────────────────────────────────
    def visitForstm(self, ctx):
        self.visit(ctx.getChild(2))

        cond_block = self.func.append_basic_block("for_cond")
        body_block = self.func.append_basic_block("for_body")
        end_block  = self.func.append_basic_block("for_end")

        self.builder.branch(cond_block)

        self.builder = ir.IRBuilder(cond_block)
        cond = self.visit(ctx.expr())
        cond = self._to_bool(cond)
        self.builder.cbranch(cond, body_block, end_block)

        self.builder = ir.IRBuilder(body_block)
        self.visit(ctx.bloque())
        self.visit(ctx.getChild(6))
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)

        self.builder = ir.IRBuilder(end_block)

    # ─────────────────────────────────────────
    # BREAK / CONTINUE / IMPORT
    # ─────────────────────────────────────────
    def visitBreakstm(self, ctx):
        if self.loop_stack:
            self.builder.branch(self.loop_stack[-1])

    def visitContinuestm(self, ctx):
        pass

    def visitImportstm(self, ctx):
        pass

    # ─────────────────────────────────────────
    # FUNCIONES
    # ─────────────────────────────────────────
    def visitFuncion(self, ctx):
        nombre      = ctx.VAR().getText()
        tipo_str    = ctx.getChild(0).getText()
        return_type = self.get_type(tipo_str)

        param_types = []
        param_names = []
        if ctx.parametros():
            for p in ctx.parametros().parametro():
                param_types.append(self.get_type(p.tipodato().getText()))
                param_names.append(p.VAR().getText())

        func_type = ir.FunctionType(return_type, param_types)
        func      = ir.Function(self.module, func_type, name=nombre)
        self.functions[nombre] = func

        block = func.append_basic_block("entry")
        prev_builder   = self.builder
        prev_func      = self.func
        prev_variables = self.variables.copy()

        self.func    = func
        self.builder = ir.IRBuilder(block)
        self.variables = {}

        for i, (pname, ptype) in enumerate(zip(param_names, param_types)):
            ptr = self.builder.alloca(ptype, name=pname)
            self.builder.store(func.args[i], ptr)
            self.variables[pname] = (ptr, ptype)

        self.visit(ctx.bloque())

        if not self.builder.block.is_terminated:
            if isinstance(return_type, ir.VoidType):
                self.builder.ret_void()
            else:
                self.builder.ret(ir.Constant(return_type, 0))

        self.builder   = prev_builder
        self.func      = prev_func
        self.variables = prev_variables

    def visitReturnstm(self, ctx):
        val = self.visit(ctx.expr())
        self.builder.ret(val)

    def visitLlamada(self, ctx):
        nombre = ctx.VAR().getText()
        if nombre not in self.functions:
            return ir.Constant(self.int_type, 0)
        func = self.functions[nombre]
        args = [self.visit(e) for e in ctx.expr()] if ctx.expr() else []
        args = [self._cast(a, t) for a, t in zip(args, func.args)]
        return self.builder.call(func, args)

    # ─────────────────────────────────────────
    # PRINT
    # ─────────────────────────────────────────
    def visitPrintstm(self, ctx):
        val = self.visit(ctx.expr())

        if isinstance(val.type, ir.IntType) and val.type.width == 32:
            fmt = "%d\n\0"
        elif isinstance(val.type, ir.DoubleType):
            fmt = "%f\n\0"
        else:
            fmt = "%d\n\0"

        fmt_bytes  = bytearray(fmt.encode("utf8"))
        fmt_type   = ir.ArrayType(ir.IntType(8), len(fmt_bytes))
        fmt_global = ir.GlobalVariable(self.module, fmt_type, name=f"fmt_{len(self.module.globals)}")
        fmt_global.global_constant = True
        fmt_global.initializer = ir.Constant(fmt_type, fmt_bytes)

        fmt_ptr = self.builder.bitcast(fmt_global, ir.IntType(8).as_pointer())
        self.builder.call(self.printf, [fmt_ptr, val])

    # ─────────────────────────────────────────
    # EXPRESIONES
    # ─────────────────────────────────────────
    def visitExpr(self, ctx):
        return self.visit(ctx.logicalOr())

    def visitLogicalOr(self, ctx):
        resultado = self.visit(ctx.logicalAnd(0))
        for i in range(1, len(ctx.logicalAnd())):
            right = self.visit(ctx.logicalAnd(i))
            resultado = self.builder.or_(self._to_bool(resultado), self._to_bool(right))
        return resultado

    def visitLogicalAnd(self, ctx):
        resultado = self.visit(ctx.igualdad(0))
        for i in range(1, len(ctx.igualdad())):
            right = self.visit(ctx.igualdad(i))
            resultado = self.builder.and_(self._to_bool(resultado), self._to_bool(right))
        return resultado

    def visitIgualdad(self, ctx):
        resultado = self.visit(ctx.comparacion(0))
        for i in range(1, len(ctx.comparacion())):
            right = self.visit(ctx.comparacion(i))
            if ctx.IGUAL(i-1):
                resultado = self.builder.icmp_signed("==", resultado, right)
            else:
                resultado = self.builder.icmp_signed("!=", resultado, right)
        return resultado

    def visitComparacion(self, ctx):
        resultado = self.visit(ctx.suma(0))
        for i in range(1, len(ctx.suma())):
            right = self.visit(ctx.suma(i))
            op = ctx.getChild(2*i - 1).getText()
            ops = {">": ">", "<": "<", ">=": ">=", "<=": "<="}
            resultado = self.builder.icmp_signed(ops[op], resultado, right)
        return resultado

    def visitSuma(self, ctx):
        resultado = self.visit(ctx.producto(0))
        for i in range(1, len(ctx.producto())):
            right = self.visit(ctx.producto(i))
            op = ctx.getChild(2*i - 1).getText()
            if op == "+":
                resultado = self.builder.add(resultado, right)
            else:
                resultado = self.builder.sub(resultado, right)
        return resultado

    def visitProducto(self, ctx):
        resultado = self.visit(ctx.unario(0))
        for i in range(1, len(ctx.unario())):
            right = self.visit(ctx.unario(i))
            op = ctx.getChild(2*i - 1).getText()
            if op == "*":
                resultado = self.builder.mul(resultado, right)
            elif op == "/":
                resultado = self.builder.sdiv(resultado, right)
            elif op == "%":
                resultado = self.builder.srem(resultado, right)
        return resultado

    def visitUnario(self, ctx):
        if ctx.NOT():
            val = self.visit(ctx.unario())
            return self.builder.not_(self._to_bool(val))
        return self.visit(ctx.primario())

    def visitPrimario(self, ctx):
        if ctx.llamada():
            return self.visit(ctx.llamada())
        if ctx.getChildCount() == 4:
            nombre = ctx.VAR().getText()
            indice = self.visit(ctx.expr())
            if nombre in self.variables:
                ptr, llvm_type, _ = self.variables[nombre]
                idx = [ir.Constant(self.int_type, 0), indice]
                elem_ptr = self.builder.gep(ptr, idx, inbounds=True)
                return self.builder.load(elem_ptr)
        if ctx.NUM():
            return ir.Constant(self.int_type, int(ctx.NUM().getText()))
        if ctx.FNUM():
            return ir.Constant(self.float_type, float(ctx.FNUM().getText()))
        if ctx.TRUE():
            return ir.Constant(self.bool_type, 1)
        if ctx.FALSE():
            return ir.Constant(self.bool_type, 0)
        if ctx.VAR():
            nombre = ctx.VAR().getText()
            if nombre in self.variables:
                ptr, llvm_type = self.variables[nombre][:2]
                return self.builder.load(ptr)
            return ir.Constant(self.int_type, 0)
        if ctx.expr():
            return self.visit(ctx.expr())
        return ir.Constant(self.int_type, 0)

    # ─────────────────────────────────────────
    # UTILIDADES
    # ─────────────────────────────────────────
    def _cast(self, val, target_type):
        if val.type == target_type:
            return val
        if isinstance(target_type, ir.DoubleType) and isinstance(val.type, ir.IntType):
            return self.builder.sitofp(val, target_type)
        if isinstance(target_type, ir.IntType) and isinstance(val.type, ir.DoubleType):
            return self.builder.fptosi(val, target_type)
        return val

    def _to_bool(self, val):
        if val.type == self.bool_type:
            return val
        if isinstance(val.type, ir.IntType):
            return self.builder.icmp_signed("!=", val, ir.Constant(val.type, 0))
        return val