# utils/validation_rol.py

class Permisos:

    def __init__(self):
        
        self.permisos = {
            "movimiento": {
                "admin": ["crear_movimiento", "editar_movimiento", "eliminar_movimiento", "ver_movimiento"],
                "editor": ["crear_movimiento", "editar_movimiento", "ver_movimiento"],
                "visor": ["ver_movimiento"]
            },
            "producto": {
                "admin": ["crear_producto", "editar_producto", "eliminar_producto", "ver_producto"],
                "editor": ["crear_producto", "editar_producto", "ver_producto"],
                "visor": ["ver_producto"]
            },
            "usuario": {
                "admin": ["crear_usuario", "editar_usuario", "eliminar_usuario", "ver_usuario"],
                "editor": ["crear_usuario", "editar_usuario", "ver_usuario"],
                "visor": ["ver_usuario"]
            }
        }

    @staticmethod
    def tiene_permiso(usuario: object, modulo:str, accion:str) -> bool:
        rol = usuario.get_rol()
        return accion in Permisos.permisos.get(modulo, {}).get(rol, [])
