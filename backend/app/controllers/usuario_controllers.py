from app.services.usuario_service import UsuarioService
from ..models.usuario_Model import UsuarioModel

class UsuarioController:

    #CREATE
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
    
    #UPDATE
    @staticmethod
    def update_usuario(data: dict, id_admin: int, id_usuario: int):
        
        try:
            respuesta = UsuarioService.update_usuario(
                id_usuario=id_usuario,
                id_admin=id_admin,
                data=data
            )
            return respuesta
        except Exception as e:
            print(f"Error al crear usuario nuevo controller: {e}")
            return False
        
    
    @staticmethod
    def delete_usuario(id_admin: int, id_usuario: int):
        try:
            respuesta = UsuarioService.delete_usuario(id_admin=id_admin, id_usuario=id_usuario)
            return respuesta
        except Exception as e:
            print(f"Error al crear usuario nuevo controller: {e}")
            return False
    
    @staticmethod
    def all_usuarios()-> dict | None:
        try:
            usuarios = UsuarioService.get_usuarios()
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios controller: {e}")
            return None