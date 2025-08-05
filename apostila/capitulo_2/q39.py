# Arquivo capitulo_2/q39.py
# Solução para a Questão 39: Modifique a classe JogoMultiplayer (Reescrita e Polimorfismo).

# Classe Jogo (base para herança da classe JogoMultiplayer)
# Inclui um construtor básico e um método 'iniciar'.
class Jogo:
    """
    Representa um jogo básico com um título e um método para iniciar.
    """
    def __init__(self, titulo="Meu Jogo", dificuldade=1):
        """
        Inicializa um novo jogo.
        :param titulo: O título do jogo.
        :param dificuldade: O nível de dificuldade (simplificado para esta questão).
        """
        self.titulo = titulo
        self._dificuldade = dificuldade # Atributo de dificuldade simplificado para esta questão

    def iniciar(self):
        """
        Imprime uma mensagem indicando que o jogo começou.
        Este é o método original que será sobrescrito.
        """
        print(f"O jogo '{self.titulo}' começou!")

# Classe Jogador (necessária para a classe JogoMultiplayer, para adicionar jogadores)
# Uma classe simples para representar um jogador.
class Jogador:
    """
    Representa um jogador simples com um nome.
    """
    def __init__(self, nome):
        """
        Inicializa um novo jogador.
        :param nome: O nome do jogador.
        """
        self.nome = nome

# Classe JogoMultiplayer (Q29, Q39: herda de Jogo, sobrescreve iniciar())
class JogoMultiplayer(Jogo):
    """
    Representa um jogo multiplayer que herda de Jogo.
    Permite adicionar múltiplos jogadores e tem uma lógica de início adaptada
    para um ambiente multiplayer.
    """
    def __init__(self, titulo="Jogo Multiplayer", dificuldade=2):
        """
        Inicializa um novo jogo multiplayer, chamando o construtor da classe base.
        :param titulo: O título do jogo multiplayer.
        :param dificuldade: O nível de dificuldade do jogo.
        """
        super().__init__(titulo, dificuldade) # Chama o construtor da classe base (Jogo)
        self.jogadores_conectados = [] # Lista para armazenar os objetos Jogador
        print(f"Jogo Multiplayer '{self.titulo}' criado.")

    def adicionar_jogador(self, jogador): # Q29: Método para adicionar jogadores
        """
        Adiciona um jogador à lista de jogadores conectados ao jogo multiplayer.
        :param jogador: O objeto Jogador a ser adicionado.
        """
        self.jogadores_conectados.append(jogador)
        print(f"{jogador.nome} conectado ao jogo multiplayer.")

    def iniciar(self): # Q39: Sobrescrita do método iniciar() para lógica multiplayer
        """
        Inicia o jogo multiplayer. Exibe uma mensagem diferente e lista os jogadores conectados.
        Demonstra o polimorfismo ao substituir o comportamento do método 'iniciar' da classe base.
        """
        print(f"Iniciando o jogo multiplayer '{self.titulo}'! Preparando para a batalha online...")
        if not self.jogadores_conectados:
            print("Aguardando jogadores... Ninguém conectado ainda.")
        else:
            print("Jogadores conectados:")
            for jogador in self.jogadores_conectados:
                print(f"- {jogador.nome}")
            print("Que a diversão comece!")

# --- Exemplo de Uso (Questão 39) ---
if __name__ == "__main__":
    print("--- Questão 39: Modifique a classe JogoMultiplayer (Reescrita e Polimorfismo) ---")

    # Exemplo de uso da classe base Jogo
    jogo_single = Jogo("Aventura Solo")
    print("\n--- Teste de Jogo Simples ---")
    jogo_single.iniciar() # Chama o método 'iniciar' da classe Jogo

    print("\n" + "=" * 40 + "\n")

    # Exemplo de uso da classe JogoMultiplayer
    jogo_multi = JogoMultiplayer("Confronto Global")

    # Cria alguns jogadores
    jogador_1 = Jogador("GuerreiroX")
    jogador_2 = Jogador("MagaY")
    jogador_3 = Jogador("CurandeiroZ")

    # Adiciona jogadores ao jogo multiplayer
    jogo_multi.adicionar_jogador(jogador_1)
    jogo_multi.adicionar_jogador(jogador_2)
    jogo_multi.adicionar_jogador(jogador_3)

    # Inicia o jogo multiplayer (chama o método 'iniciar' sobrescrito da classe JogoMultiplayer)
    print("\n--- Iniciando Jogo Multiplayer com jogadores ---")
    jogo_multi.iniciar()

    print("\n" + "=" * 40 + "\n")

    # Exemplo de JogoMultiplayer sem jogadores conectados
    jogo_multi_vazio = JogoMultiplayer("Partida Rápida")
    print("\n--- Iniciando Jogo Multiplayer sem jogadores ---")
    jogo_multi_vazio.iniciar() # A mensagem será diferente, indicando que não há jogadores

    print("\nTeste de q39.py concluído!")
