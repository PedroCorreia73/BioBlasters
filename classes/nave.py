import pygame

class Nave(pygame.Rect):

    def __init__(self):
        self.vel = 0
        self.WIDTH = 35
        self.HEIGHT = 35
        self.hp = 100
        self.invencibilidade = False
        self.colidiu_obstaculo = False
        self.pegou_item_pergunta = False
        super().__init__(self.WIDTH + 200, 400, self.WIDTH, self.HEIGHT)
    
    def gerar_imagem(self):
        NAVE_imagem = pygame.image.load("imagens/sprites_ship.png")
        NAVE_imagem = pygame.transform.scale(NAVE_imagem, (self.WIDTH + 15, self.HEIGHT + 15))
        return NAVE_imagem