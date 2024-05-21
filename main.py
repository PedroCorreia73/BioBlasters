import pygame
from telas.tela import TelaJogo
from telas.menus import Menu
from telas.tela_login import TelaLogin
from telas.tela_selecionar import TelaSelecionar
from usuario.usuario_atual import Aluno, Professor, Administrador

def main():
    tela = TelaJogo() # inicializa a tela com as medidas da tela do usuário
    repetir = True
    while repetir:
        usuario = TelaSelecionar.selecionar(tela)
        repetir = TelaLogin.login(tela, usuario)

    continuar = True
    while continuar:
        if isinstance(usuario, Aluno): 
            continuar = Menu.menu_aluno(tela)
        elif isinstance(usuario, Professor):
            continuar = Menu.menu_professor(tela)
        elif isinstance(usuario, Administrador):
            continuar = Menu.menu_administrador(tela)
    pygame.quit

if __name__ == "__main__":
    main()