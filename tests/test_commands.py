import unittest
from unittest.mock import patch, mock_open
import json
from src.commands import executar_comando

class TestCommands(unittest.TestCase):

    @patch('src.commands.os.system')
    def test_executar_comando(self, mock_os_system):
        frase = "navegador"
        with patch('builtins.open', mock_open(read_data='{"navegador": "start Chrome.exe"}')):
            result = executar_comando(frase)
        
        mock_os_system.assert_called_once_with("start Chrome.exe")
        self.assertFalse(result)

    @patch('src.commands.os.system')
    def test_executar_comando_fechar(self, mock_os_system):
        frase = "Fechar"
        with patch('builtins.open', mock_open(read_data='{"Fechar": "Exit"}')):
            result = executar_comando(frase)
        
        mock_os_system.assert_called_once_with("Exit")
        self.assertTrue(result)

    @patch('src.commands.os.system')
    def test_executar_comando_nao_reconhecido(self, mock_os_system):
        frase = "comando desconhecido"
        with patch('builtins.open', mock_open(read_data='{"navegador": "start Chrome.exe"}')):
            result = executar_comando(frase)
        
        mock_os_system.assert_not_called()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
