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

    # Getters and Setters
    def get_id_movimiento(self) -> int:
        return self.__id_movimiento

    def get_tipo(self) -> str:
        return self.__tipo
    
    def get_cantidad(self) -> int:
        return self.__cantidad

    def get_fecha(self) -> str:
        return self.__fecha

    def get_id_usuario(self) -> int:
        return self.__id_usuario
    

    def serializar(self) -> dict:
        return {
            "id_movimiento": self.get_id_movimiento(),
            "tipo": self.get_tipo(),
            "cantidad": self.get_cantidad(),
            "fecha": self.get_fecha(),
            "id_usuario": self.get_id_usuario()
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
    def validar_rol_permisos(usuario, accion: str):
        if isinstance(usuario, int) and isinstance(accion, str):
            if validar_permiso(usuario , accion):
                return True
        return False
    
    @staticmethod
    def registrar_movimiento(self, id_usuario, tipo, cantidad, id_producto, id_lugar):
        if self.validar_rol_permisos(id_usuario, "crear_movimiento"):
            try:
                conn = get_connection()
                with conn.cursor() as cursor:
                    cursor.execute("INSERT INTO movimientos (tipo, cantidad, id_producto, id_usuario, id_lugar) VALUES (%s, %s, %s, %s, %s)",
                                   (tipo, cantidad, id_producto, id_usuario, id_lugar))
                    conn.commit()
                    return True
            except Exception as e:
                print(f"Error al registrar movimiento: {e}")
                return False
            finally:
                if conn:
                    conn.close()
        return False