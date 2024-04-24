import pygame
from Botao import Botao

def tela_inicial(WIN :pygame.Surface):
    BG_INICIO = pygame.image.load("imagens/bg_inicial.png")
    WIN.blit(pygame.transform.scale(BG_INICIO, (WIN.get_width(), WIN.get_height())), (0, 0))
    print(WIN.get_size())
    pygame.display.update()
    #iniciar_imagem = pygame.image.load("imagens/start.png")
    run = True
    
    while run:
        #iniciar = Botao(WIDTH / 2, HEIGHT / 2, iniciar_imagem , 15)
        #iniciar.draw(BG_INICIO)
        
        #if iniciar.clicked == True:
        if pygame.mouse.get_pressed()[0] == True:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return run
        pygame.display.flip()
    return True

def menu():
    pass