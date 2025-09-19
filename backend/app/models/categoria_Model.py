class CategoriaModel:
    def __init__(self, id_categoria : int, nombre: str, descripcion: str):
        self.__id_categoria = id_categoria
        self.__nombre = nombre
        self.__descripcion = descripcion

    def get_id(self) -> int :
        return self.__id_categoria
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre
    
    def get_descripcion(self) -> str:
        return self.__descripcion
    
    def set_descripcion(self, descripcion: str):
        self.__descripcion = descripcion

    def serializar(self) -> dict:
        return {
            "id_categoria" : self.get_id(),
            "nombre" : self.get_nombre(),
            "descripcion": self.get_descripcion()
        }

    def deserializar(self, data_categoria : dict ) -> "CategoriaModel":
        return CategoriaModel(
            id_categoria = data_categoria.get("id_categoria"),
            nombre = data_categoria.get("nombre"),
            descripcion = data_categoria.get("descripcion")
        )