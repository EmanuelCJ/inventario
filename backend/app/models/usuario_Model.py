from ..utils.generation_password import hash_password

class UsuarioModel:

    def __init__(self, id : int, nombre: str, apellido: str,user_name :str, rol: str, contrasena: str):

        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__user_name = user_name
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

    def get_user_name(self)->str:
        return self.__user_name
    
    def set_user_name(self, nuevo: str):
        self.__user_name() = nuevo

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
        self.__contrasena = hash_password(contrasena)


    def serializar(self) -> dict:
        return {
            "id": self.get_id(),
            "nombre": self.get_nombre(),
            "apellido": self.get_apellido(),
            "user_name":self.get_user_name(),
            "rol": self.get_rol()
        }
    
    def deserializar(self, data_usuario: dict) -> "UsuarioModel":
        return UsuarioModel(
            id = data_usuario.get("id"),
            nombre = data_usuario.get("nombre"),
            apellido = data_usuario.get("apellido"),
            user_name= data_usuario.get("user_name"),
            rol = data_usuario.get("rol"),
            contrasena = data_usuario.get("contrasena")
        )

