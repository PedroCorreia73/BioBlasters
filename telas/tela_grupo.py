import pygame
import pygame_gui
from pygame_gui.core import ObjectID 
from banco_de_dados.grupo import GrupoDAO
from banco_de_dados.professor import ProfessorDAO
from banco_de_dados.aluno import AlunoDAO

class TelaGrupo:
    def __init__(self,tela, usuario):
        self.tela = tela
        self.usuario = usuario
        self.alunodao = AlunoDAO()
        self.professordao = ProfessorDAO()
        
    def entrar_grupo(self):
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
                            grupodao = GrupoDAO()
                            grupo = grupodao.procurar_grupo_por_codigo(codigo)
                            if len(grupo) == 0:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message=f'<p>O grupo não existe</p>')
                            else:
                                self.usuario.id_grupo = grupo[0][0]
                                self.alunodao.vincular_grupo(self.usuario.id_grupo, self.usuario.id)
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
    
    def criar_grupo(self):
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
        criar_grupo_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 768 * self.tela.proporcao_y), (tamanho_botao)),
                                                    text="Criar Grupo",
                                                    anchors={"centerx" : "centerx"},
                                                    manager=self.tela.manager)
        voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((-400 * self.tela.proporcao_x, 768 * self.tela.proporcao_y), (tamanho_botao[0] / 2, tamanho_botao[1])),
                                                    text="",
                                                    object_id=ObjectID(class_id="@botao_voltar"),
                                                    anchors={"right":"right"},
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
                            verificar = grupo.procurar_grupo()
                            if len(verificar) == 0:
                                grupo.adicionar_grupo()
                                self.usuario.id_grupo = grupo.id
                                self.professordao.vincular_grupo(self.usuario.id_grupo, self.usuario.id)
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
        
    def manter_grupo(self):
        continuar = True
        while continuar:
            self.tela.manager.clear_and_reset()
            grupodao = GrupoDAO()
            grupo = grupodao.mostrar_informacoes(self.usuario.id_grupo)
            lista_de_alunos = self.alunodao.ver_alunos_do_grupo(self.usuario.id_grupo)
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
            codigo_grupo = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20 * self.tela.proporcao_x, 50 * self.tela.proporcao_y),(-1,-1)),
                                                    text=f"Código Grupo: {grupo["codigo_grupo"]}",
                                                    container=caixa_fundo,
                                                    anchors={"left" : "left",
                                                                "top":"top"},
                                                    manager=self.tela.manager)
            nome_grupo = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20 * self.tela.proporcao_x, 50 * self.tela.proporcao_y),(-1,-1)),
                                                    text=f"Nome Grupo: {grupo["nome_grupo"]}",
                                                    container=caixa_fundo,
                                                    anchors={"left_target" : codigo_grupo,
                                                                "top":"top"},
                                                    manager=self.tela.manager)
            alunos = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((0, 0),(1200 * self.tela.proporcao_x, 400 * self.tela.proporcao_y)),
                                                                    item_list=lista_de_alunos,
                                                                    allow_multi_select=False,
                                                                    container=caixa_fundo,
                                                                    anchors={"centerx":"centerx",
                                                                            "centery":"centery"},
                                                                    manager=self.tela.manager)
            remover_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, -60 * self.tela.proporcao_y),(-1, -1)),
                                                        text="Remover Aluno",
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
                    elif event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                            if event.ui_element == remover_confirmacao:
                                aluno = AlunoDAO(usuario_aluno)
                                id_aluno = aluno.obter_id_aluno()[0]
                                self.alunodao.remover_aluno_do_grupo(id_aluno)
                                run = False
                    elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == voltar_botao:
                            return True
                        elif event.ui_element == remover_botao:
                            usuario_aluno = alunos.get_single_selection()
                            if usuario_aluno == None:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                         html_message="<p>Selecione um aluno</p>")
                            else:
                                remover_confirmacao = pygame_gui.windows.UIConfirmationDialog(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                manager=self.tela.manager,
                                                                                action_long_desc= "<p>Deseja mesmo remover o aluno do grupo?</p>")                
                    self.tela.manager.process_events(event)
                self.tela.manager.update(time_delta)
                self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
                self.tela.manager.draw_ui(self.tela.WIN)
                pygame.display.flip()
        return True

    def informacoes_grupo(self):
        self.tela.manager.clear_and_reset()
        grupodao = GrupoDAO()
        grupo = grupodao.mostrar_informacoes(self.usuario.id_grupo)
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
        codigo_grupo = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20 * self.tela.proporcao_x, 50 * self.tela.proporcao_y),(-1,-1)),
                                                   text=f"Código Grupo: {grupo["codigo_grupo"]}",
                                                   container=caixa_fundo,
                                                   anchors={"left" : "left",
                                                            "top":"top"},
                                                   manager=self.tela.manager)
        nome_grupo = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20 * self.tela.proporcao_x, 50 * self.tela.proporcao_y),(-1,-1)),
                                                   text=f"Nome Grupo: {grupo["nome_grupo"]}",
                                                   container=caixa_fundo,
                                                   anchors={"left_target" : codigo_grupo,
                                                            "top":"top"},
                                                   manager=self.tela.manager)
        caixa_dentro = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0,0),(1122 * self.tela.proporcao_x, 446 * self.tela.proporcao_y)),
                                                   container=caixa_fundo,
                                                   anchors={"centerx" : "centerx",
                                                            "centery" : "centery"},
                                                   manager=self.tela.manager)
        nome_usuario = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0,20 *self.tela.proporcao_y),(-1,-1)),
                                                   text=f"Usuário: {self.usuario.nome}",
                                                   container=caixa_dentro,
                                                   anchors={"centerx" : "centerx",
                                                            "top":"top"},
                                                   manager=self.tela.manager)
        senha_usuario = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0,20 *self.tela.proporcao_y),(-1,-1)),
                                                    text=f"Senha: {self.usuario.senha}",
                                                    container=caixa_dentro,
                                                    anchors={"centerx" : "centerx",
                                                             "top_target":nome_usuario},
                                                    manager=self.tela.manager)
        pontuacao_maxima = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0,20 *self.tela.proporcao_y),(-1,-1)),
                                                       text=f"Pontuação máxima: {self.usuario.pontuacao}",
                                                        container=caixa_dentro,
                                                        anchors={"centerx" : "centerx",
                                                                 "top_target":senha_usuario},
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
                        return True
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return True
        
        
