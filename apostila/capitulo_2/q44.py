# Arquivo capitulo_2/q44.py
# Solução para a Questão 44: Classe MagiaElemental e MagoElemental (Herança Múltipla).

import random # Necessário para gerar dano aleatório de magia

# Classe Personagem (base para Aliado/Mago, com setters de vida para dano de magia)
# Incluída para garantir que o arquivo q44.py seja autônomo.
class Personagem:
    """
    Representa um personagem básico com nome, vida e defesa.
    Inclui getters e setters para atributos encapsulados, permitindo
    interações como dano de magia.
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

# Classe Aliado (base para Mago)
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

# Classe Mago (base para MagoElemental)
class Mago(Aliado):
    """
    Representa um Mago, herda de Aliado.
    """
    def __init__(self, nome="Mago", vida=80, defesa=30):
        """
        Inicializa um novo Mago.
        :param nome: O nome do mago.
        :param vida: A vida inicial do mago.
        :param defesa: A defesa inicial do mago.
        """
        super().__init__(nome, vida, defesa)

    def habilidade_especial(self):
        """
        Mago lança um feitiço genérico.
        """
        print(f"{self.nome} lançou um feitiço genérico!")

# Classe MagiaElemental (Q44)
class MagiaElemental:
    """
    Classe para entidades que podem lançar magias elementais.
    """
    def lancar_magia(self, tipo_magia, alvo):
        """
        Lança uma magia elemental em um alvo.
        :param tipo_magia: O tipo de magia (fogo, água, terra, ar).
        :param alvo: O objeto (Personagem, Inimigo, etc.) a ser afetado pela magia.
        """
        dano_magia = random.randint(15, 35)
        print(f"Lançando magia de {tipo_magia} em {alvo.nome} causando {dano_magia} de dano!")
        alvo.tomar_dano(dano_magia) # Assume que o alvo tem um método tomar_dano

# Classe MagoElemental (Q44: herda de Mago e MagiaElemental)
class MagoElemental(Mago, MagiaElemental):
    """
    Representa um Mago Elemental que herda de Mago e MagiaElemental.
    Pode usar magias específicas de fogo, água, terra ou ar.
    """
    def __init__(self, nome="Elara, a Conjuradora", vida=70, defesa=20):
        """
        Inicializa um novo Mago Elemental.
        Chama o construtor da classe Mago para inicializar atributos de mago.
        :param nome: O nome do mago elemental.
        :param vida: A vida inicial do mago elemental.
        :param defesa: A defesa inicial do mago elemental.
        """
        # Chama o construtor da primeira classe pai na MRO (Method Resolution Order)
        Mago.__init__(self, nome, vida, defesa)
        # A classe MagiaElemental não tem um construtor que precise ser chamado com super()
        # ou explicitamente neste exemplo.
        print(f"Mago Elemental {self.nome} criado. Vida: {self.vida}, Defesa: {self.defesa}.")

    def habilidade_especial(self): # Sobrescrita da habilidade especial do Mago
        """
        Mago Elemental conjura uma magia poderosa de um elemento aleatório.
        """
        print(f"{self.nome} conjura uma magia poderosa!")
        # Cria um inimigo simulado para a magia afetar
        inimigo_simulado = Personagem("Gólem de Pedra", vida=150)
        # Lança uma magia de um tipo elemental aleatório
        self.lancar_magia(random.choice(["fogo", "água", "terra", "ar"]), inimigo_simulado)

# --- Exemplo de Uso (Questão 44) ---
if __name__ == "__main__":
    print("--- Questão 44: Classe MagiaElemental e MagoElemental (Herança Múltipla) ---")

    # Cria uma instância de MagoElemental
    mago_elemental = MagoElemental("Ariel")

    # Chama a habilidade especial, que por sua vez usará 'lancar_magia'
    print("\n--- Mago Elemental usa Habilidade Especial ---")
    mago_elemental.habilidade_especial()

    print("\n" + "-" * 40 + "\n")

    # Demonstração de lançamento de magia específica
    inimigo_para_magia = Personagem("Minotauro", vida=100)
    print(f"Vida inicial do {inimigo_para_magia.nome}: {inimigo_para_magia.vida}")

    print(f"\n--- {mago_elemental.nome} lança uma magia de raio em {inimigo_para_magia.nome} ---")
    mago_elemental.lancar_magia("raio", inimigo_para_magia) # Lança uma magia específica
    print(f"Vida do {inimigo_para_magia.nome} após magia: {inimigo_para_magia.vida}")

    print("\nTeste de q44.py concluído!")
