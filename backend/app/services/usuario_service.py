# service va la logica de negocio
from ..DAO.usuario_DAO import UsuarioDAO

class UsuarioService:
    
    @staticmethod
    def crear_usuario(data_usuario:dict) -> int:
        return UsuarioDAO.create_usuario(datos_user = data_usuario)