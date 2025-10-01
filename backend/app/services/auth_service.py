# services/auth_service.py
import jwt
from datetime import datetime, timedelta, timezone
import os
from ..DAO.usuario_DAO import UsuarioDAO
from werkzeug.security import check_password_hash
#cargar las variables de entorno desde el archivo .env
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()


"""
    Service genera el token y ademas verifica
"""

#obtengo super clave desde las variables de entono
SECRET_KEY = os.getenv("SECRET_KEY")  # En tu .env

class AuthService:

    @staticmethod
    def login(username, password):
        usuario = UsuarioDAO.search_username(username)
        if not usuario:
            return None

        password_hash_db = usuario["password"]
        if not password_hash_db:
            return None
        
        if not check_password_hash(password_hash_db, password):
            return None

        payload = {
            "id_usuario": usuario["id_usuario"],
            "rol": usuario["rol"],
            "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        if isinstance(token, bytes):  # compatibilidad
            token = token.decode("utf-8")

            print("Token generado:", token)  # Siempre imprime
        return token

    @staticmethod
    def verificar_token(token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload  # te da {id, rol, exp}
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
