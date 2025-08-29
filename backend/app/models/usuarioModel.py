class UsuarioModel:
    __id_usuario: int
    __nombre: str
    __apellido: str
    __rol: str
    __contrasena: str

    def __init__(self, id_usuario: int, nombre: str, apellido: str, rol: str, contrasena: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol
        self.contrasena = contrasena

    def __getID__(self):
        return self.id_usuario
    
    def __getNombre__(self):
        return self.nombre
    
    def __getApellido__(self):
        return self.apellido
    
    def __getRol__(self):
        return self.rol
    


usuario = UsuarioModel(1, "Juan", "Perez", "admin", "password123")  # Ejemplo de instancia

print(usuario.__getNombre__())  # Llamada al método para obtener el nombre

    



