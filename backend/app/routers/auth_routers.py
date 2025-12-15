# controllers/auth_controller.py
from flask import Blueprint, request, jsonify
from ..controllers.auth_controllers import AuthControllers

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    
    data = request.get_json()
    
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Faltan datos"}), 400
    
    username = data["username"]
    password = data["password"]

    token = AuthControllers.create_token(username, password)
    
    if token:
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401



@auth_bp.route("/protegido", methods=["GET"])
def protegido():
    
    token = request.headers.get("Authorization")  # Enviar: Bearer <token>
    if not token:
        return jsonify({"error": "Falta token"}), 401

    token = token.replace("Bearer ", "")  # quitar "Bearer " si lo envías así
    payload = AuthControllers.verificar_token(token)
    if not payload:
        return jsonify({"error": "Token inválido o expirado"}), 401

    return jsonify({"msg": "Acceso concedido", "datos": payload}), 200

@auth_bp.route("/", methods=["GET"])
def aviso():
    
    return "<div><h1>Aplicacion Api REST introduzca usuario y contraseña</h1></div>"

