import pygame
import pygame_gui
from telas.tela_jogar import TelaJogar


class Menu:
    def menu_aluno(tela):
        tela.manager.clear_and_reset()  # Reseta os elementos do pygame_gui
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        tela.WIN.blit(pygame.transform.scale(BG_INICIO, (tela.WIN.get_width(), tela.WIN.get_height())), (0, 0))
        pygame.display.update()
        jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((tela.centralizar_x, 429 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Jogar',
                                             manager=tela.manager)
        como_jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((tela.centralizar_x, 596 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Como Jogar',
                                             manager=tela.manager)
        grupo_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((tela.centralizar_x, 762 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Grupo',
                                             manager=tela.manager)
        ajustes_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((tela.centralizar_x, 929 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Ajustes',
                                             manager=tela.manager)
        clock = pygame.time.Clock()
        run = True
        while run:
            time_delta = clock.tick(60) / 1000.00

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == jogar_botao:
                        repetir = TelaJogar.jogar(tela)
                        if repetir == True:
                            return True
                        else:
                            return False
                    elif event.ui_element == pygame_gui.UI_BUTTON_PRESSED:
                        
                        pass
                # if event.type == pygame_gui.UI_BUTTON_ON_HOVERED:
                #     event.ui_element.set_dimensions((tamanho_botao[0] , 92 * tela.proporcao_y))
                # if event.type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
                #     event.ui_element.set_dimensions((tamanho_botao))
                tela.manager.process_events(event)
            tela.manager.update(time_delta)
            tela.manager.draw_ui(tela.WIN)
            pygame.display.flip()
        return False

    def menu_professor(tela):
        pass
    def menu_administrador(tela):
        pass