import speech_recognition as sr
import logging

def reconhecer_fala(recognizer, audio):
    try:
        frase = recognizer.recognize_google(audio, language='pt-BR')
        logging.info(f"Frase reconhecida: {frase}")
        print("Você disse: " + frase)
        return frase
    except sr.UnknownValueError:
        logging.error("Não entendi o que você disse.")
        print("Não entendi o que você disse.")
    except sr.RequestError:
        logging.error("Não foi possível completar a requisição ao Google.")
        print("Não foi possível completar a requisição ao Google.")
    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")
        print(f"Ocorreu um erro: {e}")
    return None
