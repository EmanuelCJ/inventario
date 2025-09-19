from ..db.conexion_DB import ConectDB

class LugarDAO:
    
    """
    CRUD Methods
    Create, Read, Update, Delete
    Estas funciones interactuan con la base de datos para realizar operaciones CRUD en la tabla usuario.
    Cada metodo maneja excepciones y cierra la conexion a la base de datos adecuadamente.
    """

    @staticmethod
    def create_lugar( datos_lugar : dict) -> int | None:
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    INSERT INTO lugar (nombre, descripcion)
                    VALUES (%s, %s)
                """
                values = (datos_lugar.get("nombre"), datos_lugar.get("descripcion"))
                cursor.execute(query, values)
                connection.commit()
                id_nuevo = connection.lastrowid()
                if id_nuevo:
                    return id_nuevo
                return None
            except Exception as e:
                connection.rollback()
                print(f"Error creating lugar: {e}")
                return False
            finally:
                connection.close()
                
    @staticmethod
    def read_all_lugar() -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT * FROM lugar"
                cursor.execute(query,)
                rows = cursor.fetchall()
                lugar = []
                for row in rows:
                    lugar.append(row)
                return lugar   
            except Exception as e:
                print(f"Error reading lugar: {e}")
                return None
            finally:
                connection.close()
                
    @staticmethod
    def read_one_user(id_lugar : int) -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT * FROM lugar WHERE id = %s"
                cursor.execute(query, (id_lugar,))
                return cursor.fetchone() #diccionario o None
            except Exception as e:
                print(f"Error reading lugar: {e}")
                return None
            finally:
                connection.close()
                

    @staticmethod
    def update_user( id_lugar : int, data: dict) -> bool:
        
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    UPDATE lugar
                    SET nombre=%s, descripcion=%s
                    WHERE id=%s
                 """
                values = (
                    data["nombre"],
                    data["descripcion"],
                    id_lugar
                )
                cursor.execute(query, values)
                connection.commit()  # importante para que se guarden los cambios sino no se hacen efectivo
                return cursor.rowcount > 0  # True si actualizó al menos 1 fila
            except Exception as e:
                connection.rollback() #si falla deshace cambios
                print(f"Error updating lugar: {e}")
                return False
            finally:
                connection.close()
                
    @staticmethod
    def delete_user( id_usuario : int ) -> bool:      
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