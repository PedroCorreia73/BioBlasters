import pygame
import random
def criar_item_pergunta():
    IMG_ITEM_PERGUNTA = pygame.image.load("imagens/quiz_item.png")
    IMG_ITEM_PERGUNTA = pygame.transform.scale(IMG_ITEM_PERGUNTA, (50, 50))
    return IMG_ITEM_PERGUNTA

def criar_inimigos():
    IMG_INIMIGO = pygame.image.load("imagens/sprite_enemy.png")
    IMG_INIMIGO = pygame.transform.scale(IMG_INIMIGO, (50, 50))
    return IMG_INIMIGO

def criar_nave(PLAYER_WIDTH, PLAYER_HEIGHT):
    NAVE_imagem = pygame.image.load("imagens/sprites_ship.png")
    NAVE = pygame.transform.scale(NAVE_imagem, (PLAYER_WIDTH + 15, PLAYER_HEIGHT + 15))
    return NAVE

def gerar_personagens(PLAYER_WIDTH, PLAYER_HEIGHT):
    IMG_INIMIGO = criar_inimigos()
    NAVE = criar_nave(PLAYER_WIDTH, PLAYER_HEIGHT)
    IMG_ITEM_PERGUNTA = criar_item_pergunta()

    return IMG_ITEM_PERGUNTA, IMG_INIMIGO, NAVE