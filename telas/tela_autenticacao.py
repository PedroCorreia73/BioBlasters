import pygame
import pygame_gui
import re
from banco_de_dados.aluno import AlunoDAO
from banco_de_dados.professor import ProfessorDAO
from banco_de_dados.administrador import AdministradorDAO
from usuario.usuario_atual import Aluno, Professor, Administrador

class TelaAutenticacao:
    @classmethod
    def autenticar(cls,tela, usuario):
        tela.manager.clear_and_reset()  # Reseta os elementos do pygame_gui
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        tamanho_texto = (800 * tela.proporcao_x, 85 * tela.proporcao_y)
        usuario_texto = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect((0 * tela.proporcao_x, 429 * tela.proporcao_y), tamanho_texto),
                                            placeholder_text = "Usuário",                                    
                                            manager = tela.manager,
                                            anchors={"centerx":"centerx"})
        senha_texto = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect((0 * tela.proporcao_x , 596 * tela.proporcao_y), tamanho_texto),
                                            placeholder_text = "Senha",                                    
                                            manager = tela.manager,
                                            anchors={"centerx":"centerx"})
        cadastrar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1920 / 2 * tela.proporcao_x - tela.tamanho_botao[0] , 762 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Cadastrar',
                                             manager=tela.manager)
        entrar_botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1920 / 2 * tela.proporcao_x, 762 * tela.proporcao_y), tela.tamanho_botao),
                                             text='Entrar',
                                             manager=tela.manager)
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
                            if cls.verificar_email_aluno(nome_usuario):
                                aluno = AlunoDAO(nome_usuario, senha_usuario, None)
                                verificar = AlunoDAO.consulta_aluno(aluno)
                                if len(verificar) == 1:
                                    if senha_usuario == verificar[0][2]:
                                        usuario.id = verificar[0][0]
                                        usuario.nome = nome_usuario
                                        usuario.senha = senha_usuario
                                        return False
                                    else:
                                        senha_texto.set_text("")
                                        senha_texto.set_text_hidden(is_hidden=False)
                                        pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                        manager=tela.manager,
                                                                                         html_message="<p>Senha incorreta</p>")
                                else:
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                        manager=tela.manager,
                                                                                        html_message="<p>Usuário não encontrado</p>")
                            else:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                        manager=tela.manager,
                                                                                        html_message='<p>O email deve possuir "@jpiaget.g12.br"</p>')
                        elif isinstance(usuario, Professor):
                            if cls.verificar_email_professor(nome_usuario):
                                professor = ProfessorDAO(nome_usuario, senha_usuario, None)
                                verificar = ProfessorDAO.consulta_professor(professor)
                                if len(verificar) == 1:
                                    if senha_usuario == verificar[0][2]:
                                        usuario.id = verificar[0][0]
                                        usuario.nome = nome_usuario
                                        usuario.senha = senha_usuario
                                        return False
                                    else:
                                        senha_texto.set_text("")
                                        senha_texto.set_text_hidden(is_hidden=False)
                                        pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                        manager=tela.manager,
                                                                                         html_message="<p>Senha incorreta</p>")
                                else:
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                        manager=tela.manager,
                                                                                        html_message="<p>Usuário não encontrado</p>")
                            else:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                        manager=tela.manager,
                                                                                        html_message='<p>O email deve possuir "@jpiaget.pro.br"</p>')
                        elif isinstance(usuario,Administrador):
                            administrador = AdministradorDAO(nome_usuario,senha_usuario)
                            verificar = AdministradorDAO.consulta_administrador(administrador)
                            if len(verificar) == 1:
                                if senha_usuario == verificar[0][2]:
                                    usuario.id = verificar[0][0]
                                    usuario.nome = nome_usuario
                                    usuario.senha = senha_usuario
                                    return False
                                else:
                                    senha_texto.set_text("")
                                    senha_texto.set_text_hidden(is_hidden=False)
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                    manager=tela.manager,
                                                                                        html_message="<p>Senha incorreta</p>")
                            else:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                    manager=tela.manager,
                                                                                    html_message="<p>Usuário não encontrado</p>")
                    elif event.ui_element == cadastrar_botao:
                        nome_usuario = usuario_texto.get_text()
                        senha_usuario = senha_texto.get_text()
                        if isinstance(usuario, Aluno):
                            if cls.verificar_email_aluno(nome_usuario):
                                aluno = AlunoDAO(nome_usuario, senha_usuario, None)
                                verificar = AlunoDAO.consulta_aluno(aluno)
                                if len(verificar) == 0:
                                    AlunoDAO.adicionar_aluno(aluno)
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                         manager=tela.manager,
                                                                                         html_message="<p>Usuário cadastrado!</p>")
                                else:
                                    usuario_texto.set_text("")
                                    senha_texto.set_text("")
                                    senha_texto.set_text_hidden(is_hidden=False)
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                         manager=tela.manager,
                                                                                         html_message="<p>Usuário já cadastrado!</p>")
                            else:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                        manager=tela.manager,
                                                                                        html_message='<p>O email deve possuir "@jpiaget.g12.br"</p>')
                        elif isinstance(usuario, Professor):
                            if cls.verificar_email_professor(nome_usuario):
                                professor = ProfessorDAO(nome_usuario, senha_usuario, None)
                                verificar = ProfessorDAO.consulta_professor(professor)
                                if len(verificar) == 0:
                                    ProfessorDAO.adicionar_professor(professor)
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                         manager=tela.manager,
                                                                                         html_message="<p>Usuário cadastrado!</p>")
                                else:
                                    usuario_texto.set_text("")
                                    senha_usuario.set_text("")
                                    senha_texto.set_text_hidden(is_hidden=False)
                                    pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                         manager=tela.manager,
                                                                                         html_message="<p>Usuário já cadastrado!</p>")
                            else:
                                pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                        manager=tela.manager,
                                                                                        html_message='<p>O email deve possuir "@jpiaget.pro.br"</p>')                             
                tela.manager.process_events(event)
            tela.manager.update(time_delta)
            tela.WIN.blit(pygame.transform.scale(BG_INICIO, (tela.WIN.get_width(), tela.WIN.get_height())), (0, 0))
            tela.manager.draw_ui(tela.WIN)
            pygame.display.flip()

    def validar_email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, email)):
            return True
        else:
            return False
        
    @classmethod
    def verificar_email_aluno(cls,email):
        if not cls.validar_email(email):
            return False
        else:
            email_aluno = email.split("@")[1]
            if email_aluno == "jpiaget.g12.br":
                return True
            else:
                return False
    @classmethod
    def verificar_email_professor(cls, email):
        if not cls.validar_email(email):
            return False
        else:
            email_aluno = email.split("@")[1]
            if email_aluno == "jpiaget.pro.br":
                return True
            else:
                return False

