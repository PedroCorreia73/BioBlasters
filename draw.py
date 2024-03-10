import pygame

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