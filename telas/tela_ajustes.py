import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from usuario.usuario_atual import Aluno, Professor
from banco_de_dados.aluno import AlunoDAO
from banco_de_dados.professor import ProfessorDAO

class TelaAjustes:
    def __init__(self, tela):
        self.tela = tela

    def ajustes(self, usuario):
        continuar = True
        while continuar:
            self.tela.manager.clear_and_reset()
            BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
            pygame.display.update()
            caixa_fundo = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 415 * self.tela.proporcao_y),(1400 * self.tela.proporcao_x, 650 * self.tela.proporcao_y)),
                                                    manager=self.tela.manager,
                                                    anchors={"centerx":"centerx"})
            voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((-144 * self.tela.proporcao_x, 23), (120 * self.tela.proporcao_x, 80 * self.tela.proporcao_y)),
                                                            text="",
                                                            container=caixa_fundo,
                                                            object_id=ObjectID(class_id="@botao_voltar_pequeno"),
                                                            anchors={"right":"right"},
                                                            manager=self.tela.manager)
            alterar_senha_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (-1, -1)),
                                                            text="Alterar Senha",
                                                            container=caixa_fundo,
                                                            anchors={"centerx":"centerx",
                                                                     "centery":"centery"},
                                                            manager=self.tela.manager)
            video_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, -alterar_senha_botao.relative_rect.height), (alterar_senha_botao.relative_rect.size)),
                                                            text="Video",
                                                            container=caixa_fundo,
                                                            anchors={"centerx":"centerx",
                                                                     "centery":"centery"},
                                                            manager=self.tela.manager)
            audio_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (alterar_senha_botao.relative_rect.size)),
                                                            text="Audio",
                                                            container=caixa_fundo,
                                                            anchors={"centerx":"centerx",
                                                                     "top_target" : alterar_senha_botao,
                                                                     "bottom_target": caixa_fundo},
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
                            return True
                        elif event.ui_element == video_botao:
                            repetir = self.video()
                            if not repetir:
                                return False
                            run = False
                        elif event.ui_element == alterar_senha_botao:
                            repetir = self.alterar_senha(usuario)
                            if not repetir:
                                return False
                            run = False
                    self.tela.manager.process_events(event)
                self.tela.manager.update(time_delta)
                self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
                self.tela.manager.draw_ui(self.tela.WIN)
                pygame.display.flip()
        return True

    def video(self):
        self.tela.manager.clear_and_reset()
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        configuracoes_tela = pygame_gui.elements.UIDropDownMenu(options_list=[f"{self.tela.WIDTH} x {self.tela.HEIGHT}", "1920 x 1080","1600 x 900", "1280 x 720"],
                                                                starting_option=f"{self.tela.WIDTH} x {self.tela.HEIGHT}",
                                                                relative_rect=((300 * self.tela.proporcao_x, 600 * self.tela.proporcao_y), (self.tela.tamanho_botao)),
                                                                manager=self.tela.manager)
        voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300 * self.tela.proporcao_x, 800 * self.tela.proporcao_y), (758 * self.tela.proporcao_x, 246 * self.tela.proporcao_y)),
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
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == voltar_botao:
                        run = False
                elif event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
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
    
    def alterar_senha(self, usuario):
        self.tela.manager.clear_and_reset()
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        caixa_fundo = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 415 * self.tela.proporcao_y),(1400 * self.tela.proporcao_x, 650 * self.tela.proporcao_y)),
                                                    manager=self.tela.manager,
                                                    anchors={"centerx":"centerx"})
        voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((-144 * self.tela.proporcao_x, 23), (120 * self.tela.proporcao_x, 80 * self.tela.proporcao_y)),
                                                        text="",
                                                        container=caixa_fundo,
                                                        object_id=ObjectID(class_id="@botao_voltar_pequeno"),
                                                        anchors={"right":"right"},
                                                        manager=self.tela.manager)
        nova_senha_texto = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((0, 0),(caixa_fundo.relative_rect.width/2, 85 * self.tela.proporcao_y)),
                                                               placeholder_text="Nova Senha",
                                                               container=caixa_fundo,
                                                               anchors={"centerx" : "centerx",
                                                                        "centery" : "centery"},
                                                               manager=self.tela.manager)
        confirmar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, -60 * self.tela.proporcao_y),(-1, -1)),
                                                        text="Confirmar",
                                                        container=caixa_fundo,
                                                        anchors={"centerx" : "centerx",
                                                                    "bottom":"bottom"},
                                                        manager=self.tela.manager)
        clock = pygame.time.Clock()
        run = True
        while run:
            time_delta = clock.tick(60) / 1000.00
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                    if event.ui_element == nova_senha_texto:
                        if nova_senha_texto.get_text() == "":
                            nova_senha_texto.set_text_hidden(is_hidden=False)
                        else:
                            nova_senha_texto.set_text_hidden(is_hidden=True)
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == voltar_botao:
                        run = False
                    elif event.ui_element == confirmar_botao:
                        nova_senha = nova_senha_texto.get_text()
                        if len(nova_senha) >= 4:
                            if nova_senha == usuario.senha:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                            manager=self.tela.manager,
                                                                                            html_message='<p>A senha deve ser diferente da última</p>')
                            else:    
                                if isinstance(usuario, Aluno):
                                    alunodao = AlunoDAO()
                                    alunodao.alterar_senha(usuario.id, nova_senha)
                                elif isinstance(usuario, Professor):
                                    professordao = ProfessorDAO()
                                    professordao.alterar_senha(usuario.id, nova_senha)
                                usuario.senha = nova_senha
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                            manager=self.tela.manager,
                                                                                            html_message='<p>Senha alterada</p>')
                                nova_senha_texto.set_text("")
                                nova_senha_texto.set_text_hidden(is_hidden=False)
                        else:
                            pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                            manager=self.tela.manager,
                                                                                            html_message='<p>A senha deve possuir pelo menos 4 caracteres</p>')    
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return True