# Arquivo capitulo_1\q4.py

class Pontuacao:
    """
    Representa a pontuação do jogo com um método para zerar os pontos.
    """
    def zerar_pontos(self):
        """
        Imprime uma mensagem indicando que a pontuação foi zerada.
        """
        print("Pontuação zerada!")

#Instancia a classe Pontuacao e chama o método zerar_pontos()
if __name__ == "__main__":
    placar = Pontuacao()
    placar.zerar_pontos()
