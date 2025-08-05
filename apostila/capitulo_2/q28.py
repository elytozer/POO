# Arquivo capitulo_2\q28.py

import random # Necessário para o ataque do jogador (simulação)

# Classe Pontuacao (base para a classe Jogador)
# Inclui encapsulamento para 'pontos' e um setter que impede valores negativos.
class Pontuacao:
    """
    Representa a pontuação do jogo com métodos para gerenciar pontos.
    """
    def __init__(self, pontos=0):
        self.__pontos = pontos # Private attribute for points

    @property # Getter for 'pontos'
    def pontos(self):
        """
        Returns the current score.
        """
        return self.__pontos

    @pontos.setter # Setter for 'pontos', prevents negative values (from Q19)
    def pontos(self, valor):
        """
        Sets the score, ensuring it's not negative.
        """
        if valor < 0:
            print("Score cannot be negative. Setting to 0.")
            self.__pontos = 0
        else:
            self.__pontos = valor

    def adicionar_pontos(self, quantidade):
        """
        Adds a specified amount of points to the total score.
        :param quantidade: The number of points to add.
        """
        self.pontos += quantidade # Uses the setter
        print(f"Adicionados {quantidade} pontos. Pontuação atual: {self.pontos}")

# Classe Inimigo (necessária para a simulação de ataque do Jogador)
class Inimigo:
    """
    Represents an enemy with health.
    """
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida

    def tomar_dano(self, dano):
        """
        Reduces the enemy's health by the damage value.
        If health reaches 0 or less, prints "Enemy defeated!".
        :param dano: The amount of damage to apply.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. {self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

# Classe Jogador (base para herança da classe JogadorPremium)
# Inclui encapsulamento para 'energia' e um método para atacar inimigos.
class Jogador:
    """
    Represents a player with a name, energy, and score.
    Can use energy, manage score, and attack enemies.
    """
    def __init__(self, nome, energia=50, pontos=0):
        self.nome = nome
        self.__energia = self._validar_energia(energia) # Private attribute for energy (from Q17)
        self.pontuacao = Pontuacao(pontos) # Uses the Pontuacao class
        self.vida = 100 # Added for combat simulation

    def _validar_energia(self, energia):
        """
        Helper method to ensure energy value is between 0 and 100.
        """
        if not 0 <= energia <= 100:
            print("Energy must be between 0 and 100. Adjusting value.")
            return max(0, min(100, energia))
        return energia

    @property # Getter for 'energia'
    def energia(self):
        """
        Returns the current energy of the player.
        """
        return self.__energia

    @energia.setter # Setter for 'energia'
    def energia(self, valor):
        """
        Sets the player's energy, validating the input value.
        """
        self.__energia = self._validar_energia(valor)

    def tomar_dano(self, dano):
        """
        Reduces the player's health by the damage value.
        If health reaches 0 or less, prints "Game Over!".
        :param dano: The amount of damage to apply.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

    def usar_energia(self, quantidade):
        """
        Reduces the player's energy by the specified amount.
        Returns True if energy was used successfully, False otherwise.
        :param quantidade: The amount of energy to use.
        """
        if self.energia >= quantidade:
            self.energia -= quantidade
            return True
        else:
            print(f"{self.nome} sem energia suficiente!")
            return False

    def atacar(self, inimigo):
        """
        The player attacks an enemy. Costs 10 energy per attack.
        If the enemy is defeated, points are added.
        :param inimigo: The enemy object to attack.
        """
        if not self.usar_energia(10): # Energy cost per attack
            return False # Cannot attack without enough energy

        dano = random.randint(10, 25) # Player's base damage
        print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano.")
        inimigo.tomar_dano(dano)

        if inimigo.vida <= 0:
            self.adicionar_pontos(10) # Calls the method that can be overridden by subclasses
            print(f"{self.nome} derrotou {inimigo.nome}!")
        return True

    def adicionar_pontos(self, quantidade): # Method to be overridden by subclasses (Q38)
        """
        Adds points to the player's score.
        :param quantidade: The amount of points to add.
        """
        self.pontuacao.adicionar_pontos(quantidade)

# Classe JogadorPremium (Q28: herda de Jogador, bônus de pontuação)
# Sobrescreve o método adicionar_pontos() para a Questão 38.
class JogadorPremium(Jogador):
    """
    Represents a premium player who inherits from Jogador and receives a score bonus.
    """
    def __init__(self, nome, energia=50, pontos=0, bonus_multiplicador=1.5): # Q28 constructor
        super().__init__(nome, energia, pontos) # Call base class constructor
        self.bonus_multiplicador = bonus_multiplicador
        print(f"Jogador Premium {self.nome} criado com multiplicador de bônus: {self.bonus_multiplicador}x")

    def adicionar_pontos(self, quantidade): # Q38: Overrides 'adicionar_pontos' for bonus
        """
        Adds points to the premium player's score with a multiplier.
        :param quantidade: The amount of points to add.
        """
        pontos_com_bonus = int(quantidade * self.bonus_multiplicador)
        self.pontuacao.adicionar_pontos(pontos_com_bonus) # Uses the Pontuacao object's method
        print(f"Bônus Premium! {quantidade} pontos se tornaram {pontos_com_bonus} pontos.")

# --- Exemplo de Uso (Questão 28 e 38) ---
if __name__ == "__main__":
    print("--- Questão 28: Classe JogadorPremium (Herança) ---")
    print("--- E Questão 38: Modifique a classe JogadorPremium (Reescrita e Polimorfismo) ---")

    # Create a standard player and a premium player
    jogador_padrao = Jogador("João")
    jogador_premium = JogadorPremium("Maria", bonus_multiplicador=2.0)

    # Create an enemy for combat simulation
    inimigo_teste = Inimigo("Gargula", vida=40)

    print(f"\n{jogador_padrao.nome} (Pontos: {jogador_padrao.pontuacao.pontos}) vs {inimigo_teste.nome} (Vida: {inimigo_teste.vida})")
    # Simulate defeating the enemy by the standard player
    inimigo_teste.vida = 1 # Reduce health to ensure defeat in one hit for demonstration
    jogador_padrao.atacar(inimigo_teste)
    print(f"Pontos de {jogador_padrao.nome} após derrotar inimigo: {jogador_padrao.pontuacao.pontos}")

    # Create a new enemy for the premium player
    inimigo_teste_2 = Inimigo("Gargula Elite", vida=40)
    print(f"\n{jogador_premium.nome} (Pontos: {jogador_premium.pontuacao.pontos}) vs {inimigo_teste_2.nome} (Vida: {inimigo_teste_2.vida})")
    # Simulate defeating the enemy by the premium player
    inimigo_teste_2.vida = 1 # Reduce health to ensure defeat in one hit for demonstration
    jogador_premium.atacar(inimigo_teste_2) # This will call the overridden 'adicionar_pontos'
    print(f"Pontos de {jogador_premium.nome} após derrotar inimigo: {jogador_premium.pontuacao.pontos}")

    print("\nTeste de q28.py e q38.py concluído!")
