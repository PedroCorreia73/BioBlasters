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
        caixa_fundo = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 415 * self.tela.proporcao_y),(1400 * self.tela.proporcao_x, 647 * self.tela.proporcao_y)),
                                                  manager=self.tela.manager,
                                                  anchors={"centerx":"centerx"})
        perguntas= pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((0, 0),(1200 * self.tela.proporcao_x, 400 * self.tela.proporcao_y)),
                                                            item_list=["Perguntas",
                                                                       "Pergunta 1",
                                                                       "Pergunta 2",
                                                                       "Pergunta 3",
                                                                       "Pergunta 4",
                                                                       "Pergunta 5",
                                                                       "Pergunta 6",
                                                                       "Pergunta 7",
                                                                       "Pergunta 8",
                                                                       "Pergunta 9",
                                                                       "Pergunta 10",
                                                                       "Pergunta 11",
                                                                       "Pergunta 12",
                                                                       "Pergunta 13"],
                                                            allow_multi_select=False,
                                                            container=caixa_fundo,
                                                            anchors={"centerx":"centerx",
                                                                    "centery":"centery"},
                                                            manager=self.tela.manager)
        voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((-144 * self.tela.proporcao_x, 45.58 * self.tela.proporcao_y), (86 * self.tela.proporcao_x, 50 * self.tela.proporcao_y)),
                                                    text="",
                                                    container=caixa_fundo,
                                                    object_id=ObjectID(class_id="@botao_voltar_pequeno"),
                                                    anchors={"right":"right"},
                                                    manager=self.tela.manager)
        adicionar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((12.5 * self.tela.proporcao_x, -60 * self.tela.proporcao_y),(325 * self.tela.proporcao_x, 65 * self.tela.proporcao_y)),
                                                       text="Adicionar",
                                                       container=caixa_fundo,
                                                       anchors={"bottom":"bottom"},
                                                       manager=self.tela.manager)
        remover_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((12.5 * self.tela.proporcao_x,-60 * self.tela.proporcao_y),(325 * self.tela.proporcao_x, 65 * self.tela.proporcao_y)),
                                                       text="Remover",
                                                       container=caixa_fundo,
                                                       anchors={"left_target":adicionar_botao,
                                                                "bottom":"bottom"},
                                                       manager=self.tela.manager)
        editar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((12.5 * self.tela.proporcao_x, -60 * self.tela.proporcao_y),(325 * self.tela.proporcao_x, 65 * self.tela.proporcao_y)),
                                                       text="Editar",
                                                       container=caixa_fundo,
                                                       anchors={"left_target": remover_botao,
                                                                "bottom":"bottom"},
                                                       manager=self.tela.manager)
        visualizar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((12.5 * self.tela.proporcao_x, -60 * self.tela.proporcao_y),(325 * self.tela.proporcao_x, 65 * self.tela.proporcao_y)),
                                                       text="Visualizar",
                                                       container=caixa_fundo,
                                                       anchors={"left_target":editar_botao,
                                                                "bottom":"bottom"},
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
                    elif event.ui_element == remover_botao:
                        perguntas.remove_items(perguntas.get_single_selection())
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return True
    