from ..db.conexion_DB import ConectDB
from ..utils.validation_rol import validar_permiso
from app.models.producto_Model import productoModel
from app.models.movimiento_Model import movimientos_model

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
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = "INSERT INTO usuario (nombre, apellido, rol, contrasena) VALUES (%s, %s, %s, %s)"
                values = (self.get_nombre(), self.get_apellido(), self.get_rol(), self.get_contrasena())
                cursor.execute(query, values)
                return True
            except Exception as e:
                print(f"Error creating user: {e}")
                return None
                
       
    def read_usuario(self):
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "INSERT INTO usuario (nombre, apellido, rol, contrasena) VALUES (%s, %s, %s, %s)"
                values = (self.get_nombre(), self.get_apellido(), self.get_rol(), self.get_contrasena())
                cursor.execute(query, values)
                rows = cursor.fetchall()
                productos = []
                for row in rows:
                    productos.append(row)
                return productos   
            except Exception as e:
                print(f"Error creating user: {e}")
                return None
            
    def read(self, usuario_id):
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = "SELECT id_usuario, nombre, apellido, rol, contrasena FROM usuario WHERE id_usuario = %s"
                cursor.execute(query, (usuario_id,))
                result = cursor.fetchone()
                if result:
                    return {
                    "id_usuario": result[0],
                    "nombre": result[1],
                    "apellido": result[2],
                    "rol": result[3],
                    "contrasena": result[4]
                    }
                return None
            except Exception as e:
                print(f"Error reading user: {e}")
                return None
            finally:
                if connection:
                    connection.close()

    
    def update_usuario(self, usuario_id, data):
        try:
            connection = ConectDB.get_connection()
            cursor = connection.cursor()
            query = "UPDATE usuario SET nombre=%s, apellido=%s, rol=%s, contrasena=%s WHERE id_usuario=%s"
            values = (data["nombre"], data["apellido"], data["rol"], data["contrasena"], usuario_id)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error updating user: {e}")
            return False
    
    def delete_usuario(self, usuario_id):
        try:
            connection = ConectDB.get_connection()
            cursor = connection.cursor()
            query = "DELETE FROM usuario WHERE id_usuario=%s"
            cursor.execute(query, (usuario_id,))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    # funciones del usuarioModel para usar movimientoModel y que afecten a productos
    def crear_producto(self, usuario: object , data: dict):
        #debemos saber si el usuario tiene permisos para crear productos
        if not validar_permiso(self, usuario, "crear_producto"):
            respuesta = productoModel.create(self, data)
            movimientos_model.registrar_movimiento(self, usuario, "creacion", data.get("cantidad"), respuesta, None)
        return False