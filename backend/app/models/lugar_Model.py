class lugarModel:
    def __init__(self, id_lugar: int, nombre: str, descripcion: str):
        self.id_lugar = id_lugar
        self.nombre = nombre
        self.descripcion = descripcion

    def get_ID(self):
        return self.id_lugar

    def get_nombre(self):
        return self.nombre

    def get_descripcion(self):
        return self.descripcion