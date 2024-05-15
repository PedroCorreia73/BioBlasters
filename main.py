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

IMG_ITEM_PERGUNTA, IMG_INIMIGO, NAVE = gerar_personagens(PLAYER_WIDTH, PLAYER_HEIGHT)

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

balas = []
mochila_balas = [1, 1]

pontuacao = 0
pontuacao_ganha = 0
t = 0

hp = 100
invencibilidade = False
aux_inv = 100

vel_player_atual = PLAYER_VEL

while run:
    keys_teclado = pygame.key.get_pressed()
    keys_mouse = pygame.mouse.get_pressed()
    # loop da tela---------
    if not hit_itempergunta:
        for i in range(0, tiles):
            WIN.blit(BG, (i * BG_WIDTH + scroll, 0))
        scroll -= 0.5
        if abs(scroll) > BG_WIDTH:
            scroll = 0
    # ---------------------
    WIN.blit(pygame.transform.scale(pygame.image.load("imagens/bg_gr_overlay.png").convert_alpha(), (WIDTH, HEIGHT)), (0,0))

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

    if not keys_teclado[pygame.K_SPACE]:
        aux_bala = 0
    # Sistema TEMPORÁRIO de coleta de balas
    if keys_teclado[pygame.K_c]:
        mochila_balas.append(1)
    # Sistema de spawn de balas
    if not hit_itempergunta:
        keys2 = pygame.key.get_pressed()
        if keys_teclado[pygame.K_SPACE] and aux_bala == 0:
            aux_bala = 1
            vel_player_atual = PLAYER_VEL
            if 1 in mochila_balas and aux_bala == 1:
                bala = pygame.Rect(player.x + 30, player.y + 15, BALA_WIDTH, BALA_HEIGHT)
                #bala = pygame.Rect(player.x + 30 - math.cos(math.radians(-vel_player_atual * 10)) * 10, player.y + 15 - math.sin(math.radians(-vel_player_atual * 10)) * 15, BALA_WIDTH, BALA_HEIGHT)
                balas.append(bala)
                mochila_balas.remove(1)
    #movimentação de balas
    if not hit_itempergunta:
        for bala in balas:
            bala.x += BALA_VEL
            #bala.x += BALA_VEL * math.cos(math.radians(-vel_player_atual * 10) * 1.5)
            #bala.y += BALA_VEL * math.sin(math.radians(+vel_player_atual * 10) * 1.5)
            if bala.x > WIDTH:
                balas.remove(bala)
    #hit de balas
    for bala in balas:
        for obstaculo in obstaculos:
            if bala.y in range(obstaculo.y - 15, obstaculo.y + OBSTACULO_HEIGHT + 5) and bala.x in range(obstaculo.x - 5, obstaculo.x + OBSTACULO_WIDTH):
                obstaculos.remove(obstaculo)

    # fechar o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    # -------------

    # comandos da nave

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
            if keys_mouse[0] or PLAYER_VEL < 0:
                PLAYER_VEL = 0
                player.y = 10
            else:
                PLAYER_VEL += GRAVITY
        #--borda de baixo--
        elif player.y + PLAYER_HEIGHT * 1.5 >= HEIGHT:
            if keys_mouse[0] and PLAYER_VEL <= 0:
                PLAYER_VEL -= GRAVITY
            else:
                PLAYER_VEL = 0
                player.y = HEIGHT - PLAYER_HEIGHT * 1.2
        #--entre as bordas--
        elif keys_mouse[0] and player.y - PLAYER_VEL >= 0:
            if PLAYER_VEL > -VEL_TERMINAL:
                PLAYER_VEL -= GRAVITY
        else:
            if PLAYER_VEL < VEL_TERMINAL:
                PLAYER_VEL += GRAVITY
        player.y += PLAYER_VEL
        # -----------------

    #movimentação de obstáculos
    if not hit_itempergunta:
        for obstaculo in obstaculos[:]: #esses ':' fazem a cópia da lista
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
        hit_obstaculo = False
    if invencibilidade == True and time.time() > t_invencibilidade:
        invencibilidade = False
        aux_inv = 10
    if invencibilidade:
        aux_inv += 1
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
        enunciado_exemplo = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Enunciado - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
        a_exemplo = "A) Essa não é a alternativa correta."
        b_exemplo = "B) Muito menos essa."
        c_exemplo = "C) Nem me fale dessa!"
        d_exemplo = "D) Essa parece boa, mas nem tanto."
        e_exemplo = "E) Hmmmmmmmmmmmmmmm..."
        texto_completo_exemplo = enunciado_exemplo + "\n" + a_exemplo + "\n" + b_exemplo + "\n" + c_exemplo + "\n" + d_exemplo + "\n" + e_exemplo
        fonte = pygame.font.SysFont("Arial", 30)
        collection = [word.split(' ') for word in texto_completo_exemplo.splitlines()]
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
            y += word_height
        if keys_teclado[pygame.K_a]:
            aux2 += 1
            if aux2 == 1:
                tf = time.time()
                t += tf - ti
                pontuacao_ganha += 400
            print('a')
            PLAYER_VEL = PLAYER_VEL / 1.5
            pygame.time.delay(1000)
            hit_itempergunta = False
        pygame.display.update()
    draw(player, elapsed_time, obstaculos, itenspergunta, FONT, WIN, NAVE, PLAYER_VEL, IMG_INIMIGO, IMG_ITEM_PERGUNTA, hit_itempergunta, pontuacao, aux1, invencibilidade, aux_inv, hp, balas)
pygame.quit


