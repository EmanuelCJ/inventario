# controllers/auth_controller.py
from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    token = AuthService.login(email, password)
    if token:
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401
