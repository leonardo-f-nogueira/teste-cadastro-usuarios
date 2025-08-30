import unittest
from unittest.mock import patch
from cadastro import cadastrar_usuario

class TestCadastroUsuario(unittest.TestCase):

    @patch('email_service.enviar_email_boas_vindas')
    def test_cadastro_deve_chamar_servico_de_email(self, mock_enviar_email):

        print("\nExecutando teste: O cadastro deve chamar o serviço de e-mail...")

        mock_enviar_email.return_value = True

        nome = "John Doe"
        email = "john.doe@example.com"
        cadastrar_usuario(nome, email, "password123")

        mock_enviar_email.assert_called_once_with(email)

        print("Teste concluído com sucesso!")

if __name__ == '__main__':
    unittest.main()