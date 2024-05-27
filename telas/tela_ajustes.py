import pygame
import pygame_gui
from pygame_gui.core import ObjectID

class TelaAjustes:
    def __init__(self, tela):
        self.tela = tela
    def ajustes(self):
        self.tela.manager.clear_and_reset()
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        tamanho_botao = 758 * self.tela.proporcao_x, 246 * self.tela.proporcao_y
        configuracoes_tela = pygame_gui.elements.UIDropDownMenu(options_list=[f"{self.tela.WIDTH} x {self.tela.HEIGHT}", "1920 x 1080","1600 x 900", "1280 x 720"],
                                                                starting_option=f"{self.tela.WIDTH} x {self.tela.HEIGHT}",
                                                                relative_rect=((300 * self.tela.proporcao_x, 600 * self.tela.proporcao_y), (self.tela.tamanho_botao)),
                                                                manager=self.tela.manager)
        voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300 * self.tela.proporcao_x, 800 * self.tela.proporcao_y), (tamanho_botao)),
                                                    text="",
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
                if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    if event.ui_element == configuracoes_tela:
                        medidas = event.text.split(" x ")
                        self.tela.WIDTH = int(medidas[0])
                        self.tela.HEIGHT = int(medidas[1])
                        self.tela.WIN = pygame.display.set_mode((self.tela.WIDTH, self.tela.HEIGHT))
                        self.tela.manager.set_window_resolution((self.tela.WIDTH, self.tela.HEIGHT))
                        self.tela.proporcao_x = self.tela.WIN.get_width() / 1920 # (1920 x 1080) tamanho padrão no qual as telas foram feitas
                        self.tela.proporcao_y = self.tela.WIN.get_height() / 1080
                        self.tela.tamanho_botao = (360 * self.tela.proporcao_x , 85 * self.tela.proporcao_y)
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return True