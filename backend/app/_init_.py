from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"Hola, {nombre}!"