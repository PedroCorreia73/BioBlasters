import pygame

def tela():
    pygame.font.init() #inicializar o font module (sem isso não dá para usar fontes)
    pygame.display.init() # inicializar a tela (serve para poder obter as medidas da tela do usuário)
    #WIDTH, HEIGHT = pygame.display.get_desktop_sizes()[0] #obtém as medidas da tela do usuário
    WIDTH, HEIGHT = 1200, 600
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Nome do Jogo")
    FONT = pygame.font.SysFont("comicsans", 30) #tipo e tamanho da fonte estocada na variável FONT
    return WIN, FONT

def draw(player, elapsed_time, obstaculos, FONT, WIN, NAVE, PLAYER_VEL, COVID):
    time_text = FONT.render(f"Tempo: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    #rotação da nave e carregamento da imagem na tela
    NAVE2 = pygame.transform.rotate(NAVE, -PLAYER_VEL * 10)
    WIN.blit(NAVE2, (player.x - 10, player.y - 10))

    #pygame.draw.rect(WIN, "green", player) #hitbox do player

    for obstaculo in obstaculos:
        #pygame.draw.rect(WIN, "yellow", obstaculo) #hitbox dos obstáculos
        WIN.blit(COVID, (obstaculo.x - 8, obstaculo.y -8))
    pygame.display.update()