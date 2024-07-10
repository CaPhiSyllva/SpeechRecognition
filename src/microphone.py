import speech_recognition as sr

def inicializar_microfone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Diga alguma coisa:")
        audio = recognizer.listen(source)
    return recognizer, audio
