from app.models.producto_Model import ProductoModel

class ProductoController:

    @staticmethod
    def create_producto(data):
        producto = ProductoModel(
            nombre=data.get("nombre"),
            descripcion=data.get("descripcion"),
            precio=data.get("precio"),
            id_categoria=data.get("id_categoria")
        )
        return producto.create()

    @staticmethod
    def get_producto(id_producto):
        return ProductoModel.read(id_producto)

    @staticmethod
    def get_productos():
        return ProductoModel.read_all()

    @staticmethod
    def update_producto(id_producto, data):
        producto = ProductoModel.read(id_producto)
        if not producto:
            return None
        producto.nombre = data.get("nombre", producto.nombre)
        producto.descripcion = data.get("descripcion", producto.descripcion)
        producto.precio = data.get("precio", producto.precio)
        producto.id_categoria = data.get("id_categoria", producto.id_categoria)
        success = producto.update()
        return producto if success else None

    @staticmethod
    def delete_producto(id_producto):
        return ProductoModel.delete(id_producto)
