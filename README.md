# Compilador — gramatica_v3
### Proyecto Fase III · Compiladores · Universidad Mariano Gálvez

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

Este proyecto corresponde a la **Fase III** del compilador desarrollado en el curso de Compiladores. En esta fase se evolucionó el compilador de la Fase II incorporando la **Generación de Código Intermedio** en dos representaciones complementarias: **Código de Tres Direcciones (TAC)** como instrumento teórico y **LLVM IR funcional** como artefacto ejecutable real. Adicionalmente se construyó una **Interfaz de Compilación Interactiva** y se extendió la gramática del lenguaje.

El compilador procesa un lenguaje propio implementado con **ANTLR4** para el análisis léxico y sintáctico, y **Python** para el análisis semántico, interpretación y generación de código. El sistema sigue un pipeline secuencial de **6 fases** que garantiza que el código fuente sea analizado, validado y ejecutado solo si no presenta errores.

---

## Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| Python 3 | Lenguaje principal del proyecto |
| ANTLR4 | Generación del analizador léxico y sintáctico |
| llvmlite | Generación de código LLVM IR |
| rich | Interfaz de compilación interactiva en terminal |
| WSL 2 + Ubuntu | Entorno de ejecución |
| Visual Studio Code | IDE de desarrollo |
| Git + GitHub | Control de versiones |

---

## Arquitectura del Proyecto

El compilador sigue un **pipeline secuencial de 6 fases**. Si en las fases léxica o sintáctica se detectan errores, el pipeline se detiene. Las fases TAC e IR reportan error pero no detienen el pipeline.

```
Código fuente (.src)
        │
        ▼
┌─────────────────────┐
│  Fase 1 — Léxico    │  gramatica_v3Lexer   ──► Error léxico → detener
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│  Fase 2 — Sintáctico│  gramatica_v3Parser  ──► Error sintáctico → detener
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│  Fase 3 — Semántico │  semanticVisitor     ──► Error semántico → detener
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│  Fase 4 — TAC       │  TACGenerator        ──► output.tac
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│  Fase 5 — LLVM IR   │  IRGenerator         ──► output.ll
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│  Fase 6 — Ejecución │  EvalVisitor         ──► Resultados en consola
└─────────────────────┘
```

---

## Estructura de Archivos

```
Proycto-Compilador/
│
├── antlr/
│   ├── v1/                        # Gramática original Expresiones21
│   └── v3/                        # Gramática actualizada
│       ├── gramatica_v3.g4        # Gramática del lenguaje en ANTLR4
│       ├── gramatica_v3Lexer.py   # Generado por ANTLR4
│       ├── gramatica_v3Parser.py  # Generado por ANTLR4
│       └── gramatica_v3Visitor.py # Generado por ANTLR4
│
├── src/
│   ├── pipeline_v3.py             # Orquesta las 6 fases con medición de tiempos
│   ├── main.py                    # Punto de entrada alternativo
│   ├── custom_errors.py           # Listeners para errores léxicos y sintácticos
│   ├── tabla_simbolos.py          # Tabla de símbolos con manejo de scopes
│   ├── visitador_semantico.py     # Visitor semántico
│   ├── visitador_interprete.py    # Visitor intérprete
│   ├── tac_generator.py           # Generador de código TAC
│   ├── ir_generator.py            # Generador de código LLVM IR
│   └── ui_compilador.py           # Interfaz interactiva de compilación
│
├── inputs/
│   ├── test_ok.src                # Caso de prueba válido complejo
│   ├── test_lexico.src            # Caso de prueba: error léxico
│   ├── test_sintactico.src        # Caso de prueba: error sintáctico
│   └── test_semantico.src         # Caso de prueba: error semántico
│
├── outputs/                       # Generado automáticamente (ignorado por Git)
│   ├── output.tac                 # Código de tres direcciones generado
│   └── output.ll                  # Módulo LLVM IR generado
│
└── .gitignore
```

---

## Gramática del Lenguaje (gramatica_v3)

### Tipos de datos soportados
```
int     float     string     bool     void
```

### Novedades en Fase III

#### Arreglos 1D
```
int[] nums = [1, 2, 3];
print(nums[0]);
```

#### Operador módulo
```
int r = x % 2;
```

#### Break y Continue
```
while (x > 0) {
    if (x == 5) { break; }
    x = x - 1;
}
```

#### Imports
```
import math;
```

#### Concatenación de cadenas
```
string msg = "Hola" + " mundo";
```

### Estructuras de control
```
if / else      while      for      break      continue
```

### Funciones
```
int factorial(int n) {
    if (n <= 1) { return 1; }
    return n * factorial(n - 1);
}
```

### Instrucción de impresión
```
print(resultado);
```

---

## Requisitos de instalación

### 1. Tener WSL 2 con Ubuntu instalado

