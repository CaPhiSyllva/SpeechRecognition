import unittest
from unittest.mock import patch, MagicMock
from src.microphone import inicializar_microfone

class TestMicrophone(unittest.TestCase):

    @patch('src.microphone.sr.Microphone')
    @patch('src.microphone.sr.Recognizer')
    def test_inicializar_microfone(self, MockRecognizer, MockMicrophone):
        mock_recognizer_instance = MockRecognizer.return_value
        mock_audio = MagicMock()
        mock_recognizer_instance.listen.return_value = mock_audio
        
        recognizer, audio = inicializar_microfone()
        
        self.assertEqual(recognizer, mock_recognizer_instance)
        self.assertEqual(audio, mock_audio)
        mock_recognizer_instance.adjust_for_ambient_noise.assert_called_once()

if __name__ == '__main__':
    unittest.main()
