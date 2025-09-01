class UsuarioModel:
    __id_usuario: int
    __nombre: str
    __apellido: str
    __rol: str
    __contrasena: str

    def __init__(self, id_usuario: int, nombre: str, apellido: str, rol: str, contrasena: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol
        self.contrasena = contrasena

    def _get_ID(self):
        return self.id_usuario
    
    def _get_nombre(self):
        return self.nombre
    
    def _get_apellido(self):
        return self.apellido
    
    def _get_Rol(self):
        return self.rol

    def _set_Rol(self, rol: str):
        self.rol = rol
     
    def _get_contrasena(self):
        return self.contrasena

    def _set_contrasena(self, contrasena: str):
        self.contrasena = contrasena