# Arquivo capitulo_2\q23.py

import random # Para dano aleatório

# Classe Personagem (necessária para Inimigo.atacar)
class Personagem:
    """
    Representa um personagem simples para ser alvo de ataques.
    """
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida

    def tomar_dano(self, dano):
        """
        Reduz a vida do personagem pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Game Over!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

class Inimigo:
    """
    Representa um inimigo com um construtor modificado para aceitar nome, vida e forca.
    """
    def __init__(self, nome, vida=100, forca=15): # Q23: nome, vida e forca como parâmetros
        self.nome = nome
        self.__vida = vida # Mantido privado para consistência com Q10/Q11
        self.__forca = forca # Mantido privado para consistência com Q16

    @property
    def vida(self):
        """
        Retorna a vida atual do inimigo.
        """
        return self.__vida

    @vida.setter
    def vida(self, valor):
        """
        Define a vida do inimigo, garantindo que não seja negativa.
        """
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor

    def atacar(self, alvo):
        """
        Ataca um alvo, exibindo a força do ataque.
        :param alvo: O objeto a ser atacado (Personagem).
        """
        dano = random.randint(self.__forca - 5, self.__forca + 5) # Usa __forca internamente
        print(f"{self.nome} (Força: {self.__forca}) atacou {alvo.nome} causando {dano} de dano.")
        alvo.tomar_dano(dano)

# --- Exemplo de Uso (Questão 23) ---
if __name__ == "__main__":
    print("--- Questão 23: Ajuste na classe Inimigo (Construtores) ---")

    # Criando inimigos com diferentes valores no construtor
    inimigo1 = Inimigo("Esqueleto", vida=60, forca=10)
    print(f"Inimigo 1: {inimigo1.nome}, Vida: {inimigo1.vida}, Força: {inimigo1._Inimigo__forca}") # Acesso direto ao atributo privado para demonstração

    inimigo2 = Inimigo("Minotauro", vida=150, forca=30)
    print(f"Inimigo 2: {inimigo2.nome}, Vida: {inimigo2.vida}, Força: {inimigo2._Inimigo__forca}")

    inimigo3 = Inimigo("Zumbi") # Usa vida e força padrão (100 e 15)
    print(f"Inimigo 3: {inimigo3.nome}, Vida: {inimigo3.vida}, Força: {inimigo3._Inimigo__forca}")

    # Testando o ataque
    heroi = Personagem("Aventureiro")
    print(f"\nVida inicial do {heroi.nome}: {heroi.vida}")
    inimigo2.atacar(heroi)
    print(f"Vida do {heroi.nome} após ataque: {heroi.vida}")

    print("Teste de q23.py concluído!")
