import os
import json

with open('config.json', 'r') as f:
    comandos = json.load(f)

def executar_comando(frase):
    for comando, acao in comandos.items():
        if comando in frase:
            os.system(acao)
            return comando == "Fechar"
    return False
