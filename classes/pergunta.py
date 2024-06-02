from random import choice, shuffle
import pygame
import pygame_gui
from pygame_gui.core.object_id import ObjectID
import pygame_gui.elements.ui_window
import pygame_gui.windows.ui_message_window
from banco_de_dados.pergunta import PerguntaAlternativasDAO, AlternativaDAO


class Pergunta:
    def __init__(self, tela, pergunta, alternativas):
        self.tela = tela
        self.enunciado = pergunta["texto_enunciado"]
        self.numero_tentativas = pergunta["numero_tentativas"]
        self.numero_acertos = pergunta["numero_acertos"]
        self.alternativas = alternativas

    def mostrar_pergunta(self):
        self.tela.manager.clear_and_reset()
        botoes = []
        texto_pergunta = f"<p>{self.enunciado}</p>"
        texto_pergunta += "<p></p>"
        
        for indice in range(len(self.alternativas)):
            letra_alternativa = chr(ord('A') + indice)
            texto_pergunta += f"<p>{letra_alternativa}. {self.alternativas[indice][0]}</p>"
            

        caixa_fundo = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0,0),(1760 * self.tela.proporcao_x, 980 * self.tela.proporcao_y)),
                                                    anchors={"centerx":"centerx",
                                                             "centery":"centery"},
                                                    manager=self.tela.manager)
        pergunta = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((0,  100 * self.tela.proporcao_y),(1600 * self.tela.proporcao_x, 600 * self.tela.proporcao_y)),
                                                   html_text= texto_pergunta,
                                                   container=caixa_fundo,
                                                   anchors={"top" : "top",
                                                            "centerx" : "centerx"},
                                                   manager=self.tela.manager)
        
        for indice in range(len(self.alternativas)):
            letra_alternativa = chr(ord('A') + indice)
            botoes.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect((indice * caixa_fundo.relative_rect.width / len(self.alternativas), 0),(325 * self.tela.proporcao_x, 65 * self.tela.proporcao_y)),
                                                        text= letra_alternativa,
                                                        container=caixa_fundo,
                                                        anchors={"top_target" : pergunta,
                                                                 "bottom_target" : caixa_fundo},
                                                        manager=self.tela.manager))
        clock = pygame.time.Clock()
        run = True
        acertou = False
        while run:
            time_delta = clock.tick(60) / 1000.00
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return acertou
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element in botoes:
                        acertou = self.verificar_resposta(botoes.index(event.ui_element))
                    else:
                        return acertou
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()

    def verificar_resposta(self, indice):
        if self.alternativas[indice][1] == 1:
            mensagem = pygame_gui.windows.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message=f'<p>Resposta Correta</p>')
            mensagem.set_blocking(True)
            return True
        else:
            mensagem = pygame_gui.windows.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message=f'<p>Resposta Incorreta</p>')
            mensagem.set_blocking(True)
            return False

class Perguntas:
    def __init__(self, id_grupo):
        self.id_grupo = id_grupo
        self.obter_id_perguntas()
    
    def obter_id_perguntas(self):
        lista_tuplas = PerguntaAlternativasDAO.obter_ids_perguntas(self.id_grupo)
        lista_ids = []
        for item in lista_tuplas:
            lista_ids.append(item[0])
        self.id_perguntas = lista_ids
    
    def gerar_pergunta(self, tela):
        if len(self.id_perguntas) == 0:
            self.obter_id_perguntas()
        id_escolhido = choice(self.id_perguntas)
        self.id_perguntas.remove(id_escolhido)
        enunciado_e_tentativa = PerguntaAlternativasDAO.obter_enunciado_e_tentativa(id_escolhido, self.id_grupo)
        alternativas = AlternativaDAO.obter_alternativas(id_escolhido, self.id_grupo)
        shuffle(alternativas)
        pergunta = Pergunta(tela, enunciado_e_tentativa, alternativas)
        return pergunta.mostrar_pergunta()
        