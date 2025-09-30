# controllers/auth_controller.py
from ..services.auth_service import AuthService

class AuthControllers:

    @staticmethod
    def create_token(username: str , password: str):
        token = AuthService.login(username, password)
        print(f"token esta ", token)
        if token:
            return token
        return False
    
    @staticmethod
    def verificar_token(token):
        response=AuthService.verificar_token(token=token)
        if response:
            return response
