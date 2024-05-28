import pygame
import pygame_gui
import time
from classes.obstaculo import Obstaculo, Obstaculos
from classes.nave import Nave
from classes.bala import Bala, Balas
from classes.item_pergunta import ItemPergunta, ItensPergunta
from classes.pontuacao import Pontuacao
from classes.jogo import Jogo

class TelaJogar():
    def jogar(tela):
        tela.manager.clear_and_reset() # Reseta os elementos do pygame_gui
        tela.tempo_inicio = time.time()
        nave = Nave() # Iniciando a nave do jogador
        pontuacao = Pontuacao() #Iniciando a pontuação 
        obstaculos = Obstaculos() #Iniciando coleção de obstáculos que aparecem na tela
        itens_pergunta = ItensPergunta() # Iniciando coleção de perguntas que aparecem na tela
        balas = Balas() # Iniciando coleção de balas que aparecem na tela

        # SURFACE = pygame.Surface((tela.WIDTH, tela.HEIGHT), pygame.SRCALPHA)
        bg_pergunta = pygame.image.load("imagens/bg_pergunta.png")
        origem_plano_resposta = (((tela.WIDTH - bg_pergunta.get_width())/2, (tela.HEIGHT - bg_pergunta.get_height())/2))
        
        clock = pygame.time.Clock()
        elapsed_time = 0 #tempo que se passou desde a epoch
        t = 0

        run = True
        while run:
            keys_teclado = pygame.key.get_pressed()
            keys_mouse = pygame.mouse.get_pressed()
            #pontuação e tempo
            aux_clock = 0
            aux_clock += clock.tick(Jogo.FPS)
            obstaculos.contagem += aux_clock #limitação de FPS
            itens_pergunta.contagem += aux_clock
            if not nave.pegou_item_pergunta:
                tela.loop() # responsável por mover o fundo da tela
                elapsed_time = time.time() - tela.tempo_inicio - t #tempo que se passou desde que o jogo começou
                pontuacao.tempo = round(elapsed_time)
                pontuacao.atual = pontuacao.tempo + pontuacao.ganha
            #atualização de variáveis relacionadas à pontuação
                aux_pontuacao_resposta = 0
                aux_tempo_resposta = 0
                ti = 0
                tf = 0
            #Sistema de spawn de item de pergunta
                itens_pergunta.gerar(tela)
            #Sistema de spawn de obstáculos
                tipo_obstaculo = obstaculos.gerar(tela)
                if not keys_teclado[pygame.K_SPACE]:
                    Bala.aux_bala = 0
            # Sistema TEMPORÁRIO de coleta de balas
                if keys_teclado[pygame.K_c]:
                    nave.mochila_balas.append(1)
            # Sistema de spawn de balas
                balas.gerar(nave, keys_teclado)
            #movimentação de balas
                balas.mover(tela)
            #hit de balas
                balas.colidir(obstaculos)
            #movimentação da nave
                nave.mover(tela, keys_mouse)
            #movimentação de obstáculos
                obstaculos.mover(nave)

            #-------------------hit de obstáculos-------------------
                continuar_jogo = nave.colidir(tela) # nave.colidir() retorna se o jogo deve continuar baseado na vida da nave
                if not continuar_jogo:
                    return True
            #---------------------------------------------------------
            #movimentação de itens_pergunta
                itens_pergunta.mover(nave)

            #caixa de pergunta
            else:
                aux_pontuacao_resposta += 1
                if aux_pontuacao_resposta == 1:
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
                    aux_tempo_resposta += 1
                    if aux_tempo_resposta == 1:
                        tf = time.time()
                        t += tf - ti
                        pontuacao.ganha += 400
                    nave.vel = nave.vel / 1.5
                    pygame.time.delay(1000)
                    nave.pegou_item_pergunta = False
                pygame.display.update()
            # Desenhar os elementos na tela
            tela.desenhar(nave, elapsed_time,
                            pontuacao, aux_pontuacao_resposta, balas, itens_pergunta, obstaculos, tipo_obstaculo)
            # fechar o jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
        return False
