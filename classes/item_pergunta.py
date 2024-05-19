import pygame
import random
import time
from .colecao_itens import ColecaoItens
from .pergunta import Pergunta

class ItemPergunta(pygame.Rect):

    WIDTH = 35
    HEIGHT = 35
    VEL = 5

    def __init__(self, posicao_x, posicao_y, width, height):
        super().__init__(posicao_x, posicao_y, width, height)

    @staticmethod
    def gerar_imagem():
        IMG_ITEM_PERGUNTA = pygame.image.load("imagens/quiz_item.png")
        IMG_ITEM_PERGUNTA = pygame.transform.scale(IMG_ITEM_PERGUNTA, (50, 50))
        return IMG_ITEM_PERGUNTA
    
    @staticmethod
    def gerar_caixa_pergunta(tela, nave, keys_teclado, pontuacao, origem_plano_resposta, bg_pergunta):
        aux_pontuacao_resposta += 1
        if aux_pontuacao_resposta == 1:
            pontuacao.ganha += 100
            ti = time.time()
        tela.WIN.blit(bg_pergunta, origem_plano_resposta)
        enunciado_exemplo = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Enunciado - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
        a_exemplo = "A) Essa não é a alternativa correta."
        b_exemplo = "B) Muito menos essa."
        c_exemplo = "C) Nem me fale dessa!"
        d_exemplo = "D) Essa parece boa, mas nem tanto."
        e_exemplo = "E) Hmmmmmmmmmmmmmmm..."
        texto_completo_exemplo = enunciado_exemplo + "\n" + a_exemplo + "\n" + b_exemplo + "\n" + c_exemplo + "\n" + d_exemplo + "\n" + e_exemplo
        fonte = pygame.font.SysFont("Arial", 30)
        collection = [word.split(' ') for word in texto_completo_exemplo.splitlines()]
        space = fonte.size(' ')[0]
        pos = origem_plano_resposta[0] + 10, origem_plano_resposta[1] + 10
        x = pos[0]
        y = pos[1]
        for lines in collection:
            for words in lines:
                word_surface = fonte.render(words, True, 'brown')
                word_width, word_height = word_surface.get_size()
                if x + word_width >= pos[0] + bg_pergunta.get_width() - 10:
                    x = pos[0]
                    y += word_height
                tela.WIN.blit(word_surface, (x,y))
                x += word_width + space
            x = pos[0]
            y += word_height
        if keys_teclado[pygame.K_a]:
            aux_tempo_resposta += 1
            if aux_tempo_resposta == 1:
                tf = time.time()
                t += tf - ti
                pontuacao.ganha += 400
            nave.vel = nave.vel / 1.5
            pygame.time.delay(1000)
            nave.pegou_item_pergunta = False
    
class ItensPergunta(ColecaoItens):
    def __init__(self):
        super().__init__(2000)
    def mover(self,nave):
        for item_pergunta in self.itens():
            item_pergunta.x -= ItemPergunta.VEL
            if item_pergunta.x < 0 - ItemPergunta.WIDTH - 30:
                self.remove(item_pergunta)
            if item_pergunta.colliderect(nave):
                self.remove(item_pergunta)
                nave.pegou_item_pergunta = True
    def gerar(self, tela):
        if self.contagem > self.add_increment:
            item_pergunta_y = random.randint(0, tela.HEIGHT - ItemPergunta.HEIGHT)
            item_pergunta = ItemPergunta(tela.WIDTH, item_pergunta_y, ItemPergunta.WIDTH, ItemPergunta.HEIGHT)
            self.append(item_pergunta)
            #item_pergunta_add_increment = max(200, item_pergunta_add_increment - 50)
            self.contagem = 0

    