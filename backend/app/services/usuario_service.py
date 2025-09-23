# service va la logica de negocio
from .movimiento_service import MovimientoService

class UsuarioService:
    
    @staticmethod
    def producto():
        MovimientoService.registrar_producto()

    @staticmethod
    def usuario():
        MovimientoService.registrar_usuario()

    @staticmethod
    def roles():
        MovimientoService.registrar_roles()

    @staticmethod
    def categoria():
        MovimientoService.registrar_categoria()