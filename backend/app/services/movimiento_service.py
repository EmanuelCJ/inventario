from ..services.categoria_service import CategoriaService
from ..services.lugar_service import LugarService
from ..services.producto_service import ProductoService
from ..services.usuario_service import UsuarioService

class MovimientoService:

    def __init__(self):

        self.Categoria_Service = CategoriaService()
        self.Lugar_Service = LugarService()
        self.Producto_Service = ProductoService()
        self.Usuario_Service = UsuarioService()

    def movimientos_usuario (self):
        self.Usuario_Service
        
    def movimientos_lugar (self):
        self.Lugar_Service
        
    def movimientos_producto (self):
        self.Producto_Service
        
    def movimientos_categoria (self):
        self.Usuario_Service