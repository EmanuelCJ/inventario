from flask import Flask
#importar rutas
from .routers.usuario_routers import usuario_bp
from .routers.

def create_app():
    app = Flask(__name__)

    app.register_blueprint(usuario_bp,url_prefix="/usuarios")

    @app.route('/')
    def hello():
        return "Hello, World!"
    
    return app  