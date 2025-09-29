from app.services.usuario_service import UsuarioService
from ..models.usuario_Model import UsuarioModel

class UsuarioController:
    
    @staticmethod
    def create_usuario(data: dict, current_user: int):
        try:
            nuevo_usuario = UsuarioModel.deserializar(data)  # ← tu modelo
            
            if not nuevo_usuario:
                respuesta=UsuarioService.crear_usuario(
                    new_usuario=nuevo_usuario,
                    id_admin=current_user
                )
            if respuesta:
                return nuevo_usuario
        
        except Exception as e:
            print(f"Error al crear usuario nuevo controller: {e}")
            return False
    
    @staticmethod
    def update_usuario():
        pass
    
    @staticmethod
    def delete_usuario():
        pass
    
    @staticmethod
    def get_usuarios():
        pass
    
    @staticmethod
    def get_usuarios():
        pass
