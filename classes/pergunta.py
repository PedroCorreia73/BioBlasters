

class Pergunta:
    def __init__(self, pergunta):
        self.alternativas = []
        for item in pergunta:
            if pergunta[item] == "correta":
                self.correta = pergunta[item]
                continue
            elif pergunta[item] == "enunciado":
                self.enunciado = pergunta[item]
            self.alternativas.append(pergunta[item])
    def obter_pergunta():
        pass
    def __str__():
        pass
