from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import subprocess
import tempfile
import os

# Inicia la consola con rich para mostrar salida estilizada
console = Console()


def ejecutar_pipeline(codigo):
    # Crear archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".src", mode="w") as f:
        # Escribe el código dentro del archivo temporal
        f.write(codigo)
        # Guarda la ruta/nombre del archivo para usarlo después en el pipeline
        filename = f.name

    # Ejecutar pipeline
    result = subprocess.run(
        ["python3", "main.py", filename],
        capture_output=True,
        text=True
    )

    return result.stdout

# Función principal del programa
def main():
    
    console.print(Panel("COMPILADOR v3", style="bold green"))

    console.print("[bold yellow]Escribe tu codigo (termina con CTRL+D):[/]\n")

    # Leer multiples lineas
    codigo = ""
    try:
        while True:
            linea = input()
            codigo += linea + "\n"
    except EOFError:
        pass

    output = ejecutar_pipeline(codigo)
    tac = leer_archivo("outputs/output.tac")
    ir = leer_archivo("outputs/output.ll")

    console.print(Panel(output, title="Resultado del Pipeline", style="cyan"))
    console.print(Panel(tac, title="Codigo TAC", style="magenta"))
    console.print(Panel(ir, title="LLVM IR", style="green"))
    # Agrega salto de línea final al código ingresado
    codigo += "\n" 

# Verifica si el archivo existe antes de leerlo
def leer_archivo(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return "No generado."    


# Punto de entrada del programa
if __name__ == "__main__":
    main()
   