class producto_lugarModel:
    
    def __init__(self, id_producto_lugar: int, id_producto: int, id_lugar: int, cantidad: int):
        self.id_producto_lugar = id_producto_lugar
        self.id_producto = id_producto
        self.id_lugar = id_lugar
        self.cantidad = cantidad

    def get_ID(self):
        return self.id_producto_lugar
    
    def get_ID_Producto(self):
        return self.id_producto
    
    def get_ID_Lugar(self):
        return self.id_lugar
    
    def get_cantidad(self):
        return self.cantidad