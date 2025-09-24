from ..DAO.movimiento_DAO import MovimientosDAO
from ..DAO.permisos_DAO import PermisosDAO
from ..DAO.usuario_DAO import UsuarioDAO
from ..DAO.producto_DAO import ProductoDAO
from ..DAO.categoria_DAO import CategoriaDAO

class MovimientoService:

    def __init__(self):

        self.productoDAO = ProductoDAO()
        self.usuarioDAO = UsuarioDAO()
        self.movimientoDAO = MovimientosDAO()
        self.permisosDAO = PermisosDAO()
        self.categoriaDAO = CategoriaDAO()

    def registrar_producto(self ,id_usuario: int, id_producto : int, cantidad : int, tipo_movimiento:str) -> int:
        
        usuario = self.usuarioDAO.read_one_usuario(id_usuario)
        if not usuario:
            raise Exception("Usuario no encontrado")
        
        try:
            permiso =self.permisosDAO.validar(usuario , tipo_movimiento)
            if not permiso == 1:
                raise Exception("permiso no encontrado")

            # Crear movimiento
            id_movimiento = self.movimientoDAO.create_movimiento({
            "tipo": tipo_movimiento,
            "cantidad": cantidad,
            "id_usuario": id_usuario,
            })
            
            if not id_movimiento:
                raise Exception("error al crear movimiento")

             # Ejecutar operación sobre producto
            operaciones = {
                "create": lambda: self.productoDAO.create_producto(),
                "update": lambda: self.productoDAO.update_producto(id_producto, cantidad),
                "read": lambda: self.productoDAO.read_one_producto(id_producto),
                "delete": lambda: self.productoDAO.delete_producto(id_producto),
            }

            if tipo_movimiento not in operaciones:
                raise Exception("Movimiento no soportado")

            return operaciones[tipo_movimiento]()
            
        except Exception as e:
            print(f"error al crear registro")
            return False
    
    def registrar_usuario(self, id_usuario: int, tipo_movimiento: str, data : dict):

        usuario = self.usuarioDAO.read_one_usuario(id_usuario)
        if not usuario:
            raise Exception("Usuario no encontrado")
        
        try:
            
            permiso =self.permisosDAO.validar(usuario , tipo_movimiento)
            if not permiso == 1:
                raise Exception("permiso no encontrado")
            
            # Crear movimiento
            id_movimiento = self.movimientoDAO.create_movimiento({
                "tipo": tipo_movimiento,
                "cantidad": 0,
                "id_usuario": id_usuario,
            })

            if not id_movimiento:
                raise Exception("error al crear movimiento")

             # Ejecutar operación sobre producto
            operaciones = {
                "create": lambda: self.usuarioDAO.create_usuario(data),
                "update": lambda: self.usuarioDAO.update_usuario(id_usuario, data),
                "read": lambda: self.usuarioDAO.read_one_usuario(id_usuario),
                "delete": lambda: self.usuarioDAO.delete_usuario(id_usuario),
            }

            if tipo_movimiento not in operaciones:
                raise Exception("Movimiento no soportado")

            return operaciones[tipo_movimiento]()
            
        except Exception as e:
            print(f"Error al registrar Usuario")
            return False

    def registrar_roles(self, id_usuario: int, tipo_movimiento: str, data : dict):

        usuario = self.usuarioDAO.read_one_usuario(id_usuario)
        if not usuario:
            raise Exception("Usuario no encontrado")
        
        try:
            
            permiso =self.permisosDAO.validar(usuario , tipo_movimiento)
            if not permiso == 1:
                raise Exception("permiso no encontrado")
            
            # Crear movimiento
            id_movimiento = self.movimientoDAO.create_movimiento({
                "tipo": tipo_movimiento,
                "cantidad": 0,
                "id_usuario": id_usuario,
            })

            if not id_movimiento:
                raise Exception("error al crear movimiento")
            
             # Ejecutar operación sobre producto
            operaciones = {
                "create": lambda: self.usuarioDAO.create_usuario(data),
                "update": lambda: self.usuarioDAO.update_usuario(id_usuario, data),
                "read": lambda: self.usuarioDAO.read_one_usuario(id_usuario),
                "delete": lambda: self.usuarioDAO.delete_usuario(id_usuario),
            }

            if tipo_movimiento not in operaciones:
                raise Exception("Movimiento no soportado")

            return operaciones[tipo_movimiento]()
            
        except Exception as e:
            print(f"Error al registrar Usuario")
            return False
    
    def registrar_categoria(self, id_usuario: int, tipo_movimiento: str, data : dict,id_categoria):

        usuario = self.usuarioDAO.read_one_usuario(id_usuario)
        if not usuario:
            raise Exception("Usuario no encontrado")
        
        try:
            
            permiso =self.permisosDAO.validar(usuario , tipo_movimiento)
            if not permiso == 1:
                raise Exception("permiso no encontrado")
            
            # Crear movimiento
            id_movimiento = self.movimientoDAO.create_movimiento({
                "tipo": tipo_movimiento,
                "cantidad": 0,
                "id_usuario": id_usuario,
            })

            if not id_movimiento:
                raise Exception("error al crear movimiento")

             # Ejecutar operación sobre producto
            operaciones = {
                "create": lambda: self.categoriaDAO.create_categoria(data),
                "update": lambda: self.categoriaDAO.update_categoria(id_categoria, data),
                "read": lambda: self.categoriaDAO.read_one_categoria(id_categoria),
                "delete": lambda: self.categoriaDAO.delete_categoria(id_categoria),
            }

            if tipo_movimiento not in operaciones:
                raise Exception("Movimiento no soportado")

            return operaciones[tipo_movimiento]()
            
        except Exception as e:
            print(f"Error al registrar Usuario")
            return False
