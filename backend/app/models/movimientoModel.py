from db.conexionDB import get_connection


class movimientosModel:
    
    def __init__(self, id_movimiento: int, tipo: str, cantidad: int, fecha: str, id_producto: int, id_usuario: int = None):
        self.id_movimiento = id_movimiento
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha = fecha
        #foreign keys de la relacion
        self.id_usuario = id_usuario

    def get_ID(self):
        return self.id_movimiento
    
    def get_tipo(self):
        return self.tipo
    
    def get_cantidad(self):
        return self.cantidad
    
    def get_fecha(self):
        return self.fecha
    
    def get_ID_Producto(self):
        return self.id_producto
    
    def get_ID_Usuario(self):
        return self.id_usuario