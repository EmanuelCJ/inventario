# controllers/auth_controller.py
from ..services.auth_service import AuthService

class AuthControllers:

    @staticmethod
    def login(username: str , password: str):
        token = AuthService.login(username, password)
        if token:
            return token
        return False
