# Arquivo capitulo_2/q54.py
# Solução para a Questão 54: Associação entre Aliado e Jogador.

# Classe Personagem (base para Aliado)
# Incluída para garantir que o arquivo q54.py seja autônomo.
class Personagem:
    """
    Representa um personagem básico no jogo.
    """
    def __init__(self, nome, vida=100):
        """
        Inicializa um novo personagem.
        :param nome: O nome do personagem.
        :param vida: A vida inicial do personagem.
        """
        self.nome = nome
        self.vida = vida
        print(f"Personagem '{self.nome}' foi CRIADO.")

    def dizer_nome(self):
        """
        Imprime o nome do personagem.
        """
        print(f"Meu nome é {self.nome}.")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Personagem é destruído.
        Ajuda a observar o ciclo de vida dos objetos.
        """
        print(f"Personagem '{self.nome}' foi DESTRUÍDO.")

# Classe Aliado (Q54: Associação com Jogador)
class Aliado(Personagem):
    """
    Representa um aliado que pode acompanhar um jogador.
    Demonstra a associação onde um Aliado 'tem' um Jogador para acompanhar.
    Na associação, o Aliado contém uma referência ao objeto Jogador, mas não é
    responsável pela sua criação ou destruição. O Jogador pode existir
    independentemente do Aliado.
    """
    def __init__(self, nome, vida=100):
        """
        Inicializa um novo aliado.
        :param nome: O nome do aliado.
        :param vida: A vida inicial do aliado.
        """
        super().__init__(nome, vida)
        self.acompanhando_jogador = None # Q54: Atributo para associar um objeto Jogador

    def acompanhar(self, jogador): # Q54: Método para estabelecer a associação
        """
        Define qual jogador o aliado está acompanhando.
        :param jogador: O objeto Jogador a ser acompanhado.
        """
        self.acompanhando_jogador = jogador
        print(f"{self.nome} agora está acompanhando {jogador.nome}.")

    def parar_acompanhar(self):
        """
        Faz o aliado parar de acompanhar o jogador, removendo a associação.
        """
        if self.acompanhando_jogador:
            print(f"{self.nome} parou de acompanhar {self.acompanhando_jogador.nome}.")
            self.acompanhando_jogador = None # Remove a referência ao jogador
        else:
            print(f"{self.nome} não está acompanhando ninguém.")

# Classe Jogador (base para associação)
class Jogador:
    """
    Representa um jogador no jogo.
    """
    def __init__(self, nome, vida=100):
        """
        Inicializa um novo jogador.
        :param nome: O nome do jogador.
        :param vida: A vida inicial do jogador.
        """
        self.nome = nome
        self.vida = vida # Atributo de vida para simulação
        print(f"Jogador '{self.nome}' foi CRIADO.")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Jogador é destruído.
        Ajuda a observar o ciclo de vida independente dos jogadores.
        """
        print(f"Jogador '{self.nome}' foi DESTRUÍDO.")

# --- Exemplo de Uso (Questão 54) ---
if __name__ == "__main__":
    print("--- Questão 54: Associação entre Aliado e Jogador ---")

    # 1. Criação de objetos Jogador e Aliado independentemente
    jogador_principal = Jogador("Herói Principal", vida=100)
    aliado_mago = Aliado("Mago Companheiro", vida=80)

    print(f"\nStatus inicial do aliado: {aliado_mago.nome} está acompanhando: {aliado_mago.acompanhando_jogador}")

    # 2. Aliado começa a acompanhar o jogador (estabelecendo a associação)
    print("\n--- Aliado começa a acompanhar o jogador ---")
    aliado_mago.acompanhar(jogador_principal)
    print(f"Status após acompanhar: {aliado_mago.nome} está acompanhando: {aliado_mago.acompanhando_jogador.nome}")

    # 3. Demonstração de que os objetos existem independentemente
    print("\n--- Demonstração de ciclo de vida independente ---")
    print(f"Vida do {jogador_principal.nome}: {jogador_principal.vida}")
    print(f"Vida do {aliado_mago.nome}: {aliado_mago.vida}")

    # Deletar o jogador
    print(f"\nDeletando o objeto '{jogador_principal.nome}'...")
    del jogador_principal # O objeto Jogador é destruído

    # Tentar acessar 'jogador_principal' agora resultaria em um NameError.
    # No entanto, o objeto 'aliado_mago' ainda existe.
    print(f"Aliado '{aliado_mago.nome}' ainda existe.")

    # A referência 'acompanhando_jogador' dentro de 'aliado_mago' agora aponta para um objeto que foi destruído.
    # Em Python, a referência se torna "dangling" (pendurada).
    # É uma boa prática limpar essa referência.
    print(f"Referência do aliado para o jogador: {aliado_mago.acompanhando_jogador}") # Pode ser None ou uma referência antiga

    print("\n--- Aliado para de acompanhar (limpando a referência) ---")
    aliado_mago.parar_acompanhar()
    print(f"Status após parar de acompanhar: {aliado_mago.nome} está acompanhando: {aliado_mago.acompanhando_jogador}")

    # Deletar o aliado
    print(f"\nDeletando o objeto '{aliado_mago.nome}'...")
    del aliado_mago

    print("\nTeste de q54.py concluído!")
