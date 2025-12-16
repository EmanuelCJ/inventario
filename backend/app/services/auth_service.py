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

        # Buscar usuario en la base de datos
        usuario = UsuarioDAO.search_username(username)
        if not usuario:
            return None

        if not usuario.get("password"):
            return None
        
        # Verificar contraseña
        if not check_password_hash(usuario.get("password"), password):
            print("❌ Contraseña incorrecta")
            return None

        return usuario

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

    #CREACION DE TOKENS DE ACCESO 
    @staticmethod
    def create_access_token(usuario):
        payload = {
            "id_usuario": usuario["id_usuario"],
            "rol": usuario["rol"],
            "type": "access",
            "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    #CREACION DE TOKENS DE REFRESH
    @staticmethod
    def create_refresh_token(usuario):
        payload = {
            "id_usuario": usuario["id_usuario"],
            "type": "refresh",
            "exp": datetime.now(timezone.utc) + timedelta(days=7)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")