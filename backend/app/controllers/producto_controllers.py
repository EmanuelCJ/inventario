from ..DAO.producto_DAO import ProductoDAO

class ProductoControllers:

    @staticmethod
    def create_product_controller(usuario: object, datos_product : dict) -> bool:
        if usuario.get_rol() != 'admin' and usuario.get_rol() != 'editor':
            raise PermissionError("No tienes permiso para crear un producto")
        return ProductoDAO.create_producto(datos_product)