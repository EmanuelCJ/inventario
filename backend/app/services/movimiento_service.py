from ..DAO.movimiento_DAO import MovimientosDAO
from ..DAO.permisos_DAO import PermisosDAO
from ..DAO.usuario_DAO import UsuarioDAO

class MovimientoService:
    
    @staticmethod
    def registrar(id_usuario: int, cantidad : dict, tipo_movimiento:str, producto_id : int)-> int:
        
        usuario = UsuarioDAO.read_one_user(id_usuario)
        if not usuario:
            raise Exception("Usuario no encontrado")
        
        permisos = PermisosDAO.validar(usuario, tipo_movimiento)

        if not permisos == 1:
            raise Exception("Permisos no encontrado")
  
        return True
    
    @staticmethod
    def create_movimiento():
        pass