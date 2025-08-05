# Arquivo capitulo_2\q26.py

# Classe Personagem (base para herança, com encapsulamento e construtor de Q22)
# Esta classe é incluída para garantir que o arquivo q26.py seja autônomo.
class Personagem:
    """
    Represents a character in the game with a name, health, and defense.
    Includes getters and setters for encapsulated attributes.
    """
    def __init__(self, nome, vida=100, defesa=50):
        self.nome = nome
        self.__vida = vida  # Private attribute for health
        self.__defesa = self._validar_defesa(defesa) # Private attribute for defense

    def _validar_defesa(self, defesa):
        """
        Helper method to ensure defense value is between 0 and 100.
        """
        if not 0 <= defesa <= 100:
            print("Defense must be between 0 and 100. Setting to 50.")
            return 50
        return defesa

    @property # Getter for 'vida' (health)
    def vida(self):
        """
        Returns the current health of the character.
        """
        return self.__vida

    @vida.setter # Setter for 'vida' (health)
    def vida(self, valor):
        """
        Sets the character's health, ensuring it's not negative.
        """
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor

    @property # Getter for 'defesa' (defense)
    def defesa(self):
        """
        Returns the defense value of the character.
        """
        return self.__defesa

    @defesa.setter # Setter for 'defesa' (defense), ensures value is between 0 and 100
    def defesa(self, valor):
        """
        Sets the character's defense, validating the input value.
        """
        self.__defesa = self._validar_defesa(valor)
        print(f"Defense of {self.nome} adjusted to: {self.__defesa}.")

    def dizer_nome(self):
        """
        Prints the character's name.
        """
        print(f"Meu nome é {self.nome}.")

    def tomar_dano(self, dano):
        """
        Reduces the character's health by the damage value, considering defense.
        If health reaches 0 or less, prints "Game Over!".
        :param dano: The amount of damage to be applied.
        """
        dano_real = max(0, dano - (self.defesa // 2)) # Reduces damage by half of defense
        self.vida -= dano_real # Uses the 'vida' setter
        if self.vida <= 0:
            print(f"{self.nome} received {dano_real} damage. Remaining health: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} received {dano_real} damage. Remaining health: {self.vida}.")

    def atacar(self, alvo):
        """
        Standard attack method for a character.
        :param alvo: The target to be attacked.
        """
        print(f"{self.nome} atacou {alvo.nome}.")

# Classe NPC (Q26: herda de Personagem, não pode atacar)
class NPC(Personagem):
    """
    Represents an NPC (Non-Player Character) that inherits from Personagem.
    NPCs cannot attack.
    """
    def __init__(self, nome, vida=100, defesa=50):
        # Call the constructor of the base class (Personagem)
        super().__init__(nome, vida, defesa)
        print(f"NPC {self.nome} created.")

    def atacar(self, alvo): # Q26: Overrides the 'atacar' method to prevent attack
        """
        NPCs cannot attack. This method overrides the base class's attack method.
        :param alvo: The target (ignored as NPC cannot attack).
        """
        print(f"{self.nome} (NPC) não pode atacar.")

    def falar(self): # Added for Q36 (anticipated)
        """
        NPC speaks a standard message.
        """
        print(f"{self.nome}: Olá, aventureiro! Precisa de ajuda?")

# --- Exemplo de Uso (Questão 26) ---
if __name__ == "__main__":
    print("--- Questão 26: Classe NPC (Herança) ---")

    # Create an instance of NPC
    aldeao = NPC("Aldeão João", vida=70)
    aldeao.dizer_nome()
    aldeao.falar()

    # Create a regular Personagem to be a potential target
    inimigo_simulado = Personagem("Goblin de Teste", vida=50)

    print(f"\nAttempting to make {aldeao.nome} attack {inimigo_simulado.nome}:")
    aldeao.atacar(inimigo_simulado) # This should print the message that NPC cannot attack

    print(f"\nHealth of {inimigo_simulado.nome} after attempted attack: {inimigo_simulado.vida}")

    print("Teste de q26.py concluído!")
