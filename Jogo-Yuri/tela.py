import pygame

def tela():
    pygame.font.init() #inicializar o font module (sem isso não dá para usar fontes)
    pygame.display.init() # inicializar a tela (serve para poder obter as medidas da tela do usuário)
    #WIDTH, HEIGHT = pygame.display.get_desktop_sizes()[0] #obtém as medidas da tela do usuário
    WIDTH, HEIGHT = 1200, 600
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("BioBlasters")
    FONT = pygame.font.SysFont("comicsans", 30) #tipo e tamanho da fonte estocada na variável FONT
    return WIN, FONT

def draw(player, elapsed_time, obstaculos, itenspergunta, FONT, WIN, NAVE, PLAYER_VEL, COVID, hit_itempergunta, pontuacao, aux1, invencibilidade, aux_inv_1):


    #time_text = FONT.render(f"Tempo: {round(elapsed_time)}s", 1, "white")
    #WIN.blit(time_text, (10, 10))

    pontuacao_text = FONT.render(f"Pontuação: {pontuacao}", 1, "white")
    if aux1 == 1:
         pontuacao_text.set_alpha(0)
    WIN.blit(pontuacao_text, (200, 10))

    #rotação da nave, carregamento da imagem na tela e piscadinha
    NAVE2 = pygame.transform.rotate(NAVE, -PLAYER_VEL * 10)
    if invencibilidade:
        if str(aux_inv_1)[-2] in ["0", "2", "4", "6", "8"]:
            NAVE2.set_alpha(0)
        if str(aux_inv_1)[-2] in ["1", "3", "5", "7", "9"]:
            NAVE2.set_alpha(1000)
    WIN.blit(NAVE2, (player.x - 12, player.y - 15))
    #pygame.draw.rect(WIN, "green", player) #hitbox do player

    for obstaculo in obstaculos:
        #if hit_itempergunta is True and origem_plano_resposta[0] < obstaculo.x < origem_plano_resposta[0] + bgp.get_width() and origem_plano_resposta[1] < obstaculo.y and origem_plano_resposta[1] + bgp.get_height():
       #     pass
        #else:
            #pygame.draw.rect(WIN, "yellow", obstaculo) #hitbox dos obstáculos
            WIN.blit(COVID, (obstaculo.x - 8, obstaculo.y -8))

    for itempergunta in itenspergunta:
        pygame.draw.rect(WIN, "blue", itempergunta) #hitbox dos obstáculos
        #WIN.blit(COVID, (itempergunta.x - 8, itempergunta.y -8))
    if not hit_itempergunta:
        pygame.display.update()