import pygame
import pygame_gui
from telas.tela_jogar import TelaJogar
from telas.tela_grupo import TelaGrupo
from telas.tela_perguntas import TelaPerguntas
from telas.tela_ajustes import TelaAjustes


class Menu:
    def __init__(self, tela):
        self.tela = tela

    def aluno(self, usuario):
        self.tela.manager.clear_and_reset()  # Reseta os elementos do pygame_gui
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 429 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Jogar',
                                             manager=self.tela.manager,
                                             anchors={"centerx":"centerx"})
        como_jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 596 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Como Jogar',
                                             manager=self.tela.manager,
                                             anchors={"centerx":"centerx"})
        grupo_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 762 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Grupo',
                                             manager=self.tela.manager,
                                             anchors={"centerx":"centerx"})
        ajustes_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 929 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Ajustes',
                                             manager=self.tela.manager,
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
                        repetir = TelaJogar.jogar(self.tela)
                        return repetir
                    elif event.ui_element == grupo_botao:
                        tela_grupo = TelaGrupo(self.tela)
                        repetir = tela_grupo.entrar_grupo(usuario)
                        return repetir
                    elif event.ui_element == ajustes_botao:
                        tela_ajustes = TelaAjustes(self.tela)
                        repetir = tela_ajustes.ajustes()
                        return repetir
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return False

    def professor(self, usuario):
        self.tela.manager.clear_and_reset()  # Reseta os elementos do pygame_gui
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 403 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Jogar',
                                             manager=self.tela.manager,
                                             anchors={"centerx":"centerx"})
        como_jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 553 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Como Jogar',
                                             manager=self.tela.manager,
                                             anchors={"centerx":"centerx"})
        grupo_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 693 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Grupo',
                                             manager=self.tela.manager,
                                             anchors={"centerx":"centerx"})
        ajustes_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 834 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Ajustes',
                                             manager=self.tela.manager,
                                             anchors={"centerx":"centerx"})
        perguntas_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0 * self.tela.proporcao_x, 974 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Perguntas',
                                             manager=self.tela.manager,
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
                        repetir = TelaJogar.jogar(self.tela)
                        return repetir
                    elif event.ui_element == grupo_botao:
                        tela_grupo = TelaGrupo(self.tela)
                        repetir = tela_grupo.criar_grupo(usuario)
                        return repetir
                    elif event.ui_element == ajustes_botao:
                        tela_ajustes = TelaAjustes(self.tela)
                        repetir = tela_ajustes.ajustes()
                        return repetir
                    elif event.ui_element == perguntas_botao:
                        tela_perguntas = TelaPerguntas(self.tela)
                        repetir = tela_perguntas.mostrar_perguntas(usuario)
                        return repetir
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return False
    def administrador(self, usuario):
        self.tela.manager.clear_and_reset()  # Reseta os elementos do pygame_gui
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 403 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Jogar',
                                             manager=self.tela.manager,
                                             anchors={"centerx":"centerx"})
        como_jogar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 553 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Como Jogar',
                                             manager=self.tela.manager,
                                             anchors={"centerx":"centerx"})
        clock = pygame.time.Clock()
        run = True
        while run:
            time_delta = clock.tick(60) / 1000.00
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return False