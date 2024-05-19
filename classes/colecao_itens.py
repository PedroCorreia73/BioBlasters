from abc import abstractmethod, ABCMeta

class ColecaoItens(metaclass=ABCMeta):
    def __init__(self, add_increment):
        self.colecao = []
        self.contagem = 0
        self.add_increment = add_increment # em milissegundos
    def append(self, obstaculo):
        self.colecao.append(obstaculo)
    def remove(self, obstaculo):
        self.colecao.remove(obstaculo)
    def itens(self):
        return self.colecao
    
    @abstractmethod
    def mover(self):
        pass