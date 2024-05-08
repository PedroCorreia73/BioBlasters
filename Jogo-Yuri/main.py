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
SURFACE = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
BG = criar_background_jogo()
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
BG_WIDTH, BG_HEIGHT = BG.get_width(), BG.get_height()
bg_pergunta = pygame.image.load("imagens/bg_pergunta.png")
origem_plano_resposta = (((WIDTH - bg_pergunta.get_width())/2, (HEIGHT - bg_pergunta.get_height())/2))
run = tela_inicial(WIN)

scroll = 0
tiles = math.ceil(WIDTH / BG_WIDTH) + 1

INIMIGOS, NAVE = gerar_personagens(PLAYER_WIDTH, PLAYER_HEIGHT)



player = pygame.Rect(PLAYER_WIDTH + 200, 400, PLAYER_WIDTH, PLAYER_HEIGHT)

clock = pygame.time.Clock()

start_time = time.time() #tempo que se passou desde a epoch
elapsed_time = 0

obstaculo_add_increment = 200  # 200 milisegundos
obstaculo_count = 0
obstaculos = []
hit_obstaculo = False

itempergunta_add_increment = 2000
itempergunta_count = 0
itenspergunta = []
hit_itempergunta = False

pontuacao = 0
pontuacao_ganha = 0
t = 0

hp = 100
invencibilidade = False
aux_inv_1 = 100

while run:

    # loop da tela---------
    if not hit_itempergunta:
        for i in range(0, tiles):
            WIN.blit(BG, (i * BG_WIDTH + scroll, 0))
        scroll -= 0.5
        if abs(scroll) > BG_WIDTH:
            scroll = 0
    # ---------------------

    #pontuação e tempo
    aux = 0
    aux += clock.tick(FPS)
    obstaculo_count += aux #limitação de FPS
    itempergunta_count += aux
    if not hit_itempergunta:
        elapsed_time = time.time() - start_time - t #tempo que se passou desde que o jogo começou
    if not hit_itempergunta:
        pontuacao_tempo = round(elapsed_time)
    pontuacao = pontuacao_tempo + pontuacao_ganha

    #atualização de variáveis relacionadas à pontuação
    if not hit_itempergunta:
        aux1 = 0
        aux2 = 0
        ti = 0
        tf = 0
    #Sistema de spawn de item de pergunta
    if not hit_itempergunta:
        if itempergunta_count > itempergunta_add_increment:
            for _ in range(1):
                itempergunta_y = random.randint(0, HEIGHT - OBSTACULO_HEIGHT)
                itempergunta = pygame.Rect(WIDTH, itempergunta_y, OBSTACULO_WIDTH, OBSTACULO_HEIGHT)
                itenspergunta.append(itempergunta)
            #itempergunta_add_increment = max(200, itempergunta_add_increment - 50)
            itempergunta_count = 0
    
    #Sistema de spawn de obstáculos
    if not hit_itempergunta:
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
    
    if not hit_itempergunta:
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
    if not hit_itempergunta:
        for obstaculo in obstaculos[:]:
            obstaculo.x -= OBSTACULO_VEL
            if obstaculo.x < 0 - OBSTACULO_WIDTH - 30:
                obstaculos.remove(obstaculo)
            if obstaculo.colliderect(player) and invencibilidade == False:
                obstaculos.remove(obstaculo)
                hit_obstaculo = True
                break

    #-------------------hit de obstáculos-------------------
    if hit_obstaculo:
        if invencibilidade == False:
            hp -= 10
            invencibilidade = True
            t_invencibilidade = time.time() + 2
        print(hp)
        hit_obstaculo = False
    if invencibilidade == True and time.time() > t_invencibilidade:
        invencibilidade = False
        aux_inv_1 = 10
    if invencibilidade:
        aux_inv_1 += 1
    if hp <= 0:
        lost_text = FONT.render("Você perdeu!", 1, "blue")
        WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(1000)  # 1000 milisegundos
        break
    #---------------------------------------------------------


      #movimentação de itenspergunta
    if not hit_itempergunta:
        for itempergunta in itenspergunta[:]:
            itempergunta.x -= OBSTACULO_VEL
            if itempergunta.x < 0 - OBSTACULO_WIDTH - 30:
                itenspergunta.remove(itempergunta)
            if itempergunta.colliderect(player):
                itenspergunta.remove(itempergunta)
                hit_itempergunta = True
    
      #caixa de pergunta
    if hit_itempergunta == True:
        aux1 += 1
        if aux1 == 1:
            pontuacao_ganha += 100
            ti = time.time()
        WIN.blit(bg_pergunta, origem_plano_resposta)
        texto_exemplo = "Isso é um enunciado bem longo da prova da fuvest que fala sobre algumas chatices de biologia/citologia/oquequerqueseja, mas o que importa é que isso está funcionando perfeitamente bem, desde que haja um número limite de caracteres para esse enunciado. Obrigado."
        fonte = pygame.font.SysFont("Arial", 30)
        collection = [word.split() for word in texto_exemplo.splitlines()]
        space = fonte.size(' ')[0]
        pos = origem_plano_resposta[0] + 10, origem_plano_resposta[1] + 10
        x = pos[0]
        y = pos[1]
        for lines in collection:
            for words in lines:
                word_surface = fonte.render(words, True, 'brown')
                word_width, word_height = word_surface.get_size()
                if x + word_width >= pos[0] + bg_pergunta.get_width() - 10:
                    x = pos[0]
                    y += word_height
                WIN.blit(word_surface, (x,y))
                x += word_width + space
            x = pos[0]
            y = word_height
        keys1 = pygame.key.get_pressed()
        if keys1[pygame.K_a]:
            aux2 += 1
            if aux2 == 1:
                tf = time.time()
                t += tf - ti
                pontuacao_ganha += 400
            print('c')
            PLAYER_VEL = PLAYER_VEL / 1.5
            pygame.time.delay(1000)
            hit_itempergunta = False
        pygame.display.update()
    draw(player, elapsed_time, obstaculos, itenspergunta, FONT, WIN, NAVE, PLAYER_VEL, INIMIGOS, hit_itempergunta, pontuacao, aux1, invencibilidade, aux_inv_1)
pygame.quit

