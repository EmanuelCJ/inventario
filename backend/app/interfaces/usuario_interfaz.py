from pydantic import BaseModel, field_validator, ValidationError
import re

# Patrón básico para detectar inyecciones SQL
# Esto es una simplificación; la forma más segura es usar consultas parametrizadas.
SQL_INJECTION_PATTERN = re.compile(r"(--|drop\s+table|delete\s+from|select\s+.*?\s+from)", re.IGNORECASE)

class UserInterface(BaseModel):
    """Define la estructura y reglas de validación para un objeto Usuario."""
    nombre: str
    apellido: str
    username: str
    rol: str
    password: str

    @field_validator('nombre', 'apellido', 'username', 'rol')
    @classmethod
    def check_for_sql_injection(cls, value):
        """Valida que los campos de texto no contengan posibles inyecciones SQL."""
        if SQL_INJECTION_PATTERN.search(value):
            raise ValueError(f"El campo contiene texto prohibido (posible inyección SQL): '{value}'")
        return value

    @field_validator('rol')
    @classmethod
    def check_valid_role(cls, value):
        """Valida que el campo 'rol' solo contenga valores permitidos."""
        valid_roles = {"editor", "administrador", "viewer"}
        if value not in valid_roles:
            raise ValueError(f"El valor de 'rol' debe ser uno de: {valid_roles}")
        return value