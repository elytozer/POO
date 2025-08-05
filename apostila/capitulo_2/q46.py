# Arquivo capitulo_2/q46.py
# Solução para a Questão 46: Associação entre Jogador e Arma.

import random # Necessário para gerar dano aleatório

# Classe Arma (simplificada para esta questão, baseada em Q31)
class Arma:
    """
    Representa uma arma que pode ser equipada por um jogador.
    """
    def __init__(self, nome, dano_base):
        """
        Inicializa uma nova arma.
        :param nome: O nome da arma.
        :param dano_base: O valor base de dano que a arma causa.
        """
        self.nome = nome
        self.dano_base = dano_base

    def usar(self):
        """
        Simula o uso da arma, retornando um valor de dano aleatório.
        """
        dano = random.randint(self.dano_base - 5, self.dano_base + 5)
        print(f"Usando {self.nome} causando {dano} de dano!")
        return dano

# Classe Inimigo (necessária para que o Jogador possa atacar um alvo)
class Inimigo:
    """
    Representa um inimigo simples para ser alvo de ataques.
    """
    def __init__(self, nome, vida=100):
        """
        Inicializa um novo inimigo.
        :param nome: O nome do inimigo.
        :param vida: A vida inicial do inimigo.
        """
        self.nome = nome
        self.vida = vida

    def tomar_dano(self, dano):
        """
        Reduz a vida do inimigo pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Inimigo derrotado!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

# Classe Jogador (Q46: Associação com Arma)
class Jogador:
    """
    Representa um jogador que pode equipar uma arma para usar em combate.
    Demonstra a associação onde um Jogador 'tem' uma Arma.
    """
    def __init__(self, nome, vida=100):
        """
        Inicializa um novo jogador.
        :param nome: O nome do jogador.
        :param vida: A vida inicial do jogador.
        """
        self.nome = nome
        self.vida = vida
        self.arma_equipada = None # Q46: Atributo para associar um objeto Arma

    def tomar_dano(self, dano):
        """
        Reduz a vida do jogador pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Game Over!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

    def equipar_arma(self, arma): # Q46: Método para estabelecer a associação
        """
        Equipa uma arma ao jogador.
        :param arma: O objeto Arma a ser equipado.
        """
        self.arma_equipada = arma
        print(f"{self.nome} equipou a arma: {arma.nome}")

    def atacar(self, inimigo):
        """
        O jogador ataca um inimigo. Se uma arma estiver equipada, usa-a para o ataque;
        caso contrário, usa um ataque básico.
        :param inimigo: O objeto Inimigo a ser atacado.
        """
        if self.arma_equipada:
            dano = self.arma_equipada.usar() # Usa o método 'usar' da arma equipada
        else:
            dano = random.randint(5, 15) # Dano base se não tiver arma
            print(f"{self.nome} atacou {inimigo.nome} com as mãos causando {dano} de dano.")

        inimigo.tomar_dano(dano)
        if inimigo.vida <= 0:
            print(f"{self.nome} derrotou {inimigo.nome}!")

# --- Exemplo de Uso (Questão 46) ---
if __name__ == "__main__":
    print("--- Questão 46: Associação entre Jogador e Arma ---")

    # Cria um jogador e um inimigo
    meu_jogador = Jogador("Herói da Espada")
    inimigo_alvo = Inimigo("Esqueleto", vida=50)

    print(f"Vida inicial de {inimigo_alvo.nome}: {inimigo_alvo.vida}")

    # Jogador ataca sem arma equipada
    print("\n--- Jogador ataca sem arma ---")
    meu_jogador.atacar(inimigo_alvo)
    print(f"Vida de {inimigo_alvo.nome} após ataque: {inimigo_alvo.vida}")

    # Cria uma arma
    espada_longa = Arma("Espada Longa", dano_base=25)

    # Jogador equipa a arma
    print("\n--- Jogador equipa a arma ---")
    meu_jogador.equipar_arma(espada_longa)

    # Jogador ataca com a arma equipada
    print("\n--- Jogador ataca com a arma ---")
    meu_jogador.atacar(inimigo_alvo)
    print(f"Vida de {inimigo_alvo.nome} após ataque: {inimigo_alvo.vida}")

    # A arma e o jogador existem independentemente.
    # Se o jogador for deletado, a espada_longa ainda existiria.
    # Se a espada_longa for deletada, o jogador ainda existiria (mas sem arma equipada).

    print("\nTeste de q46.py concluído!")
