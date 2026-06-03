from llvmlite import ir
from antlr.v4.gramatica_v4Visitor import gramatica_v4Visitor

class IRGenerator(gramatica_v4Visitor):

    def __init__(self, target_triple=None):
        self.module = ir.Module(name="programa")
        if target_triple: 
            self.module.triple = target_triple
        self.builder = None
        self.func = None
        self.variables = {}
        self.functions = {}
        self.loop_stack = []
        self.break_stack = []
        self.continue_stack = []
        self.struct_layouts = {}
        self._str_counter = 0
        self.struct_types = {}

        # Tipos base
        self.int_type    = ir.IntType(32)
        self.float_type  = ir.DoubleType()
        self.bool_type   = ir.IntType(1)
        self.void_type   = ir.VoidType()
        self.char_type   = ir.IntType(8)
        self.str_type    = self.char_type.as_pointer()   # i8*

        # Declarar printf externo
        printf_ty  = ir.FunctionType(self.int_type, [self.str_type], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

        # Declarar strcat externo  (para concatenacion de strings)
        strcat_ty  = ir.FunctionType(self.str_type, [self.str_type, self.str_type])
        self.strcat_fn = ir.Function(self.module, strcat_ty, name="strcat")

        # Declarar malloc externo  (para buffers dinamicos)
        malloc_ty  = ir.FunctionType(self.str_type, [ir.IntType(64)])
        self.malloc_fn = ir.Function(self.module, malloc_ty, name="malloc")

        # Función main
        main_ty   = ir.FunctionType(self.int_type, [])
        self.func = ir.Function(self.module, main_ty, name="main")
        block     = self.func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    # ─────────────────────────────────────────
    # HELPERS DE STRING
    # ─────────────────────────────────────────
    def _make_str_constant(self, text: str) -> ir.Value:
        """Crea un global de cadena constante y devuelve un i8* a ella."""
        # Quitar comillas si las tiene
        if text.startswith('"') and text.endswith('"'):
            text = text[1:-1]
        # Escapar secuencias comunes
        text = text.replace('\\n', '\n').replace('\\t', '\t')
        data = bytearray((text + '\0').encode('utf-8'))
        arr_type = ir.ArrayType(self.char_type, len(data))
        name = f"str_{self._str_counter}"
        self._str_counter += 1
        gvar = ir.GlobalVariable(self.module, arr_type, name=name)
        gvar.global_constant = True
        gvar.linkage = 'internal'
        gvar.initializer = ir.Constant(arr_type, list(data))
        idx = [ir.Constant(self.int_type, 0), ir.Constant(self.int_type, 0)]
        return self.builder.gep(gvar, idx, inbounds=True)

    def _concat_strings(self, left: ir.Value, right: ir.Value) -> ir.Value:
        """Concatena dos i8* usando un buffer dinamico."""
        buf_size = ir.Constant(ir.IntType(64), 512)
        buf = self.builder.call(self.malloc_fn, [buf_size], name="concat_buf")
        # Inicializar buffer con cadena vacia
        empty = self._make_str_constant("")
        self.builder.call(self.strcat_fn, [buf, empty])
        self.builder.call(self.strcat_fn, [buf, left])
        self.builder.call(self.strcat_fn, [buf, right])
        return buf

    def _is_str_val(self, val: ir.Value) -> bool:
        return isinstance(val.type, ir.PointerType) and val.type.pointee == self.char_type

    # ─────────────────────────────────────────
    # TIPOS
    # ─────────────────────────────────────────
    def get_type(self, tipo_str):
        if tipo_str == "int":
            return self.int_type
        elif tipo_str == "float":
            return self.float_type
        elif tipo_str == "bool":
            return self.bool_type
        elif tipo_str == "string":
            return self.str_type          # i8*
        else:
            return self.int_type

    # ─────────────────────────────────────────
    # IR FINAL
    # ─────────────────────────────────────────
    def get_ir(self):
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.int_type, 0))
        return str(self.module)

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
        nombre    = ctx.VAR().getText()
        tipo_str  = ctx.getChild(0).getText()
        llvm_type = self.get_type(tipo_str)

        if llvm_type == self.str_type:
            # Variable string: almacenamos un puntero (i8**)
            ptr = self.builder.alloca(self.str_type, name=nombre)
            if ctx.expr():
                val = self.visit(ctx.expr())
                self.builder.store(val, ptr)
            else:
                null_str = self._make_str_constant("")
                self.builder.store(null_str, ptr)
            self.variables[nombre] = (ptr, self.str_type)
        else:
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
        if nombre not in self.variables:
            return
        data = self.variables[nombre]
        if isinstance(data, dict) and data.get("kind") == "struct":
            return
        ptr, llvm_type = data[:2]
        if llvm_type != self.str_type:
            val = self._cast(val, llvm_type)
        self.builder.store(val, ptr)

    # ─────────────────────────────────────────
    # ARREGLOS
    # ─────────────────────────────────────────
    def visitArraydecl(self, ctx):
        nombre    = ctx.VAR().getText()
        tipo_str  = ctx.getChild(0).getText()
        llvm_type = self.get_type(tipo_str)
        valores   = [self.visit(e) for e in ctx.expr()]
        n         = len(valores)

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
        end_block = self.func.append_basic_block("while_end")

        self.break_stack.append(end_block)
        self.continue_stack.append(cond_block)

        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)

        self.builder = ir.IRBuilder(cond_block)
        cond = self._to_bool(self.visit(ctx.expr()))
        self.builder.cbranch(cond, body_block, end_block)

        self.builder = ir.IRBuilder(body_block)
        self.visit(ctx.bloque())

        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)

        self.builder = ir.IRBuilder(end_block)

        self.continue_stack.pop()
        self.break_stack.pop()


    # ─────────────────────────────────────────
    # FOR
    # ─────────────────────────────────────────
    def visitForstm(self, ctx):
        self.visit(ctx.getChild(2))

        cond_block = self.func.append_basic_block("for_cond")
        body_block = self.func.append_basic_block("for_body")
        update_block = self.func.append_basic_block("for_update")
        end_block = self.func.append_basic_block("for_end")

        self.break_stack.append(end_block)
        self.continue_stack.append(update_block)

        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)

        self.builder = ir.IRBuilder(cond_block)
        cond = self._to_bool(self.visit(ctx.expr()))
        self.builder.cbranch(cond, body_block, end_block)

        self.builder = ir.IRBuilder(body_block)
        self.visit(ctx.bloque())

        if not self.builder.block.is_terminated:
            self.builder.branch(update_block)

        self.builder = ir.IRBuilder(update_block)
        self.visit(ctx.getChild(6))

        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)

        self.builder = ir.IRBuilder(end_block)

        self.continue_stack.pop()
        self.break_stack.pop()

    # ─────────────────────────────────────────
    # BREAK / CONTINUE / IMPORT
    # ─────────────────────────────────────────
    def visitBreakstm(self, ctx):
        if self.break_stack and not self.builder.block.is_terminated:
            self.builder.branch(self.break_stack[-1])

    def visitContinuestm(self, ctx):
        if self.continue_stack and not self.builder.block.is_terminated: 
            self.builder.branch(self.continue_stack[-1])


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
    # PRINT  (soporta int, float, string)
    # ─────────────────────────────────────────
    def visitPrintstm(self, ctx):
        val = self.visit(ctx.expr())

        if self._is_str_val(val):
            fmt_ptr = self._make_str_constant("%s\n")
        elif isinstance(val.type, ir.IntType) and val.type.width == 32:
            fmt_ptr = self._make_str_constant("%d\n")
        elif isinstance(val.type, ir.DoubleType):
            fmt_ptr = self._make_str_constant("%f\n")
        else:
            fmt_ptr = self._make_str_constant("%d\n")

        self.builder.call(self.printf, [fmt_ptr, val])

    # ─────────────────────────────────────────
    # EXPRESIONES
    # ─────────────────────────────────────────
    def visitExpr(self, ctx):
        return self.visit(ctx.logicalOr())
    
    def visitExprSimple(self, ctx):
        return self.visit(ctx.logicalOr())

    def visitUnarioNot(self, ctx):
        val = self.visit(ctx.unario())
        return self.builder.not_(self._to_bool(val))

    def visitUnarioPrimario(self, ctx):
        return self.visit(ctx.primario())

    def visitPrimLlamada(self, ctx):
        return self.visit(ctx.llamada())

    def visitPrimArray(self, ctx):
        nombre = ctx.VAR().getText()
        indice = self.visit(ctx.expr())

        if nombre in self.variables:
            ptr, llvm_type, _ = self.variables[nombre]
            idx = [ir.Constant(self.int_type, 0), indice]
            elem_ptr = self.builder.gep(ptr, idx, inbounds=True)
            return self.builder.load(elem_ptr)

        return ir.Constant(self.int_type, 0)

    def visitPrimTrue(self, ctx):
        return ir.Constant(self.bool_type, 1)

    def visitPrimFalse(self, ctx):
        return ir.Constant(self.bool_type, 0)

    def visitPrimVar(self, ctx):
        nombre = ctx.VAR().getText()

        if nombre in self.variables:
            data = self.variables[nombre]

            if isinstance(data, dict) and data.get("kind") == "struct":
                return data["ptr"]

            ptr, llvm_type = data[:2]
            return self.builder.load(ptr)

        return ir.Constant(self.int_type, 0)

    def visitPrimNum(self, ctx):
        return ir.Constant(self.int_type, int(ctx.NUM().getText()))

    def visitPrimFnum(self, ctx):
        return ir.Constant(self.float_type, float(ctx.FNUM().getText()))

    def visitPrimStr(self, ctx):
        return self._make_str_constant(ctx.STRVAL().getText())

    def visitPrimParen(self, ctx):
        return self.visit(ctx.expr())       
    


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
            is_equal = ctx.IGUAL(i - 1) is not None

            if isinstance(resultado.type, ir.DoubleType) or isinstance(right.type, ir.DoubleType):
                if not isinstance(resultado.type, ir.DoubleType):
                    resultado = self._cast(resultado, self.float_type)

                if not isinstance(right.type, ir.DoubleType):
                    right = self._cast(right, self.float_type)

                op = "oeq" if is_equal else "one"
                resultado = self.builder.fcmp_ordered(op, resultado, right)

            else:
                op = "==" if is_equal else "!="
                resultado = self.builder.icmp_signed(op, resultado, right)

        return resultado

    def visitComparacion(self, ctx):
        resultado = self.visit(ctx.suma(0))

        for i in range(1, len(ctx.suma())):
            right = self.visit(ctx.suma(i))
            op = ctx.getChild(2 * i - 1).getText()

            # Si uno de los dos lados es float/double, ambos deben compararse como double.
            if isinstance(resultado.type, ir.DoubleType) or isinstance(right.type, ir.DoubleType):
                if not isinstance(resultado.type, ir.DoubleType):
                    resultado = self._cast(resultado, self.float_type)

                if not isinstance(right.type, ir.DoubleType):
                    right = self._cast(right, self.float_type)

                float_ops = {
                    ">": "ogt",
                    "<": "olt",
                    ">=": "oge",
                    "<=": "ole",
                }

                resultado = self.builder.fcmp_ordered(float_ops[op], resultado, right)

            else:
                int_ops = {
                    ">": ">",
                    "<": "<",
                    ">=": ">=",
                    "<=": "<=",
                }

                resultado = self.builder.icmp_signed(int_ops[op], resultado, right)

        return resultado

    def visitSuma(self, ctx):
        resultado = self.visit(ctx.producto(0))

        for i in range(1, len(ctx.producto())):
            right = self.visit(ctx.producto(i))
            op = ctx.getChild(2 * i - 1).getText()

            if op == "+" and (self._is_str_val(resultado) or self._is_str_val(right)):
                if not self._is_str_val(resultado):
                    resultado = self._int_to_str(resultado)
                if not self._is_str_val(right):
                    right = self._int_to_str(right)
                resultado = self._concat_strings(resultado, right)
                continue

            if isinstance(resultado.type, ir.DoubleType) or isinstance(right.type, ir.DoubleType):
                if not isinstance(resultado.type, ir.DoubleType):
                    resultado = self._cast(resultado, self.float_type)
                if not isinstance(right.type, ir.DoubleType):
                    right = self._cast(right, self.float_type)

                if op == "+":
                    resultado = self.builder.fadd(resultado, right)
                else:
                    resultado = self.builder.fsub(resultado, right)
            else:
                if op == "+":
                    resultado = self.builder.add(resultado, right)
                else:
                    resultado = self.builder.sub(resultado, right)

        return resultado
    def visitProducto(self, ctx):
        resultado = self.visit(ctx.unario(0))

        for i in range(1, len(ctx.unario())):
            right = self.visit(ctx.unario(i))
            op = ctx.getChild(2 * i - 1).getText()

            if isinstance(resultado.type, ir.DoubleType) or isinstance(right.type, ir.DoubleType):
                if not isinstance(resultado.type, ir.DoubleType):
                    resultado = self._cast(resultado, self.float_type)
                if not isinstance(right.type, ir.DoubleType):
                    right = self._cast(right, self.float_type)

                if op == "*":
                    resultado = self.builder.fmul(resultado, right)
                elif op == "/":
                    resultado = self.builder.fdiv(resultado, right)
                elif op == "%":
                    raise Exception("El operador % no está soportado para float")

            else:
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
        # ── STRVAL: crear global de cadena constante ──
        if ctx.STRVAL():
            return self._make_str_constant(ctx.STRVAL().getText())
        #evita que una variable estruct sea tratada como una tupla normal 
        if ctx.VAR():
            nombre = ctx.VAR().getText()
            if nombre in self.variables:
                data = self.variables[nombre]

                if isinstance(data, dict) and data.get("kind") == "struct":
                    return data["ptr"]

                ptr, llvm_type = data[:2]
                return self.builder.load(ptr)
            return ir.Constant(self.int_type, 0)
        
        if ctx.expr():
            return self.visit(ctx.expr())
        return ir.Constant(self.int_type, 0)

    # ─────────────────────────────────────────
    # UTILIDADES
    # ─────────────────────────────────────────
    def _int_to_str(self, val: ir.Value) -> ir.Value:
        """Convierte un entero a string usando sprintf en un buffer temporal."""
        buf_size = ir.Constant(ir.IntType(64), 32)
        buf = self.builder.call(self.malloc_fn, [buf_size], name="int_str_buf")
        # Declarar sprintf si no existe
        if "sprintf" not in self.module.globals:
            sprintf_ty = ir.FunctionType(self.int_type, [self.str_type, self.str_type], var_arg=True)
            sprintf_fn = ir.Function(self.module, sprintf_ty, name="sprintf")
        else:
            sprintf_fn = self.module.globals["sprintf"]
        fmt = self._make_str_constant("%d")
        self.builder.call(sprintf_fn, [buf, fmt, val])
        return buf
 
    def _cast(self, val, target_type):
        if val.type == target_type:
            return val

        if isinstance(target_type, ir.DoubleType) and isinstance(val.type, ir.IntType):
            return self.builder.sitofp(val, target_type)

        if isinstance(target_type, ir.IntType) and isinstance(val.type, ir.DoubleType):
            return self.builder.fptosi(val, target_type)

        if isinstance(target_type, ir.IntType) and isinstance(val.type, ir.IntType):
            if val.type.width < target_type.width:
                return self.builder.zext(val, target_type)
            if val.type.width > target_type.width:
                return self.builder.trunc(val, target_type)

        return val

    def _to_bool(self, val):
        if val.type == self.bool_type:
            return val
        if isinstance(val.type, ir.IntType):
            return self.builder.icmp_signed("!=", val, ir.Constant(val.type, 0))
        return val
    
    def visitUnarioCast(self, ctx): 
        valor = self.visit(ctx.unario())
        tipo = ctx.tipodato().getText()
        llvm_tipo = self.get_type(tipo)
        return self._cast(valor,llvm_tipo)
    
    #este visitor se genera por la nueva alternativa #unarioneg de la gramatica
    def visitUnarioNeg(self, ctx):
        val = self.visit(ctx.unario())

        if isinstance(val.type, ir.DoubleType):
            return self.builder.fsub(ir.Constant(self.float_type, 0.0), val)

        return self.builder.sub(ir.Constant(val.type, 0), val)
        
    # permitir operacion ternarias condicion ?  valor_verdaro : valor_falso 
    def visitTernario(self,ctx):
        cond = self._to_bool(
            self.visit(ctx.logicalOr())
        )
        verdadero = self.visit(ctx.expr(0))
        falso = self.visit(ctx.expr(1))
        return self.builder.select(
            cond,
            verdadero,
            falso
        )
    # implementar switch-case con break y default
    def visitSwitchstm(self, ctx):
        valor = self.visit(ctx.expr())

        end_block = self.func.append_basic_block("switch_end")
        default_block = (
            self.func.append_basic_block("switch_default")
            if ctx.defaultclause()
            else end_block
        )

        switch_inst = self.builder.switch(valor, default_block)
        case_blocks = []

        for case in ctx.caseclause():
            case_block = self.func.append_basic_block("switch_case")
            case_blocks.append((case, case_block))

            case_val = self.visit(case.expr())
            switch_inst.add_case(case_val, case_block)

        self.break_stack.append(end_block)

        for case, case_block in case_blocks:
            self.builder = ir.IRBuilder(case_block)

            for stmt in case.statement():
                self.visit(stmt)

            if not self.builder.block.is_terminated:
                self.builder.branch(end_block)

        if ctx.defaultclause():
            self.builder = ir.IRBuilder(default_block)

            for stmt in ctx.defaultclause().statement():
                self.visit(stmt)

            if not self.builder.block.is_terminated:
                self.builder.branch(end_block)

        self.break_stack.pop()
        self.builder = ir.IRBuilder(end_block)
        
    def visitStructdecl(self, ctx):
        nombre = ctx.VAR().getText()

        field_types = []
        field_indices = {}

        for index, campo in enumerate(ctx.campostruct()):
            field_name = campo.VAR().getText()
            field_type = self.get_type(campo.tipodato().getText())

            field_indices[field_name] = index
            field_types.append(field_type)

        struct_type = ir.LiteralStructType(field_types)

        self.struct_types[nombre] = struct_type
        self.struct_layouts[nombre] = {
            "indices": field_indices,
            "types": field_types,
        }

    def visitVarstruct(self, ctx):
        tipo_struct = ctx.VAR(0).getText()
        variable = ctx.VAR(1).getText()

        struct_type = self.struct_types[tipo_struct]
        ptr = self.builder.alloca(struct_type, name=variable)

        self.variables[variable] = {
            "kind": "struct",
            "struct_name": tipo_struct,
            "ptr": ptr,
            "type": struct_type,
        }

    def _struct_field_ptr(self, variable, campo):
        data = self.variables[variable]
        struct_name = data["struct_name"]
        field_index = self.struct_layouts[struct_name]["indices"][campo]

        return self.builder.gep(
            data["ptr"],
            [
                ir.Constant(self.int_type, 0),
                ir.Constant(self.int_type, field_index),
            ],
            inbounds=True,
        )

    def visitStructasign(self, ctx):
        variable = ctx.VAR(0).getText()
        campo = ctx.VAR(1).getText()

        field_ptr = self._struct_field_ptr(variable, campo)
        val = self.visit(ctx.expr())
        val = self._cast(val, field_ptr.type.pointee)

        self.builder.store(val, field_ptr)

    def visitPrimStructAcceso(self, ctx):
        variable = ctx.VAR(0).getText()
        campo = ctx.VAR(1).getText()

        field_ptr = self._struct_field_ptr(variable, campo)
        return self.builder.load(field_ptr)