from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class UsuarioInterfaz:
    id_usuario: Optional[int] = field(default=None)
    nombre: str = field(default="")
    apellido: str = field(default="")
    rol: str = field(default="visor")  # 'admin' o 'user'
    contrasena: str = field(default="")  # Almacenar el hash de la contraseña

    def validar_dict(data : dict) -> Usuario:
        try:
           return UsuarioInterfaz(**data)          
        except Exception as e:
          print(f"Error converting to UsuarioInterfaz: {e}")
          return None
                