### 2. Instalar Python 3 y pip
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 3. Crear y activar entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install antlr4-python3-runtime llvmlite rich
```

### 5. Instalar Java (necesario para ANTLR4)
```bash
sudo apt install default-jdk
```

### 6. Descargar ANTLR4
```bash
wget https://www.antlr.org/download/antlr-4.13.1-complete.jar
```

---

## Cómo ejecutar el proyecto

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/alexdev-sudo/Proycto-Compilador.git
cd Proycto-Compilador
```

### Paso 2: Activar el entorno virtual
```bash
source venv/bin/activate
```

### Paso 3: Regenerar archivos de ANTLR4 (si es necesario)
```bash
cd antlr/v3
antlr4 -Dlanguage=Python3 -visitor -no-listener gramatica_v3.g4
cd ../..
```

### Paso 4: Ejecutar la interfaz interactiva
```bash
python3 ui_compilador.py
```

### Paso 5: O ejecutar el pipeline directamente
```bash
python3 src/pipeline_v3.py inputs/test_ok.src
```

---

## Casos de Prueba

### Programa válido complejo (`inputs/test_ok.src`)
```
program {
    import math;
    int[] nums = [3, 1, 4, 1, 5];
    int total = 0;
    int i = 0;

    while (i < 5) {
        int r = nums[i] % 2;
        if (r == 0) {
            total = total + nums[i];
        }
        i = i + 1;
        if (total > 10) { break; }
    }

    string msg = "Resultado: " + "calculado";
    print(msg);
    print(total);
}
```
**Salida esperada:**
```
Resultado: calculado
4
```

---

### Error léxico (`inputs/test_lexico.src`)
```
program {
    int x = 10;
    int y = 20@5;
    print(x);
}
```
**Salida esperada:**
```
[Error Léxico] Línea 3, Columna 14: Símbolo no reconocido '@'
Pipeline detenido en fase léxica.
```

---

### Error sintáctico (`inputs/test_sintactico.src`)
```
program {
    int x = 10
    if (x > 5) {
        print(x)
    }
}
```
**Salida esperada:**
```
[Error Sintáctico] Línea 3, Columna 4: missing ';' at 'if'
Pipeline detenido en fase sintáctica.
```

---

### Error semántico (`inputs/test_semantico.src`)
```
program {
    int x = 10;
    print(y);
}
```
**Salida esperada:** Error detectado por el visitor semántico — variable `y` no declarada.

---

## Componentes principales

### `src/pipeline_v3.py`
Orquesta las 6 fases secuencialmente con medición de tiempos en milisegundos. Muestra un resumen final con el estado de cada fase.

### `src/tac_generator.py`
Visitor que recorre el AST y emite instrucciones de Código de Tres Direcciones. Genera temporales (`t1`, `t2`...) y etiquetas (`L1`, `L2`...) automáticamente. Soporta arreglos, funciones, break, continue, import y módulo.

### `src/ir_generator.py`
Visitor que genera un módulo LLVM IR usando `llvmlite`. Produce código compilable y ejecutable. Soporta tipos `int`, `float`, `bool`, arreglos, funciones, ciclos y break.

### `src/ui_compilador.py`
Interfaz interactiva de terminal usando `rich`. Permite escribir código fuente directamente, compilarlo con CTRL+D y visualizar el resultado del pipeline, el TAC generado y el LLVM IR en paneles estilizados.

### `src/tabla_simbolos.py`
Implementa la pila de tablas hash para el manejo de scopes. Soporta declaración de variables, arreglos y funciones con validación de tipos.

### `src/visitador_semantico.py`
Valida tipos, scopes, arreglos, funciones y nuevas instrucciones (break, continue, import).

### `src/visitador_interprete.py`
Ejecuta el programa con soporte completo para arreglos, módulo `%`, break, continue e imports.

---

## Control de versiones (Git)

El proyecto utiliza la siguiente estructura de ramas:

| Rama | Descripción |
|------|-------------|
| `main` | Rama de producción — código estable y entregable |
| `production` | Rama de producción alternativa |
| `test` | Rama de desarrollo — integración de todas las features |

Los commits están organizados de forma descriptiva por fase y componente.

---

## Resumen de cambios Fase II → Fase III

| Componente | Cambio |
|------------|--------|
| `gramatica_v3.g4` | Arreglos 1D, módulo, break, continue, imports |
| `pipeline_v3.py` | 6 fases con medición de tiempos |
| `tac_generator.py` | Nuevo — genera código TAC |
| `ir_generator.py` | Nuevo — genera LLVM IR con llvmlite |
| `ui_compilador.py` | Nuevo — interfaz interactiva con rich |
| `visitador_semantico.py` | Migrado a gramatica_v3, nuevas reglas |
| `visitador_interprete.py` | Migrado a gramatica_v3, soporte arreglos y break |
| `tabla_simbolos.py` | Soporte para tipos arreglo (`int[]`, `float[]`) |
| Estructura | Reorganización en carpetas `antlr/`, `src/`, `inputs/`, `outputs/` |

---

*Universidad Mariano Gálvez · Ingeniería en Sistemas de Información · Sede Boca del Monte*