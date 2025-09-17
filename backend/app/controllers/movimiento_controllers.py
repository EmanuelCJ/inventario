from ..services.movimiento_service import MovimientoService

class movimiento_controllers:

    @staticmethod
    def create_movimiento_controller(id_usuario:int, data_producto: dict, tipo_movimiento:str):
        return MovimientoService.registrar_movimiento(id_usuario,data_producto,tipo_movimiento)


movimiento = movimiento_controllers.create_movimiento_controller(2,{"cantidad":2},"crear_movimiento")

print(movimiento)