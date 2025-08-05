# Arquivo capitulo_2/q48.py
# Solução para a Questão 48: Composição entre Jogo e Menu.

# Classe Menu (componente da composição)
class Menu:
    """
    Representa um menu que é um componente do jogo.
    """
    def __init__(self, titulo="Menu Padrão"):
        """
        Inicializa um novo menu.
        :param titulo: O título do menu.
        """
        self.titulo = titulo
        print(f"Menu '{self.titulo}' foi CRIADO.")

    def mostrar_opcoes(self):
        """
        Imprime as opções básicas disponíveis no menu.
        """
        print(f"\n--- {self.titulo} ---")
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Menu é destruído.
        Demonstra que o Menu é destruído junto com o objeto Jogo que o compõe.
        """
        print(f"Menu '{self.titulo}' foi DESTRUÍDO.")

# Classe Jogo (compondo o Menu)
class Jogo:
    """
    Representa um jogo que COMPÕE um objeto Menu.
    Isso significa que o Menu é uma parte integral do Jogo e seu ciclo de vida
    está diretamente ligado ao ciclo de vida do Jogo.
    """
    def __init__(self, titulo="Meu Jogo"):
        """
        Inicializa um novo jogo.
        :param titulo: O título do jogo.
        """
        self.titulo = titulo
        # Q48: Composição - O objeto Menu é criado DENTRO do construtor de Jogo.
        # Isso significa que o Menu não pode existir sem o Jogo.
        self.menu = Menu(f"Menu de {self.titulo}")
        print(f"Jogo '{self.titulo}' foi CRIADO.")

    def iniciar(self):
        """
        Inicia o jogo e exibe as opções do menu.
        """
        print(f"O jogo '{self.titulo}' começou!")
        self.menu.mostrar_opcoes()

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Jogo é destruído.
        Quando o Jogo é destruído, o Menu que ele compõe também é automaticamente destruído,
        pois não há outras referências a ele fora do objeto Jogo.
        """
        print(f"Jogo '{self.titulo}' foi DESTRUÍDO.")
        # Não é necessário chamar 'del self.menu' explicitamente aqui,
        # pois o coletor de lixo do Python cuidará disso quando a referência 'self.menu'
        # for removida (quando o objeto Jogo for destruído).

# --- Exemplo de Uso (Questão 48) ---
if __name__ == "__main__":
    print("--- Questão 48: Composição entre Jogo e Menu ---")

    # Cria uma instância de Jogo. Isso automaticamente cria uma instância de Menu.
    meu_jogo = Jogo("Aventura Mágica")

    print("\nIniciando o jogo:")
    meu_jogo.iniciar()

    print("\nDeletando o jogo (observe que o menu também será destruído):")
    # Força a destruição do objeto 'meu_jogo'.
    # Isso acionará o __del__ de Jogo, e consequentemente, o __del__ de Menu.
    del meu_jogo

    print("\nTeste de q48.py concluído!")
    # Após a execução, você verá as mensagens de criação e destruição,
    # demonstrando o ciclo de vida acoplado na composição.
