from app.services.usuario_service import UsuarioService
from ..models.usuario_Model import UsuarioModel

class UsuarioController:
    
    @staticmethod
    def create_usuario(data: dict, current_user: int):
        try:
            # Validación de entrada mínima
            if not data.get("username") or not data.get("password"):
                raise ValueError("Faltan campos obligatorios")

            # Crear modelo desde dict
            nuevo_usuario = UsuarioModel.deserializar(data)

            # Llamar al service
            respuesta = UsuarioService.crear_usuario(
                new_usuario=nuevo_usuario,
                id_admin=current_user
            )

            if respuesta:
                return nuevo_usuario
            return False

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
