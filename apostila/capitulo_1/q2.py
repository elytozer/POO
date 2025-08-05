# Arquivo capitulo_1\q2.py

class Personagem:
    """
    Representa um personagem com um método para pular.
    """
    def pular(self):
        """
        Imprime uma mensagem indicando que o personagem pulou.
        """
        print("O personagem pulou!")

#Instancia a classe Personagem e chama o método pular()
if __name__ == "__main__":
    heroi = Personagem()
    heroi.pular()

