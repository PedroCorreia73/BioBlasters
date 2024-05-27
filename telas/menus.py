import pygame
import pygame_gui
from telas.tela_jogar import TelaJogar
from telas.tela_grupo import TelaGrupo
from telas.tela_perguntas import TelaPerguntas
from telas.tela_ajustes import TelaAjustes


class Menu:
    def aluno(self, tela, usuario):
        tela.manager.clear_and_reset()  # Reseta os elementos do pygame_gui
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 429 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Jogar',
                                             manager=tela.manager,
                                             anchors={"centerx":"centerx"})
        como_jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 596 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Como Jogar',
                                             manager=tela.manager,
                                             anchors={"centerx":"centerx"})
        grupo_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 762 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Grupo',
                                             manager=tela.manager,
                                             anchors={"centerx":"centerx"})
        ajustes_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 929 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Ajustes',
                                             manager=tela.manager,
                                             anchors={"centerx":"centerx"})
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
                        return repetir
                    elif event.ui_element == grupo_botao:
                        tela_grupo = TelaGrupo(tela)
                        repetir = tela_grupo.entrar_grupo(usuario)
                        return repetir
                    elif event.ui_element == ajustes_botao:
                        tela_ajustes = TelaAjustes(tela)
                        repetir = tela_ajustes.ajustes()
                        return repetir
                tela.manager.process_events(event)
            tela.manager.update(time_delta)
            tela.WIN.blit(pygame.transform.scale(BG_INICIO, (tela.WIN.get_width(), tela.WIN.get_height())), (0, 0))
            tela.manager.draw_ui(tela.WIN)
            pygame.display.flip()
        return False

    def professor(self, tela, usuario):
        tela.manager.clear_and_reset()  # Reseta os elementos do pygame_gui
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 403 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Jogar',
                                             manager=tela.manager,
                                             anchors={"centerx":"centerx"})
        como_jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 553 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Como Jogar',
                                             manager=tela.manager,
                                             anchors={"centerx":"centerx"})
        grupo_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 693 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Grupo',
                                             manager=tela.manager,
                                             anchors={"centerx":"centerx"})
        ajustes_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 834 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Ajustes',
                                             manager=tela.manager,
                                             anchors={"centerx":"centerx"})
        perguntas_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0 * tela.proporcao_x, 974 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Perguntas',
                                             manager=tela.manager,
                                             anchors={"centerx":"centerx"})
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
                        return repetir
                    elif event.ui_element == grupo_botao:
                        tela_grupo = TelaGrupo(tela)
                        repetir = tela_grupo.criar_grupo(usuario)
                        return repetir
                    elif event.ui_element == ajustes_botao:
                        tela_ajustes = TelaAjustes(tela)
                        repetir = tela_ajustes.ajustes()
                        return repetir
                    elif event.ui_element == perguntas_botao:
                        tela_perguntas = TelaPerguntas(tela)
                        repetir = tela_perguntas.mostrar_perguntas(usuario)
                        return repetir
                tela.manager.process_events(event)
            tela.manager.update(time_delta)
            tela.WIN.blit(pygame.transform.scale(BG_INICIO, (tela.WIN.get_width(), tela.WIN.get_height())), (0, 0))
            tela.manager.draw_ui(tela.WIN)
            pygame.display.flip()
        return False
    def administrador(tela):
        pass