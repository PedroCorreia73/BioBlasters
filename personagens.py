import pygame

def criar_covid():
    COVID_imagem = pygame.image.load("imagens/covid.png")
    COVID = pygame.transform.scale(COVID_imagem, (50, 50))
    return COVID

def criar_nave(PLAYER_WIDTH, PLAYER_HEIGHT):
    NAVE_imagem = pygame.image.load("imagens/nave.png")
    NAVE = pygame.transform.scale(NAVE_imagem, (PLAYER_WIDTH + 10, PLAYER_HEIGHT + 10))
    return NAVE

def gerar_personagens(PLAYER_WIDTH, PLAYER_HEIGHT):
    COVID = criar_covid()
    NAVE = criar_nave(PLAYER_WIDTH, PLAYER_HEIGHT)
    return COVID, NAVE