class Usuario:
    def __init__(self, nome, senha, id_grupo = None):
        self._nome = nome
        self._senha = senha
        self._id_grupo = id_grupo
   
    @property
    def id(self):
        return self._id
    @property
    def nome(self):
        return self._nome
    @property
    def senha(self):
        return self._senha
    @property
    def pontuacao(self):
        return self._pontuacao
    @pontuacao.setter
    def pontuacao(self, nova_pontuacao):
        self._pontuacao = nova_pontuacao