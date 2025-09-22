class RolesModel:
   def __init__(self, id_rol : int , nombre : str, descripcion : str):      
      
      self.__id_rol = id_rol
      self.__nombre = nombre
      self.__descripcion = descripcion

   def get_id_rol(self)->int:
      return self.__id_rol
      
   def set_id_rol(self, rol):
      self.__id_rol=rol

   def get_nombre(self)->str:
      return self.__nombre
   
   def set__(self, nombre: str):
      self.__nombre = nombre
   
   def get_descripcion(self)-> str:
      return self.__descripcion
   
   def set_descipcion(self, descripcion: str):
      self.__descripcion = descripcion

   def serializar(self)-> dict:
      return {
         "id_rol": self.get_id_rol(),
         "nombre": self.get_nombre(),
         "descripcion" : self.get_descripcion()
      }

   @staticmethod
   def deserializar(data_roles : dict)-> "RolesModel":
      return RolesModel(
         id_rol = data_roles.get("id_rol"),
         nombre = data_roles.get("nombre"),
         descripcion = data_roles.get("descripcion")
      )