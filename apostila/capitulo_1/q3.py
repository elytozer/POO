#Arquivo capitulo_1\q3.py

class Inimigo:
    """
    Representa um inimigo com um método para atacar.
    """
    def atacar(self):
        """
        Imprime uma mensagem indicando que o inimigo atacou.
        """
        print("O inimigo atacou!")

#Instancia a classe Inimigo e chama o método atacar()
if __name__ == "__main__":
    vilao = Inimigo()
    vilao.atacar()
