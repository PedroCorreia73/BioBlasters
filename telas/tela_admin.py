import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from banco_de_dados.aluno import AlunoDAO
from banco_de_dados.professor import ProfessorDAO
from usuario.usuario_atual import Aluno, Professor


class TelaAdmin:
    def __init__(self, tela):
        self.tela = tela
        self.alunodao = AlunoDAO()
        self.professordao = ProfessorDAO()

    def manter_alunos(self):
        continuar = True
        while continuar:
            self.tela.manager.clear_and_reset()
            lista_de_alunos = self.alunodao.ver_todos_alunos()
            lista_de_alunos = [aluno[0] for aluno in lista_de_alunos]
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
            alunos = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((0, 0),(1200 * self.tela.proporcao_x, 360 * self.tela.proporcao_y)),
                                                                    item_list=lista_de_alunos,
                                                                    allow_multi_select=False,
                                                                    container=caixa_fundo,
                                                                    anchors={"centerx":"centerx",
                                                                            "centery":"centery"},
                                                                    manager=self.tela.manager)
            remover_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, -120 * self.tela.proporcao_y),(-1, -1)),
                                                        text="Remover Aluno",
                                                        container=caixa_fundo,
                                                        anchors={"centerx" : "centerx",
                                                                    "bottom":"bottom"},
                                                        manager=self.tela.manager)
            alterar_senha = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0),(remover_botao.relative_rect.size)),
                                                        text="Alterar Senha",
                                                        container=caixa_fundo,
                                                        anchors={"centerx" : "centerx",
                                                                    "top_target":remover_botao},
                                                        manager=self.tela.manager)
            clock = pygame.time.Clock()
            run = True
            while run:
                time_delta = clock.tick(60) / 1000.00
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    elif event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                        if event.ui_element == remover_confirmacao:
                            aluno = AlunoDAO(usuario_aluno)
                            id_aluno = aluno.obter_id_aluno()[0]
                            self.alunodao.remover_aluno(id_aluno)
                            run = False
                    elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == voltar_botao:
                            return True
                        elif event.ui_element == alterar_senha:
                            usuario_aluno = alunos.get_single_selection()
                            if usuario_aluno == None:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                         html_message="<p>Selecione um aluno</p>")
                            else:
                                aluno = AlunoDAO(usuario_aluno)
                                id_aluno = aluno.obter_id_aluno()[0]
                                repetir = self.alterar_senha(id_aluno, Aluno())
                                if not repetir:
                                    return False
                                else:
                                    run = False
                        elif event.ui_element == remover_botao:
                            usuario_aluno = alunos.get_single_selection()
                            if usuario_aluno == None:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                         html_message="<p>Selecione um aluno</p>")
                            else:
                                remover_confirmacao = pygame_gui.windows.UIConfirmationDialog(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                manager=self.tela.manager,
                                                                                action_long_desc= "<p>Deseja mesmo remover o aluno?</p>")                
                    self.tela.manager.process_events(event)
                self.tela.manager.update(time_delta)
                self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
                self.tela.manager.draw_ui(self.tela.WIN)
                pygame.display.flip()
        return True
    
    def manter_professores(self):
        continuar = True
        while continuar:
            self.tela.manager.clear_and_reset()
            lista_de_professores = self.professordao.ver_todos_professores()
            lista_de_professores = [professor[0] for professor in lista_de_professores]
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
            professores = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((0, 0),(1200 * self.tela.proporcao_x, 360 * self.tela.proporcao_y)),
                                                                    item_list=lista_de_professores,
                                                                    allow_multi_select=False,
                                                                    container=caixa_fundo,
                                                                    anchors={"centerx":"centerx",
                                                                            "centery":"centery"},
                                                                    manager=self.tela.manager)
            remover_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, -120 * self.tela.proporcao_y),(-1, -1)),
                                                        text="Remover Professor",
                                                        container=caixa_fundo,
                                                        anchors={"centerx" : "centerx",
                                                                    "bottom":"bottom"},
                                                        manager=self.tela.manager)
            alterar_senha = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0),(remover_botao.relative_rect.size)),
                                                        text="Alterar Senha",
                                                        container=caixa_fundo,
                                                        anchors={"centerx" : "centerx",
                                                                    "top_target":remover_botao},
                                                        manager=self.tela.manager)
            clock = pygame.time.Clock()
            run = True
            while run:
                time_delta = clock.tick(60) / 1000.00
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    elif event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                        if event.ui_element == remover_confirmacao:
                            professor = ProfessorDAO(usuario_professor)
                            id_professor = professor.obter_id_professor()[0]
                            self.professordao.remover_professor(id_professor)
                            run = False
                    elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == voltar_botao:
                            return True
                        elif event.ui_element == alterar_senha:
                            usuario_professor = professores.get_single_selection()
                            if usuario_professor == None:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                         html_message="<p>Selecione um professor</p>")
                            else:
                                professor = ProfessorDAO(usuario_professor)
                                id_professor = professor.obter_id_professor()[0]
                                repetir = self.alterar_senha(id_professor, Professor())
                                if not repetir:
                                    return False
                                else:
                                    run = False
                        elif event.ui_element == remover_botao:
                            usuario_professor = professores.get_single_selection()
                            if usuario_professor == None:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                         html_message="<p>Selecione um professor</p>")
                            else:
                                remover_confirmacao = pygame_gui.windows.UIConfirmationDialog(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                manager=self.tela.manager,
                                                                                action_long_desc= "<p>Deseja mesmo remover o professor?</p>")                
                    self.tela.manager.process_events(event)
                self.tela.manager.update(time_delta)
                self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
                self.tela.manager.draw_ui(self.tela.WIN)
                pygame.display.flip()
        return True

    def alterar_senha(self, id_usuario, usuario):
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
                            if isinstance(usuario, Aluno):
                                alunodao = AlunoDAO()
                                alunodao.alterar_senha(id_usuario, nova_senha)
                            elif isinstance(usuario, Professor):
                                professordao = ProfessorDAO()
                                professordao.alterar_senha(id_usuario, nova_senha)
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