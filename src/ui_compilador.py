"""
ui_compilador.py — Interfaz Interactiva del Compilador v3
Muestra 6 paneles individuales: uno por cada fase del pipeline.
"""
from rich.console import Console
from rich.panel   import Panel
from rich.table   import Table
from rich.text    import Text
from rich         import box
import subprocess
import tempfile
import os
import re
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, PROJECT_ROOT)

from src.ir_manual import apply_manual_passes
from src.ir_manual import export_manual_ir
from src.ir_manual import diff_ir

console = Console()

# ─────────────────────────────────────────────────────────
# ESTILOS POR FASE
# ─────────────────────────────────────────────────────────
FASES = [
    {"numero": 1, "nombre": "LÉXICO",           "color": "bold cyan"},
    {"numero": 2, "nombre": "SINTÁCTICO",        "color": "bold blue"},
    {"numero": 3, "nombre": "SEMÁNTICO",         "color": "bold magenta"},
    {"numero": 4, "nombre": "GENERACIÓN TAC",    "color": "bold yellow"},
    {"numero": 5, "nombre": "GENERACIÓN LLVM IR","color": "bold green"},
    {"numero": 6, "nombre": "EJECUCIÓN",         "color": "bold white"},
    {"numero": 7, "nombre": "OPTIMIZACION O3", "color": "bold bright_green"},
    {"numero": 8, "nombre": "BINARIO NATIVO", "color": "bold bright_blue"},
]

# ─────────────────────────────────────────────────────────
# EJECUTAR PIPELINE
# ─────────────────────────────────────────────────────────
def ejecutar_pipeline(codigo: str, target: str):
    """Ejecuta el pipeline y retorna (stdout, stderr)."""

    outputs_dir = os.path.join(PROJECT_ROOT, "outputs")

    for name in ("output.tac", "output.ll", "output.opt.ll", "output.manual.ll"):
        path = os.path.join(outputs_dir, name)

        if os.path.exists(path):
            os.remove(path)

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".src",
        mode="w",
        encoding="utf-8"
    ) as f:
        f.write(codigo)
        filename = f.name

    pipeline_path = os.path.join(
        PROJECT_ROOT,
        "src",
        "pipeline_v3.py"
    )

    result = subprocess.run(
        ["python3", pipeline_path, filename, "--target", target],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True
    )

    os.unlink(filename)

    return result.stdout, result.stderr


# ─────────────────────────────────────────────────────────
# PARSEAR SALIDA EN FASES
# ─────────────────────────────────────────────────────────
def parsear_fases(stdout: str) -> dict:
    """
    Formato real del pipeline:
      ===...===
        FASE N: NOMBRE
      ===...===
        Estado: OK | Tiempo: X
        [salida de la fase]
      (línea vacía)
      ===...===   <- inicio siguiente fase
    """
    fases_data = {}
    lineas = stdout.splitlines()
    n = len(lineas)
    i = 0

    while i < n:
        # Buscar separador ===
        if re.match(r"={10,}", lineas[i].strip()):
            i += 1
            # La línea siguiente debería ser "  FASE N: NOMBRE"
            if i < n:
                m = re.match(r"\s*FASE\s+(\d+)\s*:\s*(.+)", lineas[i])
                if m:
                    num    = int(m.group(1))
                    nombre = m.group(2).strip()
                    i += 1
                    # Saltar el segundo separador ===
                    if i < n and re.match(r"={10,}", lineas[i].strip()):
                        i += 1
                    # Leer contenido hasta línea vacía o nuevo ===
                    estado = "ERROR"
                    contenido_lines = []
                    while i < n:
                        l = lineas[i]
                        ls = l.strip()
                        if re.match(r"={10,}", ls):
                            break
                        if ls.startswith("Estado:"):
                            estado = "OK" if "OK" in ls else "ERROR"
                        if ls:
                            contenido_lines.append(ls)
                        i += 1

                    fases_data[num] = {
                        "nombre":    nombre,
                        "estado":    estado,
                        "contenido": "\n".join(contenido_lines),
                    }
                    continue
        i += 1

    # Resumen final
    m_resumen = re.search(r"RESUMEN DEL PIPELINE(.+)", stdout, re.DOTALL)
    fases_data["resumen"] = m_resumen.group(1).strip() if m_resumen else ""

    return fases_data


# ─────────────────────────────────────────────────────────
# LEER ARCHIVO DE SALIDA
# ─────────────────────────────────────────────────────────
def leer_archivo(path: str) -> str:
    full_path = path

    if not os.path.isabs(path):
        full_path = os.path.join(PROJECT_ROOT, path)

    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()

    return "No generado."


# ─────────────────────────────────────────────────────────
# MOSTRAR PANEL DE FASE
# ─────────────────────────────────────────────────────────
def mostrar_panel_fase(num: int, nombre: str, estado: str, contenido: str, color: str):
    """Imprime el panel con resultado de una fase individual."""
    icono   = "✅" if estado == "OK" else "❌"
    titulo  = f"[{color}]FASE {num}: {nombre}  {icono}[/{color}]"
    estilo  = "green" if estado == "OK" else "red"
    texto   = contenido if contenido else f"  Estado: {estado}"
    console.print(Panel(texto, title=titulo, border_style=estilo, padding=(0, 1)))
    console.print()


