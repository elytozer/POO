import pygame
import random
  
pygame.init()

# Constantes
LINHAS, COLUNAS = 6, 6
TAMANHO_CARTA = 80
LARGURA = COLUNAS * TAMANHO_CARTA
ALTURA = LINHAS * TAMANHO_CARTA
TELA = pygame.display.set_mode((LARGURA, ALTURA + 100))
pygame.display.set_caption("Jogo da Memória - 2 Jogadores (POO)")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
VERMELHO = (200, 0, 0)

fonte = pygame.font.SysFont(None, 36)

CORES = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255),
    (0, 255, 255), (255, 165, 0), (128, 0, 128), (0, 128, 128),
    (128, 128, 0), (210, 105, 30), (0, 0, 128), (255, 192, 203),
    (173, 255, 47), (100, 149, 237), (112, 128, 144), (75, 0, 130),
    (244, 164, 96),
]


class Carta:
    def __init__(self, cor):
        self.cor = cor
        self.revelada = False
        self.encontrada = False

    def desenhar(self, x, y):
        rect = pygame.Rect(x + 5, y + 5, TAMANHO_CARTA - 10, TAMANHO_CARTA - 10)
        if self.revelada or self.encontrada:
            pygame.draw.rect(TELA, self.cor, rect)
        else:
            pygame.draw.rect(TELA, PRETO, rect)


class JogoMemoria:
    def __init__(self):
        self.cartas = self.gerar_cartas()
        self.primeira = None
        self.segunda = None
        self.aguardando = False
        self.placar = [0, 0, 0]
        self.tentativas = [0, 0]  
        self.rodando = True

    def gerar_cartas(self):
        cores_pares = CORES * 2
        random.shuffle(cores_pares)
        cartas = []
        for linha in range(LINHAS):
            linha_cartas = []
            for coluna in range(COLUNAS):
                idx = linha * COLUNAS + coluna
                linha_cartas.append(Carta(cores_pares[idx]))
            cartas.append(linha_cartas)
        return cartas

    def desenhar(self):
        TELA.fill(BRANCO)
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                x = coluna * TAMANHO_CARTA
                y = linha * TAMANHO_CARTA
                self.cartas[linha][coluna].desenhar(x, y)

        # Placar
        pygame.draw.rect(TELA, CINZA, (0, ALTURA, LARGURA, 100))
        texto_placar = fonte.render(f"Jogador 1: {self.placar[0]}  Jogador 2: {self.placar[1]}", True, PRETO)
        texto_turno = fonte.render(f"Turno: Jogador {self.placar[2] + 1}", True, VERMELHO)
        TELA.blit(texto_placar, (20, ALTURA + 20))
        TELA.blit(texto_turno, (20, ALTURA + 60))
        pygame.display.flip()

    def obter_posicao(self, pos):
        x, y = pos
        if y >= ALTURA:
            return None, None
        return y // TAMANHO_CARTA, x // TAMANHO_CARTA

    def checar_fim_de_jogo(self):
        return all(c.encontrada for linha in self.cartas for c in linha)

    def mostrar_fim_de_jogo(self):
        vencedor = "Empate!"
        if self.placar[0] > self.placar[1]:
            vencedor = "Jogador 1 venceu!"
        elif self.placar[1] > self.placar[0]:
            vencedor = "Jogador 2 venceu!"

        TELA.fill(BRANCO)
        texto = fonte.render(vencedor, True, PRETO)
        TELA.blit(texto, (LARGURA // 2 - 100, ALTURA // 2 - 20))
        pygame.display.flip()
        pygame.time.delay(3000)

    def reiniciar(self):
        self.cartas = self.gerar_cartas()
        self.primeira = self.segunda = None
        self.placar = [0, 0, 0]

    def rodar(self):
        while self.rodando:
            self.desenhar()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False

                if evento.type == pygame.MOUSEBUTTONDOWN and not self.aguardando:
                    linha, coluna = self.obter_posicao(pygame.mouse.get_pos())
                    if linha is not None:
                        carta = self.cartas[linha][coluna]
                        if not carta.revelada:
                            carta.revelada = True
                            if self.primeira is None:
                                self.primeira = (linha, coluna)
                            elif self.segunda is None:
                                self.segunda = (linha, coluna)
                                self.aguardando = True
                                self.desenhar()
                                pygame.time.delay(700)

                                c1 = self.cartas[self.primeira[0]][self.primeira[1]]
                                c2 = self.cartas[self.segunda[0]][self.segunda[1]]
                                if c1.cor == c2.cor:
                                    c1.encontrada = True
                                    c2.encontrada = True
                                    self.placar[self.placar[2]] += 1
                                else:
                                    c1.revelada = False
                                    c2.revelada = False
                                    self.placar[2] = 1 - self.placar[2]
                                self.primeira = self.segunda = None
                                self.aguardando = False

            if self.checar_fim_de_jogo():
                self.desenhar()
                pygame.time.delay(1000)
                self.mostrar_fim_de_jogo()
                self.reiniciar()


if __name__ == "__main__":
    jogo = JogoMemoria()
    jogo.rodar()
    pygame.quit()
