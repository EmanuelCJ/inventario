from flask import request, jsonify
from app.services.usuario_service import UsuarioService

class UsuarioController:
    
    @staticmethod
    def create_usuario():
        data = request.json
        filas = UsuarioService.crear_usuario(
            nombre=data["nombre"],
            apellido=data["apellido"],
            username=data["username"],
            rol=data["rol"],
            password=data["password"],
            id_usuario=data["id_admin"]
        )
        return jsonify({"success": filas > 0})
    
    @staticmethod
    def update_usuario():
        pass
    
    @staticmethod
    def delete_usuario():
        pass
    
    @staticmethod
    def read_usuario():
        pass
