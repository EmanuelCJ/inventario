#DAO tiene la persistencia de datos y se comunica con la base de datos
from ..db.conexion_DB import ConectDB
from werkzeug.security import generate_password_hash

class UsuarioDAO:
    
    """
    CRUD Methods
    Create, Read, Update, Delete
    Estas funciones interactuan con la base de datos para realizar operaciones CRUD en la tabla usuario.
    Cada metodo maneja excepciones y cierra la conexion a la base de datos adecuadamente.
    """

    @staticmethod
    def create_usuario(nombre: str,apellido: str,username:str,rol: str, password_hash: str) -> int | bool:
        
        #Este metodo encripta la password
        password = generate_password_hash(password=password_hash)
        
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    INSERT INTO usuarios (nombre, apellido, username , rol, password)
                    VALUES (%s, %s, %s, %s, %s)
                """
                values = (nombre, apellido, username, rol, password)
                cursor.execute(query, values)
                connection.commit()
                return cursor.lastrowid # manda el id ultimo de la tabla
            except Exception as e:
                connection.rollback()
                print(f"Error crear usuarioDAO: {e}")
                return False
            finally:
                connection.close()
                
    @staticmethod
    def read_all_usuarios() -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT id_usuario, username , nombre, apellido, rol FROM usuarios"
                cursor.execute(query,)
                rows = cursor.fetchall()
                usuarios = []
                for row in rows:
                    usuarios.append(row)
                if usuarios :
                    return usuarios
                return None
            except Exception as e:
                print(f"Error read usuarioDAO: {e}")
                return False
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
                print(f"Error read usuarioDAO: {e}")
                return None
            finally:
                connection.close()
    #UPDATE
    @staticmethod
    def update(id_usuario: int, data: dict) -> bool:

        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                # Validar campos permitidos
                campos_permitidos = ['nombre', 'apellido', 'username', 'rol', 'password']
                for key in data.keys():
                 if key not in campos_permitidos:
                    raise ValueError(f"Campo no permitido para actualizar: {key}")
    
                # Validar que haya al menos un campo
                if not data:
                    raise ValueError("No se proporcionaron campos para actualizar")
                
                # Construir la parte SET de la query dinámicamente
                # Ejemplo: "nombre=%s, apellido=%s, rol=%s"
                set_clause = ", ".join([f"{campo}=%s" for campo in data.keys()])
            
                # Query completa
                query = f"""
                    UPDATE usuarios
                    SET {set_clause}
                    WHERE id_usuario=%s
                """
            
                # Los valores en el orden correcto
                values = tuple(data.values()) + (id_usuario,)
            
                # Debug (opcional, comentar en producción)
                print(f"Query: {query}")
                print(f"Values: {values}")
            
                cursor.execute(query, values)
                connection.commit()
            
                return cursor.rowcount > 0  # True si actualizó al menos 1 fila
            
            except Exception as e:
                connection.rollback()
                print(f"Error update usuarioDAO: {e}")
                return False
            finally:
                connection.close()
    

    @staticmethod
    def update_usuario( id_usuario : int, nombre: str, apellido: str , username : str, rol: str, contrasena : str) -> bool:
        
        #Este metodo encripta la password
        password = generate_password_hash(password=contrasena)

        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = """
                    UPDATE usuarios
                    SET nombre=%s, apellido=%s, rol=%s,username=%s, password=%s
                    WHERE id_usuario=%s
                 """
                values = (
                    nombre,
                    apellido,
                    rol,
                    username,
                    password,
                    id_usuario
                )
                cursor.execute(query, values)
                connection.commit()  # importante para que se guarden los cambios sino no se hacen efectivo
                return cursor.rowcount > 0  # True si actualizó al menos 1 fila
            except Exception as e:
                connection.rollback() #si falla deshace cambios
                print(f"Error update usuarioDAO: {e}")
                return False
            finally:
                connection.close()
                
    @staticmethod
    def delete_usuario( id_usuario : int ) -> bool:      
        connection = ConectDB.get_connection()
        with connection.cursor() as cursor:
            try:
                query = "DELETE FROM usuarios WHERE id_usuario=%s"
                cursor.execute(query, (id_usuario,))
                connection.commit()
                return True
            except Exception as e:
                connection.rollback()
                print(f"Error delete usuarioDAO: {e}")
                return False
            finally:
                connection.close()

    @staticmethod
    def search_username(username: str) -> dict | None:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT * FROM usuarios WHERE username = %s"
                cursor.execute(query,(username,))
                row = cursor.fetchone()
                return row
            except Exception as e:
                print(f"Error buscar por username usuarioDAO: {e}")
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
                print(f"Error buscar por rol usuarioDAO: {e}")
                connection.rollback()
                return False
            finally:
                connection.close()       

    @staticmethod
    def username_exists(username: str) -> bool:
        connection = ConectDB.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            try:
                query = "SELECT 1 FROM usuarios WHERE username = %s LIMIT 1"
                cursor.execute(query, (username,))
                result = cursor.fetchone()
                return result is not None
            except Exception as e:
                print(f"Error al verificar existencia de username: {e}")
                return False
            finally:
                connection.close()