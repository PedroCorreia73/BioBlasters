import pygame
import time
import random
import math
from menus import tela_inicial
from classes.tela import TelaJogo
from constantes import *
from background import criar_background_jogo
from classes.obstaculo import Obstaculo, Obstaculos
from classes.nave import Nave
from classes.bala import Bala
from classes.item_pergunta import ItemPergunta
from classes.pontuacao import Pontuacao




tela = TelaJogo() # inicializa a tela com as medidas da tela do usuário
nave = Nave() # iniciando a nave do jogador
pontuacao = Pontuacao() #Iniciando a pontuação
SURFACE = pygame.Surface((tela.WIDTH, tela.HEIGHT), pygame.SRCALPHA)
BG = criar_background_jogo()
BG = pygame.transform.scale(BG, (tela.WIDTH, tela.HEIGHT))
BG_WIDTH, BG_HEIGHT = BG.get_width(), BG.get_height()
bg_pergunta = pygame.image.load("imagens/bg_pergunta.png")
origem_plano_resposta = (((tela.WIDTH - bg_pergunta.get_width())/2, (tela.HEIGHT - bg_pergunta.get_height())/2))
run = tela_inicial(tela.WIN)


scroll = 0
tiles = math.ceil(tela.WIDTH / BG_WIDTH) + 1


clock = pygame.time.Clock()

start_time = time.time() #tempo que se passou desde a epoch
elapsed_time = 0

obstaculo_add_increment = 200  # 200 milisegundos
obstaculo_count = 0


item_pergunta_add_increment = 2000
item_pergunta_count = 0
itenspergunta = []

balas = []
mochila_balas = [1, 1]



t = 0

aux_inv = 100



