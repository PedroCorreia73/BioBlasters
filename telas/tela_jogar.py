import pygame
import pygame_gui
from pygame_gui.core import ObjectID
import time
from usuario.usuario_atual import Aluno, Professor
from banco_de_dados.aluno import AlunoDAO
from banco_de_dados.professor import ProfessorDAO
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

        hud_jogo = HUD(self.tela, nave) # Objeto responsável por gerar o HUD durante o jogo
        hud_jogo.gerar_elementos() # Gera os elementos do HUD
        self.tela.HEIGHT -= hud_jogo.HEIGHT # Faz com que nenhum objeto possa ultrapassar o HUD

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
                    self.tela.HEIGHT += hud_jogo.HEIGHT #Retomando o tamanho da tela
                    tela_derrota = TelaDerrota(self.tela)
                    continuar = tela_derrota.mostrar(self.usuario, pontuacao)
                    return continuar
            #---------------------------------------------------------
            #movimentação de itens_pergunta
                itens_pergunta.mover(nave)

            #caixa de pergunta
            else:
                tempo_antes_da_pergunta = time.time()
                acertou = perguntas.gerar_pergunta(self.tela)
                self.tela.manager.clear_and_reset()
                self.tela.WIN.blit(pygame.transform.scale(self.tela.BG, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
                hud_jogo.gerar_elementos() # Gera os elementos do HUD
                tempo_em_perguntas += time.time() - tempo_antes_da_pergunta
                nave.pegou_item_pergunta = False
                if acertou:
                    pontuacao.ganha += 400 # Aumenta a pontuação caso o usuário tenha acertado a pergunta
                    nave.mochila_balas.append(1)
                nave.invencibilidade = True # Permite que o usuário fique invencível durante um tempo
                nave.tempo_invencibilidade = time.time() + 1

            # fechar o jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                self.tela.manager.process_events(event)
            # Desenhar os elementos na tela
            self.tela.manager.update(aux_clock)
            self.tela.manager.draw_ui(self.tela.WIN)
            self.tela.desenhar(nave, pontuacao, balas, itens_pergunta, obstaculos)

        self.tela.HEIGHT += hud_jogo.HEIGHT #Retomando o tamanho da tela
        return False
    
class HUD:
    def __init__(self, tela, nave):
        self.tela = tela
        self.nave = nave
        
    def gerar_elementos(self):
        self.hud_jogo = pygame_gui.elements.UIPanel(relative_rect= ((0, -100 * self.tela.proporcao_y), (self.tela.WIN.get_width(), 100 * self.tela.proporcao_y)),
                                        manager=self.tela.manager,
                                        object_id=ObjectID(class_id="@hud"),
                                        anchors={"bottom":"bottom"})
        self.vida_nave = pygame_gui.elements.UIStatusBar(relative_rect=((100 * self.tela.proporcao_x , 10), (500 * self.tela.proporcao_x, 50 * self.tela.proporcao_y)),
                                                percent_method= lambda : self.nave.hp / 100,
                                                container=self.hud_jogo,
                                                manager= self.tela.manager,
                                                anchors={"centery":"centery"})
        self.HEIGHT = self.hud_jogo.get_relative_rect().height

class TelaDerrota:
    def __init__(self, tela):
        self.tela = tela

    def mostrar(self, usuario, pontuacao):
        self.tela.manager.clear_and_reset()
        BG_INICIO = pygame.image.load("imagens/bgbg.png")
        caixa_fundo = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 0),(1400 * self.tela.proporcao_x, 650 * self.tela.proporcao_y)),
                                                    manager=self.tela.manager,
                                                    anchors={"centerx" : "centerx",
                                                             "centery" : "centery"})
        pygame.display.update()
        texto = "<p>Você perdeu!</p>"
        if isinstance(usuario, Aluno):
            alunodao = AlunoDAO()
            if pontuacao.atual > usuario.pontuacao: 
                alunodao.atualizar_pontuacao(usuario.id, pontuacao.atual)
                texto += f"<p>Parabéns! Sua pontuação aumentou para: {pontuacao.atual}</p>"
                texto += f"<p>Antes era: {usuario.pontuacao}</p>"
                usuario.pontuacao = pontuacao.atual
            else:
                texto += f"Sua maior pontuação continua sendo: {usuario.pontuacao}"
        elif isinstance(usuario, Professor):
            professordao = ProfessorDAO()
            if pontuacao.atual > usuario.pontuacao: 
                professordao.atualizar_pontuacao(usuario.id, pontuacao.atual)
                texto += f"<p>Parabéns! Sua pontuação aumentou para: {pontuacao.atual}</p>"
                texto += f"<p>Antes era: {usuario.pontuacao}</p>"
                usuario.pontuacao = pontuacao.atual
            else:
                texto += f"Sua maior pontuação continua sendo: {usuario.pontuacao}"

        caixa_texto = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((0, -75 * self.tela.proporcao_y),(1300 * self.tela.proporcao_x, 250 * self.tela.proporcao_y)),
                                                             html_text=texto,
                                                             container=caixa_fundo,
                                                             anchors={"centerx" : "centerx",
                                                                      "centery":"centery"},
                                                             manager=self.tela.manager)
        voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, -60 * self.tela.proporcao_y),(-1, -1)),
                                                        text="Voltar ao Menu Principal",
                                                        container=caixa_fundo,
                                                        anchors={"centerx" : "centerx",
                                                                    "bottom":"bottom"},
                                                        manager=self.tela.manager)
        
        clock = pygame.time.Clock()
        run = True
        while run:
            time_delta = clock.tick(60) / 1000.00
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == voltar_botao:
                        return True
                self.tela.manager.process_events(event)
            # Desenhar os elementos na tela
            self.tela.manager.update(time_delta)
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return False

        
        