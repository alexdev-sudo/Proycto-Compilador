from rich.console import Console
from rich.panel import Panel
import subprocess
import tempfile
import os

console = Console()

def ejecutar_pipeline(codigo):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".src", mode="w") as f:
        f.write(codigo)
        filename = f.name

    result = subprocess.run(
        ["python3", "src/pipeline_v3.py", filename],
        capture_output=True,
        text=True
    )

    os.unlink(filename)
    return result.stdout, result.stderr

def leer_archivo(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return "No generado."

def main():
    console.print(Panel("🔧 COMPILADOR v3", style="bold green"))
    console.print("[bold yellow]Escribe tu código (termina con CTRL+D):[/]\n")

    codigo = ""
    try:
        while True:
            linea = input()
            codigo += linea + "\n"
    except EOFError:
        pass

    console.print("\n[bold cyan]Compilando...[/]\n")

    stdout, stderr = ejecutar_pipeline(codigo)

    console.print(Panel(stdout or "Sin salida", title="Resultado del Pipeline", style="cyan"))

    if stderr:
        console.print(Panel(stderr, title="Errores", style="bold red"))

    tac = leer_archivo("outputs/output.tac")
    ir  = leer_archivo("outputs/output.ll")

    console.print(Panel(tac, title="Código TAC", style="magenta"))
    console.print(Panel(ir,  title="LLVM IR",    style="green"))

if __name__ == "__main__":
    main()