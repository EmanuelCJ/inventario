from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.usuario_controllers import UsuarioController

usuario_bp = Blueprint("usuario_bp", __name__)

# CREATE
@usuario_bp.route("/usuarios", methods=["POST"])
@jwt_required()
def create_usuario():
    current_user = get_jwt_identity() 
    
    if current_user["rol"] != "admin":
        return jsonify({"error": "No autorizado"}), 403
    
    data = request.get_json()
    usuario = UsuarioController.create_usuario(data, current_user["id_usuario"])
    
    if not usuario:
        return jsonify(usuario.to_dict()), 201
    
    return jsonify({"error": "No se pudo crear el usuario"}), 400

# READ ONE
@usuario_bp.route("/usuarios/<int:id_usuario>", methods=["GET"])
def get_usuarios_one(id_usuario):
    usuario = UsuarioController.get_usuarios(id_usuario)
    if usuario:
        return jsonify(usuario.to_dict()), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

# READ ALL
@usuario_bp.route("/usuarios", methods=["GET"])
def get_usuarios_all():
    usuarios = UsuarioController.get_usuarios()
    return jsonify([p.to_dict() for p in usuarios]), 200

# UPDATE
@usuario_bp.route("/usuarios/<int:id_usuario>", methods=["PUT"])
def update_usuario(id_usuario):
    data = request.get_json()
    usuario = UsuarioController.update_usuario(id_usuario, data)
    if usuario:
        return jsonify(usuario.to_dict()), 200
    return jsonify({"error": "No se pudo actualizar el usuario"}), 400

# DELETE
@usuario_bp.route("/usuarios/<int:id_usuario>", methods=["DELETE"])
def delete_usuario(id_usuario):
    success = UsuarioController.delete_usuario(id_usuario)
    if success:
        return jsonify({"message": "usuario eliminado"}), 200
    return jsonify({"error": "No se pudo eliminar el usuario"}), 400