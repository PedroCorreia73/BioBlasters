import pygame
import pygame_gui
import math
from classes.obstaculo import Obstaculo, Obstaculos
from classes.item_pergunta import ItemPergunta
from time import time


class TelaJogo:

    def criar_background(self):
        BG = pygame.image.load("imagens/bg_start_v3.png").convert_alpha()
        self.BG = pygame.transform.scale(BG, (self.WIDTH, self.HEIGHT))

    def __init__(self):
        pygame.font.init() #inicializar o font module (sem isso não dá para usar fontes)
        pygame.display.init() # inicializar a tela (serve para poder obter as medidas da tela do usuário)
        self.WIDTH, self.HEIGHT = pygame.display.get_desktop_sizes()[0] #obtém as medidas da tela do usuário
        # WIDTH, HEIGHT = 1200, 600
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("BioBlasters")
        self.FONT = pygame.font.SysFont("comicsans", 30) #tipo e tamanho da fonte estocada na variável FONT
        self.manager = pygame_gui.UIManager((self.WIN.get_size()), theme_path="pygame_gui_configs/configuracoes.json",enable_live_theme_updates=False)
        self.criar_background()
        self.tempo_inicio = time()
        self.scroll = 0
        self.tiles = math.ceil(self.WIDTH / self.BG.get_width()) + 1
        self.proporcao_x = self.WIN.get_width() / 1920 # (1920 x 1080) tamanho padrão no qual as telas foram feitas
        self.proporcao_y = self.WIN.get_height() / 1080
        self.tamanho_botao = (360 * self.proporcao_x , 85 * self.proporcao_y)


    def desenhar(self, nave, elapsed_time, pontuacao, aux_pontuacao_resposta, balas, itens_pergunta, obstaculos):
        
        #time_text = FONT.render(f"Tempo: {round(elapsed_time)}s", 1, "white")
        #WIN.blit(time_text, (10, 10))
        hp_text = self.FONT.render(f"HP: {nave.hp}", 1, "white")
        self.WIN.blit(hp_text, (10, 10))
        pontuacao_text = self.FONT.render(f"Pontuação: {pontuacao.atual}", 1, "white")
        if aux_pontuacao_resposta == 1:
            pontuacao_text.set_alpha(0)
        self.WIN.blit(pontuacao_text, (200, 10))

        #rotação da nave, carregamento da imagem na tela e piscadinha
        NAVE2 = pygame.transform.rotate(nave.gerar_imagem(), -nave.vel * 10)
        if nave.invencibilidade:
            if str(nave.aux_inv)[-2] in ["0", "2", "4", "6", "8"]:
                NAVE2.set_alpha(0)
            if str(nave.aux_inv)[-2] in ["1", "3", "5", "7", "9"]:
                NAVE2.set_alpha(1000)
        NAVE2_RECT = NAVE2.get_rect(center = (nave.x + 15, nave.y + 15))
        self.WIN.blit(NAVE2, (NAVE2_RECT))
        #pygame.draw.rect(WIN, "green", nave) #hitbox do nave

        for obstaculo in obstaculos.itens():
            #if hit_itempergunta is True and origem_plano_resposta[0] < obstaculo.x < origem_plano_resposta[0] + bgp.get_width() and origem_plano_resposta[1] < obstaculo.y and origem_plano_resposta[1] + bgp.get_height():
        #     pass
            #else:
                #pygame.draw.rect(WIN, "yellow", obstaculo) #hitbox dos obstáculos
                self.WIN.blit(Obstaculo.gerar_imagem(), (obstaculo.x - 8, obstaculo.y -8))

        for itempergunta in itens_pergunta.itens():
            pygame.draw.rect(self.WIN, "blue", itempergunta) #hitbox dos obstáculos
            self.WIN.blit(ItemPergunta.gerar_imagem(), (itempergunta.x - 8, itempergunta.y -8))
        
        for bala in balas.itens():
            pygame.draw.rect(self.WIN, "grey", bala)
            self.WIN.blit(pygame.transform.rotozoom(pygame.image.load("imagens/shot.png"), 0, 3), (bala.x, bala.y))
        if not nave.pegou_item_pergunta:
            pygame.display.update()
            
    def loop(self):
        for i in range(0, self.tiles):
            self.WIN.blit(self.BG, (i * self.BG.get_width() + self.scroll, 0))
        self.scroll -= 0.5
        if abs(self.scroll) > self.BG.get_width():
            self.scroll = 0
