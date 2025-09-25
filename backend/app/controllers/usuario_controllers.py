from flask import request, jsonify
from app.services.usuario_service import UsuarioService
from ..utils.generation_password import hash_password

class UsuarioController:
    
    @staticmethod
    def update_usuario():
        data = request.json
        filas = UsuarioService.actualizar_usuario(
            id_usuario=data["id_usuario"],
            nombre=data["nombre"],
            email=data["email"],
            rol=data["rol"],
            admin_id=data["admin_id"]
        )
        return jsonify({"success": filas > 0})
    
