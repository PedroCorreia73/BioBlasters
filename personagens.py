import pygame

def criar_inimigos():
    INIMIGOS = pygame.image.load("imagens/sprite_enemy.png")
    INIMIGOS = pygame.transform.scale(INIMIGOS, (50, 50))
    return INIMIGOS

def criar_nave(PLAYER_WIDTH, PLAYER_HEIGHT):
    NAVE_imagem = pygame.image.load("imagens/sprites_ship.png")
    NAVE = pygame.transform.scale(NAVE_imagem, (PLAYER_WIDTH + 10, PLAYER_HEIGHT + 10))
    return NAVE

def gerar_personagens(PLAYER_WIDTH, PLAYER_HEIGHT):
    INIMIGOS = criar_inimigos()
    NAVE = criar_nave(PLAYER_WIDTH, PLAYER_HEIGHT)
    return INIMIGOS, NAVE