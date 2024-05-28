import pygame
import pygame_gui
import pygame_gui.elements.ui_panel
from pygame_gui.core import ObjectID

class TelaPerguntas:
    def __init__(self, tela):
        self.tela = tela
    def mostrar_perguntas(self, usuario):
        self.tela.manager.clear_and_reset()
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        tamanho_botao = self.tela.tamanho_botao
        caixa_fundo = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((296 * self.tela.proporcao_x, 415 * self.tela.proporcao_y),(1292 * self.tela.proporcao_x, 647 * self.tela.proporcao_y)),
                                                  manager=self.tela.manager)
        perguntas= pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((0, 0),(1163.75 * self.tela.proporcao_x, 400 * self.tela.proporcao_y)),
                                                            item_list=["Perguntas",
                                                                       "Pergunta",
                                                                       "Pergunta",
                                                                       "Pergunta",
                                                                       "Pergunta",
                                                                       "Pergunta",
                                                                       "Pergunta",
                                                                       "Pergunta",
                                                                       "Pergunta",
                                                                       "Pergunta",
                                                                       "Pergunta",
                                                                       "Pergunta",
                                                                       "Pergunta",
                                                                       "Pergunta"],
                                                            container=caixa_fundo,
                                                            anchors={"centerx":"centerx",
                                                                    "centery":"centery"},
                                                            manager=self.tela.manager)
        voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((144 * self.tela.proporcao_x, 45.58 * self.tela.proporcao_y), (86 * self.tela.proporcao_x, 50 * self.tela.proporcao_y)),
                                                    text="",
                                                    container=caixa_fundo,
                                                    object_id=ObjectID(class_id="@botao_voltar_pequeno"),
                                                    manager=self.tela.manager)
        clock = pygame.time.Clock()
        run = True
        while run:
            time_delta = clock.tick(60) / 1000.00
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == voltar_botao:
                        run = False
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return True
    