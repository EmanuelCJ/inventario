# controllers/auth_controller.py
from flask import Blueprint, request, jsonify, make_response
from ..controllers.auth_controllers import AuthControllers
import os

#importar variables de entorno
IS_PROD = os.getenv("FLASK_ENV") == "production"

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return {"error": "Faltan datos"}, 400

    tokens = AuthControllers.create_token(
        data["username"], data["password"]
    )

    if not tokens:
        return {"error": "Credenciales inválidas"}, 401

    resp = make_response({"ok": True})

    resp.set_cookie(
        "access_token",
        tokens["access_token"],
        httponly=True,
        secure=IS_PROD,
        samesite="Strict" if IS_PROD else "Lax",
        max_age=1800
    )

    resp.set_cookie(
        "refresh_token",
        tokens["refresh_token"],
        httponly=True,
        secure=IS_PROD,
        samesite="Strict" if IS_PROD else "Lax",
        max_age=604800
    )

    return resp

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

