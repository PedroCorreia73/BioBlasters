import pygame
import time
import random
import math

pygame.font.init()

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nome do Jogo")



PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
PLAYER_VEL = 0
VEL_TERMINAL = 5
GRAVITY = 12 / FPS

COVID_imagem = pygame.image.load("covid.png")
NAVE_imagem = pygame.image.load("nave.png")
COVID = pygame.transform.scale(COVID_imagem, (50, 50))
NAVE = pygame.transform.scale(NAVE_imagem, (PLAYER_WIDTH + 10, PLAYER_HEIGHT + 10))
BG = pygame.image.load("background espaço.jpg")
BG_WIDTH = BG.get_width()
BG_HEIGHT = BG.get_height()
scroll = 0
tiles = math.ceil(WIDTH / BG_WIDTH) + 1

FONT = pygame.font.SysFont("comicsans", 30)

OBSTACULO_WIDTH = 10
OBSTACULO_HEIGHT = 10
OBSTACULO_VEL = 5


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


# def main():

run = True

player = pygame.Rect(PLAYER_WIDTH + 200, 400, PLAYER_WIDTH, PLAYER_HEIGHT)

clock = pygame.time.Clock()

start_time = time.time()
elapsed_time = 0

obstaculo_add_increment = 20  # 2000 milisegundos
obstaculo_count = 0

obstaculos = []
hit = False

while run:

    # loop da tela---------
    for i in range(0, tiles):
        WIN.blit(BG, (i * BG_WIDTH + scroll, 0))
    scroll -= 0.5
    if abs(scroll) > BG_WIDTH:
        scroll = 0
    # ---------------------

    obstaculo_count += clock.tick(FPS)
    elapsed_time = time.time() - start_time

    if obstaculo_count > obstaculo_add_increment:
        for _ in range(1):
            obstaculo_y = random.randint(0, HEIGHT - OBSTACULO_HEIGHT)
            obstaculo = pygame.Rect(WIDTH, obstaculo_y, OBSTACULO_WIDTH, OBSTACULO_HEIGHT)
            obstaculos.append(obstaculo)
        obstaculo_add_increment = max(200, obstaculo_add_increment - 50)
        obstaculo_count = 0

    # fechar o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    # -------------

    # comandos da nave
    keys = pygame.mouse.get_pressed()

    # if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
    # player.x -= (PLAYER_VEL - 3)
    # if keys[pygame.K_d] and player.x + PLAYER_VEL + player.width <= WIDTH:
    # player.x += PLAYER_VEL
    # if keys[pygame.K_w] and player.y - PLAYER_VEL >= 0:
    # player.y -= PLAYER_VEL
    # if keys[pygame.K_s] and player.y + PLAYER_VEL + player.height <= HEIGHT:
    # player.y += PLAYER_VEL
    if keys[0] and player.y - PLAYER_VEL >= 0:
        if PLAYER_VEL > -VEL_TERMINAL:
            PLAYER_VEL -= GRAVITY
    else:
        if PLAYER_VEL < VEL_TERMINAL:
            PLAYER_VEL += GRAVITY

    if player.y + PLAYER_HEIGHT * 1.5 >= HEIGHT:
        if keys[0]:
            PLAYER_VEL -= GRAVITY
        else:
            PLAYER_VEL = 0
            player.y = HEIGHT - PLAYER_HEIGHT * 1.5
    elif player.y <= 0:
        PLAYER_VEL = 1
    player.y += PLAYER_VEL


    # -----------------

    for obstaculo in obstaculos[:]:
        obstaculo.x -= OBSTACULO_VEL
        if obstaculo.x < 0 - OBSTACULO_WIDTH - 30:
            obstaculos.remove(obstaculo)
        if obstaculo.colliderect(player):
            obstaculos.remove(obstaculo)
            hit = True
            break

    if hit:
        lost_text = FONT.render("Você perdeu!", 1, "blue")
        WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(1000)  # 1000 milisegundos
        break

    draw(player, elapsed_time, obstaculos)

pygame.quit


# if name == "main":
# main()