class LugarModel:
    def __init__(self, id_lugar: int, nombre: str, descripcion: str):
        self.__id_lugar = id_lugar
        self.__nombre = nombre
        self.__descripcion = descripcion

    def get_id_lugar(self)-> int:
        return self.__id_lugar

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
            "id_lugar": self.get_id_lugar(),
            "nombre": self.get_nombre(),
            "descripcion": self.get_descripcion()
        }

    def deserializar(self, data_lugar: dict)-> "LugarModel":
        return LugarModel(
            id_lugar = data_lugar.get("id_lugar"),
            nombre = data_lugar.get("nombre"),
            descripcion = data_lugar.get("descripcion")
        )