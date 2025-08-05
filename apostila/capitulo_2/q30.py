# Arquivo capitulo_2\q30.py

# Classe Menu (base para herança da classe MenuAvancado)
# Inclui um construtor que aceita um título e métodos para exibir opções.
class Menu:
    """
    Representa um menu básico com um título e métodos para interagir com o jogo.
    """
    def __init__(self, titulo="Menu Padrão"): # Constructor from Q25
        self.titulo = titulo

    def iniciar_jogo(self):
        """
        Imprime uma mensagem indicando que o jogo está iniciando a partir deste menu.
        """
        print(f"Iniciando o jogo a partir do '{self.titulo}'...")

    def mostrar_opcoes(self):
        """
        Imprime as opções básicas disponíveis no menu, exibindo o título.
        """
        print(f"\n--- {self.titulo} ---")
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")

    def sair(self):
        """
        Imprime uma mensagem de saída do jogo, mencionando o título do menu.
        """
        print(f"Saindo do '{self.titulo}'. Até a próxima!")

    def exibir(self): # Method to be overridden by subclasses (from Q40 requirement)
        """
        Exibe as opções do menu. This method is designed for polymorphism.
        """
        self.mostrar_opcoes()

# Classe MenuAvancado (Q30: herda de Menu, permite salvar configurações)
# Sobrescreve o método exibir() para a Questão 40.
class MenuAvancado(Menu):
    """
    Representa um menu avançado que herda de Menu.
    Permite salvar configurações personalizadas e exibe opções adicionais.
    """
    def __init__(self, titulo="Menu Avançado"):
        # Call the constructor of the base class (Menu)
        super().__init__(titulo)
        self.configuracoes_personalizadas = {} # Dictionary to store custom settings
        print(f"Menu Avançado '{self.titulo}' criado.")

    def salvar_configuracoes(self, chave, valor): # Q30: Method to save custom settings
        """
        Saves a personalized configuration.
        :param chave: The key for the configuration (e.g., "volume_musica").
        :param valor: The value of the configuration (e.g., 80).
        """
        self.configuracoes_personalizadas[chave] = valor
        print(f"Configuração '{chave}' salva como '{valor}'.")

    def exibir(self): # Q40: Overrides the 'exibir' method to show additional options
        """
        Exibe as opções do menu, including additional advanced options.
        It calls the base class's 'exibir' method first.
        """
        super().exibir() # Calls the 'exibir' method from the parent class (Menu)
        print("4. Salvar Configurações")
        print("5. Carregar Jogo")
        print("--- Opções Avançadas ---")

# --- Exemplo de Uso (Questão 30 e 40) ---
if __name__ == "__main__":
    print("--- Questão 30: Classe MenuAvancado (Herança) ---")
    print("--- E Questão 40: Modifique a classe MenuAvancado (Reescrita e Polimorfismo) ---")

    # Example of using the base Menu class
    menu_simples = Menu("Menu Básico do Jogo")
    print("\n--- Exibindo Menu Simples ---")
    menu_simples.exibir() # Calls the base class's exibir method

    print("\n" + "=" * 40 + "\n")

    # Example of using the MenuAvancado class
    menu_avancado = MenuAvancado("Menu de Sistema do Jogo")
    print("\n--- Exibindo Menu Avançado ---")
    menu_avancado.exibir() # Calls the overridden exibir method with additional options

    # Demonstrate saving custom settings (Q30)
    print("\n--- Salvando Configurações Personalizadas ---")
    menu_avancado.salvar_configuracoes("volume_musica", 80)
    menu_avancado.salvar_configuracoes("sensibilidade_mouse", 0.75)
    menu_avancado.salvar_configuracoes("resolucao", "1920x1080")

    print("\nConfigurações salvas no Menu Avançado:")
    for chave, valor in menu_avancado.configuracoes_personalizadas.items():
        print(f"- {chave}: {valor}")

    print("\nTeste de q30.py e q40.py concluído!")
