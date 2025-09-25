from ..db.conexion_DB import ConectDB

class AuditoriaDAO:
    
    @staticmethod
    def registrar(entidad, id_entidad, accion, descripcion, id_usuario)-> int:

        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    INSERT INTO auditoria (entidad, id_entidad, accion, descripcion, id_usuario) 
                    VALUES (%s, %s, %s, %s, %s)
                 """
                cursor.execute(query, (entidad, id_entidad, accion, descripcion, id_usuario))
                connection.commit()
                return cursor.lastrowid
            except Exception as e:
                print (f"Error al intentar persistir auditoria : {e}")
                connection.rollback()
                return False
            finally:
                connection.close()
        
