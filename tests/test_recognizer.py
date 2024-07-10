import unittest
from unittest.mock import patch, MagicMock
from src.recognizer import reconhecer_fala
import speech_recognition as sr

class TestRecognizer(unittest.TestCase):

    @patch('src.recognizer.sr.Recognizer.recognize_google')
    def test_reconhecer_fala(self, mock_recognize_google):
        mock_recognize_google.return_value = "navegador"
        recognizer = sr.Recognizer()
        audio = MagicMock()
        
        frase = reconhecer_fala(recognizer, audio)
        
        self.assertEqual(frase, "navegador")
        mock_recognize_google.assert_called_once_with(audio, language='pt-BR')

    @patch('src.recognizer.sr.Recognizer.recognize_google', side_effect=sr.UnknownValueError)
    def test_reconhecer_fala_unknown_value_error(self, mock_recognize_google):
        recognizer = sr.Recognizer()
        audio = MagicMock()
        
        frase = reconhecer_fala(recognizer, audio)
        
        self.assertIsNone(frase)

    @patch('src.recognizer.sr.Recognizer.recognize_google', side_effect=sr.RequestError)
    def test_reconhecer_fala_request_error(self, mock_recognize_google):
        recognizer = sr.Recognizer()
        audio = MagicMock()
        
        frase = reconhecer_fala(recognizer, audio)
        
        self.assertIsNone(frase)

if __name__ == '__main__':
    unittest.main()
