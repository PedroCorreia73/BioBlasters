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
    menu = Menu()
    while continuar:
        if isinstance(usuario, Aluno): 
            continuar = menu.aluno(tela, usuario)
        elif isinstance(usuario, Professor):
            continuar = menu.professor(tela, usuario)
        elif isinstance(usuario, Administrador):
            continuar = menu.administrador(tela, usuario)
    pygame.quit

if __name__ == "__main__":
    main()