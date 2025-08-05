# Arquivo capitulo_2/q32.py
# Solução para a Questão 32: Classe Missao e subclasses (MissaoPrincipal e MissaoSecundaria).

class Missao:
    """
    Classe base para missões.
    Define a estrutura comum para todas as missões no jogo.
    """
    def __init__(self, nome, descricao, recompensa_base):
        """
        Inicializa uma nova missão.
        :param nome: O nome da missão.
        :param descricao: Uma breve descrição da missão.
        :param recompensa_base: A recompensa padrão ao completar a missão.
        """
        self.nome = nome
        self.descricao = descricao
        self.recompensa_base = recompensa_base

    def completar(self):
        """
        Marca a missão como completada e retorna a recompensa base.
        """
        print(f"Missão '{self.nome}' completada!")
        return self.recompensa_base

class MissaoPrincipal(Missao):
    """
    Representa uma missão principal, que herda da classe Missao.
    Missões principais oferecem uma recompensa base e um bônus de XP.
    """
    def __init__(self, nome, descricao, recompensa_base=100, xp_bonus=50):
        """
        Inicializa uma missão principal, chamando o construtor da classe base.
        :param nome: O nome da missão principal.
        :param descricao: Uma breve descrição da missão principal.
        :param recompensa_base: A recompensa padrão em moedas.
        :param xp_bonus: O bônus de pontos de experiência (XP) ao completar.
        """
        super().__init__(nome, descricao, recompensa_base)
        self.xp_bonus = xp_bonus

    def completar(self):
        """
        Sobrescreve o método 'completar' para incluir o bônus de XP.
        Retorna a soma da recompensa base com o bônus de XP.
        """
        recompensa = super().completar() # Chama o método 'completar' da classe pai
        print(f"Recompensa Principal: {recompensa} moedas e {self.xp_bonus} XP!")
        return recompensa + self.xp_bonus # A recompensa final inclui o XP como valor

class MissaoSecundaria(Missao):
    """
    Representa uma missão secundária, que herda da classe Missao.
    Missões secundárias oferecem uma recompensa base e um item adicional.
    """
    def __init__(self, nome, descricao, recompensa_base=30, item_recompensa="Poção de Cura"):
        """
        Inicializa uma missão secundária, chamando o construtor da classe base.
        :param nome: O nome da missão secundária.
        :param descricao: Uma breve descrição da missão secundária.
        :param recompensa_base: A recompensa padrão em moedas.
        :param item_recompensa: O nome de um item que é dado como recompensa adicional.
        """
        super().__init__(nome, descricao, recompensa_base)
        self.item_recompensa = item_recompensa

    def completar(self):
        """
        Sobrescreve o método 'completar' para mencionar o item de recompensa.
        Retorna apenas a recompensa base em moedas.
        """
        recompensa = super().completar() # Chama o método 'completar' da classe pai
        print(f"Recompensa Secundária: {recompensa} moedas e 1 {self.item_recompensa}!")
        return recompensa # Retorna apenas moedas, o item é um bônus "virtual" para este exemplo

# --- Exemplo de Uso (Questão 32) ---
if __name__ == "__main__":
    print("--- Questão 32: Classe Missao e subclasses (MissaoPrincipal e MissaoSecundaria) ---")

    # Cria uma instância de MissaoPrincipal
    missao_dragao = MissaoPrincipal(
        "Derrotar o Dragão",
        "Elimine o temível dragão que aterroriza a vila.",
        recompensa_base=200,
        xp_bonus=100
    )
    print(f"\nDetalhes da Missão Principal: {missao_dragao.nome} - {missao_dragao.descricao}")
    recompensa_dragao = missao_dragao.completar()
    print(f"Total de recompensa numérica obtida: {recompensa_dragao}")

    print("\n" + "-" * 40 + "\n")

    # Cria uma instância de MissaoSecundaria
    missao_coleta = MissaoSecundaria(
        "Coletar Ervas",
        "Colete 5 ervas medicinais raras na floresta escura.",
        recompensa_base=20,
        item_recompensa="Erva Rara de Cura"
    )
    print(f"Detalhes da Missão Secundária: {missao_coleta.nome} - {missao_coleta.descricao}")
    recompensa_coleta = missao_coleta.completar()
    print(f"Total de recompensa numérica obtida: {recompensa_coleta}")

    print("\nTeste de q32.py concluído!")
