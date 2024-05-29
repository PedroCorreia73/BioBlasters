import pygame
from telas.tela import TelaJogo
from telas.menus import Menu
from telas.tela_autenticacao import TelaAutenticacao
from telas.tela_selecionar import TelaSelecionar

def main():
    tela = TelaJogo() # inicializa a tela com as medidas da tela do usuário
    repetir = True
    while repetir:
        usuario = TelaSelecionar.selecionar(tela)
        if usuario == None:
            break
        repetir = TelaAutenticacao.autenticar(tela, usuario)

    continuar = True
    menu = Menu(tela)
    if usuario != None:
        if usuario.nome != None:
            while continuar:
                continuar = usuario.entrar_menu(menu)
    pygame.quit
if __name__ == "__main__":
    main()