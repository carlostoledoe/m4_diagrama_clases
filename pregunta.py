from alternativa import Alternativa

class Pregunta():
    def __init__(self, enunciado:str, ayuda:str, requerido:bool, lista_alternativas:list):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.lista_alternativas = [
            Alternativa(a['contenido'], a['ayuda']) for a in lista_alternativas
        ]
        self.requerido = requerido