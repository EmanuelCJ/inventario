from ..services.usuario_service import UsuarioService

class TestUser:

    @staticmethod
    def crear_usuario_test():

        #test
        respuesta = UsuarioService.crear_usuario(
            nombre = "nico",
            apellido  =  "ex", 
            username =  "arsa2021", 
            rol =  "visor", 
            password =  "arsa2025",
            id_admin =  1
        )
        return respuesta
    
    @staticmethod
    def update_usuario_test():

        #test
        respuesta = UsuarioService.update_usuario(
            id_usuario = 23,
            nombre = "nico",
            apellido  =  "ex", 
            username =  "HOLA MUNDO", 
            rol =  "editor", 
            password =  "casad",
            id_admin=  1
        )
        return respuesta

print(f"Crear Usuario + registrar movimiento: ")
#print(TestUser.crear_usuario_test())

print(f"Update Usuario + registrar movimiento: ")
print(TestUser.update_usuario_test())