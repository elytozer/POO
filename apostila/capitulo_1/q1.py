# Arquivo capitulo_1/q1.py

class Jogo:
    """
    Representa um jogo com um método para iniciar.
    """
    def iniciar(self):
        """
        Imprime uma mensagem indicando que o jogo começou.
        """
        print("O jogo começou!")

#Instancia a classe Jogo e chama o método iniciar()
if __name__ == "__main__":
    meu_jogo = Jogo()
    meu_jogo.iniciar()
