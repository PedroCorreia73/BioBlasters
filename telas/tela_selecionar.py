import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from usuario.usuario_atual import Aluno, Professor, Administrador

class TelaSelecionar:
    def __init__(self,tela):
        self.tela = tela

    def selecionar(self):
        self.tela.manager.clear_and_reset()  # Reseta os elementos do pygame_gui
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        aluno_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1920 / 2 * self.tela.proporcao_x - self.tela.tamanho_botao[0] , 500 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Aluno',
                                             manager=self.tela.manager)
        professor_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1920 / 2 * self.tela.proporcao_x, 500 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Professor',
                                             manager=self.tela.manager)
        administrador_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((-180 * self.tela.proporcao_x,-150 * self.tela.proporcao_y), (200 * self.tela.proporcao_x , 150 * self.tela.proporcao_y)),
                                             text='',
                                             object_id=ObjectID(class_id="@botao_admin"),
                                             anchors={"bottom":"bottom",
                                                      "right":"right"},
                                             manager=self.tela.manager)
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
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()