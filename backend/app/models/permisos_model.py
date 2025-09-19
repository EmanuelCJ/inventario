
class PermisosModel:
    
    def __init__(self, id_permisos: int, nombre : str , descripcion : str):
        self.__id_permisos = id_permisos
        self.__nombre = nombre
        self.__descripcion = descripcion

    def get_id_permisos(self)-> int :
        return self.__id_permisos
   
    def set_id_permisos(self, id_permiso: int):
        self.__id_permisos = id_permiso
    
    def get_nombre(self)->str:
        return self.__nombre
   
    def set_nombre(self, nombre : str):
        self.__nombre = nombre

    def get_de(self)->str:
        return self.__descripcion
   
    def set_descripcion(self, descripcion: str):
        self.__descripcion = descripcion