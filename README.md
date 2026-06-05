# Compilador — Proyecto Final (v4)
### Proyecto Final · Compiladores · Universidad Mariano Gálvez · Ciclo 2026

---

## Integrantes — Grupo 2

| Nombre | Carné |
|--------|-------|
| Jermi Emanuel Pinto Patzan | 7690-20-11486 |
| Cintia Yadira Robles Sotoj | 7690-16-13986 |
| Ezequiel Alexander Castro | 7690-21-7934 |
| Cristian Roméo García de La Rosa | 7690-23-12903 |
| Madelin Velvet Mendoza Bedoya | 7690-22-4338 |

---

## Descripción

Este proyecto corresponde al **Proyecto Final** del curso de Compiladores. Se consolidó el compilador desarrollado en los Proyectos 1, 2 y 3 en un producto de software funcional de nivel de producción, incorporando tres capacidades avanzadas que completan la cadena de compilación moderna:

- **Optimización automática O3** mediante el Pass Manager de LLVM
- **Módulo de optimización manual** con selector de passes individuales y comparador diff
- **Generación de binarios nativos** para Linux y Windows (.exe) desde WSL2

Adicionalmente se extendió la gramática a la versión v4 con soporte para switch/case, operador ternario, casting explícito y structs. El pipeline ahora consta de **8 fases en secuencia estricta**.

---

## Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| Python 3 | Lenguaje principal del proyecto |
| ANTLR4 | Generación del analizador léxico y sintáctico |
| llvmlite | Generación de LLVM IR y optimización con Pass Manager |
| rich | Interfaz interactiva en terminal |
| clang + mingw-w64 | Compilación de binarios Linux y Windows desde WSL2 |
| WSL2 + Ubuntu | Entorno de ejecución |
| Visual Studio Code | IDE de desarrollo |
| Git + GitHub | Control de versiones |

---

## Pipeline v4 — 8 Fases en Secuencia Estricta

```
Código fuente (.src)
        │
        ▼
┌─────────────────────────┐
│  Fase 1 — Léxico        │  gramatica_v4Lexer    ──► Error léxico → detener
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│  Fase 2 — Sintáctico    │  gramatica_v4Parser   ──► Error sintáctico → detener
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│  Fase 3 — Semántico     │  semanticVisitor      ──► Error semántico → detener
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│  Fase 4 — TAC           │  TACGenerator         ──► outputs/output.tac
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│  Fase 5 — LLVM IR       │  IRGenerator          ──► outputs/output.ll
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│  Fase 6 — Ejecución     │  EvalVisitor          ──► Salida en consola
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│  Fase 7 — Optimización  │  optimizer.py (O3)    ──► outputs/output.opt.ll
│          O3             │  métricas antes/después
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│  Fase 8 — Binario       │  clang + mingw-w64    ──► outputs/program_linux
│          Nativo         │  selector: Linux /        outputs/program_windows.exe
│                         │  Windows / Ambas
└─────────────────────────┘
```

---

## Estructura de Archivos

```
Proycto-Compilador/
│
├── antlr/
│   ├── v1/                          # Gramática original Expresiones21
│   ├── v3/                          # Gramática Fase III
│   └── v4/                          # Gramática Proyecto Final
│       ├── gramatica_v4.g4          # Gramática extendida con switch, ternario, casting, structs
│       ├── gramatica_v4Lexer.py     # Generado por ANTLR4
│       ├── gramatica_v4Parser.py    # Generado por ANTLR4
│       └── gramatica_v4Visitor.py   # Generado por ANTLR4
│
├── src/
│   ├── pipeline_v4.py               # Orquesta las 8 fases con medición de tiempos
│   ├── main.py                      # Punto de entrada alternativo
│   ├── custom_errors.py             # Listeners para errores léxicos y sintácticos
│   ├── tabla_simbolos.py            # Tabla de símbolos con manejo de scopes
│   ├── visitador_semantico.py       # Visitor semántico (gramática v4)
│   ├── visitador_interprete.py      # Visitor intérprete
│   ├── tac_generator.py             # Generador de código TAC
│   ├── ir_generator.py              # Generador LLVM IR con target triple parametrizable
│   ├── optimizer.py                 # Optimización automática O3 con métricas
│   ├── ir_manual.py                 # Módulo de optimización manual con diff y re-ejecución
│   └── ui_compilador.py             # Interfaz interactiva con panel IR Manual y selector de plataforma
│
├── inputs/
│   ├── test_completo.src            # Programa completo con todas las features v4
│   ├── test_ok.src                  # Demo de structs y casting explícito
│   ├── test_switch_ternario.src     # Demo de switch/case y operador ternario
│   ├── test_lexico.src              # Caso de prueba: error léxico
│   ├── test_sintactico.src          # Caso de prueba: error sintáctico
│   └── test_semantico.src           # Caso de prueba: error semántico
│
├── outputs/                         # Generado automáticamente (ignorado por Git)
│   ├── output.tac                   # Código de tres direcciones
│   ├── output.ll                    # LLVM IR original
│   ├── output.opt.ll                # LLVM IR optimizado O3
│   ├── output.manual.ll             # LLVM IR con passes manuales
│   ├── output.native.ll             # IR saneado para clang
│   ├── program_linux                # Binario ejecutable Linux
│   └── program_windows.exe          # Ejecutable Windows (cross-compiled)
│
└── .gitignore
```

