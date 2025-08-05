# Arquivo capitulo_1\q7.py

class Pontuacao:
    """
    Representa a pontuação do jogo com métodos para adicionar e mostrar pontos.
    """
    def __init__(self):
        """
        Inicializa a pontuação em 0.
        """
        self.pontos = 0

    def adicionar_pontos(self, quantidade):
        """
        Adiciona uma quantidade específica de pontos à pontuação total.
        :param quantidade: O número de pontos a ser adicionado.
        """
        self.pontos += quantidade
        print(f"Adicionados {quantidade} pontos. Pontuação atual: {self.pontos}")

    def mostrar_pontos(self):
        """
        Imprime a pontuação atual.
        """
        print(f"Pontuação atual: {self.pontos}")

#Instancia a classe Pontuacao e testa seus métodos
if __name__ == "__main__":
    placar_do_jogo = Pontuacao()
    placar_do_jogo.mostrar_pontos() #Deve imprimir 0
    placar_do_jogo.adicionar_pontos(50)
    placar_do_jogo.adicionar_pontos(25)
    placar_do_jogo.mostrar_pontos() #Deve imprimir 75
