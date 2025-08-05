# Arquivo capitulo_2/q40.py
# Solução para a Questão 40: Modifique a classe MenuAvancado (Reescrita e Polimorfismo).

# Classe Menu (base para herança da classe MenuAvancado)
# Inclui um construtor que aceita um título e métodos para exibir opções.
class Menu:
    """
    Representa um menu básico com um título e métodos para interagir com o jogo.
    """
    def __init__(self, titulo="Menu Padrão"):
        """
        Inicializa um novo menu.
        :param titulo: O título do menu.
        """
        self.titulo = titulo

    def mostrar_opcoes(self):
        """
        Imprime as opções básicas disponíveis no menu, exibindo o título.
        """
        print(f"\n--- {self.titulo} ---")
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")

    def exibir(self): # Método a ser sobrescrito
        """
        Exibe as opções do menu. Este método é projetado para polimorfismo.
        """
        self.mostrar_opcoes()

# Classe MenuAvancado (Q30, Q40: herda de Menu, sobrescreve exibir())
class MenuAvancado(Menu):
    """
    Representa um menu avançado que herda de Menu.
    Permite salvar configurações personalizadas (Q30) e exibe opções adicionais (Q40).
    """
    def __init__(self, titulo="Menu Avançado"):
        """
        Inicializa um novo menu avançado, chamando o construtor da classe base.
        :param titulo: O título do menu avançado.
        """
        super().__init__(titulo)
        self.configuracoes_personalizadas = {} # Dicionário para armazenar configurações personalizadas

    def salvar_configuracoes(self, chave, valor): # Método da Q30
        """
        Salva uma configuração personalizada.
        :param chave: A chave para a configuração (ex: "volume_musica").
        :param valor: O valor da configuração (ex: 80).
        """
        self.configuracoes_personalizadas[chave] = valor
        print(f"Configuração '{chave}' salva como '{valor}'.")

    def exibir(self): # Q40: Sobrescrita do método 'exibir()'
        """
        Exibe as opções do menu, incluindo opções adicionais.
        Demonstra o polimorfismo ao estender o comportamento do método 'exibir' da classe base.
        """
        super().exibir() # Chama o método 'exibir' da classe pai (Menu)
        print("4. Salvar Configurações")
        print("5. Carregar Jogo")
        print("--- Opções Avançadas ---")

# --- Exemplo de Uso (Questão 40) ---
if __name__ == "__main__":
    print("--- Questão 40: Modifique a classe MenuAvancado (Reescrita e Polimorfismo) ---")

    # Exemplo de uso da classe base Menu
    menu_simples = Menu("Menu Básico do Jogo")
    print("\n--- Exibindo Menu Simples ---")
    menu_simples.exibir() # Chama o método 'exibir' da classe Menu

    print("\n" + "=" * 40 + "\n")

    # Exemplo de uso da classe MenuAvancado
    menu_avancado = MenuAvancado("Menu de Sistema do Jogo")
    print("\n--- Exibindo Menu Avançado ---")
    menu_avancado.exibir() # Chama o método 'exibir' sobrescrito da classe MenuAvancado

    # Demonstração do método 'salvar_configuracoes' (da Q30)
    print("\n--- Salvando Configurações Personalizadas ---")
    menu_avancado.salvar_configuracoes("volume_musica", 80)
    menu_avancado.salvar_configuracoes("sensibilidade_mouse", 0.75)
    menu_avancado.salvar_configuracoes("resolucao", "1920x1080")

    print("\nConfigurações salvas no Menu Avançado:")
    for chave, valor in menu_avancado.configuracoes_personalizadas.items():
        print(f"- {chave}: {valor}")

    print("\nTeste de q40.py concluído!")
