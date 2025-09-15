from ..DAO.usuario_DAO import UsuarioDAO
from ..DAO.producto_DAO import ProductoDAO
from ..models.usuario_Model import UsuarioModel
from ..utils.generation_password import hash_password

class UsuarioController:
    
    @staticmethod
    def create_user_controller(usuario : object, datos_user : dict) -> bool:
        return UsuarioDAO.create_user(usuario,datos_user)

    @staticmethod
    def create_product_controller(Usuario: object, datos_product : dict) -> bool:
        return ProductoDAO.create_product(Usuario, datos_product)
    

"""

este codigo de abajo debe borrarse se usa para ver si funciona

"""


user = UsuarioModel("Emanuel","Sanchez","editor","1234")

nuevo = {
    "nombre": "Emanuel",
    "apellido": "castrillo",
    "rol": "admin",
    "password_hash":  hash_password("miclave124")
}

producto = {
    "nombre":"mouse",
    "descripcion":"esto es una prueba",
    "condicion": "nuevo", 
    "cantidad": 10
}

respuesta = UsuarioController.create_product_controller(user, nuevo)

print (respuesta)
