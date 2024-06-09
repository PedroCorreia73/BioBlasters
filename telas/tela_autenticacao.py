import pygame
import pygame_gui
import re
from banco_de_dados.aluno import AlunoDAO
from banco_de_dados.professor import ProfessorDAO
from banco_de_dados.administrador import AdministradorDAO
from usuario.usuario_atual import Aluno, Professor, Administrador

class TelaAutenticacao:
    def __init__(self, tela):
        self.tela = tela

    def autenticar(self, usuario):
        self.tela.manager.clear_and_reset()  # Reseta os elementos do pygame_gui
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        tamanho_texto = (800 * self.tela.proporcao_x, 85 * self.tela.proporcao_y)
        usuario_texto = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect((0 * self.tela.proporcao_x, 429 * self.tela.proporcao_y), tamanho_texto),
                                            placeholder_text = "Usuário",                                    
                                            manager = self.tela.manager,
                                            anchors={"centerx":"centerx"})
        senha_texto = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect((0 * self.tela.proporcao_x , 596 * self.tela.proporcao_y), tamanho_texto),
                                            placeholder_text = "Senha",                                    
                                            manager = self.tela.manager,
                                            anchors={"centerx":"centerx"})
        cadastrar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1920 / 2 * self.tela.proporcao_x - self.tela.tamanho_botao[0] , 762 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Cadastrar',
                                             manager=self.tela.manager)
        entrar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1920 / 2 * self.tela.proporcao_x, 762 * self.tela.proporcao_y), self.tela.tamanho_botao),
                                             text='Entrar',
                                             manager=self.tela.manager)
        clock = pygame.time.Clock()
        run = True
        while run:
            time_delta = clock.tick(60) / 1000.00
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                    if event.ui_element == senha_texto:
                        if senha_texto.get_text() == "":
                            senha_texto.set_text_hidden(is_hidden=False)
                        else:
                            senha_texto.set_text_hidden(is_hidden=True)
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == entrar_botao:
                        nome_usuario = usuario_texto.get_text()
                        senha_usuario = senha_texto.get_text()
                        if isinstance(usuario, Aluno):
                            if self.verificar_email_aluno(nome_usuario):
                                aluno = AlunoDAO(nome_usuario, senha_usuario, None)
                                verificar = aluno.consulta_aluno()
                                if len(verificar) == 1:
                                    if senha_usuario == verificar[0][2]:
                                        usuario.id = verificar[0][0]
                                        usuario.nome = nome_usuario
                                        usuario.senha = senha_usuario
                                        usuario.id_grupo = verificar[0][3]
                                        usuario.pontuacao = verificar[0][4]
                                        return False
                                    else:
                                        senha_texto.set_text("")
                                        senha_texto.set_text_hidden(is_hidden=False)
                                        pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                         html_message="<p>Senha incorreta</p>")
                                else:
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message="<p>Usuário não encontrado</p>")
                            else:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message='<p>O email deve possuir "@jpiaget.g12.br"</p>')
                        elif isinstance(usuario, Professor):
                            if self.verificar_email_professor(nome_usuario):
                                professor = ProfessorDAO(nome_usuario, senha_usuario, None)
                                verificar = professor.consulta_professor()
                                if len(verificar) == 1:
                                    if senha_usuario == verificar[0][2]:
                                        usuario.id = verificar[0][0]
                                        usuario.nome = nome_usuario
                                        usuario.senha = senha_usuario
                                        usuario.id_grupo = verificar[0][3]
                                        usuario.pontuacao = verificar[0][4]
                                        return False
                                    else:
                                        senha_texto.set_text("")
                                        senha_texto.set_text_hidden(is_hidden=False)
                                        pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                         html_message="<p>Senha incorreta</p>")
                                else:
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message="<p>Usuário não encontrado</p>")
                            else:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message='<p>O email deve possuir "@jpiaget.pro.br"</p>')
                        elif isinstance(usuario,Administrador):
                            administrador = AdministradorDAO(nome_usuario,senha_usuario)
                            verificar = administrador.consulta_administrador()
                            if len(verificar) == 1:
                                if senha_usuario == verificar[0][2]:
                                    usuario.id = verificar[0][0]
                                    usuario.nome = nome_usuario
                                    usuario.senha = senha_usuario
                                    return False
                                else:
                                    senha_texto.set_text("")
                                    senha_texto.set_text_hidden(is_hidden=False)
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                    manager=self.tela.manager,
                                                                                        html_message="<p>Senha incorreta</p>")
                            else:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                    manager=self.tela.manager,
                                                                                    html_message="<p>Usuário não encontrado</p>")
                    elif event.ui_element == cadastrar_botao:
                        nome_usuario = usuario_texto.get_text()
                        senha_usuario = senha_texto.get_text()
                        if isinstance(usuario, Aluno):
                            if self.verificar_email_aluno(nome_usuario):
                                aluno = AlunoDAO(nome_usuario, senha_usuario, None)
                                verificar = aluno.consulta_aluno()
                                if len(verificar) == 0:
                                    if not self.verificar_senha(senha_usuario):
                                        pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message='<p>A senha deve possuir pelo menos 6 caracteres</p>')  
                                    else:
                                        aluno.adicionar_aluno()
                                        pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                            manager=self.tela.manager,
                                                                                            html_message="<p>Usuário cadastrado!</p>")
                                else:
                                    usuario_texto.set_text("")
                                    senha_texto.set_text("")
                                    senha_texto.set_text_hidden(is_hidden=False)
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message="<p>Usuário já cadastrado!</p>")
                            else:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message='<p>O email deve possuir "@jpiaget.g12.br"</p>')
                        elif isinstance(usuario, Professor):
                            if self.verificar_email_professor(nome_usuario):
                                professor = ProfessorDAO(nome_usuario, senha_usuario, None)
                                verificar = professor.consulta_professor()
                                if len(verificar) == 0:
                                    if not self.verificar_senha(senha_usuario):
                                        pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message='<p>A senha deve possuir pelo menos 6 caracteres</p>')  
                                    else: 
                                        professor.adicionar_professor()
                                        pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message="<p>Usuário cadastrado!</p>")
                                else:
                                    usuario_texto.set_text("")
                                    senha_texto.set_text("")
                                    senha_texto.set_text_hidden(is_hidden=False)
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message="<p>Usuário já cadastrado!</p>")
                            else:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * self.tela.proporcao_x, 448 * self.tela.proporcao_y), (1009 * self.tela.proporcao_x, 472.95 * self.tela.proporcao_y)),
                                                                                        manager=self.tela.manager,
                                                                                        html_message='<p>O email deve possuir "@jpiaget.pro.br"</p>')                     
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()

    def validar_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, email)):
            return True
        else:
            return False
        
    def verificar_email_aluno(self,email):
        if not self.validar_email(email):
            return False
        else:
            email_aluno = email.split("@")[1]
            if email_aluno == "jpiaget.g12.br":
                return True
            else:
                return False
    def verificar_email_professor(self, email):
        if not self.validar_email(email):
            return False
        else:
            email_aluno = email.split("@")[1]
            if email_aluno == "jpiaget.pro.br":
                return True
            else:
                return False
            
    def verificar_senha(self, senha):
        return len(senha) >= 6

