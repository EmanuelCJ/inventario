
from ..db.conexion_DB import ConectDB

class MovimientosDAO:

    @staticmethod
    def create_movimiento(data_movimiento: dict) -> int | None:
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    INSERT INTO movimientos (tipo, cantidad, id_usuario)
                    VALUES (%s, %s, %s)
                """
                values = (data_movimiento["tipo"], data_movimiento["cantidad"], data_movimiento["id_usuario"], ) 
                cursor.execute(query, values)
                connection.commit()
                id_nuevo = cursor.lastrowid
                if id_nuevo:
                    return id_nuevo
                return None
            except Exception as e:
                print(f"Error creating movimiento: {e}")
                connection.rollback()
                return False
            finally:
                connection.close()

    @staticmethod
    def read_all_movimiento() -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT id_movimiento, tipo, fecha, cantidad, id_usuario FROM movimientos"
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
    def read_movimiento_usuario(id_usuario  : int) -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT id_movimiento, tipo, fecha, cantidad, id_usuario FROM movimientos WHERE id_usuario = %s"
                cursor.execute(query, (id_usuario ,))
                return cursor.fetchone() #diccionario o None
            except Exception as e:
                print(f"Error reading movimientos: {e}")
                return None
            finally:
                connection.close()
                

    @staticmethod
    def update_movimiento( id_usuario : int, data_movimiento: dict) -> bool:
        
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    UPDATE movimientos
                    SET tipo=%s, fecha=%s, cantidad=%s, id_usuario=%s
                    WHERE id_usuario=%s
                 """
                values = (
                    data_movimiento["tipo"],
                    data_movimiento["fecha"],
                    data_movimiento["cantidad"],
                    data_movimiento["id_usuario"],
                    id_usuario
                )
                cursor.execute(query, values)
                connection.commit()  # importante para que se guarden los cambios sino no se hacen efectivo
                return cursor.rowcount > 0  # True si actualizó al menos 1 fila
            except Exception as e:
                connection.rollback() #si falla deshace cambios
                print(f"Error updating movimiento: {e}")
                return False
            finally:
                connection.close()
                
    @staticmethod
    def delete_movimiento( id_movimientos : int ) -> bool:      
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = "DELETE FROM movimientos WHERE id_movimientos=%s"
                cursor.execute(query, (id_movimientos,))
                connection.commit()
                return True
            except Exception as e:
                connection.rollback()
                print(f"Error deleting movimiento: {e}")
                return False
            finally:
                connection.close()

    @staticmethod
    def search_movimiento_tipo(tipo_movimiento: str) -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT * FROM usuarios WHERE tipo = %s"
                cursor.execute(query,(tipo_movimiento,))
                rows = cursor.fetchall()
                usuarios = []
                for row in rows:
                    usuarios.append(row)
                if usuarios :
                    return usuarios
                else:
                    return None
            except Exception as e:
                print(f"Error search movimiento: {e}")
                connection.rollback()
                return False
            finally:
                connection.close()

    @staticmethod
    def search_movimiento_fecha(rol_user: str) -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT id, nombre, apellido, rol FROM usuarios WHERE rol = %s"
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
                print(f"Error search movimiento: {e}")
                connection.rollback()
                return False
            finally:
                connection.close()
    
                

        