class categoriaModel:
    def __init__(self, id_categoria: int, nombre: str, descripcion: str):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion

    def get_ID(self):
        return self.id_categoria
    
    def get_nombre(self):
        return self.nombre
    
    def get_descripcion(self):
        return self.descripcion
    
    def _set_nombre(self, nombre: str):
        self.nombre = nombre
    
    def _set_descripcion(self, descripcion: str):
        self.descripcion = descripcion