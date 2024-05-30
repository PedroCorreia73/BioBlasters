from banco_de_dados.pergunta import PerguntaAlternativasDAO

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
    def obter_pergunta(self):
        pass
    def gerar_pergunta(self):
        pass
class Perguntas:
    def __init__(self, id_grupo):
        self.id_grupo = id_grupo
        self.obter_id_perguntas()
    
    def obter_id_perguntas(self):
        lista_tuplas = PerguntaAlternativasDAO.obter_ids_perguntas(self.id_grupo)
        lista_ids = []
        for item in lista_tuplas:
            lista_ids.append(item[0])
        self.id_perguntas = lista_ids