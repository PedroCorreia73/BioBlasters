import pygame
import pygame_gui

class TelaComoJogar:
    def __init__(self, tela):
        self.tela = tela

    def como_jogar(self):
        self.tela.manager.clear_and_reset()
        BG_INICIO = pygame.image.load("imagens/bg_menu_titlescreen.png")
        pygame.display.update()
        clock = pygame.time.Clock()
        imagem_inicial = pygame.image.load("imagens/como_jogar_parte1.png")
        imagem_final = pygame.image.load("imagens/como_jogar_parte2.png")
        imagem = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((85 * self.tela.proporcao_x, 52 * self.tela.proporcao_y),(1750 * self.tela.proporcao_x, 975 * self.tela.proporcao_y)),
                                             manager=self.tela.manager,
                                             image_surface=imagem_inicial)
        contador = 0
        run = True
        while run:
            time_delta = clock.tick(60) / 1000.00
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    contador += 1
                    if contador == 1:
                        imagem.set_image(imagem_final)
                    elif contador == 2:
                        return True
                self.tela.manager.process_events(event)
            self.tela.manager.update(time_delta)
            self.tela.WIN.blit(pygame.transform.scale(BG_INICIO, (self.tela.WIN.get_width(), self.tela.WIN.get_height())), (0, 0))
            self.tela.manager.draw_ui(self.tela.WIN)
            pygame.display.flip()
        return False

    