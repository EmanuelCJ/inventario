from ..services.usuario_service import UsuarioService

class TestUser:

    @staticmethod
    def crear_usuario_test():

        

        #test
        respuesta = UsuarioService.crear_usuario(
            nombre = "ALEX",
            apellido  =  "ALEJO", 
            username =  "doom123", 
            rol =  "editor", 
            password =  "arsa2025",
            id_admin =  1
        )
        return respuesta
    
    @staticmethod
    def update_usuario_test():

        #test
        respuesta = UsuarioService.update_usuario(
            id_usuario = 31,
            nombre = "nico",
            apellido  =  "ex", 
            username =  "HOLA MUNDO", 
            rol =  "editor", 
            password =  "casad",
            id_admin=  1
        )
        return respuesta
    
    @staticmethod
    def delete_usuario_test():
        respuesta = UsuarioService.delete_usuario(1,30)
        return respuesta
    
    @staticmethod
    def read_usuario_test():
        return UsuarioService.read_usuario()


print("Read usuario + registrar movimiento: ")
print(TestUser.read_usuario_test())

print("Crear Usuario + registrar movimiento: ")
print(TestUser.crear_usuario_test())

print("Update Usuario + registrar movimiento: ")
print(TestUser.update_usuario_test())

print("Elimina un usuario:")
print(TestUser.delete_usuario_test())