# service va la logica de negocio
from .movimiento_service import MovimientoService

class UsuarioService:
    
    @staticmethod
    def create():
        MovimientoService.registrar()

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass

    @staticmethod
    def read():
        pass