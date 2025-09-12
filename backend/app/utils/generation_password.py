from werkzeug.security import generate_password_hash

def hash_password(password: str) -> str:
    # Usa pbkdf2:sha256 con 260000 iteraciones (valor recomendado)
    return generate_password_hash(password, method="pbkdf2:sha256", salt_length=16)
