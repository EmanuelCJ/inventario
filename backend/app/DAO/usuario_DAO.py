#DAO tiene la persistencia de datos y se comunica con la base de datos

from ..db.conexion_DB import ConectDB

class UsuarioDAO:
    
    """
    CRUD Methods
    Create, Read, Update, Delete
    Estas funciones interactuan con la base de datos para realizar operaciones CRUD en la tabla usuario.
    Cada metodo maneja excepciones y cierra la conexion a la base de datos adecuadamente.
    """

    @staticmethod
    def create_user(datos_user : dict) -> bool:
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    INSERT INTO usuarios (nombre, apellido, rol, password_hash)
                    VALUES (%s, %s, %s, %s)
                """
                values = (datos_user.get("nombre"), datos_user.get("apellido"), datos_user.get("rol"), datos_user.get("password_hash"))
                cursor.execute(query, values)
                connection.commit()
                return True
            except Exception as e:
                print(f"Error creating user: {e}")
                return False
            finally:
                connection.close()
                
    @staticmethod
    def read_all_user():

        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT id, nombre, apellido, rol, password_hash FROM usuarios"
                cursor.execute(query,)
                rows = cursor.fetchall()
                usuarios = []
                for row in rows:
                    usuarios.append(row)
                return usuarios   
            except Exception as e:
                print(f"Error creating user: {e}")
                return None
            finally:
                connection.close()
                
    @staticmethod
    def read_one_user(usuario_id : int):
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT id, nombre, apellido, rol, password_hash FROM usuarios WHERE id = %s"
                cursor.execute(query, (usuario_id,))
                return cursor.fetchone() #diccionario o None
            except Exception as e:
                print(f"Error reading user: {e}")
                return None
            finally:
                connection.close()
                

    @staticmethod
    def update_user(usuario: object, id_usuario : int, data: dict):
        
        if usuario.get_rol() != 'admin':
            raise PermissionError("No tienes permiso para modificar un usuario")
        
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    UPDATE usuarios
                    SET nombre=%s, apellido=%s, email=%s, rol=%s, password_hash=%s
                    WHERE id=%s
                 """
                values = (
                    data["nombre"],
                    data["apellido"],
                    data["rol"],
                    data["password_hash"],
                    id_usuario
                )
                cursor.execute(query, values)
                connection.commit()  # importante para que se guarden los cambios
                return cursor.rowcount > 0  # True si actualizó al menos 1 fila
            except Exception as e:
                print(f"Error updating user: {e}")
                return False
            finally:
                connection.close()
                
                
    @staticmethod
    def delete_user(usuario: object, id_usuario : int ):
        
        if usuario.get_rol() != 'admin':
            raise PermissionError("No tienes permiso para eliminar un usuario")
        
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = "DELETE FROM usuarios WHERE id=%s"
                cursor.execute(query, (id_usuario,))
                connection.commit()
                return True
            except Exception as e:
                print(f"Error deleting user: {e}")
                return False
            finally:
                connection.close()
