from ..controllers.movimiento_controllers import MovimientoControllers
from ..models.usuario_Model import UsuarioModel

class TestUser:
    
    def crear_usuario_test():

        usuario = UsuarioModel({
        "nombre": "alex",
        "apellido" : "j", 
        "username" : "Arsa1", 
        "rol" : "editor", 
        "password": "arsa2025"
        })   

        #test
        respuesta = MovimientoControllers.create_usuario(1,usuario,"crear_usuario")

        print(respuesta)
