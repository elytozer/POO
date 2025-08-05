# Arquivo capitulo_2/q35.py
# Solução para a Questão 35: Classe Aliado e subclasses (Mago e Guerreiro).
# Inclui a associação entre Aliado e Jogador para a Questão 54.

# Classe Personagem (base para Aliado, com setters de vida e defesa para interações)
class Personagem:
    """
    Representa um personagem básico com nome, vida e defesa.
    Inclui getters e setters para atributos encapsulados, permitindo
    interações como cura e aumento de defesa por itens ou habilidades.
    """
    def __init__(self, nome, vida=100, defesa=50):
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
        Setter para o atributo de vida, garantindo que não seja negativo
        e não exceda 100 (limite comum para personagens).
        """
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor
        if self.__vida > 100: # Limite de vida para cura
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
            print("Defesa deve ser entre 0 e 100. Ajustando para 50.")
            self.__defesa = 50
        else:
            self.__defesa = valor
        if self.__defesa > 100: # Limite de defesa para equipamento
            self.__defesa = 100

    def dizer_nome(self):
        """
        Imprime o nome do personagem.
        """
        print(f"Meu nome é {self.nome}.")

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

# Classe Aliado (Q35: Classe base para aliados, herda de Personagem)
# Inclui a associação para a Questão 54.
class Aliado(Personagem):
    """
    Classe base para aliados, que herda de Personagem.
    Aliados podem acompanhar um jogador e possuem uma habilidade especial.
    """
    def __init__(self, nome, vida=100, defesa=50):
        super().__init__(nome, vida, defesa)
        self.acompanhando_jogador = None # Q54: Associação - Aliado pode acompanhar um Jogador

    def habilidade_especial(self):
        """
        Método abstrato para a habilidade especial do aliado.
        Deve ser implementado por todas as subclasses de Aliado.
        """
        raise NotImplementedError("Habilidade especial deve ser implementada pelas subclasses.")

    def acompanhar(self, jogador): # Q54: Método para associar o aliado a um jogador
        """
        Define qual jogador o aliado está acompanhando.
        :param jogador: O objeto Jogador a ser acompanhado.
        """
        self.acompanhando_jogador = jogador
        print(f"{self.nome} agora está acompanhando {jogador.nome}.")

# Classe Mago (Q35: Herda de Aliado)
class Mago(Aliado):
    """
    Representa um Mago, que herda de Aliado.
    Sua habilidade especial é um feitiço de cura.
    """
    def __init__(self, nome="Gandalf", vida=80, defesa=30):
        super().__init__(nome, vida, defesa)

    def habilidade_especial(self):
        """
        Mago lança um feitiço de cura.
        Se estiver acompanhando um jogador, cura a vida desse jogador.
        """
        print(f"{self.nome} lançou um feitiço de cura!")
        if self.acompanhando_jogador:
            # Assume que o objeto Jogador tem um atributo 'vida' com setter
            self.acompanhando_jogador.vida += 30 # Cura 30 pontos de vida
            # O setter de vida do Jogador (se implementado) deve lidar com o limite de 100
            print(f"{self.nome} curou {self.acompanhando_jogador.nome}. Vida atual: {self.acompanhando_jogador.vida}")
        else:
            print(f"{self.nome} não está acompanhando ninguém para curar.")

# Classe Guerreiro (Q35: Herda de Aliado)
class Guerreiro(Aliado):
    """
    Representa um Guerreiro, que herda de Aliado.
    Sua habilidade especial é um golpe poderoso.
    """
    def __init__(self, nome="Boromir", vida=120, defesa=70):
        super().__init__(nome, vida, defesa)

    def habilidade_especial(self):
        """
        Guerreiro usa um golpe poderoso.
        (Neste exemplo, apenas imprime uma mensagem, mas poderia causar dano a um inimigo).
        """
        print(f"{self.nome} usou um golpe poderoso!")
        print("Causou grande dano a um inimigo próximo (simulado)!")

# Classe Jogador (necessária para Aliado.acompanhar e Mago.habilidade_especial)
# Uma versão simplificada com o atributo 'vida' e seu setter.
class Jogador:
    """
    Representa um jogador simples, necessário para demonstração da associação com Aliado.
    Possui um atributo de vida com setter.
    """
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.__vida = vida

    @property
    def vida(self):
        """
        Getter para o atributo de vida do jogador.
        """
        return self.__vida

    @vida.setter
    def vida(self, valor):
        """
        Setter para o atributo de vida do jogador, garantindo que não seja negativo
        e não exceda 100.
        """
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor
        if self.__vida > 100:
            self.__vida = 100

# --- Exemplo de Uso (Questão 35 e 54) ---
if __name__ == "__main__":
    print("--- Questão 35: Classe Aliado e subclasses (Mago e Guerreiro) ---")
    print("--- E Questão 54: Associação entre Aliado e Jogador ---")

    # Cria instâncias das subclasses de Aliado
    mago_aliado = Mago("Merlin")
    guerreiro_aliado = Guerreiro("Conan")

    print("\n--- Testando Habilidades Especiais sem acompanhamento ---")
    mago_aliado.habilidade_especial() # Deve dizer que não há ninguém para curar
    guerreiro_aliado.habilidade_especial()

    print("\n" + "=" * 40 + "\n")

    # Cria uma instância de Jogador para o aliado acompanhar
    jogador_principal = Jogador("Herói Principal", vida=70)
    print(f"Vida inicial do {jogador_principal.nome}: {jogador_principal.vida}")

    # Demonstração da associação (Q54)
    print(f"\n--- {mago_aliado.nome} irá acompanhar {jogador_principal.nome} ---")
    mago_aliado.acompanhar(jogador_principal)
    print(f"Status de acompanhamento do {mago_aliado.nome}: {mago_aliado.acompanhando_jogador.nome}")

    # Mago usa habilidade especial para curar o jogador que ele está acompanhando
    print(f"\n--- {mago_aliado.nome} usa sua Habilidade Especial para curar ---")
    mago_aliado.habilidade_especial() # Agora deve curar o jogador
    print(f"Vida do {jogador_principal.nome} após cura: {jogador_principal.vida}")

    print("\n" + "=" * 40 + "\n")

    # Demonstração do Guerreiro (sem acompanhamento específico para a habilidade aqui)
    print(f"--- {guerreiro_aliado.nome} usa sua Habilidade Especial ---")
    guerreiro_aliado.habilidade_especial()

    print("\nTeste de q35.py e q54.py concluído!")
