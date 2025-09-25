# service va la logica de negocio
from ..DAO.usuario_DAO import UsuarioDAO
from ..services.auditoria_service import AuditoriaService

class UsuarioService:
    
    @staticmethod
    def crear_usuario(data_usuario:dict) -> int:
        return UsuarioDAO.create_usuario(datos_user = data_usuario)

    @staticmethod
    def actualizar_usuario(id_usuario, nombre, email, rol, admin_id):
        filas = UsuarioDAO.update_usuario(id_usuario, nombre, email, rol)

        if filas > 0:
            AuditoriaService.registrar(
                entidad="usuario",
                id_entidad=id_usuario,
                accion="update",
                descripcion=f"El admin {admin_id} modificó al usuario {id_usuario}",
                id_usuario=admin_id
            )
        return filas