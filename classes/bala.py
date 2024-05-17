import pygame
from .colecao_itens import ColecaoItens


class Bala(pygame.Rect):
    WIDTH = 20
    HEIGHT = 10
    VEL = 6

    def __init__(self, posicao_x, posicao_y, width, height):
        super().__init__(posicao_x, posicao_y, width, height)

class Balas(ColecaoItens):
    def __init__(self):
        super().__init__(None)
