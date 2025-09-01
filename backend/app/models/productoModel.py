class productoModel:
    def __init__(self, id_producto: int, nombre: str, descripcion: str, precio: float, cantidad: int):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def get_ID(self):
        return self.id_producto
    
    def get_nombre(self):
        return self.nombre
    
    def get_descripcion(self):
        return self.descripcion
    
    def get_precio(self):
        return self.precio
    
    def get_cantidad(self):
        return self.cantidad