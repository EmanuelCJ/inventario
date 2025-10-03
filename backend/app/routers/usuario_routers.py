from flask import Blueprint, request, jsonify
from app.controllers.usuario_controllers import UsuarioController
from ..utils.validacion_token import token_required


usuario_bp = Blueprint("usuario_bp", __name__)

# CREATE
@usuario_bp.route("/create", methods=["POST"])
@token_required
def create_usuario(current_user):   # payload inyectado aca
    if current_user["rol"] != "admin":
        return jsonify({"error": "No autorizado"}), 403
    
    data = request.get_json()
    usuario = UsuarioController.create_usuario(data, current_user["id_usuario"])
    
    if usuario:
        return jsonify(usuario.serializar()), 201
    
    return jsonify({"error": "No se pudo crear el usuario"}), 400

# UPDATE
# UPDATE
@usuario_bp.route("/update/<int:id>", methods=["PUT"])
@token_required
def update_usuario(current_user, id):  # ← Agregar 'id' como parámetro
    # Verificar que sea admin
    if current_user["rol"] != "admin":
        return jsonify({"error": "No autorizado"}), 403
    
    data = request.get_json()
    
    # Validar que se enviaron datos
    if not data:
        return jsonify({"error": "No se proporcionaron datos"}), 400
    
    # Campos permitidos para actualizar
    campos_actualizables = ['nombre', 'apellido', 'username', 'rol', 'password']
    campos_a_actualizar = {}
    
    # Filtrar solo los campos permitidos
    for campo in campos_actualizables:
        if campo in data:
            campos_a_actualizar[campo] = data[campo]
    
    # Validar que al menos un campo fue enviado
    if not campos_a_actualizar:
        return jsonify({"error": "No se proporcionaron campos válidos para actualizar"}), 400
    
    # Actualizar el usuario con el ID de la URL
    usuario = UsuarioController.update_usuario(id, campos_a_actualizar)  # ← Usar 'id' de la ruta
    
    if usuario:
        return jsonify({
            "mensaje": "Usuario actualizado correctamente",
            "usuario": usuario.serializar(),
            "campos_actualizados": list(campos_a_actualizar.keys())
        }), 200
    
    return jsonify({"error": "Usuario no encontrado o no se pudo actualizar"}), 404

# READ ONE
@usuario_bp.route("/search/<int:id_usuario>", methods=["GET"])
def get_usuarios_one(id_usuario):
    usuario = UsuarioController.get_usuarios(id_usuario)
    if usuario:
        return jsonify(usuario.to_dict()), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

# READ ALL
@usuario_bp.route("/read", methods=["GET"])
def get_usuarios_all():
    usuarios = UsuarioController.get_usuarios()
    return jsonify([p.to_dict() for p in usuarios]), 200


# DELETE
@usuario_bp.route("/delete/<int:id_usuario>", methods=["DELETE"])
def delete_usuario(id_usuario):
    success = UsuarioController.delete_usuario(id_usuario)
    if success:
        return jsonify({"message": "usuario eliminado"}), 200
    return jsonify({"error": "No se pudo eliminar el usuario"}), 400