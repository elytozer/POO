# Arquivo capitulo_2/q45.py
# Solução para a Questão 45: Classe AnimalMontaria e Cavaleiro (Herança Múltipla).

import random # Necessário para gerar dano aleatório de ataque

# Classe Personagem (base para Aliado/Guerreiro, com setters de vida para dano)
# Incluída para garantir que o arquivo q45.py seja autônomo.
class Personagem:
    """
    Representa um personagem básico com nome, vida e defesa.
    Inclui getters e setters para atributos encapsulados, permitindo
    interações como tomar dano.
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
        if self.__vida > 100: # Limite de vida (exemplo)
            self.__vida = 100

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

    def tomar_dano(self, dano):
        """
        Reduz a vida do personagem pelo valor do dano, considerando a defesa.
        :param dano: A quantidade de dano a ser aplicada.
        """
        dano_real = max(0, dano - (self.defesa // 2)) # Reduz dano pela metade da defesa
        self.vida -= dano_real # Usa o setter de vida
        if self.vida <= 0:
            print(f"{self.nome} recebeu {dano_real} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano_real} de dano. Vida restante: {self.vida}.")

    def atacar(self, alvo):
        """
        Método de ataque padrão.
        :param alvo: O objeto a ser atacado.
        """
        dano = random.randint(10, 20)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
        alvo.tomar_dano(dano)

# Classe Aliado (base para Guerreiro)
class Aliado(Personagem):
    """
    Classe base para aliados, herda de Personagem.
    """
    def __init__(self, nome, vida=100, defesa=50):
        """
        Inicializa um novo aliado.
        :param nome: O nome do aliado.
        :param vida: A vida inicial do aliado.
        :param defesa: A defesa inicial do aliado.
        """
        super().__init__(nome, vida, defesa)

    def habilidade_especial(self):
        """
        Método abstrato para a habilidade especial do aliado.
        Deve ser implementado por todas as subclasses de Aliado.
        """
        raise NotImplementedError("Habilidade especial deve ser implementada pelas subclasses.")

# Classe Guerreiro (base para Cavaleiro)
class Guerreiro(Aliado):
    """
    Representa um Guerreiro, herda de Aliado.
    """
    def __init__(self, nome="Guerreiro", vida=120, defesa=70):
        """
        Inicializa um novo Guerreiro.
        :param nome: O nome do guerreiro.
        :param vida: A vida inicial do guerreiro.
        :param defesa: A defesa inicial do guerreiro.
        """
        super().__init__(nome, vida, defesa)

    def habilidade_especial(self):
        """
        Guerreiro usa um golpe poderoso.
        """
        print(f"{self.nome} usou um golpe poderoso!")

# Classe AnimalMontaria (Q45)
class AnimalMontaria:
    """
    Classe para animais que podem ser montados.
    """
    def __init__(self, nome_montaria="Cavalo", velocidade=20):
        """
        Inicializa um novo animal de montaria.
        :param nome_montaria: O nome da montaria (ex: "Cavalo", "Pégaso").
        :param velocidade: A velocidade da montaria.
        """
        self.nome_montaria = nome_montaria
        self.velocidade = velocidade

    def montar(self):
        """
        Imprime uma mensagem ao montar o animal.
        """
        print(f"Você montou o {self.nome_montaria} e está pronto para cavalgar!")

# Classe Cavaleiro (Q45: herda de Guerreiro e AnimalMontaria)
class Cavaleiro(Guerreiro, AnimalMontaria):
    """
    Representa um Cavaleiro que herda de Guerreiro e AnimalMontaria.
    Pode lutar montado em uma criatura, combinando habilidades de combate e mobilidade.
    """
    def __init__(self, nome="Sir Galahad", vida=130, defesa=75, nome_montaria="Cavalo de Guerra"):
        """
        Inicializa um novo Cavaleiro.
        Chama os construtores das classes base Guerreiro e AnimalMontaria.
        :param nome: O nome do cavaleiro.
        :param vida: A vida inicial do cavaleiro.
        :param defesa: A defesa inicial do cavaleiro.
        :param nome_montaria: O nome da montaria do cavaleiro.
        """
        # Chama o construtor da classe Guerreiro
        Guerreiro.__init__(self, nome, vida, defesa)
        # Chama o construtor da classe AnimalMontaria
        AnimalMontaria.__init__(self, nome_montaria)
        print(f"Cavaleiro {self.nome} criado com sua montaria {self.nome_montaria}.")

    def atacar_montado(self, alvo):
        """
        Ataque especial do cavaleiro enquanto montado, causando dano extra.
        :param alvo: O objeto a ser atacado.
        """
        dano_montado = random.randint(20, 40)
        print(f"{self.nome} atacou {alvo.nome} montado em {self.nome_montaria} causando {dano_montado} de dano!")
        alvo.tomar_dano(dano_montado)

# --- Exemplo de Uso (Questão 45) ---
if __name__ == "__main__":
    print("--- Questão 45: Classe AnimalMontaria e Cavaleiro (Herança Múltipla) ---")

    # Cria uma instância de Cavaleiro
    cavaleiro_montado = Cavaleiro("Ricardo Coração de Leão", nome_montaria="Fúria")

    # Cria um inimigo para ser o alvo dos ataques
    inimigo_alvo = Personagem("Bandido", vida=80)
    print(f"\nVida inicial do {inimigo_alvo.nome}: {inimigo_alvo.vida}")

    print("\n--- Cavaleiro usa habilidades de suas classes base e própria ---")
    cavaleiro_montado.montar() # Chama o método da classe AnimalMontaria
    cavaleiro_montado.atacar(inimigo_alvo) # Chama o método da classe Guerreiro (ataque padrão)
    cavaleiro_montado.atacar_montado(inimigo_alvo) # Chama o método próprio da classe Cavaleiro

    print(f"\nVida do {inimigo_alvo.nome} após ataques: {inimigo_alvo.vida}")

    print("\nTeste de q45.py concluído!")
