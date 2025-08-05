# Arquivo capitulo_2/q42.py
# Solução para a Questão 42: Classe Voador e Dragao (Herança Múltipla).

import random # Necessário para gerar dano aleatório

# Classe Inimigo (base para herança da classe Dragao)
# Inclui encapsulamento para 'vida' e 'forca' e métodos para tomar dano e atacar.
class Inimigo:
    """
    Representa um inimigo no jogo com nome, vida e força.
    """
    def __init__(self, nome, vida=100, forca=15):
        """
        Inicializa um novo inimigo.
        :param nome: O nome do inimigo.
        :param vida: A vida inicial do inimigo.
        :param forca: A força base de ataque do inimigo.
        """
        self.nome = nome
        self.__vida = vida    # Atributo privado para vida
        self.__forca = forca  # Atributo privado para força

    @property # Getter para 'vida'
    def vida(self):
        """
        Retorna a vida atual do inimigo.
        """
        return self.__vida

    @vida.setter # Setter para 'vida'
    def vida(self, valor):
        """
        Define a vida do inimigo, garantindo que não seja negativa.
        """
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor

    @property # Getter para 'forca'
    def forca(self):
        """
        Retorna a força do inimigo.
        """
        return self.__forca

    def tomar_dano(self, dano):
        """
        Reduz a vida do inimigo pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Inimigo derrotado!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano # Usa o setter de vida
        if self.vida <= 0:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. {self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

    def atacar(self, alvo):
        """
        Ataca um alvo, causando dano baseado na força do inimigo.
        :param alvo: O objeto a ser atacado (Personagem ou outro Inimigo).
        """
        dano = random.randint(self.__forca - 5, self.__forca + 5) # Usa o atributo privado __forca
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
        alvo.tomar_dano(dano) # Assume que o alvo tem um método tomar_dano

# Classe Personagem (necessária para que o método atacar() do Inimigo/Dragao funcione)
# Inclui um método básico para tomar dano.
class Personagem:
    """
    Representa um personagem simples para ser alvo de ataques.
    """
    def __init__(self, nome, vida=100):
        """
        Inicializa um novo personagem.
        :param nome: O nome do personagem.
        :param vida: A vida inicial do personagem.
        """
        self.nome = nome
        self.vida = vida # Não encapsulado para simplicidade, mas Personagem em outras Qs tem encapsulamento

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

# Classe Voador (Q42)
class Voador:
    """
    Classe para entidades que podem voar.
    """
    def voar(self):
        """
        Imprime uma mensagem de voo.
        """
        print("Estou voando alto!")

# Classe Dragao (Q42: herda de Inimigo e Voador)
class Dragao(Inimigo, Voador):
    """
    Representa um Dragão que herda de Inimigo e Voador.
    Pode atacar e voar.
    """
    def __init__(self, nome="Dragão de Fogo", vida=300, forca=40):
        """
        Inicializa um novo Dragão.
        Chama o construtor da classe Inimigo para inicializar atributos de inimigo.
        :param nome: O nome do dragão.
        :param vida: A vida inicial do dragão.
        :param forca: A força de ataque do dragão.
        """
        # Chama o construtor da primeira classe pai na MRO (Method Resolution Order)
        # Para herança múltipla, é comum chamar explicitamente os construtores
        # das classes base para garantir que todos os atributos sejam inicializados.
        Inimigo.__init__(self, nome, vida, forca)
        # A classe Voador não tem um construtor que precise ser chamado com super()
        # ou explicitamente neste exemplo.
        print(f"Dragão {self.nome} criado. Vida: {self.vida}, Força: {self.forca}.")

    def baforar_fogo(self, alvo):
        """
        Ataque especial de baforar fogo do dragão.
        :param alvo: O objeto a ser atacado.
        """
        dano_fogo = random.randint(25, 50)
        print(f"{self.nome} baforou fogo em {alvo.nome} causando {dano_fogo} de dano de fogo!")
        alvo.tomar_dano(dano_fogo)

# --- Exemplo de Uso (Questão 42) ---
if __name__ == "__main__":
    print("--- Questão 42: Classe Voador e Dragao (Herança Múltipla) ---")

    # Cria uma instância de Dragão
    dragao_vermelho = Dragao("Smaug", vida=500, forca=60)

    # Cria um personagem para ser o alvo dos ataques do dragão
    heroi = Personagem("Cavaleiro Destemido", vida=300)

    print("\n--- Demonstração das habilidades do Dragão ---")
    dragao_vermelho.voar() # Chama o método da classe Voador
    dragao_vermelho.atacar(heroi) # Chama o método da classe Inimigo
    dragao_vermelho.baforar_fogo(heroi) # Chama o método próprio da classe Dragao

    print(f"\nVida do {heroi.nome} após ataques: {heroi.vida}")

    print("\nTeste de q42.py concluído!")
