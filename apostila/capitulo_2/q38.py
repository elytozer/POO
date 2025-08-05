# Arquivo capitulo_2/q38.py
# Solução para a Questão 38: Modifique a classe JogadorPremium (Reescrita e Polimorfismo).

# Classe Pontuacao (base para a classe Jogador)
# Inclui encapsulamento para 'pontos' e um setter que impede valores negativos.
class Pontuacao:
    """
    Representa a pontuação do jogo com métodos para gerenciar pontos.
    """
    def __init__(self, pontos=0):
        """
        Inicializa um objeto Pontuacao com um valor inicial de pontos.
        :param pontos: O valor inicial da pontuação.
        """
        self.__pontos = pontos # Atributo privado para pontos

    @property # Getter para 'pontos'
    def pontos(self):
        """
        Retorna a pontuação atual.
        """
        return self.__pontos

    @pontos.setter # Setter para 'pontos', impede valores negativos (da Q19)
    def pontos(self, valor):
        """
        Define a pontuação, garantindo que não seja negativa.
        Se um valor negativo for fornecido, a pontuação é definida como 0.
        """
        if valor < 0:
            print("Pontuação não pode ser negativa. Definindo para 0.")
            self.__pontos = 0
        else:
            self.__pontos = valor

    def adicionar_pontos(self, quantidade):
        """
        Adiciona uma quantidade específica de pontos à pontuação total.
        Este método usa o setter 'pontos' para garantir a validação.
        :param quantidade: A quantidade de pontos a ser adicionada.
        """
        self.pontos += quantidade # Usa o setter 'pontos'
        print(f"Adicionados {quantidade} pontos. Pontuação atual: {self.pontos}")

# Classe Jogador (base para herança da classe JogadorPremium)
# Inclui um método básico para adicionar pontos que será sobrescrito.
class Jogador:
    """
    Representa um jogador básico no jogo com nome e pontuação.
    """
    def __init__(self, nome, pontos=0):
        """
        Inicializa um novo jogador.
        :param nome: O nome do jogador.
        :param pontos: A pontuação inicial do jogador.
        """
        self.nome = nome
        self.pontuacao = Pontuacao(pontos) # Usa a classe Pontuacao para gerenciar pontos

    def adicionar_pontos(self, quantidade): # Método a ser sobrescrito pela subclasse
        """
        Adiciona pontos à pontuação do jogador.
        Este método delega a adição de pontos ao objeto Pontuacao.
        :param quantidade: A quantidade de pontos a ser adicionada.
        """
        self.pontuacao.adicionar_pontos(quantidade)

# Classe JogadorPremium (Q28, Q38: herda de Jogador, sobrescreve adicionar_pontos())
class JogadorPremium(Jogador):
    """
    Representa um jogador premium que herda de Jogador.
    Recebe um bônus de pontuação ao adicionar pontos, através da sobrescrita do método.
    """
    def __init__(self, nome, pontos=0, bonus_multiplicador=1.5):
        """
        Inicializa um novo jogador premium.
        :param nome: O nome do jogador premium.
        :param pontos: A pontuação inicial do jogador premium.
        :param bonus_multiplicador: O multiplicador de pontos para este jogador premium.
        """
        super().__init__(nome, pontos) # Chama o construtor da classe base (Jogador)
        self.bonus_multiplicador = bonus_multiplicador
        print(f"Jogador Premium {self.nome} criado com multiplicador de bônus: {self.bonus_multiplicador}x")

    def adicionar_pontos(self, quantidade): # Q38: Sobrescrita do método 'adicionar_pontos()'
        """
        Adiciona pontos à pontuação do jogador premium, aplicando um multiplicador.
        :param quantidade: A quantidade base de pontos a ser adicionada.
        """
        pontos_com_bonus = int(quantidade * self.bonus_multiplicador)
        self.pontuacao.adicionar_pontos(pontos_com_bonus) # Usa o método do objeto Pontuacao
        print(f"Bônus Premium! {quantidade} pontos base se tornaram {pontos_com_bonus} pontos.")

# --- Exemplo de Uso (Questão 38) ---
if __name__ == "__main__":
    print("--- Questão 38: Modifique a classe JogadorPremium (Reescrita e Polimorfismo) ---")

    # Cria uma instância de jogador normal
    jogador_normal = Jogador("Lucas")
    print(f"\nPontuação inicial de {jogador_normal.nome}: {jogador_normal.pontuacao.pontos}")

    # Adiciona pontos ao jogador normal (sem bônus)
    print("\nAdicionando 50 pontos ao jogador normal:")
    jogador_normal.adicionar_pontos(50)
    print(f"Pontuação final de {jogador_normal.nome}: {jogador_normal.pontuacao.pontos}")

    print("\n" + "=" * 40 + "\n")

    # Cria uma instância de jogador premium com um multiplicador de 2.5
    jogador_vip = JogadorPremium("Sofia", bonus_multiplicador=2.5)
    print(f"\nPontuação inicial de {jogador_vip.nome}: {jogador_vip.pontuacao.pontos}")

    # Adiciona pontos ao jogador premium (com bônus)
    print("\nAdicionando 50 pontos ao jogador premium:")
    jogador_vip.adicionar_pontos(50) # 50 * 2.5 = 125 pontos serão adicionados
    print(f"Pontuação final de {jogador_vip.nome}: {jogador_vip.pontuacao.pontos}")

    print("\nTeste de q38.py concluído!")
