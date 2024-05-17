from classes.tela import TelaJogo
from menus import Menu
import pygame

def main():
    tela = TelaJogo() # inicializa a tela com as medidas da tela do usuário
    Menu.tela_inicial(tela)
    pygame.quit

if __name__ == "__main__":
    main()