from flask_restx import Namespace, Resource, fields
from flask import request
from services.usuario_service import UsuarioService

usuario_ns = Namespace('usuarios', description='Operaciones relacionadas con usuarios')

usuario_model = usuario_ns.model('Usuario', {
    'nombre': fields.String(required=True, description='Nombre del usuario'),
    'correo': fields.String(required=True, description='Correo del usuario'),
    'rol': fields.String(required=True, description='Rol del usuario')
})

@usuario_ns.route('/')
class UsuarioList(Resource):
    @usuario_ns.doc('listar_usuarios')
    def get(self):
        """Listar todos los usuarios"""
        return UsuarioService.listar_usuarios()

    @usuario_ns.expect(usuario_model)
    @usuario_ns.doc('crear_usuario')
    def post(self):
        """Crear un nuevo usuario"""
        data = request.json
        return UsuarioService.crear_usuario(data)

@usuario_ns.route('/<int:id>')
@usuario_ns.response(404, 'Usuario no encontrado')
class Usuario(Resource):
    @usuario_ns.doc('eliminar_usuario')
    def delete(self, id):
        """Eliminar un usuario por su ID"""
        UsuarioService.eliminar_usuario(id)
        return {"message": "Usuario eliminado correctamente"}
