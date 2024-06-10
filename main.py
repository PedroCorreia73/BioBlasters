import pygame
import pygame_gui
import pygame_gui.windows.ui_message_window
from telas.tela import TelaJogo
from telas.menus import Menu
from telas.tela_autenticacao import TelaAutenticacao
from telas.tela_selecionar import TelaSelecionar

def main():
    tela = TelaJogo() # inicializa a tela com as medidas da tela do usuário
    try:
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
    except Exception:
        tela.manager.clear_and_reset()
        BG_INICIO = pygame.image.load("imagens/bgbg.png")
        mensagem = pygame_gui.windows.ui_message_window.UIMessageWindow(rect=((456 * tela.proporcao_x, 448 * tela.proporcao_y), (1009 * tela.proporcao_x, 472.95 * tela.proporcao_y)),
                                                                                         manager=tela.manager,
                                                                                         html_message="<p>Ocorreu um erro inesperado!</p>")
        clock = pygame.time.Clock()
        run = True
        while run:
            time_delta = clock.tick(60) / 1000.00
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == mensagem.dismiss_button:
                        run = False
                tela.manager.process_events(event)
            # Desenhar os elementos na tela
            tela.manager.update(time_delta)
            tela.WIN.blit(pygame.transform.scale(BG_INICIO, (tela.WIN.get_width(), tela.WIN.get_height())), (0, 0))
            tela.manager.draw_ui(tela.WIN)
            pygame.display.flip()
        pygame.quit()
      
if __name__ == "__main__":
    main()
    