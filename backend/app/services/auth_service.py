# services/auth_service.py
import jwt
from datetime import datetime, timedelta, timezone
import os
from ..DAO.usuario_DAO import UsuarioDAO
from werkzeug.security import check_password_hash
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")  # En tu .env

class AuthService:

    @staticmethod
    def login(username, password):
        usuario = UsuarioDAO.search_username(username)
        if not usuario:
            return None

        print(f"Usuario encontrado: {usuario}")
        print(f"Password hash en DB: {usuario.get('password')}")
        print(f"Password ingresada: {password}")

        if not usuario.get("password"):
            return None

        # Verificar contraseña
        if not check_password_hash(usuario.get("password"), password):
            print("❌ Contraseña incorrecta")
            return None

        # Crear payload del token
        payload = {
            "id_usuario": usuario["id_usuario"],
            "rol": usuario["rol"],
            "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
        }

        print(f"Token expira: {payload['exp']}")

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        if isinstance(token, bytes):
            token = token.decode("utf-8")

        print("✅ Token generado:", token)
        return token

    @staticmethod
    def verificar_token(token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            print("✅ Token válido:", payload)
            return payload
        except jwt.ExpiredSignatureError:
            print("❌ Token expirado")
            return None
        except jwt.InvalidTokenError:
            print("❌ Token inválido")
            return None
