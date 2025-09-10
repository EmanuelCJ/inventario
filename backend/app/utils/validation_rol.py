# utils/validation_rol.py

PERMISOS = {
    "admin": ["crear_movimiento", "editar_movimiento", "eliminar_movimiento", "ver_movimiento"],
    "editor": ["crear_movimiento", "editar_movimiento", "ver_movimiento"],
    "visor": ["ver_movimiento"]
}

def validar_permiso(usuario, accion):
    if accion in PERMISOS.get(usuario.get_rol(), []):
        return True
    return False
