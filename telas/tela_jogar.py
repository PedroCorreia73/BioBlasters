import pygame
import pygame_gui
import time
from classes.obstaculo import Obstaculos
from classes.nave import Nave
from classes.bala import Bala, Balas
from classes.item_pergunta import ItensPergunta
from classes.pontuacao import Pontuacao
from classes.jogo import Jogo
from classes.pergunta import Perguntas

class TelaJogar():
    def __init__(self, tela, usuario):
        self.tela = tela
        self.usuario = usuario

    def jogar(self):
        self.tela.manager.clear_and_reset() # Reseta os elementos do pygame_gui
        nave = Nave() # Iniciando a nave do jogador
        pontuacao = Pontuacao() #Iniciando a pontuação 
        obstaculos = Obstaculos() #Iniciando coleção de obstáculos que aparecem na tela
        itens_pergunta = ItensPergunta() # Iniciando coleção de perguntas que aparecem na tela
        balas = Balas() # Iniciando coleção de balas que aparecem na tela
        perguntas = Perguntas(self.usuario.id_grupo) #Iniciando coleção de perguntas

        self.tela.tempo_inicio = time.time()
        tempo_em_perguntas = 0 # Tempo total que o usuário gastou nas perguntas -- Serve apenas para ajustar a pontuação

        run = True
        clock = pygame.time.Clock()
        while run:
            keys_teclado = pygame.key.get_pressed()
            keys_mouse = pygame.mouse.get_pressed()
            #pontuação e tempo
            aux_clock = 0
            aux_clock += clock.tick(Jogo.FPS)
            obstaculos.contagem += aux_clock #limitação de FPS
            itens_pergunta.contagem += aux_clock
            if not nave.pegou_item_pergunta:
                self.tela.loop() # responsável por mover o fundo da tela
                elapsed_time = time.time() - self.tela.tempo_inicio - tempo_em_perguntas #tempo que se passou desde que o jogo começou
                pontuacao.tempo = round(elapsed_time)
                pontuacao.atual = pontuacao.tempo + pontuacao.ganha
            #Sistema de spawn de item de pergunta
                itens_pergunta.gerar(self.tela)
            #Sistema de spawn de obstáculos
                obstaculos.gerar(self.tela)
                if not keys_teclado[pygame.K_SPACE]:
                    Bala.aux_bala = 0
            # Sistema TEMPORÁRIO de coleta de balas
                if keys_teclado[pygame.K_c]:
                    nave.mochila_balas.append(1)
            # Sistema de spawn de balas
                balas.gerar(nave, keys_teclado)
            #movimentação de balas
                balas.mover(self.tela)
            #hit de balas
                balas.colidir(obstaculos)
            #movimentação da nave
                nave.mover(self.tela, keys_mouse)
            #movimentação de obstáculos
                obstaculos.mover(nave)

            #-------------------hit de obstáculos-------------------
                continuar_jogo = nave.colidir(self.tela) # nave.colidir() retorna se o jogo deve continuar baseado na vida da nave
                if not continuar_jogo:
                    return True
            #---------------------------------------------------------
            #movimentação de itens_pergunta
                itens_pergunta.mover(nave)

            #caixa de pergunta
            else:
                tempo_antes_da_pergunta = time.time()
                acertou = perguntas.gerar_pergunta(self.tela)
                tempo_em_perguntas += time.time() - tempo_antes_da_pergunta
                nave.pegou_item_pergunta = False
                if acertou:
                    pontuacao.ganha += 400
                nave.invencibilidade = True
                nave.t_invencibilidade = time.time() + 2

            # Desenhar os elementos na tela
            self.tela.desenhar(nave, pontuacao, balas, itens_pergunta, obstaculos)

            # fechar o jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
        return False
