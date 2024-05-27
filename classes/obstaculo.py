import pygame 
import random
from .colecao_itens import ColecaoItens

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
        if self.contagem > self.add_increment: #tempo entre um obstáculo e o próximo obstáculo
            obstaculo_y = random.randint(0, tela.HEIGHT - Obstaculo.HEIGHT) #criando o local no eixo y no qual o obtáculo surgirá
            obstaculo = Obstaculo(tela.WIDTH, obstaculo_y)
            self.append(obstaculo)
            self.add_increment = max(200, self.add_increment - 50)
            self.contagem = 0