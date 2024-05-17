import pygame
import pygame_gui
import time
import random
import math
from classes.obstaculo import Obstaculo, Obstaculos
from classes.nave import Nave
from classes.bala import Bala, Balas
from classes.item_pergunta import ItemPergunta, ItensPergunta
from classes.pontuacao import Pontuacao
from classes.jogo import Jogo


def jogar(tela):
    nave = Nave() # Iniciando a nave do jogador
    pontuacao = Pontuacao() #Iniciando a pontuação 
    obstaculos = Obstaculos() #Iniciando coleção de obstáculos que aparecem na tela
    itens_pergunta = ItensPergunta() # Iniciando coleção de perguntas que aparecem na tela
    balas = Balas() # Iniciando coleção de balas que aparecem na tela

    # SURFACE = pygame.Surface((tela.WIDTH, tela.HEIGHT), pygame.SRCALPHA)
    bg_pergunta = pygame.image.load("imagens/bg_pergunta.png")
    origem_plano_resposta = (((tela.WIDTH - bg_pergunta.get_width())/2, (tela.HEIGHT - bg_pergunta.get_height())/2))
    


    scroll = 0
    tiles = math.ceil(tela.WIDTH / tela.BG.get_width()) + 1


    clock = pygame.time.Clock()

    start_time = time.time() #tempo que se passou desde a epoch
    elapsed_time = 0

    t = 0

    aux_inv = 100
    run = True
    while run:
        keys_teclado = pygame.key.get_pressed()
        keys_mouse = pygame.mouse.get_pressed()
        # loop da tela---------
        if not nave.pegou_item_pergunta:
            for i in range(0, tiles):
                tela.WIN.blit(tela.BG, (i * tela.BG.get_width() + scroll, 0))
            scroll -= 0.5
            if abs(scroll) > tela.BG.get_width():
                scroll = 0
        # ---------------------

        #pontuação e tempo
        aux = 0
        aux += clock.tick(Jogo.FPS)
        obstaculos.contagem += aux #limitação de FPS
        itens_pergunta.contagem += aux
        if not nave.pegou_item_pergunta:
            elapsed_time = time.time() - start_time - t #tempo que se passou desde que o jogo começou
            pontuacao.tempo = round(elapsed_time)
        pontuacao.atual = pontuacao.tempo + pontuacao.ganha

        #atualização de variáveis relacionadas à pontuação
        if not nave.pegou_item_pergunta:
            aux1 = 0
            aux2 = 0
            ti = 0
            tf = 0
        #Sistema de spawn de item de pergunta
            if itens_pergunta.contagem > itens_pergunta.add_increment:
                for _ in range(1):
                    item_pergunta_y = random.randint(0, tela.HEIGHT - Obstaculo.HEIGHT)
                    item_pergunta = ItemPergunta(tela.WIDTH, item_pergunta_y, Obstaculo.WIDTH, Obstaculo.HEIGHT)
                    itens_pergunta.append(item_pergunta)
                #item_pergunta_add_increment = max(200, item_pergunta_add_increment - 50)
                itens_pergunta.contagem = 0
        
        #Sistema de spawn de obstáculos
            if obstaculos.contagem > obstaculos.add_increment: #tempo entre um obstáculo e o próximo obstáculo
                    for _ in range(1):
                        obstaculo_y = random.randint(0, tela.HEIGHT - Obstaculo.HEIGHT) #criando o local no eixo y no qual o obtáculo surgirá
                        obstaculo = Obstaculo(tela.WIDTH, obstaculo_y)
                        obstaculos.append(obstaculo)
                    obstaculos.add_increment = max(200, obstaculos.add_increment - 50)
                    obstaculos.contagem = 0

        if not keys_teclado[pygame.K_SPACE]:
            aux_bala = 0
        # Sistema TEMPORÁRIO de coleta de balas
        if keys_teclado[pygame.K_c]:
            nave.mochila_balas.append(1)
        # Sistema de spawn de balas
        if not nave.pegou_item_pergunta:
            keys2 = pygame.key.get_pressed()
            if keys_teclado[pygame.K_SPACE] and aux_bala == 0:
                aux_bala = 1
                if 1 in nave.mochila_balas and aux_bala == 1:
                    bala = Bala(nave.x + 30, nave.y + 15, Bala.WIDTH, Bala.HEIGHT)
                    #bala = pygame.Rect(nave.x + 30 - math.cos(math.radians(-vel_player_atual * 10)) * 10, nave.y + 15 - math.sin(math.radians(-vel_player_atual * 10)) * 15, Bala.WIDTH, Bala.HEIGHT)
                    balas.append(bala)
                    nave.mochila_balas.remove(1)
        #movimentação de balas
            for bala in balas.itens():
                bala.x += Bala.VEL
                #bala.x += Bala.VEL * math.cos(math.radians(-vel_player_atual * 10) * 1.5)
                #bala.y += Bala.VEL * math.sin(math.radians(+vel_player_atual * 10) * 1.5)
                if bala.x > tela.WIDTH:
                    balas.remove(bala)
        #hit de balas
        for bala in balas.itens():
            for obstaculo in obstaculos.itens():
                if bala.y in range(obstaculo.y - 15, obstaculo.y + Obstaculo.HEIGHT + 5) and bala.x in range(obstaculo.x - 5, obstaculo.x + Obstaculo.WIDTH):
                    obstaculos.remove(obstaculo)

        # fechar o jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
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
                    nave.vel += Jogo.GRAVIDADE
            #--borda de baixo--
            elif nave.y + nave.HEIGHT * 1.5 >= tela.HEIGHT:
                if keys_mouse[0] and nave.vel <= 0:
                    nave.vel -= Jogo.GRAVIDADE
                else:
                    nave.vel = 0
                    nave.y = tela.HEIGHT - nave.HEIGHT * 1.2
            #--entre as bordas--
            elif keys_mouse[0] and nave.y - nave.vel >= 0:
                if nave.vel > -Jogo.VEL_TERMINAL:
                    nave.vel -= Jogo.GRAVIDADE
            else:
                if nave.vel < Jogo.VEL_TERMINAL:
                    nave.vel += Jogo.GRAVIDADE
            nave.y += nave.vel
            # -----------------

        #movimentação de obstáculos
            for obstaculo in obstaculos.itens():
                obstaculo.x -= Obstaculo.VEL
                if obstaculo.x < 0 - Obstaculo.WIDTH - 30:
                    obstaculos.remove(obstaculo)
                if obstaculo.colliderect(nave) and nave.invencibilidade == False:
                    obstaculos.remove(obstaculo)
                    nave.colidiu_obstaculo = True
                    break

        #-------------------hit de obstáculos-------------------
        if nave.colidiu_obstaculo:
            if nave.invencibilidade == False:
                nave.hp -= 10
                nave.invencibilidade = True
                t_invencibilidade = time.time() + 2
            nave.colidiu_obstaculo = False
        if nave.invencibilidade and time.time() > t_invencibilidade:
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


        #movimentação de itens_pergunta
        if not nave.pegou_item_pergunta:
            for item_pergunta in itens_pergunta.itens():
                item_pergunta.x -= Obstaculo.VEL
                if item_pergunta.x < 0 - Obstaculo.WIDTH - 30:
                    itens_pergunta.remove(item_pergunta)
                if item_pergunta.colliderect(nave):
                    itens_pergunta.remove(item_pergunta)
                    nave.pegou_item_pergunta = True

        #caixa de pergunta
        if nave.pegou_item_pergunta:
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
                nave.vel = nave.vel / 1.5
                pygame.time.delay(1000)
                nave.pegou_item_pergunta = False
            pygame.display.update()
        tela.desenhar(nave, elapsed_time,
                        pontuacao, aux1, aux_inv, balas, itens_pergunta, obstaculos)
    return False
if __name__ == "__main__":
    jogar()