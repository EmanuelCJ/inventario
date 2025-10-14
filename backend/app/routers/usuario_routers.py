from flask import Blueprint, request, jsonify
from app.controllers.usuario_controllers import UsuarioController
from ..utils.validacion_token import token_required
from ..interfaces.usuario_interfaz import UsuarioShema
from pydantic import ValidationError




usuario_bp = Blueprint("usuario_bp", __name__)

# CREATE
@usuario_bp.route("/create", methods=["POST"])
@token_required
def create_usuario(current_user):
    
    if current_user["rol"] != "admin":
        return jsonify({"error": "No autorizado"}), 403

    data = request.get_json()

    try:
        
        validacion = UsuarioShema(**data)
        # data_validado = validacion.model_dump()
        # print("Datos validados:", data_validado)

        # usuario = UsuarioController.create_usuario(data, current_user["id_usuario"])
        
        # if usuario:
        #    return jsonify({
        #         "mensaje": "Validación exitosa",
        #         "usuario": usuario.serializar()
        #         }), 200
        
        # return jsonify({"error": "No se pudo crear el usuario"}), 400

    except ValidationError as e:
        errores = e.errors()
        print("Errores de validación:")
        for err in errores:
            print(f"Campo: {err['loc'][0]}, Error: {err['msg']}")
        return jsonify({"errores": errores}), 400

    except Exception as e:
        print(f"Error en la ruta create usuario: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500


        

# UPDATE
@usuario_bp.route("/update/<int:id>", methods=["PUT"])
@token_required
def update_usuario(current_user, id ):

    # Verificar que sea admin
    if current_user["rol"] != "admin":
        return jsonify({"error": "No autorizado"}), 403
    
    data = request.get_json()

    # Validar que se enviaron datos
    if not data:
        return jsonify({"error": "No se proporcionaron datos"}), 400
    
    # Campos permitidos para actualizar
    campos_actualizables = ['nombre', 'apellido', 'username', 'rol', 'password']

    #Campos para actualizar
    campos_a_actualizar = {}
    
    # Filtrar solo los campos permitidos
    for campo in campos_actualizables:
        if campo in data:
            campos_a_actualizar[campo] = data[campo]

    # Validar que al menos un campo fue enviado
    if not campos_a_actualizar:
        return jsonify({"error": "No se proporcionaron campos válidos para actualizar"}), 400

    mensaje = UsuarioController.update_usuario(
            data=campos_a_actualizar,
            id_admin=current_user["id_usuario"], 
            id_usuario=id
        )
    
    if mensaje.get("status") == True:
        return jsonify({
            "mensaje": "Usuario actualizado correctamente",
            "id_auditoria": mensaje,
            "campos_actualizados": list(campos_a_actualizar.keys())
        }), 200    
    
    return jsonify(mensaje), 404

# DELETE
@usuario_bp.route("/delete/<int:id_usuario>", methods=["DELETE"])
@token_required
def delete_usuario(current_user,id_usuario):

    # Verificar que sea admin
    if current_user["rol"] != "admin":
        return jsonify({"error": "No autorizado"}), 403
    
    success = UsuarioController.delete_usuario(id_admin=current_user["id_usuario"],id_usuario=id_usuario)
    if success:
        return jsonify({"message": "usuario eliminado"}), 200
    return jsonify({"error": "No se pudo eliminar el usuario"}), 400

# READ ONE
@usuario_bp.route("/read/<int:id_usuario>", methods=["GET"])
@token_required
def get_usuarios_one(current_user,id_usuario):

    # Verificar que sea admin o editor
    if current_user["rol"] != "admin" and current_user["rol"] != "editor":
        return jsonify({"error": "No autorizado"}), 403
    
    usuario = UsuarioController.get_usuario(id_usuario)
    if usuario:
        return jsonify(usuario), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

# READ ALL
@usuario_bp.route("/read", methods=["GET"])
@token_required
def get_usuarios_all(current_user):
    
    # Verificar que sea admin o editor
    if current_user["rol"] != "admin" and current_user["rol"] != "editor":
        return jsonify({"error": "No autorizado"}), 403
    
    usuarios = UsuarioController.get_usuarios()
    if usuarios is None:
        return jsonify({"error": "No se pudieron obtener los usuarios"}), 400
    return jsonify(usuarios), 200