---

## Nuevas Características — Gramática v4

### Structs con acceso a campos
```
struct Punto { int x; int y; }
Punto p;
p.x = 3;
p.y = 4;
```

### Operador ternario
```
string etiqueta = dist > 20.0 ? "lejos" : "cerca";
```

### Switch / case con default
```
switch(opcion) {
    case 1: print("uno"); break;
    case 2: print("dos"); break;
    default: print("otro");
}
```

### Casting explícito entre tipos
```
float division = (float)a / (float)b;
int entero = (int)3.14;
```

---

## Módulos Nuevos — Proyecto Final

### `optimizer.py`
Aplica el Pass Manager de LLVM a nivel O3 sobre el IR generado. Retorna el IR optimizado junto con métricas de reducción:
- Instrucciones antes de la optimización
- Instrucciones después de la optimización
- Porcentaje de reducción

### `ir_manual.py`
Módulo de optimización manual. Permite seleccionar passes individuales y aplicarlos programáticamente:

| Función | Descripción |
|---------|-------------|
| `apply_manual_passes(ir_text, passes)` | Aplica los passes seleccionados y retorna métricas |
| `export_manual_ir(ir_text)` | Guarda el IR resultante en `outputs/output.manual.ll` |
| `diff_ir(original, optimizado)` | Genera diff unificado entre IR original y optimizado |
| `run_ir(ir_path)` | Re-ejecuta el IR resultante con llvmlite JIT |

**Passes disponibles:** `mem2reg`, `instcombine`, `simplifycfg`, `dce`, `inline`, `loop-unroll`

---

## Casos de Prueba

### Programa completo v4 (`inputs/test_completo.src`)
Ejercita todas las características del lenguaje: struct, casting, ternario, switch, fibonacci recursivo, arrays con módulo y break.

**Salida esperada:**
```
lejos
opcion dos
55
42
```

### Demo switch/ternario (`inputs/test_switch_ternario.src`)
Demuestra de forma aislada el operador ternario anidado y switch/case con default.

### Demo structs/casting (`inputs/test_ok.src`)
Demuestra structs con dos campos y casting explícito int↔float.

### Error léxico (`inputs/test_lexico.src`)
El símbolo `@` no pertenece al alfabeto — falla en **Fase 1**.

### Error sintáctico (`inputs/test_sintactico.src`)
`while` sin paréntesis de cierre — falla en **Fase 2**.

### Error semántico (`inputs/test_semantico.src`)
Variable `y` usada sin declarar — falla en **Fase 3**.

---

## Requisitos de Instalación

### 1. WSL2 con Ubuntu

### 2. Python 3 y entorno virtual
```bash
sudo apt update && sudo apt install python3 python3-pip
python3 -m venv venv
source venv/bin/activate
pip install antlr4-python3-runtime llvmlite rich
```

### 3. Java para ANTLR4
```bash
sudo apt install default-jdk
wget https://www.antlr.org/download/antlr-4.13.1-complete.jar
```

### 4. Herramientas para generación de binarios
```bash
sudo apt install llvm clang mingw-w64
```

---

## Cómo Ejecutar

### Clonar el repositorio
```bash
git clone https://github.com/alexdev-sudo/Proycto-Compilador.git
cd Proycto-Compilador/Proycto-Compilador
source ../venv/bin/activate
```

### Interfaz interactiva (recomendado)
```bash
python3 src/ui_compilador.py
```

### Pipeline directo — solo Linux
```bash
python3 src/pipeline_v4.py inputs/test_completo.src
```

### Pipeline directo — Linux y Windows
```bash
python3 src/pipeline_v4.py inputs/test_completo.src --target both
```

### Ejecutar binario generado
```bash
# Linux
./outputs/program_linux

# Windows (desde WSL2 al escritorio de Windows)
cp outputs/program_windows.exe /mnt/c/Users/$USER/Desktop/
```

---

## Resumen de Cambios — Fase III → Proyecto Final

| Componente | Cambio |
|------------|--------|
| `gramatica_v4.g4` | Nueva — switch/case, ternario, casting, structs |
| `pipeline_v4.py` | 8 fases, migrado a gramática v4, selector de plataforma |
| `optimizer.py` | Nuevo — optimización O3 con métricas |
| `ir_manual.py` | Nuevo — optimización manual, diff, re-ejecución |
| `ir_generator.py` | Target triple parametrizable (Linux/Windows) |
| `ui_compilador.py` | Panel IR Manual, selector plataforma, métricas |
| `visitador_semantico.py` | Soporte para gramática v4 |
| `inputs/` | 6 casos de prueba cubriendo todas las features y errores |

---

*Universidad Mariano Gálvez · Ingeniería en Sistemas de Información · Sede Boca del Monte · Ciclo 2026*