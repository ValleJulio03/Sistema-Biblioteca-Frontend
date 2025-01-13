from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    @staticmethod
    def listar_usuarios():
        return [usuario.serialize() for usuario in UsuarioRepository.get_all()]

    @staticmethod
    def crear_usuario(data):
        return UsuarioRepository.create(data)

    @staticmethod
    def eliminar_usuario(usuario_id):
        UsuarioRepository.delete(usuario_id)
