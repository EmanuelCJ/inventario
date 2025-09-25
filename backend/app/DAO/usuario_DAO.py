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
    def create_usuario( datos_user : dict) -> int | None:
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    INSERT INTO usuarios (nombre, apellido, username , rol, password)
                    VALUES (%s, %s, %s, %s, %s)
                """
                values = (datos_user.get("nombre"), datos_user.get("apellido"),datos_user.get("username"), datos_user.get("rol"), datos_user.get("password"))
                cursor.execute(query, values)
                connection.commit()
                return cursor.rowcount  # si se modifica la fila
            except Exception as e:
                connection.rollback()
                print(f"Error creating user: {e}")
                return False
            finally:
                connection.close()
                
    @staticmethod
    def read_all_user() -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT id_usuario, username , nombre, apellido, rol FROM usuarios"
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
    def read_one_usuario(id_usuario : int) -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT id_usuario, username , nombre, apellido, rol FROM usuarios WHERE id_usuario = %s"
                cursor.execute(query, (id_usuario,))
                return cursor.fetchone() #diccionario o None
            except Exception as e:
                print(f"Error reading user: {e}")
                return None
            finally:
                connection.close()
                

    @staticmethod
    def update_usuario( id_usuario : int, data: dict) -> bool:
        
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    UPDATE usuarios
                    SET nombre=%s, apellido=%s, rol=%s, password_hash=%s
                    WHERE id=%s
                 """
                values = (
                    data["nombre"],
                    data["apellido"],
                    data["user_name"],
                    data["rol"],
                    data["password_hash"],
                    id_usuario
                )
                cursor.execute(query, values)
                connection.commit()  # importante para que se guarden los cambios sino no se hacen efectivo
                return cursor.rowcount > 0  # True si actualizó al menos 1 fila
            except Exception as e:
                connection.rollback() #si falla deshace cambios
                print(f"Error updating user: {e}")
                return False
            finally:
                connection.close()
                
    @staticmethod
    def delete_usuario( id_usuario : int ) -> bool:      
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = "DELETE FROM usuarios WHERE id=%s"
                cursor.execute(query, (id_usuario,))
                connection.commit()
                return True
            except Exception as e:
                connection.rollback()
                print(f"Error deleting user: {e}")
                return False
            finally:
                connection.close()

    @staticmethod
    def search_user_name(user_name: str) -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT id, user_name , nombre, apellido, rol FROM usuarios WHERE nombre = %s"
                cursor.execute(query,(user_name,))
                rows = cursor.fetchall()
                usuarios = []
                for row in rows:
                    usuarios.append(row)
                if usuarios :
                    return usuarios
                else:
                    return None
            except Exception as e:
                print(f"Error deleting user: {e}")
                connection.rollback()
                return False
            finally:
                connection.close()

    @staticmethod
    def search_user_rol(rol_user: str) -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT id, user_name , nombre, apellido, rol FROM usuarios WHERE rol = %s"
                cursor.execute(query,(rol_user,))
                rows = cursor.fetchall()
                usuarios = []
                for row in rows:
                    usuarios.append(row)
                if usuarios :
                    return usuarios
                else:
                    return None
            except Exception as e:
                print(f"Error deleting user: {e}")
                connection.rollback()
                return False
            finally:
                connection.close()
    
                

        