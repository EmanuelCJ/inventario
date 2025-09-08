from db.conexionDB import get_connection

class movimientosModel:
    
    def __init__(self, id_movimiento: int, tipo: str, cantidad: int, fecha: str, id_producto: int, id_usuario: int = None):
        self.__id_movimiento = id_movimiento
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__fecha = fecha
        #foreign keys de la relacion
        self.__id_usuario = id_usuario


    def serializar(self) -> dict:
        return {
            "id_movimiento": self.id_movimiento,
            "tipo": self.tipo,
            "cantidad": self.cantidad,
            "fecha": self.fecha,
            "id_usuario": self.id_usuario
        }
    def deserializar(self, data: dict):
        return data(
            id_movimiento = data.get("id_movimiento"),
            tipo = data.get("tipo"),
            cantidad = data.get("cantidad"),
            fecha = data.get("fecha"),
            id_usuario = data.get("id_usuario")
        )
    @staticmethod
    def registrar_movimiento(usuario, tipo, cantidad, id_producto, id_lugar):
        if usuario.rol not in ["admin", "editor"]:
            raise PermissionError("No tenés permiso para crear movimientos")
        
            conn = get_connection()
