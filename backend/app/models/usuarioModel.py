class UsuarioModel:
    id_usuario: int
    nombre: str
    apellido: str
    rol: str
    contrasena: str

    def __init__(self, id_usuario: int, nombre: str, apellido: str, rol: str, contrasena: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol
        self.contrasena = contrasena

    def __mostrar__(self):
        return f"<Usuario {self.nombre} {self.apellido}, Rol: {self.rol}>"