while run:
    keys_teclado = pygame.key.get_pressed()
    keys_mouse = pygame.mouse.get_pressed()
    # loop da tela---------
    if not nave.pegou_item_pergunta:
        for i in range(0, tiles):
            tela.WIN.blit(BG, (i * BG_WIDTH + scroll, 0))
        scroll -= 0.5
        if abs(scroll) > BG_WIDTH:
            scroll = 0
    # ---------------------

    #pontuação e tempo
    aux = 0
    aux += clock.tick(FPS)
    obstaculo_count += aux #limitação de FPS
    item_pergunta_count += aux
    if not nave.pegou_item_pergunta:
        elapsed_time = time.time() - start_time - t #tempo que se passou desde que o jogo começou
    if not nave.pegou_item_pergunta:
        pontuacao.tempo = round(elapsed_time)
    pontuacao.atual = pontuacao.tempo + pontuacao.ganha

    #atualização de variáveis relacionadas à pontuação
    if not nave.pegou_item_pergunta:
        aux1 = 0
        aux2 = 0
        ti = 0
        tf = 0
    #Sistema de spawn de item de pergunta
    if not nave.pegou_item_pergunta:
        if item_pergunta_count > item_pergunta_add_increment:
            for _ in range(1):
                item_pergunta_y = random.randint(0, tela.HEIGHT - Obstaculo.HEIGHT)
                item_pergunta = ItemPergunta(tela.WIDTH, item_pergunta_y, Obstaculo.WIDTH, Obstaculo.HEIGHT)
                itenspergunta.append(item_pergunta)
            #item_pergunta_add_increment = max(200, item_pergunta_add_increment - 50)
            item_pergunta_count = 0
    
    #Sistema de spawn de obstáculos
    if not nave.pegou_item_pergunta:
        if obstaculo_count > obstaculo_add_increment: #tempo entre um obstáculo e o próximo obstáculo
                for _ in range(1):
                    obstaculo_y = random.randint(0, tela.HEIGHT - Obstaculo.HEIGHT) #criando o local no eixo y no qual o obtáculo surgirá
                    obstaculo = Obstaculo(tela.WIDTH, obstaculo_y)
                    Obstaculos.append(obstaculo)
                obstaculo_add_increment = max(200, obstaculo_add_increment - 50)
                obstaculo_count = 0

    if not keys_teclado[pygame.K_SPACE]:
        aux_bala = 0
    # Sistema TEMPORÁRIO de coleta de balas
    if keys_teclado[pygame.K_c]:
        mochila_balas.append(1)
    # Sistema de spawn de balas
    if not nave.pegou_item_pergunta:
        keys2 = pygame.key.get_pressed()
        if keys_teclado[pygame.K_SPACE] and aux_bala == 0:
            aux_bala = 1
            if 1 in mochila_balas and aux_bala == 1:
                bala = pygame.Rect(nave.x + 30, nave.y + 15, Bala.WIDTH, Bala.HEIGHT)
                #bala = pygame.Rect(nave.x + 30 - math.cos(math.radians(-vel_player_atual * 10)) * 10, nave.y + 15 - math.sin(math.radians(-vel_player_atual * 10)) * 15, Bala.WIDTH, Bala.HEIGHT)
                balas.append(bala)
                mochila_balas.remove(1)
    #movimentação de balas
    if not nave.pegou_item_pergunta:
        for bala in balas:
            bala.x += Bala.VEL
            #bala.x += Bala.VEL * math.cos(math.radians(-vel_player_atual * 10) * 1.5)
            #bala.y += Bala.VEL * math.sin(math.radians(+vel_player_atual * 10) * 1.5)
            if bala.x > tela.WIDTH:
                balas.remove(bala)
    #hit de balas
    for bala in balas:
        for obstaculo in Obstaculos.itens():
            if bala.y in range(obstaculo.y - 15, obstaculo.y + Obstaculo.HEIGHT + 5) and bala.x in range(obstaculo.x - 5, obstaculo.x + Obstaculo.WIDTH):
                Obstaculos.remove(obstaculo)

    # fechar o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    # -------------

    # comandos da nave

    # if keys[pygame.K_a] and nave.x - PLAYER_VEL >= 0:
    # nave.x -= (PLAYER_VEL - 3)
    # if keys[pygame.K_d] and nave.x + PLAYER_VEL + nave.width <= WIDTH:
    # nave.x += PLAYER_VEL
    # if keys[pygame.K_w] and nave.y - PLAYER_VEL >= 0:
    # nave.y -= PLAYER_VEL
    # if keys[pygame.K_s] and nave.y + PLAYER_VEL + nave.height <= HEIGHT:
    # nave.y += PLAYER_VEL
    
    if not nave.pegou_item_pergunta:
        #--borda de cima--
        if nave.y <= 10:
            if keys_mouse[0] or nave.vel < 0:
                nave.vel = 0
                nave.y = 10
            else:
                nave.vel += GRAVITY
        #--borda de baixo--
        elif nave.y + nave.HEIGHT * 1.5 >= tela.HEIGHT:
            if keys_mouse[0] and nave.vel <= 0:
                nave.vel -= GRAVITY
            else:
                nave.vel = 0
                nave.y = tela.HEIGHT - nave.HEIGHT * 1.2
        #--entre as bordas--
        elif keys_mouse[0] and nave.y - nave.vel >= 0:
            if nave.vel > -VEL_TERMINAL:
                nave.vel -= GRAVITY
        else:
            if nave.vel < VEL_TERMINAL:
                nave.vel += GRAVITY
        nave.y += nave.vel
        # -----------------

    #movimentação de obstáculos
    if not nave.pegou_item_pergunta:
        for obstaculo in Obstaculos.itens():
            obstaculo.x -= Obstaculo.VEL
            if obstaculo.x < 0 - Obstaculo.WIDTH - 30:
                Obstaculos.remove(obstaculo)
            if obstaculo.colliderect(nave) and nave.invencibilidade == False:
                Obstaculos.remove(obstaculo)
                nave.colidiu_obstaculo = True
                break

    #-------------------hit de obstáculos-------------------
    if nave.colidiu_obstaculo:
        if nave.invencibilidade == False:
            nave.hp -= 10
            nave.invencibilidade = True
            t_invencibilidade = time.time() + 2
        nave.colidiu_obstaculo = False
    if nave.invencibilidade == True and time.time() > t_invencibilidade:
        nave.invencibilidade = False
        aux_inv = 10
    if nave.invencibilidade:
        aux_inv += 1
    if nave.hp <= 0:
        lost_text = tela.FONT.render("Você perdeu!", 1, "blue")
        tela.WIN.blit(lost_text, (tela.WIDTH / 2 - lost_text.get_width() / 2, tela.HEIGHT / 2 - lost_text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(1000)  # 1000 milisegundos
        break
    #---------------------------------------------------------


      #movimentação de itenspergunta
    if not nave.pegou_item_pergunta:
        for item_pergunta in itenspergunta[:]:
            item_pergunta.x -= Obstaculo.VEL
            if item_pergunta.x < 0 - Obstaculo.WIDTH - 30:
                itenspergunta.remove(item_pergunta)
            if item_pergunta.colliderect(nave):
                itenspergunta.remove(item_pergunta)
                nave.pegou_item_pergunta = True

      #caixa de pergunta
    if nave.pegou_item_pergunta == True:
        aux1 += 1
        if aux1 == 1:
            pontuacao.ganha += 100
            ti = time.time()
        tela.WIN.blit(bg_pergunta, origem_plano_resposta)
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
                tela.WIN.blit(word_surface, (x,y))
                x += word_width + space
            x = pos[0]
            y += word_height
        if keys_teclado[pygame.K_a]:
            aux2 += 1
            if aux2 == 1:
                tf = time.time()
                t += tf - ti
                pontuacao.ganha += 400
            print('a')
            nave.vel = nave.vel / 1.5
            pygame.time.delay(1000)
            nave.pegou_item_pergunta = False
        pygame.display.update()
    tela.desenhar(nave, elapsed_time, itenspergunta,
                    pontuacao, aux1, aux_inv, balas)
pygame.quit
