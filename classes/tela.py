import pygame


class Tela:

    def __init__(self):
        pygame.font.init() #inicializar o font module (sem isso não dá para usar fontes)
        pygame.display.init() # inicializar a tela (serve para poder obter as medidas da tela do usuário)
        WIDTH, HEIGHT = pygame.display.get_desktop_sizes()[0] #obtém as medidas da tela do usuário
        # WIDTH, HEIGHT = 1200, 600
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("BioBlasters")
        self.FONT = pygame.font.SysFont("comicsans", 30) #tipo e tamanho da fonte estocada na variável FONT

    def desenhar(self, player, elapsed_time, obstaculos, itenspergunta, FONT, WIN, NAVE, PLAYER_VEL, IMG_INIMIGO, IMG_ITEM_PERGUNTA, hit_itempergunta, pontuacao, aux1, invencibilidade, aux_inv, hp, balas):


        #time_text = FONT.render(f"Tempo: {round(elapsed_time)}s", 1, "white")
        #WIN.blit(time_text, (10, 10))
        hp_text = FONT.render(f"HP: {hp}", 1, "white")
        WIN.blit(hp_text, (10, 10))
        pontuacao_text = FONT.render(f"Pontuação: {pontuacao}", 1, "white")
        if aux1 == 1:
            pontuacao_text.set_alpha(0)
        WIN.blit(pontuacao_text, (200, 10))

        #rotação da nave, carregamento da imagem na tela e piscadinha
        NAVE2 = pygame.transform.rotate(NAVE, -PLAYER_VEL * 10)
        if invencibilidade:
            if str(aux_inv)[-2] in ["0", "2", "4", "6", "8"]:
                NAVE2.set_alpha(0)
            if str(aux_inv)[-2] in ["1", "3", "5", "7", "9"]:
                NAVE2.set_alpha(1000)
        NAVE2_RECT = NAVE2.get_rect(center = (player.x + 15, player.y + 15))
        WIN.blit(NAVE2, (NAVE2_RECT))
        #pygame.draw.rect(WIN, "green", player) #hitbox do player

        for obstaculo in obstaculos:
            #if hit_itempergunta is True and origem_plano_resposta[0] < obstaculo.x < origem_plano_resposta[0] + bgp.get_width() and origem_plano_resposta[1] < obstaculo.y and origem_plano_resposta[1] + bgp.get_height():
        #     pass
            #else:
                #pygame.draw.rect(WIN, "yellow", obstaculo) #hitbox dos obstáculos
                WIN.blit(IMG_INIMIGO, (obstaculo.x - 8, obstaculo.y -8))

        for itempergunta in itenspergunta:
            pygame.draw.rect(WIN, "blue", itempergunta) #hitbox dos obstáculos
            WIN.blit(IMG_ITEM_PERGUNTA, (itempergunta.x - 8, itempergunta.y -8))
        
        for bala in balas:
            pygame.draw.rect(WIN, "grey", bala)
            WIN.blit(pygame.transform.rotozoom(pygame.image.load("imagens/shot.png"), 0, 3), (bala.x, bala.y))
        if not hit_itempergunta:
            pygame.display.update()
    
    @property
    def WIDTH(self):
        return self.WIN.get_width()
    @property
    def HEIGHT(self):
        return self.WIN.get_height()