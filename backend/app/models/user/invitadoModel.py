from ..usuarioModel import UsuarioModel

class invitado (UsuarioModel):
    
    def __init__(self, id_usuario: int, nombre: str, apellido: str, rol: str, contrasena: str):
        super().__init__(id_usuario, nombre, apellido, rol, contrasena)

    def saludo(self):
        return f"Hola, soy el invitado {self._get_nombre()} {self._get_apellido()}"