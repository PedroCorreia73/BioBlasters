import pygame
import time
import random
import math
from menus import tela_inicial
from tela import tela, draw
from constantes import *
from background import criar_background_jogo
from personagens import gerar_personagens



WIN , FONT = tela() # inicializa a tela com as medidas da tela do usuário
WIDTH, HEIGHT = WIN.get_width(), WIN.get_height()
BG = criar_background_jogo()
BG_WIDTH, BG_HEIGHT = BG.get_width(), BG.get_height()
run = tela_inicial(WIDTH, HEIGHT)

scroll = 0
tiles = math.ceil(WIDTH / BG_WIDTH) + 1

COVID, NAVE = gerar_personagens(PLAYER_WIDTH, PLAYER_HEIGHT)



player = pygame.Rect(PLAYER_WIDTH + 200, 400, PLAYER_WIDTH, PLAYER_HEIGHT)

clock = pygame.time.Clock()

start_time = time.time() #tempo que se passou desde a epoch
elapsed_time = 0

obstaculo_add_increment = 200  # 200 milisegundos
obstaculo_count = 0
obstaculos = []

hit_obstaculo = False

while run:

    # loop da tela---------
    for i in range(0, tiles):
        WIN.blit(BG, (i * BG_WIDTH + scroll, 0))
    scroll -= 0.5
    if abs(scroll) > BG_WIDTH:
        scroll = 0
    # ---------------------

    obstaculo_count += clock.tick(FPS) #limitação de FPS
    elapsed_time = time.time() - start_time #tempo que se passou desde que o jogo começou

    #Sistema de spawn de obstáculos
    if obstaculo_count > obstaculo_add_increment: #tempo entre um obstáculo e o próximo obstáculo
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
    

    #--borda de cima--
    if player.y <= 10:
        if keys[0] or PLAYER_VEL < 0:
            PLAYER_VEL = 0
            player.y = 10
        else:
            PLAYER_VEL += GRAVITY
    #--borda de baixo--
    elif player.y + PLAYER_HEIGHT * 1.5 >= HEIGHT:
        if keys[0] and PLAYER_VEL <= 0:
            PLAYER_VEL -= GRAVITY
        else:
            PLAYER_VEL = 0
            player.y = HEIGHT - PLAYER_HEIGHT * 1.2
    #--entre as bordas--
    elif keys[0] and player.y - PLAYER_VEL >= 0:
        if PLAYER_VEL > -VEL_TERMINAL:
            PLAYER_VEL -= GRAVITY
    else:
        if PLAYER_VEL < VEL_TERMINAL:
            PLAYER_VEL += GRAVITY
    player.y += PLAYER_VEL
    # -----------------

    #movimentação de obstáculos
    for obstaculo in obstaculos[:]:
        obstaculo.x -= OBSTACULO_VEL
        if obstaculo.x < 0 - OBSTACULO_WIDTH - 30:
            obstaculos.remove(obstaculo)
        if obstaculo.colliderect(player):
            obstaculos.remove(obstaculo)
            hit_obstaculo = True
            break
    
    #hit de obstáculos
    if hit_obstaculo:
        lost_text = FONT.render("Você perdeu!", 1, "blue")
        WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(1000)  # 1000 milisegundos
        break

    draw(player, elapsed_time, obstaculos, FONT, WIN, NAVE, PLAYER_VEL, COVID)

pygame.quit


