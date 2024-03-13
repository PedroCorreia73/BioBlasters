import pygame
from Botao import Botao

def tela_inicial(WIDTH, HEIGHT):
    superficie = pygame.Surface((WIDTH,HEIGHT))
    superficie.blit(superficie)
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
                break
        

def menu():
    pass