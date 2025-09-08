from db.conexionDB import get_connection
from ..utils.validation_rol import validar_permiso

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
    def validar_rol_permisos(self, usuario, data: str):
        if isinstance(usuario, object) and isinstance(data, str):
            if validar_permiso(usuario , data):
                return True
        return False
    
    @staticmethod
    def registrar_movimiento(self,usuario, tipo, cantidad, id_producto, id_lugar):
        if self.validar_rol_permisos(usuario, "crear_movimiento"):
            try:
                conn = get_connection()
                with conn.cursor() as cursor:
                    cursor.execute("INSERT INTO movimientos (tipo, cantidad, id_producto, id_usuario, id_lugar) VALUES (%s, %s, %s, %s, %s)",
                                   (tipo, cantidad, id_producto, usuario.id_usuario, id_lugar))
                    conn.commit()
                    return True
            except Exception as e:
                print(f"Error al registrar movimiento: {e}")
                return False
            finally:
                if conn:
                    conn.close()
        return False
    
    def create_producto(self, usuario):
        if self.validar_rol_permisos(self, usuario, "crear_producto"):
            pass
    def put_producto(self, usuario):
        if self.validar_rol_permisos(self, usuario, "editar_producto"):
            pass
    def delete_producto(self, usuario):
        if self.validar_rol_permisos(self, usuario, "eliminar_producto"):
            pass
    def update_producto(self, usuario):
        if self.validar_rol_permisos(self, usuario, "editar_producto"):
            pass