class Pontuacao:
    def __init__(self):
        self.pontuacao = 0
        self.tempo = 0
        self.ganha = 0


    @property
    def atual(self):
        return self.pontuacao
    @atual.setter
    def atual(self, nova_pontuacao):
        self.pontuacao = nova_pontuacao