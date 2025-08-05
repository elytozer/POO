# Arquivo capitulo_1\q6.py

class Personagem:
    """
    Representa um personagem com um atributo nome e um método para dizer o nome.
    """
    def __init__(self, nome):
        """
        Inicializa um novo personagem com um nome.
        :param nome: O nome do personagem.
        """
        self.nome = nome

    def dizer_nome(self):
        """
        Imprime o nome do personagem.
        """
        print(f"Meu nome é {self.nome}.")

#Instancia a classe Personagem com um nome e testa o método
if __name__ == "__main__":
    heroi = Personagem("Aragorn")
    heroi.dizer_nome()
