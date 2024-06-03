import pygame
import pygame_gui
import pygame_gui.elements.ui_panel
from banco_de_dados.pergunta import PerguntaAlternativasDAO, AlternativaDAO
from pygame_gui.core import ObjectID

class TelaPerguntas:
    def __init__(self, tela):
        self.tela = tela
        self.alternativas = ["","","","",""]
        self.enunciado = ""
    def mostrar_perguntas(self, usuario):
        continuar = True
        while continuar:
            self.tela.manager.clear_and_reset()
            BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
            pygame.display.update()
            lista_de_perguntas = self.obter_perguntas(usuario)
            caixa_fundo = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 415 * self.tela.proporcao_y),(1400 * self.tela.proporcao_x, 650 * self.tela.proporcao_y)),
                                                    manager=self.tela.manager,
                                                    anchors={"centerx":"centerx"})
            perguntas= pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((0, 0),(1200 * self.tela.proporcao_x, 400 * self.tela.proporcao_y)),
                                                                item_list=lista_de_perguntas,
                                                                allow_multi_select=False,
                                                                container=caixa_fundo,
                                                                anchors={"centerx":"centerx",
                                                                        "centery":"centery"},
                                                                manager=self.tela.manager)
            voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((-144 * self.tela.proporcao_x, 23), (120 * self.tela.proporcao_x, 80 * self.tela.proporcao_y)),
                                                        text="",
                                                        container=caixa_fundo,
                                                        object_id=ObjectID(class_id="@botao_voltar_pequeno"),
                                                        anchors={"right":"right",
                                                                 "top":"top"},
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
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20 * self.tela.proporcao_x, 50 * self.tela.proporcao_y), (-1,-1)),
                                        container=caixa_fundo,
                                        anchors={"bottom_target" : perguntas},
                                        text="Perguntas:",
                                        manager=self.tela.manager)
            
            clock = pygame.time.Clock()
            run = True
            while run:
                time_delta = clock.tick(60) / 1000.00
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    if event.type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                        if event.ui_element == remover_confirmacao:
                            continuar = self.remover_pergunta(pergunta_selecionada.split()[0], usuario.id_grupo)
                            if continuar == False:
                                return False
                            else:
                                run = False
                    elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == voltar_botao:
                            return True
                        elif event.ui_element == adicionar_botao:
                            continuar = self.adicionar_perguntas(usuario)
                            if continuar == False:
                                return False
                            else:
                                run = False
                        elif event.ui_element == remover_botao:
                            pergunta_selecionada = perguntas.get_single_selection()
                            if pergunta_selecionada == None:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                         html_message="<p>Selecione uma pergunta</p>")
                            else:
                                remover_confirmacao = pygame_gui.windows.UIConfirmationDialog(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                            manager=self.tela.manager,
                                                                            action_long_desc= "<p>Deseja mesmo remover a pergunta?</p>")
                        elif event.ui_element == visualizar_botao:
                            pergunta_selecionada = perguntas.get_single_selection()
                            if pergunta_selecionada == None:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                         html_message="<p>Selecione uma pergunta</p>")
                            else:
                                continuar = self.visualizar_pergunta(pergunta_selecionada.split()[0], usuario.id_grupo)
                                if continuar == False:
                                    return False
                                else:
                                    run = False
                        elif event.ui_element == editar_botao:
                            pergunta_selecionada = perguntas.get_single_selection()
                            if pergunta_selecionada == None:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                         html_message="<p>Selecione uma pergunta</p>")
                            else:
                                continuar = self.editar_pergunta(pergunta_selecionada.split()[0], usuario.id_grupo)
                                if continuar == False:
                                    return False
                                else:
                                    run = False
                    self.tela.manager.process_events(event)
                self.tela.manager.update(time_delta)
                self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
                self.tela.manager.draw_ui(self.tela.WIN)
                pygame.display.flip()
        return True
    
    def obter_perguntas(self, usuario):
        lista_de_perguntas = PerguntaAlternativasDAO.ver_previa_perguntas(usuario.id_grupo)
        lista_final = []
        for item in lista_de_perguntas:
            lista_final.append(f"{item[0]} - {item[1][:50]}")
        return lista_final
    
    def adicionar_perguntas(self, usuario):
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
            enunciado_texto = pygame_gui.elements.UITextEntryBox(relative_rect=pygame.Rect((0, -75 * self.tela.proporcao_y),(1300 * self.tela.proporcao_x, 250 * self.tela.proporcao_y)),
                                                                container=caixa_fundo,
                                                                anchors={"centerx" : "centerx",
                                                                        "centery":"centery"},
                                                                manager=self.tela.manager)
            alternativas = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((0,0),(1300 * self.tela.proporcao_x, 150 * self.tela.proporcao_y)),
                                                                item_list=["Alternativa correta",
                                                                        "Segunda alternativa",
                                                                        "Terceira alternativa",
                                                                        "Quarta alternativa",
                                                                        "Quinta alternativa"],
                                                                allow_multi_select=False,
                                                                container=caixa_fundo,
                                                                anchors={"centerx":"centerx",
                                                                        "top_target" : enunciado_texto},
                                                                manager=self.tela.manager)
            cancelar_botao = pygame_gui.elements.UIButton(pygame.Rect((-112.5 * self.tela.proporcao_x, -60 * self.tela.proporcao_y),(325 * self.tela.proporcao_x, 65 * self.tela.proporcao_y)),
                                                            text="Cancelar",
                                                            container=caixa_fundo,
                                                            anchors={"centerx":"centerx",
                                                                    "bottom":"bottom"},
                                                            manager=self.tela.manager)
            confirmar_botao = pygame_gui.elements.UIButton(pygame.Rect((0, -60 * self.tela.proporcao_y),(325 * self.tela.proporcao_x, 65 * self.tela.proporcao_y)),
                                                            text="Confirmar",
                                                            container=caixa_fundo,
                                                            anchors={"left_target":cancelar_botao,
                                                                    "bottom":"bottom"},
                                                            manager=self.tela.manager)
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20 * self.tela.proporcao_x, 50 * self.tela.proporcao_y), (-1,-1)),
                                        container=caixa_fundo,
                                        anchors={"bottom_target" : enunciado_texto},
                                        text="Digite o enunciado:",
                                        manager=self.tela.manager)
            enunciado_texto.focus()
            clock = pygame.time.Clock()
            run = True
            enunciado_texto.set_text(self.enunciado)
            while run:
                time_delta = clock.tick(60) / 1000.00
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == voltar_botao:
                            return True
                        elif event.ui_element == confirmar_botao:
                            if enunciado_texto.get_text() == "":
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                         html_message="<p>É necessário preencher o enunciado</p>")
                            elif len(enunciado_texto.get_text()) > 700:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                         html_message=f"<p>O enunciado deve ter no máximo 700 caracteres</p><p>Tamanho atual: {len(enunciado_texto.get_text())} caracteres</p>")
                            elif self.alternativas[0] == "":
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                       html_message="<p>É necessário preencher a Alternativa Correta</p>")
                            else:                                                           
                                alternativas_preenchidas = [alt for alt in self.alternativas if alt != ""]
                                if len(alternativas_preenchidas) < 2:
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                            manager=self.tela.manager,
                                                                                            html_message="<p>Preencha pelo menos duas alternativas</p>")
                                else:
                                    PerguntaAlternativasDAO.adicionar_pergunta(usuario.id_grupo, enunciado_texto.get_text(), alternativas_preenchidas)
                                    self.alternativas = ["","","","",""]
                                    self.enunciado = ""
                                    enunciado_texto.set_text("")
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                            manager=self.tela.manager,
                                                                                            html_message="<p>Pergunta criada</p>")
                    elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                        self.enunciado = enunciado_texto.get_text()
                    elif event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                        if event.ui_element == alternativas:
                            indice = int(alternativas.get_single_selection_start_percentage() * len(alternativas.item_list))
                            texto = alternativas.get_single_selection()
                            continuar = self.adicionar_alternativa(indice, texto)
                            if continuar == False:
                                return False
                            else:
                                run = False
                    self.tela.manager.process_events(event)
                self.tela.manager.update(time_delta)
                self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
                self.tela.manager.draw_ui(self.tela.WIN)
                pygame.display.flip()
        return True
    
    def adicionar_alternativa(self, indice, texto):
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
        alternativa_texto = pygame_gui.elements.UITextEntryBox(relative_rect=pygame.Rect((0, -75 * self.tela.proporcao_y),(1300 * self.tela.proporcao_x, 250 * self.tela.proporcao_y)),
                                                             container=caixa_fundo,
                                                             anchors={"centerx" : "centerx",
                                                                      "centery":"centery"},
                                                             manager=self.tela.manager)
        cancelar_botao = pygame_gui.elements.UIButton(pygame.Rect((-112.5 * self.tela.proporcao_x, -60 * self.tela.proporcao_y),(325 * self.tela.proporcao_x, 65 * self.tela.proporcao_y)),
                                                        text="Cancelar",
                                                        container=caixa_fundo,
                                                        anchors={"centerx":"centerx",
                                                                 "bottom":"bottom"},
                                                        manager=self.tela.manager)
        confirmar_botao = pygame_gui.elements.UIButton(pygame.Rect((0, -60 * self.tela.proporcao_y),(325 * self.tela.proporcao_x, 65 * self.tela.proporcao_y)),
                                                        text="Confirmar",
                                                        container=caixa_fundo,
                                                        anchors={"left_target":cancelar_botao,
                                                                 "bottom":"bottom"},
                                                        manager=self.tela.manager)
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20 * self.tela.proporcao_x, 50 * self.tela.proporcao_y), (-1, -1)),
                                    container=caixa_fundo,
                                    anchors={"bottom_target" : alternativa_texto},
                                    text=f"Insira a {texto}:",
                                    manager=self.tela.manager)
        clock = pygame.time.Clock()
        run = True
        alternativa_texto.focus()
        alternativa_texto.set_text(self.alternativas[indice])
        while run:
            time_delta = clock.tick(60) / 1000.00
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                    self.alternativas[indice]  = alternativa_texto.get_text()
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == voltar_botao:
                        return True
                    elif event.ui_element == confirmar_botao:
                        if len(alternativa_texto.get_text()) > 300:
                            pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                            manager=self.tela.manager,
                                                                                            html_message=f"<p>A alternativa deve ter no máximo 300 caracteres</p><p>Tamanho atual: {len(alternativa_texto.get_text())} caracteres</p>")
                        else:
                            self.alternativas[indice] = alternativa_texto.get_text()
                            return True
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return True
    
    def visualizar_pergunta(self, id_pergunta, id_grupo):
        self.tela.manager.clear_and_reset()
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")

        enunciado_e_tentativa = PerguntaAlternativasDAO.obter_enunciado_e_tentativa(id_pergunta, id_grupo)

        enunciado = enunciado_e_tentativa["texto_enunciado"]
        numero_tentativas = enunciado_e_tentativa["numero_tentativas"]
        numero_acertos = enunciado_e_tentativa["numero_acertos"]

        alternativas = AlternativaDAO.obter_alternativas(id_pergunta, id_grupo)

        texto_pergunta = f"<p>{enunciado}</p>"
        texto_pergunta += "<p></p>"
        
        for indice in range(len(alternativas)):
            letra_alternativa = chr(ord('A') + indice)
            if alternativas[indice][1] == 1:
                texto_pergunta += f"<p>{letra_alternativa}. {alternativas[indice][0]} (Correta)</p>"
            else:
                texto_pergunta += f"<p>{letra_alternativa}. {alternativas[indice][0]}</p>"

        texto_pergunta += "<p></p>"
        texto_pergunta += f"<p>Número de tentativas: {numero_tentativas}</p>"
        texto_pergunta += f"<p>Número de acertos: {numero_acertos}</p>"

            

        caixa_fundo = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 415 * self.tela.proporcao_y),(1400 * self.tela.proporcao_x, 650 * self.tela.proporcao_y)),
                                                    anchors={"centerx":"centerx"},
                                                    manager=self.tela.manager)
        voltar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((-144 * self.tela.proporcao_x, 23), (120 * self.tela.proporcao_x, 80 * self.tela.proporcao_y)),
                                                    text="",
                                                    container=caixa_fundo,
                                                    object_id=ObjectID(class_id="@botao_voltar_pequeno"),
                                                    anchors={"right":"right"},
                                                    manager=self.tela.manager)
        pergunta = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((0, 110 * self.tela.proporcao_y),(1300 * self.tela.proporcao_x, 500 * self.tela.proporcao_y)),
                                                   html_text= texto_pergunta,
                                                   container=caixa_fundo,
                                                   anchors={"centerx" : "centerx",
                                                            "top" : "top"},
                                                   manager=self.tela.manager)
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20 * self.tela.proporcao_x, 50 * self.tela.proporcao_y), (-1, -1)),
                                    container=caixa_fundo,
                                    anchors={"bottom_target" : pergunta},
                                    text=f"Pergunta {id_pergunta} do grupo {id_grupo}:",
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
    
    def editar_pergunta(self,id_pergunta,id_grupo):
        enunciado_e_tentativa = PerguntaAlternativasDAO.obter_enunciado_e_tentativa(id_pergunta, id_grupo)
        self.enunciado = enunciado_e_tentativa["texto_enunciado"]
        alternativas_tuplas = AlternativaDAO.obter_alternativas(id_pergunta, id_grupo)

        for indice in range(len(alternativas_tuplas)):
            if alternativas_tuplas[indice][1] == 1:
                alternativas_tuplas[0], alternativas_tuplas[indice] = alternativas_tuplas[indice], alternativas_tuplas[0] # Caso a alternativa correta não seja a primeira 
                break
        self.alternativas = ["","","","",""]
        for indice in range(len(alternativas_tuplas)):
            self.alternativas[indice] = alternativas_tuplas[indice][0]
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
            enunciado_texto = pygame_gui.elements.UITextEntryBox(relative_rect=pygame.Rect((0, -75 * self.tela.proporcao_y),(1300 * self.tela.proporcao_x, 250 * self.tela.proporcao_y)),
                                                                container=caixa_fundo,
                                                                anchors={"centerx" : "centerx",
                                                                        "centery":"centery"},
                                                                manager=self.tela.manager)
            alternativas = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((0,0),(1300 * self.tela.proporcao_x, 150 * self.tela.proporcao_y)),
                                                                item_list=["Alternativa correta",
                                                                        "Segunda alternativa",
                                                                        "Terceira alternativa",
                                                                        "Quarta alternativa",
                                                                        "Quinta alternativa"],
                                                                allow_multi_select=False,
                                                                container=caixa_fundo,
                                                                anchors={"centerx":"centerx",
                                                                        "top_target" : enunciado_texto},
                                                                manager=self.tela.manager)
            cancelar_botao = pygame_gui.elements.UIButton(pygame.Rect((-112.5 * self.tela.proporcao_x, -60 * self.tela.proporcao_y),(325 * self.tela.proporcao_x, 65 * self.tela.proporcao_y)),
                                                            text="Cancelar",
                                                            container=caixa_fundo,
                                                            anchors={"centerx":"centerx",
                                                                    "bottom":"bottom"},
                                                            manager=self.tela.manager)
            confirmar_botao = pygame_gui.elements.UIButton(pygame.Rect((0, -60 * self.tela.proporcao_y),(325 * self.tela.proporcao_x, 65 * self.tela.proporcao_y)),
                                                            text="Confirmar",
                                                            container=caixa_fundo,
                                                            anchors={"left_target":cancelar_botao,
                                                                    "bottom":"bottom"},
                                                            manager=self.tela.manager)
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect((20 * self.tela.proporcao_x, 50 * self.tela.proporcao_y), (-1,-1)),
                                        container=caixa_fundo,
                                        anchors={"bottom_target" : enunciado_texto},
                                        text="Digite o enunciado:",
                                        manager=self.tela.manager)
            enunciado_texto.focus()
            clock = pygame.time.Clock()
            run = True
            enunciado_texto.set_text(self.enunciado)
            while run:
                time_delta = clock.tick(60) / 1000.00
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == voltar_botao:
                            return True
                        elif event.ui_element == confirmar_botao:
                            if enunciado_texto.get_text() == "":
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                         html_message="<p>É necessário preencher o enunciado</p>")
                            elif len(enunciado_texto.get_text()) > 700:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                         html_message=f"<p>O enunciado deve ter no máximo 700 caracteres</p><p>Tamanho atual: {len(enunciado_texto.get_text())} caracteres</p>")
                            elif self.alternativas[0] == "":
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                         manager=self.tela.manager,
                                                                                       html_message="<p>É necessário preencher a Alternativa Correta</p>")
                            else:                                                           
                                alternativas_preenchidas = [alt for alt in self.alternativas if alt != ""]
                                if len(alternativas_preenchidas) < 2:
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                            manager=self.tela.manager,
                                                                                            html_message="<p>Preencha pelo menos duas alternativas</p>")
                                else:
                                    PerguntaAlternativasDAO.editar_pergunta(id_pergunta, id_grupo, enunciado_texto.get_text(), self.alternativas)
                                    self.alternativas = ["","","","",""]
                                    self.enunciado = ""
                                    enunciado_texto.set_text("")
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                            manager=self.tela.manager,
                                                                                            html_message="<p>Pergunta editada</p>")
                    elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                        self.enunciado = enunciado_texto.get_text()
                    elif event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                        if event.ui_element == alternativas:
                            indice = int(alternativas.get_single_selection_start_percentage() * len(alternativas.item_list))
                            texto = alternativas.get_single_selection()
                            continuar = self.adicionar_alternativa(indice, texto)
                            if continuar == False:
                                return False
                            else:
                                run = False
                    self.tela.manager.process_events(event)
                self.tela.manager.update(time_delta)
                self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
                self.tela.manager.draw_ui(self.tela.WIN)
                pygame.display.flip()
        self.alternativas = ["","","","",""]
        self.enunciado = ""
        return True
            
    def remover_pergunta(self, id_pergunta, id_grupo):
        PerguntaAlternativasDAO.remover_pergunta(id_pergunta, id_grupo)
        return True