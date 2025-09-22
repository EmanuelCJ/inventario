from ..services.movimiento_service import MovimientoService

class MovimientoControllers:

    @staticmethod
    def create_movimiento_controller(id_usuario:int, data_producto: dict, tipo_movimiento:str):
        return MovimientoService.registrar(id_usuario,data_producto,tipo_movimiento)


movimiento = MovimientoControllers.create_movimiento_controller(2,{"cantidad":2},"crear_movimiento")

print(movimiento)