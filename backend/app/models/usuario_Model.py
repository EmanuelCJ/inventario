from ..db.conexion_DB import ConectDB
from ..utils.generation_password import hash_password

class UsuarioModel:

    def __init__(self, id : int, nombre: str, apellido: str, rol: str, contrasena: str):

        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__rol = rol
        self.__contrasena = hash_password(contrasena)

    def get_id(self) -> int:
        return self.__id

    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def get_apellido(self) -> str:
        return self.__apellido
    
    def set_apellido(self, apellido: str):
        self.__apellido = apellido

    def get_rol(self) -> str:
        return self.__rol
    
    def set_rol(self, rol: str):
        if self.get_rol() != 'admin':
            raise PermissionError("No tienes permiso para cambiar rol")
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
            "nombre": self.get_nombre(),
            "apellido": self.get_apellido(),
            "rol": self.get_rol()
        }
    
    def deserializar(self, data: dict) -> dict:
        return data(
            nombre = data.get("nombre"),
            apellido = data.get("apellido"),
            rol = data.get("rol"),
            contrasena = data.get("contrasena")
        )

