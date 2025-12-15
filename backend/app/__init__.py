from flask import Flask
from flask_cors import CORS 

#importar rutas
from app.routers.usuario_routers import usuario_bp
from app.routers.auth_routers import auth_bp
from app.routers.producto_routers import producto_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    #rutas del sistema 
    app.register_blueprint(usuario_bp,url_prefix="/usuarios") #prefijo de ruta para usuarios
    app.register_blueprint(auth_bp, url_prefix="/auth") #prefijo de ruta para autenticación
    #app.register_blueprint(producto_bp, url_prefix="/productos") #prefijo de ruta para productos

    @app.route("/")
    def home():
        return "<div><h1>API REST con Flask</h1></div>"
    
    return app  