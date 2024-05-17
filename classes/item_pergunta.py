import pygame
from .colecao_itens import ColecaoItens

class ItemPergunta(pygame.Rect):

    def __init__(self, posicao_x, posicao_y, width, height):
        super().__init__(posicao_x, posicao_y, width, height)

    @staticmethod
    def gerar_imagem():
        IMG_ITEM_PERGUNTA = pygame.image.load("imagens/quiz_item.png")
        IMG_ITEM_PERGUNTA = pygame.transform.scale(IMG_ITEM_PERGUNTA, (50, 50))
        return IMG_ITEM_PERGUNTA
    
class ItensPergunta(ColecaoItens):
    def __init__(self):
        super().__init__(2000)
    