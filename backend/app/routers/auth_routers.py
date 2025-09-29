# controllers/auth_controller.py
from flask import Blueprint, request, jsonify
from ..controllers.auth_controllers import AuthControllers

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    token = AuthControllers.login(username, password)
    if token:
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401