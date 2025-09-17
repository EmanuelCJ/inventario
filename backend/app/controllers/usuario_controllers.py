from ..DAO.usuario_DAO import UsuarioDAO
from ..models.usuario_Model import UsuarioModel
from ..utils.generation_password import hash_password

class UsuarioController:

    @staticmethod
    def create_user_controller(usuario : object, datos_user : dict) -> int:
        if usuario.get_rol() != 'admin' and usuario.get_rol() != 'editor':
            raise PermissionError("No tienes permiso para crear un producto")
        return UsuarioDAO.create_user(datos_user)

    @staticmethod
    def update_user_controller(usuario: object, id_usuario : int , data: dict) -> bool:
        if usuario.get_rol() != 'admin' and usuario.get_rol() != 'editor':
            raise PermissionError("No tienes permiso para crear un producto")
        return UsuarioDAO.update_user(id_usuario, data)

    @staticmethod
    def delect_user_controller(usuario: object , id_usuario: int)-> bool:
        if usuario.get_rol() != "admin" and usuario.get_rol() != "editor":
            raise PermissionError("No tienes permiso para modificar un usuario")
        return UsuarioDAO.delete_user(id_usuario)

    @staticmethod
    def read_user_controller(id_usuario: int) -> dict:
        return UsuarioDAO.read_one_user(id_usuario)

    @staticmethod
    def read_all_user_controller() -> dict:
        return UsuarioDAO.read_all_user()
    
    @staticmethod
    def search_user_controller( nombre_user: str ) -> dict:
        return UsuarioDAO.search_user_name(nombre_user)

    @staticmethod
    def search_user_rol(rol_user: str) -> dict:
        return UsuarioDAO.search_user_rol(rol_user)
    
"""

este codigo de abajo debe borrarse se usa para ver si funciona

"""


user = UsuarioModel("Emanuel","Sanchez","editor","1234")

nuevo = {
    "nombre": "emanuel",
    "apellido": "castrillo",
    "rol": "admin",
    "password_hash":  hash_password("miclave1e4")
}

editado2 = {
    "nombre": "juan",
    "apellido": "bruno",
    "rol": "mar",
    "password_hash":  hash_password("miclave124")
}
editado = {
    "nombre": None,
    "apellido": None,
    "rol": "visor",
    "password_hash": None
}

#respuesta = UsuarioController.create_user_controller(user, nuevo)

#print (respuesta)

# update = UsuarioController.update_user_controller(user,3,editado)

# print(update)

delect = UsuarioController.delect_user_controller(user,4)

print(delect)

# read_one = UsuarioController.read_user_controller(2)

# read_all= UsuarioController.read_all_user_controller()

# print(read_all[1])

# if read_one == None:
#     print("No existe usuario")
# print(read_one)

#buscar = UsuarioController.search_user_rol("admin")

#print(buscar)

