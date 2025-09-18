from backend.app.db.conexion_DB import get_connection
from ..utils.validation_rol import validar_permiso

class movimientos_model:
    
    def __init__(self, id_movimiento: int, tipo: str, cantidad: int, fecha_creacion: str,fecha_modificacion: str, id_producto: int, id_usuario: int = None):
        
        self.__id_movimiento = id_movimiento
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__fecha_creacion = fecha_creacion
        self.__fecha_modificacion = fecha_modificacion
        #foreign keys de la relacion
        self.__id_usuario = id_usuario

    # Getters and Setters
    def get_id_movimiento(self) -> int:
        return self.__id_movimiento

    def get_tipo(self) -> str:
        return self.__tipo
    
    def set_tipo(self, tipo: str ):
        self.__tipo = tipo
    
    def get_cantidad(self) -> int:
        return self.__cantidad
    
    def set_cantidad(self, cantidad: int):
        self.__cantidad = cantidad

    def get_fecha_creacion(self) -> str:
        return self.__fecha_creacion
    
    def set_fecha_creacion(self, fecha: str):
        self.__fecha_creacion= fecha
    
    def get_fecha_modificacion(self) -> str:
        return self.__fecha_modificacion

    def set_fecha_modificacion(self, fecha: str):
        self.__fecha_modificacion = fecha

    def get_id_usuario(self) -> int:
        return self.__id_usuario
    
    def set_id_usuario(self, id: int):
        self.__id_usuario = id
    

    def serializar(self) -> dict:
        return {
            "id_movimiento": self.get_id_movimiento(),
            "tipo": self.get_tipo(),
            "cantidad": self.get_cantidad(),
            "fecha_creacion": self.get_fecha_creacion(),
            "fecha_modificacion": self.get_fecha_modificacion(),
            "id_usuario": self.get_id_usuario()
        }
    
    def deserializar(self, data_movimiento: dict) -> "movimientos_model":
        return movimientos_model(
            id_movimiento = data_movimiento.get("id_movimiento"),
            tipo = data_movimiento.get("tipo"),
            cantidad = data_movimiento.get("cantidad"),
            fecha_creacion = data_movimiento.get("fecha_creacion"),
            fecha_modificacion = data_movimiento.get("fecha_modificacion"),
            id_usuario = data_movimiento.get("id_usuario")
        )