# Compilador — Expresiones21
### Proyecto Fase II · Compiladores · Universidad Mariano Gálvez

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

Este proyecto corresponde a la **Fase II** del compilador desarrollado en el curso de Compiladores. En esta fase se evolucionó el analizador de la Fase I hacia un **front-end de compilación completo** con un **intérprete funcional**.

El compilador procesa un lenguaje propio llamado **Expresiones21**, implementado con **ANTLR4** para el análisis léxico y sintáctico, y **Python** para el análisis semántico y la interpretación. El sistema sigue un pipeline secuencial que garantiza que el código fuente sea analizado, validado y ejecutado solo si no presenta errores.

---

## Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| Python 3 | Lenguaje principal del proyecto |
| ANTLR4 | Generación del analizador léxico y sintáctico |
| WSL 2 + Ubuntu | Entorno de ejecución |
| Visual Studio Code | IDE de desarrollo |
| Git + GitHub | Control de versiones |

---

## Arquitectura del Proyecto

El compilador sigue un **pipeline secuencial** de 4 fases. Si en cualquier fase se detectan errores, el pipeline se detiene y no continúa a la siguiente fase.

```
Código fuente (.txt)
        │
        ▼
┌─────────────────┐
│  Fase Léxica    │  Expresiones21Lexer  ──► Error léxico → detener
└─────────────────┘
        │
        ▼
┌─────────────────┐
│  Fase Sintáctica│  Expresiones21Parser ──► Error sintáctico → detener
└─────────────────┘
        │
        ▼
┌─────────────────┐
│  Fase Semántica │  semanticVisitor     ──► Error semántico → detener
└─────────────────┘
        │
        ▼
┌─────────────────┐
│  Intérprete     │  EvalVisitor         ──► Ejecución y resultados
└─────────────────┘
```

---

## Estructura de Archivos

```
Proycto-Compilador/
│
├── Expresiones21.g4              # Gramática del lenguaje en ANTLR4
│
├── Pipeline.py                   # Punto de entrada: orquesta todas las fases
├── custom_errors.py              # Listeners personalizados para errores léxicos y sintácticos
├── tabla_simbolos.py             # Tabla de símbolos: pila de tablas hash para scopes
├── visitador_semantico.py        # Visitor semántico: validaciones de tipos y scopes
├── visitador_interprete.py       # Visitor intérprete: ejecuta el árbol sintáctico
│
├── Expresiones21Lexer.py         # Generado por ANTLR4
├── Expresiones21Parser.py        # Generado por ANTLR4
├── Expresiones21Visitor.py       # Generado por ANTLR4
│
└── entradas/
    ├── programa_valido.txt       # Caso de prueba: programa válido completo
    ├── error_lexico.txt          # Caso de prueba: error léxico
    ├── error_sintactico.txt      # Caso de prueba: error sintáctico
    └── error_semantico.txt       # Caso de prueba: error semántico
```

---

## Gramática del Lenguaje (Expresiones21)

### Tipos de datos soportados
```
int     float     string     bool     void
```

### Estructuras de control
```
if / else      while      for
```

### Funciones
```
// Definición
int factorial(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

// Llamada
int resultado;
resultado = factorial(5);
```

### Instrucción de impresión
```
print(resultado);
print(x);
```

### Declaración de variables
```
int x;
float precio;
string nombre;
bool activo;
```

---

## Requisitos de instalación

### 1. Tener WSL 2 con Ubuntu instalado

### 2. Instalar Python 3 y pip
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 3. Instalar ANTLR4 runtime para Python
```bash
pip install antlr4-python3-runtime
```

### 4. Instalar Java (necesario para ANTLR4)
```bash
sudo apt install default-jdk
```

### 5. Descargar ANTLR4
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

### Paso 2: Generar los archivos de ANTLR4
```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 Expresiones21.g4 -visitor
```

### Paso 3: Activar el entorno virtual (si aplica)
```bash
source venv/bin/activate
```

### Paso 4: Ejecutar el pipeline con un archivo de entrada
```bash
python3 Pipeline.py entradas/programa_valido.txt
```

---

## Casos de Prueba

### Programa válido
```
program {
    int x;
    x = 10;
    string prefijo;
    prefijo = "El resultado es: ";

    int factorial(int n) {
        if (n <= 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    while (x > 0) {
        int temp;
        temp = factorial(x);
        print(prefijo);
        print(temp);
        x = x - 2;
    }
}
```
**Salida esperada:** Imprime los factoriales de 10, 8, 6, 4, 2.

---

### Error semántico — Tipos incompatibles
```
program {
    int x;
    x = "hola";
}
```
**Salida esperada:**
```
[Error semántico] en línea 3, columna 0: Tipo incompatible: no se puede asignar 'string' a 'int'
Error en Fase Semantica, Pipeline detenido
```

---

### Error sintáctico — Falta semicolon
```
program {
    int x
    x = 10;
}
```
**Salida esperada:**
```
[Error sintáctico] en línea 3, columna 4: ...
Error en Fase Sintactica, Pipeline detendo
```

---

### Error léxico — Carácter no reconocido
```
program {
    int x;
    x = 10 @ 5;
}
```
**Salida esperada:**
```
[Error léxico] carácter no reconocido '@'
Error en Fase Lexica, Pipeline detendo
```

---

## Componentes principales

### `Pipeline.py`
Punto de entrada del compilador. Orquesta las 4 fases secuencialmente. Si alguna fase falla, detiene la ejecución e imprime los errores encontrados.

### `tabla_simbolos.py`
Implementa la **pila de tablas hash** para el manejo de scopes. Permite declarar, buscar y actualizar variables y funciones respetando la jerarquía de ámbitos.

Métodos principales:
- `declare(name, tipo)` — Registra una variable en el scope actual
- `assign(name, tipo)` — Actualiza una variable en los scopes activos
- `lookup(name)` — Busca una variable respetando la jerarquía de scopes
- `declare_function(name, return_type, params, ctx)` — Registra una función en el scope global
- `get_function(name)` — Recupera la información de una función declarada

### `visitador_semantico.py`
Visitor que recorre el árbol sintáctico realizando validaciones lógicas:
- Verificación de tipos en asignaciones y expresiones
- Validación de variables declaradas antes de su uso
- Manejo de scopes mediante creación y eliminación de ámbitos
- Validación de funciones, parámetros y tipo de retorno

### `visitador_interprete.py`
Visitor que ejecuta el programa una vez superadas todas las validaciones:
- Soporte para estructuras de control: `while`, `for`, `if/else`
- Soporte para funciones con parámetros y retorno
- Instrucción `print` para mostrar resultados en terminal
- Reconocimiento de tipos: `int`, `float`, `string`, `bool`

---

## Observaciones y Limitaciones conocidas

- La ejecución de funciones no está completamente implementada en tiempo de ejecución.
- El manejo de instrucciones `return` no está totalmente integrado en el proceso de interpretación.
- No se dispone de un stack de llamadas para gestionar funciones anidadas correctamente.

---

## Control de versiones (Git)

El proyecto utiliza la siguiente estructura de ramas:

| Rama | Descripción |
|------|-------------|
| `main` | Rama de producción — código estable y entregable |
| `test` | Rama de desarrollo — commits de trabajo y pruebas |

Los commits están organizados de forma descriptiva para evidenciar el progreso incremental del proyecto.

---

*Universidad Mariano Gálvez · Ingeniería en Sistemas de Información · Sede Boca del Monte*
