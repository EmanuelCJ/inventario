from flask import Flask
#importar rutas
from .routers.usuario_routers import usuario_bp
from .routers.auth_routers import auth_bp

def create_app():
    app = Flask(__name__)

    #rutas del sistema
    app.register_blueprint(usuario_bp,url_prefix="/usuarios")
    app.register_blueprint(auth_bp,url_prefix="/login")

    return app  