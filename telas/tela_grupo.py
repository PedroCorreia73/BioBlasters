import pygame
import pygame_gui
from banco_de_dados.grupo import GrupoDAO

class TelaGrupo:
    def __init__(self,tela):
        self.tela = tela
        
    def entrar_grupo(self, usuario):
        self.tela.manager.clear_and_reset()
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
        pygame.display.update()
        tamanho_botao = 758 * self.tela.proporcao_x, 246 * self.tela.proporcao_y
        codigo_texto = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((581 * self.tela.proporcao_y, 434 * self.tela.proporcao_y),(tamanho_botao)),
                                             placeholder_text='Código',
                                             manager=self.tela.manager)
        entrar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((268 * self.tela.proporcao_x, 768 * self.tela.proporcao_y),(tamanho_botao)),
                                                    text="Entrar",
                                                    manager=self.tela.manager)
        voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1250 * self.tela.proporcao_x, 768 * self.tela.proporcao_y), (tamanho_botao)),
                                                    text="",
                                                    manager=self.tela.manager)
        # codigo_texto.set_allowed_characters('numbers')
        clock = pygame.time.Clock()
        run = True
        while run:
            time_delta = clock.tick(60) / 1000.00
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == entrar_botao:
                        codigo = codigo_texto.get_text()
                        if codigo != None:
                            grupo = GrupoDAO.procurar_grupo(codigo)
                            print(grupo)
                            if len(grupo) == 0:
                                print("Sem valor")
                            else:
                                usuario.id_grupo = grupo[0][0]
                                print(usuario.id_grupo)
                                run = False
                    elif event.ui_element == voltar_botao:
                        run = False
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return True