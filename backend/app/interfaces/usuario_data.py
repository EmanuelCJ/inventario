from pydantic import BaseModel, field_validator, ValidationError
import re

# 🔒 Patrón para detectar intentos de inyección SQL básicos
SQL_INJECTION_PATTERN = re.compile(
    r"(?:--|\b(drop|delete|insert|update|select|alter|truncate|exec|union|create)\b)",
    re.IGNORECASE
)

class UserInterface(BaseModel):
    """Define la estructura y reglas de validación para un usuario nuevo."""

    nombre: str
    apellido: str
    username: str
    rol: str
    password: str

    # --- 🔹 Validaciones generales para tipo y SQL Injection ---
    @field_validator("nombre", "apellido", "username", "password", "rol")
    @classmethod
    def validar_tipo_y_sql(cls, value: str, field):
        """Verifica tipo string, que no esté vacío y sin SQL injection."""
        if not isinstance(value, str):
            raise TypeError(f"El campo '{field.name}' debe ser una cadena de texto (str).")

        if not value.strip():
            raise ValueError(f"El campo '{field.name}' no puede estar vacío.")

        if SQL_INJECTION_PATTERN.search(value):
            raise ValueError(f"El campo '{field.name}' contiene texto prohibido o sospechoso (inyección SQL).")

        return value.strip()

    # --- 🔹 Validación de longitud mínima ---
    @field_validator("nombre", "apellido", "username")
    @classmethod
    def validar_longitud(cls, value: str, field):
        if len(value) < 4:
            raise ValueError(f"El campo '{field.name}' debe tener al menos 4 caracteres.")
        return value

    # --- 🔹 Validación de rol permitido ---
    @field_validator("rol")
    @classmethod
    def validar_rol(cls, value: str):
        roles_validos = {"admin", "editor", "visor"}
        if value not in roles_validos:
            raise ValueError(f"El campo 'rol' debe ser uno de: {roles_validos}.")
        return value

    # --- 🔹 Validación opcional de password mínima ---
    @field_validator("password")
    @classmethod
    def validar_password(cls, value: str):
        if len(value) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")
        return value
