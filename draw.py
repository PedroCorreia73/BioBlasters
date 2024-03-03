from jogo import *
import pygame

def draw(player, elapsed_time, obstaculos):
    time_text = FONT.render(f"Tempo: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    #rotação da nave e carregamento da imagem na tela
    NAVE2 = pygame.transform.rotate(NAVE, -PLAYER_VEL * 10)
    WIN.blit(NAVE2, (player.x, player.y))

    # pygame.draw.rect(WIN, "green", player)

    for obstaculo in obstaculos:
        # pygame.draw.rect(WIN, "yellow", obstaculo)
        WIN.blit(COVID, (obstaculo.x, obstaculo.y))
    pygame.display.update()