# ─────────────────────────────────────────────────────────
# MOSTRAR PANEL DE ARTEFACTO (TAC / IR)
# ─────────────────────────────────────────────────────────
def mostrar_artefacto(titulo: str, contenido: str, color: str):
    console.print(Panel(contenido, title=f"[{color}]{titulo}[/{color}]",
                        border_style=color.split()[0], padding=(0, 1)))
    console.print()


# ─────────────────────────────────────────────────────────
# MOSTRAR TABLA RESUMEN
# ─────────────────────────────────────────────────────────
def mostrar_resumen(fases_data: dict):
    tabla = Table(title="📊 RESUMEN DEL PIPELINE", box=box.ROUNDED,
                  show_header=True, header_style="bold white on dark_blue")
    tabla.add_column("Fase",   style="bold cyan",   no_wrap=True, min_width=20)
    tabla.add_column("Estado", style="bold",        no_wrap=True, min_width=8)
    tabla.add_column("Info",   style="dim",         no_wrap=False)

    for num, meta in fases_data.items():
        if num == "resumen":
            continue
        estado  = meta.get("estado", "?")
        nombre  = meta.get("nombre", f"Fase {num}")
        info    = meta.get("contenido", "")
        # Extraer solo la línea de tiempo si existe
        m = re.search(r"Tiempo:\s*([\d.]+ms)", info)
        tiempo  = m.group(1) if m else "-"
        color   = "green" if estado == "OK" else "red"
        tabla.add_row(nombre, f"[{color}]{estado}[/{color}]", tiempo)

    console.print(tabla)
    console.print()


# ─────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────
def main():
    console.print()
    console.print(Panel(
        "[bold white]🔧  COMPILADOR INTERACTIVO  v3[/bold white]\n"
        "[dim]Ingresa código fuente y observa el resultado de cada fase del pipeline.[/dim]",
        style="bold dark_blue",
        padding=(1, 4)
    ))
    console.print("[bold yellow]Escribe tu código (termina con CTRL+D o CTRL+Z en Windows):[/]\n")

    codigo = ""
    try:
        while True:
            linea = input()
            codigo += linea + "\n"
    except EOFError:
        pass

    if not codigo.strip():
        console.print("[red]No se ingresó código.[/red]")
        return

    console.print("[bold cyan]Plataforma destino:[/bold cyan]")
    console.print("1. Linux")
    console.print("2. Windows")
    console.print("3. Ambas")

    opcion = input("Selecciona 1/2/3: ").strip()

    target = {
        "1": "linux",
        "2": "windows",
        "3": "both",
    }.get(opcion, "linux")

    console.print("\n[bold cyan]⚙  Compilando...[/bold cyan]\n")

    stdout, stderr = ejecutar_pipeline(codigo, target)

    # ── Mostrar errores de Python (si los hay) ──────────────
    if stderr and stderr.strip():
        console.print(
            Panel(
                stderr,
                title="[bold red]⚠  Errores del sistema[/bold red]",
                border_style="red"
            )
        )
        console.print()

    # ── Parsear y mostrar 6 paneles de fase ─────────────────
    fases_data = parsear_fases(stdout)

    console.print("[bold underline]RESULTADOS POR FASE[/bold underline]\n")

    for meta in FASES:
        num    = meta["numero"]
        nombre = meta["nombre"]
        color  = meta["color"]

        if num in fases_data:
            estado    = fases_data[num]["estado"]
            contenido = fases_data[num]["contenido"]
        else:
            # La fase no se ejecutó (pipeline detenido antes)
            estado    = "NO EJECUTADA"
            contenido = "Pipeline detenido en una fase anterior."

        mostrar_panel_fase(num, nombre, estado, contenido, color)

    # ── Panel especial: contenido del TAC generado ──────────
    tac = leer_archivo("outputs/output.tac")
    mostrar_artefacto("📄  CÓDIGO TAC  (outputs/output.tac)", tac, "bold yellow")

    # ── Panel especial: contenido del LLVM IR generado ──────
    ir_code = leer_archivo("outputs/output.ll")
    mostrar_artefacto("⚡  LLVM IR  (outputs/output.ll)", ir_code, "bold green")

    ir_opt = leer_archivo("outputs/output.opt.ll")

    mostrar_artefacto(
        "LLVM IR OPTIMIZADO O3 (outputs/output.opt.ll)",
        ir_opt,
        "bold bright_green"
    )

if ir_code == "No generado.":
    console.print(
        "[yellow]IR Manual omitido: no existe outputs/output.ll.[/yellow]"
    )
else:
    console.print("[bold cyan]IR Manual - passes disponibles:[/bold cyan]")
    console.print(
        "mem2reg, instcombine, simplifycfg, dce, inline, loop-unroll"
    )

    raw = input(
        "Passes separados por coma, o Enter para omitir: "
    ).strip()

    if raw:
        selected = [p.strip() for p in raw.split(",") if p.strip()]

        try:
            manual_ir, info = apply_manual_passes(
                ir_code,
                selected
            )

            export_manual_ir(manual_ir)

            mostrar_artefacto(
                "IR MANUAL (outputs/output.manual.ll)",
                manual_ir,
                "bold magenta"
            )

            mostrar_artefacto(
                "DIFF ORIGINAL VS MANUAL",
                diff_ir(ir_code, manual_ir),
                "bold red"
            )

        except Exception as e:
            mostrar_artefacto(
                "ERROR IR MANUAL",
                str(e),
                "bold red"
            )        

    # ── Tabla resumen final ──────────────────────────────────
    if fases_data:
        mostrar_resumen(fases_data)


if __name__ == "__main__":
    main()