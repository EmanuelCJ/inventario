from ..db.conexion_DB import ConectDB

class CategoriaDAO:

    """
    CRUD Methods
    Create, Read, Update, Delete
    Estas funciones interactuan con la base de datos para realizar operaciones CRUD en la tabla usuario.
    Cada metodo maneja excepciones y cierra la conexion a la base de datos adecuadamente.
    """

    @staticmethod
    def create_categoria( data_categoria : dict) -> int | None:
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    INSERT INTO categoria (nombre, descripcion)
                    VALUES (%s, %s)
                """
                values = (data_categoria.get("nombre"), data_categoria.get("descripcion"))
                cursor.execute(query, values)
                connection.commit()
                id_nuevo = connection.lastrowid()
                if id_nuevo:
                    return id_nuevo
                return None
            except Exception as e:
                connection.rollback()
                print(f"Error creating categoria: {e}")
                return False
            finally:
                connection.close()
                
    @staticmethod
    def read_all_categoria() -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT * FROM categoria"
                cursor.execute(query,)
                rows = cursor.fetchall()
                usuarios = []
                for row in rows:
                    usuarios.append(row)
                return usuarios   
            except Exception as e:
                print(f"Error creating categoria: {e}")
                return None
            finally:
                connection.close()
                
    @staticmethod
    def read_one_categoria(id_categoria : int) -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT * FROM categoria WHERE id_categoria = %s"
                cursor.execute(query, (id_categoria,))
                return cursor.fetchone() #diccionario o None
            except Exception as e:
                print(f"Error reading categoria: {e}")
                return None
            finally:
                connection.close()
                

    @staticmethod
    def update_categoria( id_usuario : int, data: dict) -> bool:
        
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
                    data["categoria_name"],
                    data["rol"],
                    data["password_hash"],
                    id_usuario
                )
                cursor.execute(query, values)
                connection.commit()  # importante para que se guarden los cambios sino no se hacen efectivo
                return cursor.rowcount > 0  # True si actualizó al menos 1 fila
            except Exception as e:
                connection.rollback() #si falla deshace cambios
                print(f"Error updating categoria: {e}")
                return False
            finally:
                connection.close()
                
    @staticmethod
    def delete_categoria( id_usuario : int ) -> bool:      
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = "DELETE FROM usuarios WHERE id=%s"
                cursor.execute(query, (id_usuario,))
                connection.commit()
                return True
            except Exception as e:
                connection.rollback()
                print(f"Error deleting categoria: {e}")
                return False
            finally:
                connection.close()

    @staticmethod
    def search_categoria_name(categoria_name: str) -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT id, categoria_name , nombre, apellido, rol FROM usuarios WHERE nombre = %s"
                cursor.execute(query,(categoria_name,))
                rows = cursor.fetchall()
                usuarios = []
                for row in rows:
                    usuarios.append(row)
                if usuarios :
                    return usuarios
                else:
                    return None
            except Exception as e:
                print(f"Error deleting categoria: {e}")
                connection.rollback()
                return False
            finally:
                connection.close()

    @staticmethod
    def search_categoria_rol(rol_categoria: str) -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT id, categoria_name , nombre, apellido, rol FROM usuarios WHERE rol = %s"
                cursor.execute(query,(rol_categoria,))
                rows = cursor.fetchall()
                usuarios = []
                for row in rows:
                    usuarios.append(row)
                if usuarios :
                    return usuarios
                else:
                    return None
            except Exception as e:
                print(f"Error deleting categoria: {e}")
                connection.rollback()
                return False
            finally:
                connection.close()
    
                

        