import pygame
from .colecao_itens import ColecaoItens
from .obstaculo import Obstaculo

class Bala(pygame.Rect):
    aux_bala = 0
    WIDTH = 20
    HEIGHT = 10
    VEL = 6

    def __init__(self, posicao_x, posicao_y, width, height):
        super().__init__(posicao_x, posicao_y, width, height)

class Balas(ColecaoItens):
    def __init__(self):
        super().__init__(None)
    def mover(self, tela):
        for bala in self.itens():
            bala.x += Bala.VEL
            #bala.x += Bala.VEL * math.cos(math.radians(-vel_player_atual * 10) * 1.5)
            #bala.y += Bala.VEL * math.sin(math.radians(+vel_player_atual * 10) * 1.5)
            if bala.x > tela.WIDTH:
                self.remove(bala)
    def gerar(self, nave,keys_teclado):
        if keys_teclado[pygame.K_SPACE] and Bala.aux_bala == 0:
            Bala.aux_bala = 1
            if 1 in nave.mochila_balas and Bala.aux_bala == 1:
                bala = Bala(nave.x + 30, nave.y + 15, Bala.WIDTH, Bala.HEIGHT)
                #bala = pygame.Rect(nave.x + 30 - math.cos(math.radians(-vel_player_atual * 10)) * 10, nave.y + 15 - math.sin(math.radians(-vel_player_atual * 10)) * 15, Bala.WIDTH, Bala.HEIGHT)
                self.append(bala)
                nave.mochila_balas.remove(1)
    def colidir(self, obstaculos):
        for bala in self.itens():
            for obstaculo in obstaculos.itens():
                if bala.y in range(obstaculo.y - 15, obstaculo.y + Obstaculo.HEIGHT + 5) and bala.x in range(obstaculo.x - 5, obstaculo.x + Obstaculo.WIDTH):
                    obstaculos.remove(obstaculo)
