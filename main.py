from src.microphone import inicializar_microfone
from src.recognizer import reconhecer_fala
from src.commands import executar_comando
import logging

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')

def ouvir_microfone():
    recognizer, audio = inicializar_microfone()
    frase = reconhecer_fala(recognizer, audio)
    if frase:
        return executar_comando(frase)
    return False

# Loop principal
if __name__ == "__main__":
    while True:
        if ouvir_microfone():
            break
