import pygame
from tela import tela
from Botao import Botao

def tela_inicial(WIDTH, HEIGHT):
    WIN, _ = tela()
    superficie = pygame.Surface((WIDTH,HEIGHT))
    superficie.fill((0,0,0))
    superficie.set_colorkey((255,255,255))
    WIN.blit(superficie, (WIDTH, HEIGHT))
    iniciar_imagem = pygame.image.load("imagens/start.png")
    run = True
    while run:
        iniciar = Botao(WIDTH / 2, HEIGHT / 2, iniciar_imagem , 15)
        iniciar.draw(superficie)
        if iniciar.clicked == True:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return run
    return True

def menu():
    pass