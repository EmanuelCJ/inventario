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
    

user = UsuarioModel("Emanuel","Sanchez","admin","1234")

nuevo = {
    "nombre": "Eduardo",
    "apellido": "Sanchez",
    "rol": "editor",
    "password_hash":  hash_password("1245")
}

respuesta = UsuarioController.create_user_controller(user, nuevo)

print (respuesta)
