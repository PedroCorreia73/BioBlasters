import pygame

def criar_background_jogo():
    BG = pygame.image.load("imagens/bg_start_v3.png").convert_alpha()
    #BG = pygame.image.load("imagens/bgbg.png").convert_alpha()
    return BG