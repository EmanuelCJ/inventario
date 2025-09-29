# services/auth_service.py
import jwt
from datetime import datetime, timedelta, timezone
import os
from ..DAO.usuario_DAO import UsuarioDAO
from werkzeug.security import check_password_hash

"""
        Service genera el token y ademas verifica
"""
#obtengo super clave desde las variables de entono
SECRET_KEY = os.getenv("SECRET_KEY")  # En tu .env

class AuthService:
    
    @staticmethod
    def login(username, password):
        usuario = UsuarioDAO.search_username(username)
        if usuario and check_password_hash(usuario["password"], password):
            payload = {
                "id": usuario["id_usuario"],
                "rol": usuario["rol"],
                "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
            return token
        return None

    @staticmethod
    def verificar_token(token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload  # te da {id, rol, exp}
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
