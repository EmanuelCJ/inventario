from ..DAO.auditorias_DAO import AuditoriaDAO

class AuditoriaService:
    
    @staticmethod
    def registrar(entidad, id_entidad, accion, descripcion, id_admin):
        return AuditoriaDAO.registrar(entidad, id_entidad, accion, descripcion, id_admin)
