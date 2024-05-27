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
        usuario_texto = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect((368.83 * self.tela.proporcao_x , 453.23 * self.tela.proporcao_y), tamanho_botao),
                                            placeholder_text = "Usuário", 
                                            container =caixa_fundo,                                   
                                            manager = self.tela.manager)
        voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300 * self.tela.proporcao_x, 460.58 * self.tela.proporcao_y), (83.92 * self.tela.proporcao_x, 48.53 * self.tela.proporcao_y)),
                                                    text="",
                                                    container=caixa_fundo,
                                                    object_id=ObjectID(class_id="@botao_voltar"),
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
    