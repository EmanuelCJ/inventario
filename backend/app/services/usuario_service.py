# service va la logica de negocio entre usuarios ejemplo crear, update, read, delete.
from ..DAO.usuario_DAO import UsuarioDAO
from ..DAO.permisos_DAO import PermisosDAO
from ..services.auditoria_service import AuditoriaService

class UsuarioService:
    
    @staticmethod
    def crear_usuario(nombre: str, apellido: str , username : str, rol: str, password : str , id_admin: int) -> bool:
        
        #Verifica si el id corresponde a un usuario y lo devuelve
        usuario = UsuarioDAO.read_one_usuario(id_admin)
        if not usuario:
            raise Exception("Usuario no encontrado")
        
        try:
            permiso = PermisosDAO.validar_permisos(usuario , "crear_usuario")
            if not permiso == 1:
                raise Exception("permiso no encontrado")

        
            id_nuevo_usuario = UsuarioDAO.create_usuario(nombre,apellido,username,rol,password)

            if id_nuevo_usuario:
                respuesta = AuditoriaService.registrar(
                    entidad="usuario",
                    id_entidad=id_nuevo_usuario,
                    accion="create",
                    descripcion=f"Usuario: {usuario["username"]} creo al usuario {username}",
                    id_admin=usuario["id_usuario"]
                )

            return respuesta
        
        except Exception as e:

            print(f"Error en create usuario_service {e}")
            return False
        
    @staticmethod
    def update_usuario(id_usuario : str,nombre: str, apellido: str , username : str, rol: str, password : str , id_admin: int) -> int:
        
        #Verifica si el id corresponde a un usuario y lo devuelve
        usuario = UsuarioDAO.read_one_usuario(id_admin)
        if not usuario:
            raise Exception("Usuario no encontrado")
        
        try:
            permiso = PermisosDAO.validar_permisos(usuario , "update_usuario")
            if not permiso == 1:
                raise Exception("permiso no encontrado")
            
            id_nuevo_usuario = UsuarioDAO.update_usuario(id_usuario,nombre,apellido,username,rol,password)

            if id_nuevo_usuario:

                respuesta = AuditoriaService.registrar(
                    entidad="usuario",
                    id_entidad=id_usuario,
                    accion="update",
                    descripcion=f"Usuario : {usuario["username"]} modificó al usuario : {username}",
                    id_admin=usuario["id_usuario"]
                )
                return respuesta
            

        except Exception as e:

            print(f"Error en update usuario_service : {e}")
            return False
    
    @staticmethod
    def delete_usuario(id_admin: int, id_usuario: int):
        
        #Verifica si el id corresponde a un usuario y lo devuelve
        usuario = UsuarioDAO.read_one_usuario(id_admin)
        if not usuario:
            raise Exception("Usuario no encontrado")
        
        permiso = PermisosDAO.validar_permisos(usuario , "delete_usuario")
        if not permiso == 1:
            raise Exception("permiso no encontrado")
        
        try:
            
            #verifica si existe el usuario a eliminar
            usuario_eliminado = UsuarioDAO.read_one_usuario(id_usuario)
            if not usuario:
                raise Exception("Usuario no encontrado")

            respuesta = UsuarioDAO.delete_usuario(id_usuario=id_usuario)

            if respuesta:
                AuditoriaService.registrar(
                    entidad="usuario",
                    id_entidad=id_usuario,
                    accion="delete",
                    descripcion=f"Usuario : {usuario["username"]} elimino al usuario : {usuario_eliminado["username"]}",
                    id_admin=id_admin
                )
            return True
        
        except Exception as e:
            print(f"Error al delete usuario_service: {e}")
            return False

    @staticmethod
    def read_usuario()->dict:
        return UsuarioDAO.read_all_user()
    
    @staticmethod
    def read_one_usuario(id_usuario: int) -> dict:
        return UsuarioDAO.read_one_usuario(id_usuario=id_usuario)