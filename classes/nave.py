import pygame
import time
from classes.jogo import Jogo

class Nave(pygame.Rect):

    def __init__(self):
        self.vel = 0
        self.WIDTH = 35
        self.HEIGHT = 35
        self.hp = 20
        self.invencibilidade = False
        self.aux_inv = 100
        self.colidiu_obstaculo = False
        self.pegou_item_pergunta = False
        self.mochila_balas = [1, 1]
        super().__init__(self.WIDTH + 200, 400, self.WIDTH, self.HEIGHT)
    
    def gerar_imagem(self):
        NAVE_imagem = pygame.image.load("imagens/sprites_ship.png")
        NAVE_imagem = pygame.transform.scale(NAVE_imagem, (self.WIDTH + 15, self.HEIGHT + 15))
        return NAVE_imagem
    
    def mover(self, tela, keys_mouse):
        #--borda de cima--
        if self.y <= 10:
            if keys_mouse[0] or self.vel < 0:
                self.vel = 0
                self.y = 10
            else:
                self.vel += Jogo.GRAVIDADE
        #--borda de baixo--
        elif self.y + self.HEIGHT * 1.5 >= tela.HEIGHT:
            if keys_mouse[0] and self.vel <= 0:
                self.vel -= Jogo.GRAVIDADE
            else:
                self.vel = 0
                self.y = tela.HEIGHT - self.HEIGHT * 1.2
        #--entre as bordas--
        elif keys_mouse[0] and self.y - self.vel >= 0:
            if self.vel > -Jogo.VEL_TERMINAL:
                self.vel -= Jogo.GRAVIDADE
        else:
            if self.vel < Jogo.VEL_TERMINAL:
                self.vel += Jogo.GRAVIDADE
        self.y += self.vel



    def colidir(self, tela):
        if self.colidiu_obstaculo:
            if not self.invencibilidade:
                self.hp -= 10
                self.invencibilidade = True
                self.tempo_invencibilidade = time.time() + 2
            self.colidiu_obstaculo = False
        if self.invencibilidade and time.time() > self.tempo_invencibilidade:
            self.invencibilidade = False
            self.aux_inv = 10
        if self.invencibilidade:
            self.aux_inv += 1
        if self.hp <= 0:
            return False
        return True