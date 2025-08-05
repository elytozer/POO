# Arquivo capitulo_1/q10.py

class Personagem:
    """
    Representa um personagem no jogo com nome e vida.
    """
    def __init__(self, nome):
        """
        Inicializa um novo personagem.
        :param nome: O nome do personagem.
        """
        self.nome = nome
        self.vida = 100  # Vida inicializada em 100

    def dizer_nome(self):
        """
        Imprime o nome do personagem.
        """
        print(f"Meu nome é {self.nome}.")

    def tomar_dano(self, dano):
        """
        Reduz a vida do personagem pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Game Over!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0 # Garante que a vida não seja negativa
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

#Classe Inimigo
class Inimigo:
    """
    Representa um inimigo no jogo com nome e vida, capaz de atacar um Personagem.
    """
    def __init__(self, nome):
        """
        Inicializa um novo inimigo.
        :param nome: O nome do inimigo.
        """
        self.nome = nome
        self.vida = 100  #Vida inicializada em 100

    def atacar(self, alvo):
        """
        Ataca um objeto da classe Personagem, reduzindo sua vida em 10 pontos.
        :param alvo: O objeto Personagem a ser atacado.
        """
        dano = 10
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
        alvo.tomar_dano(dano) #Chama o método tomar_dano do alvo

#Exemplo de Uso
if __name__ == "__main__":
    print("--- Testando a Classe Inimigo e sua interação com Personagem ---")

    #Cria um personagem para ser o alvo
    heroi_alvo = Personagem("Heroi Teste")
    print(f"Vida inicial de {heroi_alvo.nome}: {heroi_alvo.vida}")

    #Cria um inimigo
    goblin = Inimigo("Goblin Malvado")
    print(f"Vida inicial de {goblin.nome}: {goblin.vida}")

    #O inimigo ataca o herói
    goblin.atacar(heroi_alvo)
    goblin.atacar(heroi_alvo)
    goblin.atacar(heroi_alvo)

    print(f"Vida final de {heroi_alvo.nome}: {heroi_alvo.vida}")
    print("Teste de q10.py concluído!")
