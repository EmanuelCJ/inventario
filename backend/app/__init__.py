from flask import Flask
#importar rutas


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, World!"
    return app  