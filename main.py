import pygame
from telas.tela import TelaJogo
from telas.menus import Menu
from telas.tela_autenticacao import TelaAutenticacao
from telas.tela_selecionar import TelaSelecionar

def main():
    tela = TelaJogo() # inicializa a tela com as medidas da tela do usuário
    tela_selecionar = TelaSelecionar(tela)
    tela_autenticacao = TelaAutenticacao(tela)
    repetir = True
    while repetir:
        usuario = tela_selecionar.selecionar()
        if usuario == None:
            break
        repetir = tela_autenticacao.autenticar(usuario)

    continuar = True
    menu = Menu(tela)
    if usuario != None:
        if usuario.nome != None:
            while continuar:
                continuar = usuario.entrar_menu(menu)
    pygame.quit()
    
if __name__ == "__main__":
    main()