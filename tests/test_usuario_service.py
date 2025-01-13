import unittest
from unittest.mock import patch
from services.usuario_service import UsuarioService

class TestUsuarioService(unittest.TestCase):
    @patch('repositories.usuario_repository.UsuarioRepository.get_all')
    def test_listar_usuarios(self, mock_get_all):
        mock_get_all.return_value = [
            {"id": 1, "nombre": "Juan", "correo": "juan@example.com", "rol": "admin"}
        ]
        resultado = UsuarioService.listar_usuarios()
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]['nombre'], "Juan")

    @patch('repositories.usuario_repository.UsuarioRepository.create')
    def test_crear_usuario(self, mock_create):
        data = {"nombre": "Carlos", "correo": "carlos@example.com", "rol": "user"}
        mock_create.return_value = data
        resultado = UsuarioService.crear_usuario(data)
        self.assertEqual(resultado['nombre'], "Carlos")

if __name__ == "__main__":
    unittest.main()
