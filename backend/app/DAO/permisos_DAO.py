from ..db.conexion_DB import ConectDB
from ..models.usuario_Model import UsuarioModel



class PermisosDAO:
    """
        Esta funcion realizar una query a la base de datos verificando si el usuario tiene permisos para realizar la accion.
    """
    @staticmethod
    def validar_permisos(usuario: dict, permiso: str)-> bool:

        #Obtenemos el username
        username = usuario["username"]

        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    SELECT EXISTS (
                        SELECT 1
                        FROM usuarios u
                        JOIN usuarios_roles ur ON u.id_usuario = ur.id_usuario
                        JOIN roles r ON ur.id_rol = r.id_rol
                        JOIN roles_permisos rp ON r.id_rol = rp.id_rol
                        JOIN permisos p ON rp.id_permiso = p.id_permiso
                        WHERE u.username = %s
                        AND p.nombre = %s
                    ) AS tiene_permiso;
                """
                values = (username, permiso,)
                cursor.execute(query, values)
                resultado = cursor.fetchone()
                # result es un diccionario: {"tiene_permiso": 1} o {"tiene_permiso": 0}
                return bool(resultado["tiene_permiso"])
            
            except Exception as e:
                print(f"Error validando Permiso : {e}")
                connection.rollback()
                return False
            finally:
                connection.close()
                