class TablaSibolos:
    def __init__(self):
        self.Scopes = [{}] # Lista de diccionarios para manejar los scopes
    # entrar a neuvo escope
    def push(self):
        self.Scopes.append({})
    # salir de un escope
    def pop(self):
        self.Scopes.pop()

    #declarar la variable 
    def declare(self, name, tipo):
        if name in self.Scopes[-1]:
            raise Exception(f"Variable '{name}' ya declarada en el scope actual.")
        self.Scopes[-1][name] = tipo

    # Busca la variable en todos los scopes activos y actualiza su tipo si existe
    def assign(self, name, tipo):
        for scope in reversed(self.Scopes):
            if name in scope:
                scope[name] = tipo
                return
        raise Exception(f"Variable '{name}' no declarada.")
    # obtener el tipo de una variable
    def lookup(self, name):
        for scope in reversed(self.Scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Variable '{name}' no declarada.")
    
    #Registra una función en el scope global con su tipo de retorno, parámetros y contexto
    def declare_function(self, name, return_type, params, ctx):
        if name in self.Scopes[0]:  # Solo se permiten funciones en el scope global
            raise Exception(f"Función '{name}' ya declarada en el scope actual.")
        self.Scopes[0][name] = {
            'kind': 'function',
            'return_type': return_type,
            'params': params,
            'ctx': ctx}  # Guardamos el contexto para reportar errores semánticos
        
    #Recupera la información de una función previamente declarada en el scope global
    def get_function(self, name):
        if name in self.Scopes[0]:
            return self.Scopes[0][name]
        raise Exception(f"Función '{name}' no declarada")
