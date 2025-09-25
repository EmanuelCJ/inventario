from flask import Blueprint
from ..controllers.usuario_controllers import UsuarioController

usuario_bp = Blueprint("usuario", __name__)

usuario_bp.route("/usuarios/update", methods=["PUT"])(UsuarioController.update_usuario)