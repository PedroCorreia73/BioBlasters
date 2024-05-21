import pygame
import pygame_gui
from usuario.usuario_atual import Aluno, Professor, Administrador

class TelaSelecionar:
    def selecionar(tela):
        tela.manager.clear_and_reset()  # Reseta os elementos do pygame_gui
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        tela.WIN.blit(pygame.transform.scale(BG_INICIO, (tela.WIN.get_width(), tela.WIN.get_height())), (0, 0))
        pygame.display.update()
        aluno_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1920 / 2 * tela.proporcao_x - tela.tamanho_botao[0] , 500 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Aluno',
                                             manager=tela.manager)
        professor_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1920 / 2 * tela.proporcao_x, 500 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Professor',
                                             manager=tela.manager)
        administrador_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1920 / 2 * tela.proporcao_x, 900 * tela.proporcao_y), tela.tamanho_botao),
                                             text=' ',
                                             manager=tela.manager)
        clock = pygame.time.Clock()
        run = True
        while run:
            time_delta = clock.tick(60) / 1000.00
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == aluno_botao:
                        return Aluno()
                    elif event.ui_element == professor_botao:
                        return Professor()
                    elif event.ui_element == administrador_botao:
                        return Administrador()
                tela.manager.process_events(event)
            tela.manager.update(time_delta)
            tela.manager.draw_ui(tela.WIN)
            pygame.display.flip()