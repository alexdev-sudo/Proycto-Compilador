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