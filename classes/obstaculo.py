import pygame 
import random
from .colecao_itens import ColecaoItens

class Obstaculo(pygame.Rect):

    WIDTH = 35
    HEIGHT = 0
    HEIGHT1 = 35
    HEIGHT2 = 80
    VEL = 5

    def __init__(self, posicao_x, posicao_y, tipo):
        self.tipo = tipo
        if tipo == 1:
            super().__init__(posicao_x, posicao_y, self.WIDTH, self.HEIGHT1)
        else:
            super().__init__(posicao_x, posicao_y, self.WIDTH, self.HEIGHT2)



    def gerar_imagem(self):
        if self.tipo == 1:
            IMG_INIMIGO = pygame.image.load("imagens/sprite_enemy.png")
            IMG_INIMIGO = pygame.transform.scale(IMG_INIMIGO, (50, 50))
        else:
            IMG_INIMIGO = pygame.image.load("imagens/sprite_enemy2.png")
            IMG_INIMIGO = pygame.transform.scale(IMG_INIMIGO, (50, 100))
        return IMG_INIMIGO
    

class Obstaculos(ColecaoItens):
    def __init__(self):
        super().__init__(200)

    def mover(self, nave):
        for obstaculo in self.itens():
            obstaculo.x -= Obstaculo.VEL
            if obstaculo.x < 0 - Obstaculo.WIDTH - 30:
                self.remove(obstaculo)
            if obstaculo.colliderect(nave) and not nave.invencibilidade:
                self.remove(obstaculo)
                nave.colidiu_obstaculo = True
                break
    def gerar(self, tela):
        tipo_aux = random.randint(1, 10)
        if 1 <= tipo_aux <= 7: #70% de chance de ser o vírus vermelho
            self.tipo = 1
        else:                  #30% de chance de ser o vírus roxo
            self.tipo = 2
        if self.contagem > self.add_increment: #tempo entre um obstáculo e o próximo obstáculo
            if self.tipo == 1:
                obstaculo_y = random.randint(0, tela.HEIGHT - Obstaculo.HEIGHT1) #criando o local no eixo y no qual o obtáculo surgirá
            else:
                obstaculo_y = random.randint(0, tela.HEIGHT - Obstaculo.HEIGHT2)
            obstaculo = Obstaculo(tela.WIDTH, obstaculo_y, self.tipo)
            self.append(obstaculo)
            self.add_increment = max(200, self.add_increment - 50)
            self.contagem = 0
        return self.tipo