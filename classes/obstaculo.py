from pygame import Rect

class Obstaculo(Rect):

    WIDTH = 35
    HEIGHT = 35
    VEL = 5

    def __init__(self, posicao_x, posicao_y):
        self.x = posicao_x
        self.y = posicao_y
        super().__init__(self.x, self.y, self.WIDTH, self.HEIGHT)

class Obstaculos:
    obstaculos = []
    @classmethod
    def append(cls, obstaculo):
        cls.obstaculos.append(obstaculo)
    @classmethod
    def remove(cls, obstaculo):
        cls.obstaculos.remove(obstaculo)
    @classmethod
    def __getitem__(cls, indice):
        return cls.obstaculos[indice]
    @classmethod
    def itens(cls):
        return cls.obstaculos
