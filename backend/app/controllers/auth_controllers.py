# controllers/auth_controller.py
from ..services.auth_service import AuthService

class AuthControllers:

    @staticmethod
    def create_token(username: str , password: str):
        
        usuario_autenticado = AuthService.login(username, password)
        if usuario_autenticado is not None:
            token_access = AuthService.create_access_token(usuario_autenticado)
            token_refresh = AuthService.create_refresh_token(usuario_autenticado)
            return {
                "access_token": token_access,
                "refresh_token": token_refresh
            }
        return False
    
    @staticmethod
    def verificar_token(token):
        response=AuthService.verificar_token(token=token)
        if response:
            return response
