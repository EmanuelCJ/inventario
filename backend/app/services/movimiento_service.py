from ..DAO.movimiento_DAO import MovimientosDAO
from ..DAO.producto_DAO import ProductoDAO
from ..DAO.usuario_DAO import UsuarioDAO
from ..utils.validation_rol import Permisos

class MovimientoService:
    
    @staticmethod
    def registrar_movimiento(usuario_id: int, producto_id :int , data_product : dict, tipo:str)-> int:
        usuario = UsuarioDAO.read_one_user(usuario_id)
        if not usuario:
            raise Exception("Usuario no encontrado")

        
        cantidad = data_product["cantidad"]

        # CRUD
        if tipo == "entrada":
            if not Permisos.tiene_permisos(usuario["rol"],"editar_producto"):
                return PermissionError("Usuario sin permisos")
            ProductoDAO.incrementar_stock(producto_id, cantidad)
        elif tipo == "salida":
            if not Permisos.tiene_permisos(usuario["rol"],"editar_producto"):
                return PermissionError("Usuario sin permisos")
            ProductoDAO.decrementar_stock(producto_id, cantidad)
        elif tipo == "update":
            if not Permisos.tiene_permisos(usuario["rol"],"editar_producto"):
                return PermissionError("Usuario sin permisos")
            ProductoDAO.delete_product(producto_id)
        elif tipo == "create":
            if not Permisos.tiene_permisos(usuario["rol"],"editar_producto"):
                return PermissionError("Usuario sin permisos")
            ProductoDAO.create_product(data_product)
        elif tipo == "delete":
            if not Permisos.tiene_permisos(usuario["rol"],"editar_producto"):
                return PermissionError("Usuario sin permisos")
            ProductoDAO.delete_product(producto_id)

        if not Permisos.tiene_permisos( usuario["rol"] , "registrar_movimiento"):
            raise PermissionError("Usuario sin permisos")
        
        # Crear movimiento
        movimiento_id = MovimientosDAO.create({
            "tipo": tipo,
            "cantidad": cantidad,
            "usuario_id": usuario_id,
            "producto_id": producto_id
        })
        return movimiento_id