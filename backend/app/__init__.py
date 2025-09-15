from flask import Flask
#importar rutas
from app.routers.usuario_routers import usuario_router

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, World!"
    return app  