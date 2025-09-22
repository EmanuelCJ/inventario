
class ProductoModel:
    def __init__(self, id_producto: int, nombre : str, condicion: str, descripcion: str, stock_actual : int, id_categoria: int = None, id_movimiento: int = None):

        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__stock_actual = stock_actual 
        self.__condicion = condicion
        #atributos de la relacion
        self.__id_categoria = id_categoria
        self.__id_movimiento = id_movimiento


    # Getters and Setters
    def get_id_producto(self) -> int:
        return self.__id_producto
        
    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre
        
    def get_descripcion(self) -> str:
        return self.__descripcion
    
    def set_descripcion(self, descripcion: str):
        self.__descripcion = descripcion

    def get_stock_actual(self)-> str:
        return self.__stock_actual
    
    def set_stock_actual(self, stock: int):
        self.__stock_actual = stock
        
    def get_condicion(self) -> str:
        return self.__condicion
    
    def set_condicion(self, condicion: str):
        self.__condicion = condicion
        
    def get_id_categoria(self) -> int:
        return self.__id_categoria
    
    def set_id_categoria(self, id_categoria: int):
        self.__id_categoria = id_categoria
        
    def get_id_movimiento(self) -> int:
        return self.__id_movimiento
    
    def set_id_movimiento(self, nuevo: str):
        self.__id_movimiento = nuevo
    
    
    def serializar(self) -> dict:
        return {
            "id_producto": self.get_id_producto(),
            "nombre": self.get_nombre(),
            "descripcion": self.get_descripcion(),
            "stock_actual": self.get_stock_actual(),
            "condicion": self.get_condicion(),
            "id_categoria": self.get_id_categoria(),
            "id_movimiento": self.get_id_movimiento()
        }

    @staticmethod
    def deserializar(data_producto: dict) -> "ProductoModel":
        return ProductoModel(
            id_producto = data_producto.get("id_producto"),
            nombre = data_producto.get("nombre"),
            condicion = data_producto.get("condicion"),
            descripcion = data_producto.get("descripcion"),
            stock_actual = data_producto.get("stock_actual"),
            id_categoria = data_producto.get("id_categoria"),
            id_movimiento = data_producto.get("id_movimiento")
        )
        