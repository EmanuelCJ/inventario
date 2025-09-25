class Auditoria:
    def __init__(self, id_auditoria, entidad, id_entidad, accion, descripcion, id_usuario, fecha=None):
        self.id_auditoria = id_auditoria
        self.entidad = entidad
        self.id_entidad = id_entidad
        self.accion = accion
        self.descripcion = descripcion
        self.id_usuario = id_usuario
        self.fecha = fecha

    
    def serializar(self):
        return {
            "id_auditoria": self.id_auditoria,
            "entidad": self.entidad,
            "id_entidad": self.id_entidad,
            "accion": self.accion,
            "descripcion": self.descripcion,
            "id_usuario": self.id_usuario,
            "fecha": self.fecha,
        }
