import re
import llvmlite.binding as llvm


llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

INSTRUCTION_RE = re.compile(
    r"^\s*(?:[%@][\w.$-]+\s*=\s*)?"
    r"(alloca|load|store|add|sub|mul|sdiv|srem|fadd|fsub|fmul|fdiv|"
    r"icmp|fcmp|br|switch|call|ret|getelementptr|select|sitofp|fptosi|"
    r"zext|trunc)\b"
)
def count_instructions(ir_text):
    total = 0

    for line in ir_text.splitlines():
        clean = line.strip()

        if clean and not clean.startswith(";") and INSTRUCTION_RE.match(clean):
            total += 1

    return total
    
def optimize_o3(ir_text):
    before = count_instructions(ir_text)

    module = llvm.parse_assembly(ir_text)
    module.verify()

    # New Pass Manager para llvmlite 0.47+
    pto = llvm.PipelineTuningOptions(speed_level=3, size_level=0)
    pto.loop_unrolling = True
    pto.loop_vectorization = True
    pto.slp_vectorization = True

    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()

    pass_builder = llvm.create_pass_builder(target_machine, pto)
    module_pass_manager = pass_builder.getModulePassManager()

    module_pass_manager.run(module, pass_builder)

    optimized = str(module)
    after = count_instructions(optimized)

    reduction = ((before - after) / before * 100.0) if before else 0.0

    return optimized, {
        "instructions_before": before,
        "instructions_after": after,
        "reduction_percent": reduction,
        "passes": "O3",
    }