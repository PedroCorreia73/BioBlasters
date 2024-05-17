import pygame
import pygame_gui
from jogar import jogar


class Menu:
    def tela_inicial(tela):
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        tela.WIN.blit(pygame.transform.scale(BG_INICIO, (tela.WIN.get_width(), tela.WIN.get_height())), (0, 0))
        pygame.display.update()
        #iniciar_imagem = pygame.image.load("imagens/start.png")
        run = True
        proporcao_x = tela.WIN.get_width() / 1920 # (1920 x 1080) tamanho padrão no qual as telas foram feitas
        proporcao_y = tela.WIN.get_height() / 1080
        tamanho_botao = (360 * proporcao_x , 85 * proporcao_y)
        jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((781 * proporcao_x, 429 * proporcao_y), tamanho_botao),
                                             text='Jogar',
                                             manager=tela.manager)
        como_jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((781 * proporcao_x, 596 * proporcao_y), tamanho_botao),
                                             text='Como Jogar',
                                             manager=tela.manager)
        grupo_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((781 * proporcao_x, 762 * proporcao_y), tamanho_botao),
                                             text='Grupo',
                                             manager=tela.manager)
        ajustes_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((781 * proporcao_x, 929 * proporcao_y), tamanho_botao),
                                             text='Ajustes',
                                             manager=tela.manager)
        clock = pygame.time.Clock()
        while run:
            time_delta = clock.tick(60) / 1000.00
            #iniciar = Botao(WIDTH / 2, HEIGHT / 2, iniciar_imagem , 15)
            #iniciar.draw(BG_INICIO)
            
            #if iniciar.clicked == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == jogar_botao:
                        run = jogar(tela)
                        if run == False:
                            return
                        tela.WIN.blit(pygame.transform.scale(BG_INICIO, (tela.WIN.get_width(), tela.WIN.get_height())), (0, 0))
                # if event.type == pygame_gui.UI_BUTTON_ON_HOVERED:
                #     event.ui_element.set_dimensions((tamanho_botao[0] , 92 * proporcao_y))
                # if event.type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
                #     event.ui_element.set_dimensions((tamanho_botao))
                tela.manager.process_events(event)
            tela.manager.update(time_delta)
            tela.manager.draw_ui(tela.WIN)
            pygame.display.flip()


    def menu():
        pass