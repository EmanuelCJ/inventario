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

    tokens = AuthControllers.create_token(username, password)
    
    if tokens is not None:
        
        resp = jsonify({"ok": True})

        token_access = tokens["access_token"]
        token_refresh = tokens["refresh_token"]

        resp.set_cookie(
            "access_token",
            token_access,
            httponly=True,
            secure=True,
            samesite="Strict",
            max_age=1800  # 30 min
        )

        resp.set_cookie(
            "refresh_token",
            token_refresh,
            httponly=True,
            secure=True,
            samesite="Strict",
            max_age=604800  # 7 días
        )

        return resp

    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

# verifica el token enviado en headers (borrar s)
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

