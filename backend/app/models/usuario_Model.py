from ..utils.generation_password import hash_password

class UsuarioModel:

    def __init__(self, id_usuario : int, nombre: str, apellido: str,username :str, rol: str, password: str):

        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__user_name = username
        self.__rol = rol
        self.__password = hash_password(password)

    def get_id(self) -> int:
        return self.__id_usuario

    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def get_apellido(self) -> str:
        return self.__apellido
    
    def set_apellido(self, apellido: str):
        self.__apellido = apellido

    def get_username(self)->str:
        return self.__user_name
    
    def set_username(self, nuevo: str):
        self.__user_name = nuevo

    def get_rol(self) -> str:
        return self.__rol
    
    def set_rol(self, rol: str):
        self.__rol = rol

    def get_password(self) -> str:
        return self.__password
    
    def set_password(self, password: str):
        self.__password = hash_password(password)


    def serializar(self) -> dict:
        return {
            "id_usuario": self.get_id(),
            "nombre": self.get_nombre(),
            "apellido": self.get_apellido(),
            "user_name":self.get_username(),
            "rol": self.get_rol()
        }
    
    @staticmethod
    def deserializar(data_usuario: dict) -> "UsuarioModel":
        return UsuarioModel(
            id_usuario = data_usuario.get("id_usuario"),
            nombre = data_usuario.get("nombre"),
            apellido = data_usuario.get("apellido"),
            username= data_usuario.get("user_name"),
            rol = data_usuario.get("rol"),
            password = data_usuario.get("password")
        )

