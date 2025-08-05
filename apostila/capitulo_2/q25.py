# Arquivo capitulo_2\q25.py

class Menu:
    """
    Representa um menu com um construtor modificado para aceitar um título.
    """
    def __init__(self, titulo="Menu Padrão"): # Q25: Aceita um título como parâmetro
        self.titulo = titulo

    def iniciar_jogo(self):
        """
        Imprime uma mensagem indicando que o jogo está iniciando a partir deste menu.
        """
        print(f"Iniciando o jogo a partir do '{self.titulo}'...")

    def mostrar_opcoes(self):
        """
        Imprime as opções disponíveis no menu, exibindo o título.
        """
        print(f"\n--- {self.titulo} ---") # Q25: Exibe o título do menu
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")

    def sair(self):
        """
        Imprime uma mensagem de saída do jogo, mencionando o título do menu.
        """
        print(f"Saindo do '{self.titulo}'. Até a próxima!")

# --- Exemplo de Uso (Questão 25) ---
if __name__ == "__main__":
    print("--- Questão 25: Ajuste na classe Menu (Construtores) ---")

    # Criando um menu com um título específico
    menu_principal = Menu("Menu Principal do RPG Fantástico")
    menu_principal.mostrar_opcoes()
    menu_principal.iniciar_jogo()
    menu_principal.sair()

    print("\n" + "-" * 30 + "\n")

    # Criando outro menu com um título diferente
    menu_config = Menu("Menu de Configurações do Sistema")
    menu_config.mostrar_opcoes()

    print("\nTeste de q25.py concluído!")
