from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()   #  inicializa la clase padre
        self.errors = []

  
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        token = offendingSymbol.text if offendingSymbol else "?"
        self.errors.append(
            f"[Error Sintáctico] Línea {line}, Columna {column}: {msg} (encontrado: '{token}')"
        )

class LexerErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(
            f"[Error Léxico] Línea {line}, Columna {column}: Símbolo no reconocido"
        )