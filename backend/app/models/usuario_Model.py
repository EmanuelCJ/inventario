from app.db.conexionDB import get_connection
from ..utils.validation_rol import validar_permiso
from app.models.movimiento_Model import movimientosModel

class usuario_model:

    def __init__(self, id_usuario: int, nombre: str, apellido: str, rol: str, contrasena: str):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__rol = rol
        self.__contrasena = contrasena

    def get_id_usuario(self) -> int:
        return self.__id_usuario
    
    def set_id_usuario(self, id_usuario: int):
        #validar que sea admin para modificar id_usuario
        self.__id_usuario = id_usuario

    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, nombre: str):
        #validar que sea admin para modificar
        self.__nombre = nombre

    def get_apellido(self) -> str:
        return self.__apellido
    
    def set_apellido(self, apellido: str):
        #validar que sea admin para modificar
        self.__apellido = apellido

    def get_rol(self) -> str:
        return self.__rol
    
    def set_rol(self, rol: str):
        #validar que sea admin para modificar rol
        self.__rol = rol

    def get_contrasena(self) -> str:
        #validar que sea admin para mostrar contrasena
        return self.__contrasena
    
    def set_contrasena(self, contrasena: str):
        #validar que sea admin para modificar contrasena
        self.__contrasena = contrasena


    def serializar(self) -> dict:
        return {
            "id_usuario": self.get_id_usuario(),
            "nombre": self.get_nombre(),
            "apellido": self.get_apellido(),
            "rol": self.get_rol(),
            "contrasena": self.get_contrasena()
        }
    
    def deserializar(self, data: dict):
        return data(
            id_usuario = data.get("id_usuario"),
            nombre = data.get("nombre"),
            apellido = data.get("apellido"),
            rol = data.get("rol"),
            contrasena = data.get("contrasena")
        )
    
        
    def create_usuario(self):
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO usuario (nombre, apellido, rol, contrasena) VALUES (%s, %s, %s, %s)"
        values = (self.nombre, self.apellido, self.rol, self.contrasena)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return cursor.lastrowid

    def read(self, usuario_id):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM usuario WHERE id_usuario=%s"
        values = (usuario_id,)
        cursor.execute(query, values)
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        if row:
            return usuario_model(
                id_usuario=row["id_usuario"],
                nombre=row["nombre"],
                apellido=row["apellido"],
                rol=row["rol"],
                contrasena=row["contrasena"]
            )
        return None
    
    def update_usuario(self, usuario_id, data):
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE usuario SET nombre=%s, apellido=%s, rol=%s, contrasena=%s WHERE id_usuario=%s"
        values = (data.get("nombre"), data.get("apellido"), data.get("rol"), data.get("contrasena"), usuario_id)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    
    def delete_usuario(self, usuario_id):
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM usuario WHERE id_usuario=%s"
        values = (usuario_id,)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return True

    # funciones del usuarioModel para usar movimientoModel y que afecten a productos
    def crear_producto(self):
        #debemos saber si el usuario tiene permisos para crear productos
        if not validar_permiso(self, "crear_producto"):
           movimientosModel.registrar_movimiento(self.get_id_usuario(), "crear_producto", 0, 0, 0)

           pass