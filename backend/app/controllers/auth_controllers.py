# controllers/auth_controller.py
from ..services.auth_service import AuthService

class AuthControllers:

    @staticmethod
    def create_token(username, password):
        usuario_autenticado = AuthService.login(username, password)
        if usuario_autenticado:
            return {
            "access_token": AuthService.create_access_token(usuario_autenticado),
            "refresh_token": AuthService.create_refresh_token(usuario_autenticado)
            }
        return None

    @staticmethod
    def verificar_token(token):
        response=AuthService.verificar_token(token=token)
        if response:
            return response
