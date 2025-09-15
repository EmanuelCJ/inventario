#DAO tiene la persistencia de datos y se comunica con la base de datos

from ..db.conexion_DB import ConectDB

class ProductoDAO:
    
    """
    CRUD Methods
    Create, Read, Update, Delete
    Estas funciones interactuan con la base de datos para realizar operaciones CRUD en la tabla usuario.
    Cada metodo maneja excepciones y cierra la conexion a la base de datos adecuadamente.
    """

    @staticmethod
    def create_product(datos_product : dict) -> bool:
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    INSERT INTO producto (nombre, descripcion, condicion, cantidad)
                    VALUES (%s, %s, %s, %s)
                """
                values = (datos_product.get("nombre"), datos_product.get("descripcion"), datos_product.get("condicion"), datos_product.get("cantidad"))
                cursor.execute(query, values)
                connection.commit()
                return True
            except Exception as e:
                print(f"Error creating user: {e}")
                return False
            finally:
                connection.close()
                
    @staticmethod
    def read_all_product():

        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT * FROM producto"
                cursor.execute(query,)
                rows = cursor.fetchall()
                product = []
                for row in rows:
                    product.append(row)
                return product   
            except Exception as e:
                print(f"Error creating user: {e}")
                return None
            finally:
                connection.close()
                
    @staticmethod
    def read_one_product(product_id : int):
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT * FROM producto WHERE id = %s"
                cursor.execute(query, (product_id,))
                return cursor.fetchone() #diccionario o None
            except Exception as e:
                print(f"Error reading user: {e}")
                return None
            finally:
                connection.close()
                

    @staticmethod
    def update_product(usuario: object, id_producto : int, data: dict):
        
        if usuario.get_rol() != 'admin':
            raise PermissionError("No tienes permiso para modificar un usuario")
        
        
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    UPDATE producto
                    SET nombre=%s, descripcion=%s, condicion=%s, cantidad=%s, id_categoria=%s , id_movimientos=%s
                    WHERE id=%s
                 """
                values = (
                    data["nombre"],
                    data["descripcion"],
                    data["cantidad"],
                    data["id_categoria"],
                    data["id_movimientos"],
                    id_producto
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
    def delete_product(usuario: object, id_product : int ):
        
        if usuario.get_rol() != 'admin' or usuario.get_rol() != 'editor':
            raise PermissionError("No tienes permiso para eliminar un producto")
        
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = "DELETE FROM usuarios WHERE id=%s"
                cursor.execute(query, (id_product,))
                connection.commit()
                return True
            except Exception as e:
                print(f"Error deleting user: {e}")
                return False
            finally:
                connection.close()
