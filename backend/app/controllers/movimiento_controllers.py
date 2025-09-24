from ..services.movimiento_service import MovimientoService

class MovimientoControllers:

    @staticmethod
    def create_usuario( id_usuario:int, data_usuario : dict , tipo_movimiento: str)->int:
        service = MovimientoService()
        return service.movimientos_usuario(id_usuario, data_usuario, tipo_movimiento)
