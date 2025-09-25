from ..db.conexion_DB import ConectDB

class AuditoriaDAO:
    
    @staticmethod
    def registrar(entidad, id_entidad, accion, descripcion, id_usuario)-> int:
        conection = ConectDB.get_connection()
        with conection.cursor as cursor:
            try:
                query = """
                    INSERT INTO auditoria (entidad, id_entidad, accion, descripcion, id_usuario) 
                    VALUES (%s, %s, %s, %s, %s)
                 """
                cursor.execute(query, (entidad, id_entidad, accion, descripcion, id_usuario))
                conection.commit()
                return cursor.lastrowid()
            except Exception as e:
                conection.rollback()
                return False
            finally:
                conection.close()
        
