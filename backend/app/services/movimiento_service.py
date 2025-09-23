from ..DAO.movimiento_DAO import MovimientosDAO
from ..DAO.permisos_DAO import PermisosDAO
from ..DAO.usuario_DAO import UsuarioDAO
from .producto_service import ProductoService

class MovimientoService:

    def __init__(self):
        self.producto_service = ProductoService()
        self.movimientoDAO = MovimientosDAO()

    def registrar(self ,id_usuario: int, id_producto : int, cantidad : int, tipo_movimiento:str) -> int:
        
        usuario = UsuarioDAO.read_one_user(id_usuario)
        if not usuario:
            raise Exception("Usuario no encontrado")
        
        try:
            permiso = PermisosDAO.validar(usuario , tipo_movimiento)
            if not permiso == 1:
                raise Exception("permiso no encontrado")

            # Crear movimiento
            id_movimiento = MovimientosDAO.create_movimiento({
            "tipo": tipo_movimiento,
            "cantidad": cantidad,
            "id_usuario": id_usuario,
            })
            
            if not id_movimiento:
                raise Exception("error al crear movimiento")

             # Ejecutar operación sobre producto
            operaciones = {
                "create": lambda: self.producto_service.create_producto(),
                "update": lambda: self.producto_service.update_cantidad(id_producto, cantidad),
                "read": lambda: self.producto_service.read_producto(id_producto),
                "delete": lambda: self.producto_service.delete_producto(id_producto),
            }

            if tipo_movimiento not in operaciones:
                raise Exception("Movimiento no soportado")

            return operaciones[tipo_movimiento]()
            
        except Exception as e:
            print(f"error al crear registro")
            return False

 