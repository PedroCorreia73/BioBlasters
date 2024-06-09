import pygame
import random
from .colecao_itens import ColecaoItens

class ItemPergunta(pygame.Rect):

    WIDTH = 35
    HEIGHT = 35
    VEL = 5

    def __init__(self, posicao_x, posicao_y, width, height):
        super().__init__(posicao_x, posicao_y, width, height)

    @staticmethod
    def gerar_imagem():
        IMG_ITEM_PERGUNTA = pygame.image.load("imagens/quiz_item.png")
        IMG_ITEM_PERGUNTA = pygame.transform.scale(IMG_ITEM_PERGUNTA, (50, 50))
        return IMG_ITEM_PERGUNTA
    
class ItensPergunta(ColecaoItens):
    def __init__(self):
        super().__init__(5000)
    def mover(self,nave):
        for item_pergunta in self.itens():
            item_pergunta.x -= ItemPergunta.VEL
            if item_pergunta.x < 0 - ItemPergunta.WIDTH - 30:
                self.remove(item_pergunta)
            if item_pergunta.colliderect(nave):
                self.remove(item_pergunta)
                nave.pegou_item_pergunta = True
    def gerar(self, tela):
        if self.contagem > self.add_increment:
            item_pergunta_y = random.randint(0, tela.HEIGHT - ItemPergunta.HEIGHT)
            item_pergunta = ItemPergunta(tela.WIDTH, item_pergunta_y, ItemPergunta.WIDTH, ItemPergunta.HEIGHT)
            self.append(item_pergunta)
            #item_pergunta_add_increment = max(200, item_pergunta_add_increment - 50)
            self.contagem = 0

    