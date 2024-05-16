import pygame 
class Obstaculo(pygame.Rect):

    WIDTH = 35
    HEIGHT = 35
    VEL = 5

    def __init__(self, posicao_x, posicao_y):
        super().__init__(posicao_x, posicao_y, self.WIDTH, self.HEIGHT)

    @staticmethod
    def gerar_imagem():
        IMG_INIMIGO = pygame.image.load("imagens/sprite_enemy.png")
        IMG_INIMIGO = pygame.transform.scale(IMG_INIMIGO, (50, 50))
        return IMG_INIMIGO
    

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
