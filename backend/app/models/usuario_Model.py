from app.db.conexionDB import get_connection
from .producto_Model import productoModel
from ..utils.validation_rol import validar_permiso

class usuarioModel:

    def __init__(self, id_usuario: int, nombre: str, apellido: str, rol: str, contrasena: str):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__rol = rol
        self.__contrasena = contrasena

        
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
            return usuarioModel(
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

    # funciones del usuarioModel para usar productoModel y movimientoModel
    def crear_producto(self, producto_data):
        #debemos saber si el usuario tiene permisos para crear productos
        if not validar_permiso(self, "crear_producto"):
           pass