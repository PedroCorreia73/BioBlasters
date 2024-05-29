import pygame
import pygame_gui
from pygame_gui.core import ObjectID 
from banco_de_dados.grupo import GrupoDAO
from banco_de_dados.professor import ProfessorDAO
from banco_de_dados.aluno import AlunoDAO

class TelaGrupo:
    def __init__(self,tela):
        self.tela = tela
        
    def entrar_grupo(self, usuario):
        self.tela.manager.clear_and_reset()
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
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
                    if event.ui_element == entrar_botao:
                        codigo = codigo_texto.get_text()
                        if codigo != None:
                            grupo = GrupoDAO.procurar_grupo_por_codigo(codigo)
                            if len(grupo) == 0:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message=f'<p>O grupo não existe</p>')
                            else:
                                usuario.id_grupo = grupo[0][0]
                                AlunoDAO.vincular_grupo(usuario)
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message=f'<p>Bem vindo ao grupo: {grupo[0][1]}</p>')
                    elif event.ui_element == voltar_botao:
                        run = False
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return True
    
    def criar_grupo(self, usuario):
        self.tela.manager.clear_and_reset()
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        tamanho_botao = (758 * self.tela.proporcao_x, 246 * self.tela.proporcao_y)
        tamanho_texto = (800 * self.tela.proporcao_x, 85 * self.tela.proporcao_y)
        nome_grupo_texto = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((0 * self.tela.proporcao_y, 434 * self.tela.proporcao_y),(tamanho_texto)),
                                             placeholder_text='Nome do Grupo',
                                             manager=self.tela.manager,
                                             anchors={"centerx":"centerx"})
        codigo_grupo_texto = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((0 * self.tela.proporcao_y, 600 * self.tela.proporcao_y),(tamanho_texto)),
                                             placeholder_text='Código do Grupo',
                                             manager=self.tela.manager,
                                             anchors={"centerx":"centerx"})
        criar_grupo_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1920 / 2 * self.tela.proporcao_x - tamanho_botao[0], 768 * self.tela.proporcao_y), (tamanho_botao)),
                                                    text="Criar Grupo",
                                                    manager=self.tela.manager)
        voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1920 / 2 * self.tela.proporcao_x, 768 * self.tela.proporcao_y), (tamanho_botao)),
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
                    if event.ui_element == criar_grupo_botao:
                        nome = nome_grupo_texto.get_text()
                        codigo = codigo_grupo_texto.get_text()
                        if codigo != "" and nome != "":
                            grupo = GrupoDAO(nome, codigo)
                            verificar = GrupoDAO.procurar_grupo(grupo)
                            if len(verificar) == 0:
                                GrupoDAO.adicionar_grupo(grupo)
                                usuario.id_grupo = grupo.id
                                ProfessorDAO.vincular_grupo(usuario)
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message=f'<p>Grupo criado</p>')
                            else:
                                if verificar[0][1] == nome:
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message=f'<p>O nome de grupo: {nome} já está em uso</p>')
                                else:
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message=f'<p>O código de grupo: {codigo} já está em uso</p>')
                        else:
                             pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message=f'<p>Preencha os campos de nome e código do grupo</p>')
                    elif event.ui_element == voltar_botao:
                        return True
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return True
        
