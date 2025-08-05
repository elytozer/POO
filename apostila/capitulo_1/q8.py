# Arquivo capitulo_1\q8.py

class Personagem:
    """
    Representa um personagem com atributos nome e vida, e um método para tomar dano.
    """
    def __init__(self, nome):
        """
        Inicializa um novo personagem com nome e vida.
        :param nome: O nome do personagem.
        """
        self.nome = nome
        self.vida = 100  # Vida inicializada em 100

    def tomar_dano(self, dano):
        """
        Reduz a vida do personagem pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Game Over!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0 #Garante que a vida não seja negativa
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

#Instancia a classe Personagem e testa o método tomar_dano()
if __name__ == "__main__":
    guerreiro = Personagem("Conan")
    print(f"Vida inicial de {guerreiro.nome}: {guerreiro.vida}")

    guerreiro.tomar_dano(30)
    guerreiro.tomar_dano(45)
    guerreiro.tomar_dano(30) #Isso deve levar a vida a 0 e imprimir "Game Over!"
    print(f"Vida final de {guerreiro.nome}: {guerreiro.vida}")
