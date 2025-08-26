from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/saludo/<int:usario_id>')
def saludo(usario_id):
    return f"Hola, {usario_id}!"