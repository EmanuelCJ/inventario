class ProductoLugarModel:
    
    def __init__(self, id_producto_lugar: int, id_producto: int, id_lugar: int, cantidad: int):
        self.__id_producto_lugar = id_producto_lugar
        self.__id_producto = id_producto
        self.__id_lugar = id_lugar
        self.__cantidad = cantidad

    def get_id_producto_lugar(self)->int:
        return self.__id_producto_lugar

    def set_id_producto_lugar(self, nuevo : int):
        self.__id_producto_lugar = nuevo
    
    def get_id_Producto(self):
        return self.__id_producto

    def set_id_Producto(self, nuevo : int):
        self.__id_producto = nuevo
    
    def get_id_lugar(self) -> int:
        return self.__id_lugar

    def set_id_lugar(self, nuevo: int):
        self.__id_lugar = nuevo
    
    def get_cantidad(self) -> int:
        return self.__cantidad 

    def set_cantidad(self, cantidad : int):
        self.__cantidad = cantidad

    def serializar(self) -> dict:
        return {
            "id_producto_lugar": self.get_id_producto_lugar(),
            "id_producto": self.get_id_Producto(),
            "id_lugar": self.get_id_lugar(),
            "cantidad": self.get_cantidad()
        }

    def deserializar(self, data: dict)->"ProductoLugarModel":
        return ProductoLugarModel(
            id_producto_lugar = data.get("id_producto_lugar"),
            id_producto = data.get("id_producto"),
            id_lugar = data.get("id_lugar"),
            cantidad = data.get("cantidad")
        )