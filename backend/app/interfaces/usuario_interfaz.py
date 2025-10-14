from pydantic import BaseModel, Field, field_validator
from typing import Literal

class UsuarioShema(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    nombre: str = Field(..., min_length=2)
    apellido: str = Field(..., min_length=2)
    rol: Literal["admin", "editor", "visor"]
    password: str = Field(..., min_length=8)

    @field_validator("password")
    def validar_password_segura(cls, value):
        if not any(char.isdigit() for char in value):
            raise ValueError("La contraseña debe contener al menos un número.")
        if not any(char.isupper() for char in value):
            raise ValueError("La contraseña debe contener al menos una mayúscula.")
        return value
