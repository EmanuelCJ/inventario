from app.db.conexionDB import get_connection
from ..utils.validation_rol import validar_permiso

class UsuarioModel:

    def __init__(self, id_usuario: int, nombre: str, apellido: str, rol: str, contrasena: str):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__rol = rol
        self.__contrasena = contrasena

    
 
    
    
    def update_movimiento(self, usuario, data):
        if self.crear_movimiento(self, usuario, data):
            #llama al movimiento de actualizar producto
            pass
    
    
    def delete_movimiento(self, usuario, data):
        if self.crear_movimiento(self, usuario, data):
            pass

    
    def create_movimiento(self, usuario, data):
        if self.crear_movimiento(self, usuario, data):
            pass

    
    def put_movimiento(self, data):
        if self.crear_movimiento(self, data):
            pass