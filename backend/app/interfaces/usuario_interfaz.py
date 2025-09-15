from pydantic import BaseModel

class UsuarioInterfaz(BaseModel):
    id: int
    nombre: str
    apellido: str
    rol: str
    password: str

    
