from flask import Flask
from flask_cors import CORS 

#importar rutas
from app.routers.usuario_routers import usuario_bp
from app.routers.auth_routers import auth_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    #rutas del sistema
    app.register_blueprint(usuario_bp,url_prefix="/usuarios")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    @app.route("/")
    def home():
        return "API Flask funcionando correctamente"
    
    return app  