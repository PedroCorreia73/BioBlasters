import pygame
import pygame_gui
import math
import json
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
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("BioBlasters")
        self.FONT = pygame.font.SysFont("comicsans", 30) #tipo e tamanho da fonte estocada na variável FONT
        self.criar_background()
        self.tempo_inicio = time()
        self.scroll = 0
        self.tiles = math.ceil(self.WIDTH / self.BG.get_width()) + 1
        self.proporcao_x = self.WIN.get_width() / 1920 # (1920 x 1080) tamanho padrão no qual as telas foram feitas
        self.proporcao_y = self.WIN.get_height() / 1080
        self.tamanho_botao = (360 * self.proporcao_x , 85 * self.proporcao_y)
        with open("pygame_gui_configs/configuracoes.json") as arquivo:
            tema : dict = json.load(arquivo)
            for item in tema:
                if "font" in tema[item]:
                    tema[item]["font"]["size"] = round(self.proporcao_x * tema[item]["font"]["size"]) # Ajustando o tamanho da fonte
        self.manager = pygame_gui.UIManager((self.WIN.get_size()), theme_path= tema,enable_live_theme_updates=False)


    def desenhar(self, nave, pontuacao, balas, itens_pergunta, obstaculos):
        
        pontuacao_text = self.FONT.render(f"Pontuação: {pontuacao.atual}", 1, "white")
        self.WIN.blit(pontuacao_text, (200, 10))

        #rotação da nave, carregamento da imagem na tela e piscadinha
        NAVE2 = pygame.transform.rotate(nave.gerar_imagem(), -nave.vel * 10)      
        if nave.invencibilidade:
            if nave.aux_inv % 100 // 10 % 2 == 0: 
                NAVE2.set_alpha(0)
            else:
                NAVE2.set_alpha(1000)
        NAVE2_RECT = NAVE2.get_rect(center = (nave.x + 15, nave.y + 15))
        self.WIN.blit(NAVE2, (NAVE2_RECT))

        for obstaculo in obstaculos.itens():
            self.WIN.blit(obstaculo.gerar_imagem(), (obstaculo.x - 8, obstaculo.y -8))

        for itempergunta in itens_pergunta.itens():
            self.WIN.blit(ItemPergunta.gerar_imagem(), (itempergunta.x - 8, itempergunta.y -8))
        
        for bala in balas.itens():
            pygame.draw.rect(self.WIN, "grey", bala)
            self.WIN.blit(pygame.transform.rotozoom(pygame.image.load("imagens/shot.png"), 0, 3), (bala.x, bala.y))
        pygame.display.update()
            
    def loop(self):
        for i in range(0, self.tiles):
            self.WIN.blit(self.BG, (i * self.BG.get_width() + self.scroll, 0))
        self.scroll -= 0.5
        if abs(self.scroll) > self.BG.get_width():
            self.scroll = 0
