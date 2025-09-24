from ..services.categoria_service import CategoriaService
from ..services.lugar_service import LugarService
from ..services.producto_service import ProductoService
from ..services.usuario_service import UsuarioService
from ..services.permisos_service import PermisosService

class MovimientoService:

    def __init__(self):

        self.Categoria_Service = CategoriaService()
        self.Lugar_Service = LugarService()
        self.Producto_Service = ProductoService()
        self.Usuario_Service = UsuarioService()
        self.Permisos_Service = PermisosService()

    def movimientos_usuario (self , id_usuario : int, data : dict , tipo_movimiento: str) -> int:
        if self.Permisos_Service.validar_permisos(id_usuario, tipo_movimiento):
            id_nuevo_usuario = self.Usuario_Service.crear_usuario(data)
            return id_nuevo_usuario
        
    def movimientos_lugar (self):
        self.Lugar_Service
        
    def movimientos_producto (self):
        self.Producto_Service
        
    def movimientos_categoria (self):
        self.Usuario_Service