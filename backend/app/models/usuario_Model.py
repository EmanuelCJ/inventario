from ..db.conexion_DB import ConectDB
from ..utils.generation_password import hash_password

class UsuarioModel:

    def __init__(self, nombre: str, apellido: str, rol: str, contrasena: str):

        self.__nombre = nombre
        self.__apellido = apellido
        self.__rol = rol
        self.__contrasena = hash_password(contrasena)


    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, nombre: str):
        #validar que sea admin para modificar
        self.__nombre = nombre

    def get_apellido(self) -> str:
        return self.__apellido
    
    def set_apellido(self, apellido: str):
        #validar que sea admin para modificar
        self.__apellido = apellido

    def get_rol(self) -> str:
        return self.__rol
    
    def set_rol(self, rol: str):
        #validar que sea admin para modificar rol
        self.__rol = rol

    def get_contrasena(self) -> str:
        if self.get_rol() != 'admin':
            raise PermissionError("No tienes permiso para ver la contrasena")
        return self.__contrasena
    
    def set_contrasena(self, contrasena: str):
        if self.get_rol() != 'admin':
            raise PermissionError("No tienes permiso para modificar la contrasena")
        self.__contrasena = contrasena


    def serializar(self) -> dict:
        return {
            "id_usuario": self.get_id_usuario(),
            "nombre": self.get_nombre(),
            "apellido": self.get_apellido(),
            "rol": self.get_rol()
        }
    
    def deserializar(self, data: dict):
        return data(
            id_usuario = data.get("id_usuario"),
            nombre = data.get("nombre"),
            apellido = data.get("apellido"),
            rol = data.get("rol"),
            contrasena = data.get("contrasena")
        )

