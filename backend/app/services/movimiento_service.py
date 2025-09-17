from ..DAO.movimiento_DAO import MovimientosDAO
from ..DAO.producto_DAO import ProductoDAO
from ..DAO.usuario_DAO import UsuarioDAO
from ..utils.validation_rol import Permisos

class MovimientoService:
    
    @staticmethod
    def registrar_movimiento(id_usuario: int, data_product : dict, tipo_movimiento:str, producto_id : int)-> int:
        usuario = UsuarioDAO.read_one_user(id_usuario)
        if not usuario:
            raise Exception("Usuario no encontrado")
  
        cantidad = data_product["cantidad"]

        # Crear movimiento
        movimiento_id = MovimientosDAO.create_movimiento({
            "tipo": tipo_movimiento,
            "cantidad": cantidad,
            "id_usuario": id_usuario,
        })

        # CRUD
        if tipo_movimiento == "entrada":
            if not Permisos.tiene_permisos(usuario["rol"],"editar_producto"):
                return PermissionError("Usuario sin permisos")
            ProductoDAO.incrementar_stock(producto_id, cantidad)

        elif tipo_movimiento == "salida":
            if not Permisos.tiene_permisos(usuario["rol"],"editar_producto"):
                return PermissionError("Usuario sin permisos")
            ProductoDAO.decrementar_stock(producto_id, cantidad)

        elif tipo_movimiento == "update":
            if not Permisos.tiene_permisos(usuario["rol"],"editar_producto"):
                return PermissionError("Usuario sin permisos")
            ProductoDAO.delete_product(producto_id)

        elif tipo_movimiento == "create":
            if not Permisos.tiene_permisos(usuario["rol"],"editar_producto"):
                return PermissionError("Usuario sin permisos")
            ProductoDAO.create_product(data_product)

        elif tipo_movimiento == "delete":
            if not Permisos.tiene_permisos(usuario["rol"],"editar_producto"):
                return PermissionError("Usuario sin permisos")
            ProductoDAO.delete_product(producto_id)

        return True
    
    