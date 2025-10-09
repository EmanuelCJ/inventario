class UsuarioModel:

    def __init__(self, nombre: str, apellido: str,username :str, rol: str, password: str):

        self.__nombre = nombre
        self.__apellido = apellido
        self.__username = username
        self.__rol = rol
        self.__password = password


    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def get_apellido(self) -> str:
        return self.__apellido
    
    def set_apellido(self, apellido: str):
        self.__apellido = apellido

    def get_username(self)->str:
        return self.__username
    
    def set_username(self, nuevo: str):
        self.__username = nuevo

    def get_rol(self) -> str:
        return self.__rol
    
    def set_rol(self, rol: str):
        self.__rol = rol

    def get_password(self) -> str:
        return self.__password
    
    def set_password(self, password: str):
        self.__password =password


    def serializar(self) -> dict:
        return {
            "nombre": self.get_nombre(),
            "apellido": self.get_apellido(),
            "username":self.get_username(),
            "rol": self.get_rol()
        }
    
    @staticmethod
    def deserializar(data_usuario: dict) -> "UsuarioModel":
        return UsuarioModel(
            nombre = data_usuario["nombre"],
            apellido = data_usuario["apellido"],
            username= data_usuario["username"],
            rol = data_usuario["rol"],
            password = data_usuario["password"]
        )

