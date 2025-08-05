# Arquivo capitulo_2/q36.py
# Solução para a Questão 36: Modifique a classe NPC (Reescrita e Polimorfismo).

# Classe Personagem (base para a classe NPC)
# Incluída para garantir que o arquivo q36.py seja autônomo.
class Personagem:
    """
    Representa um personagem básico no jogo.
    """
    def __init__(self, nome, vida=100, defesa=50):
        """
        Inicializa um novo personagem.
        :param nome: O nome do personagem.
        :param vida: A vida inicial do personagem.
        :param defesa: A defesa inicial do personagem.
        """
        self.nome = nome
        self.__vida = vida
        self.__defesa = defesa

    @property
    def vida(self):
        """
        Getter para o atributo de vida.
        """
        return self.__vida

    @vida.setter
    def vida(self, valor):
        """
        Setter para o atributo de vida, garantindo que não seja negativo.
        """
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor

    @property
    def defesa(self):
        """
        Getter para o atributo de defesa.
        """
        return self.__defesa

    @defesa.setter
    def defesa(self, valor):
        """
        Setter para o atributo de defesa, garantindo que o valor fique entre 0 e 100.
        """
        if not 0 <= valor <= 100:
            print("Defesa deve ser entre 0 e 100. Definindo como 50.")
            self.__defesa = 50
        else:
            self.__defesa = valor

    def falar(self):
        """
        Método 'falar' original da classe Personagem.
        """
        print(f"{self.nome}: Eu sou um personagem genérico.")

# Classe NPC (Q26, Q36: herda de Personagem, sobrescreve falar())
class NPC(Personagem):
    """
    Representa um NPC (Non-Player Character) que herda de Personagem.
    Sobrescreve o método 'falar()' para ter uma fala específica de NPC.
    """
    def __init__(self, nome, vida=100, defesa=50):
        """
        Inicializa um novo NPC, chamando o construtor da classe base (Personagem).
        :param nome: O nome do NPC.
        :param vida: A vida inicial do NPC.
        :param defesa: A defesa inicial do NPC.
        """
        super().__init__(nome, vida, defesa)

    def falar(self): # Q36: Sobrescrita do método 'falar()'
        """
        NPC fala uma mensagem diferente do método original de Personagem,
        demonstrando polimorfismo.
        """
        print(f"{self.nome}: Olá, viajante! Precisa de alguma coisa? Posso ajudar.")

# --- Exemplo de Uso (Questão 36) ---
if __name__ == "__main__":
    print("--- Questão 36: Modifique a classe NPC (Reescrita e Polimorfismo) ---")

    # Cria uma instância da classe base Personagem
    personagem_generico = Personagem("Aventureiro Comum")
    print("\nPersonagem Genérico falando:")
    personagem_generico.falar() # Chama o método 'falar' da classe Personagem

    print("\n" + "=" * 40 + "\n")

    # Cria uma instância da classe NPC
    aldeao = NPC("Aldeão Simples")
    print("NPC falando:")
    aldeao.falar() # Chama o método 'falar' sobrescrito da classe NPC

    print("\nTeste de q36.py concluído!")
