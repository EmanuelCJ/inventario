from ..DAO.permisos_DAO import PermisosDAO
from ..DAO.usuario_DAO import UsuarioDAO

class PermisosService:
    
    @staticmethod
    def validar_permisos(id_usuario : int, tipo_movimiento: str):

        usuario = UsuarioDAO.read_one_usuario(id_usuario)
        if not usuario:
            return False
        
        
        return PermisosDAO.validar_permisos(usuario, tipo_movimiento)