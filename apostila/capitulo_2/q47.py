# Arquivo capitulo_2/q47.py
# Solução para a Questão 47: Associação entre Personagem e Missao.

# Classe Missao (simplificada para esta questão, baseada em Q32)
class Missao:
    """
    Representa uma missão no jogo.
    """
    def __init__(self, nome, descricao):
        """
        Inicializa uma nova missão.
        :param nome: O nome da missão.
        :param descricao: Uma breve descrição da missão.
        """
        self.nome = nome
        self.descricao = descricao

    def __str__(self):
        """
        Retorna uma representação em string da missão para fácil visualização.
        """
        return f"Missão: {self.nome} - {self.descricao}"

# Classe Personagem (Q47: Associação com Missao)
class Personagem:
    """
    Representa um personagem que pode aceitar múltiplas missões.
    Demonstra a associação onde um Personagem 'tem' várias Missões.
    """
    def __init__(self, nome):
        """
        Inicializa um novo personagem.
        :param nome: O nome do personagem.
        """
        self.nome = nome
        self.missoes = [] # Q47: Atributo para associar múltiplos objetos Missao

    def aceitar_missao(self, missao): # Q47: Método para estabelecer a associação
        """
        Adiciona uma missão à lista de missões que o personagem aceitou.
        :param missao: O objeto Missao a ser aceito.
        """
        self.missoes.append(missao)
        print(f"{self.nome} aceitou a missão: {missao.nome}")

    def listar_missoes(self):
        """
        Lista todas as missões que o personagem aceitou.
        """
        print(f"\n--- Missões de {self.nome} ---")
        if not self.missoes:
            print("Nenhuma missão aceita.")
        else:
            for i, missao in enumerate(self.missoes):
                print(f"{i+1}. {missao}") # Usa o método __str__ da Missao para imprimir

# --- Exemplo de Uso (Questão 47) ---
if __name__ == "__main__":
    print("--- Questão 47: Associação entre Personagem e Missao ---")

    # Cria um personagem
    heroi_missao = Personagem("Sir Galahad")

    # Cria várias instâncias de Missao
    missao1 = Missao("Resgatar Princesa", "Salvar a princesa do castelo do dragão.")
    missao2 = Missao("Coletar Itens Raros", "Encontrar 3 artefatos antigos na masmorra.")
    missao3 = Missao("Derrotar o Lich", "Eliminar o necromante que assola a região.")

    # Personagem aceita as missões
    heroi_missao.aceitar_missao(missao1)
    heroi_missao.aceitar_missao(missao2)
    heroi_missao.aceitar_missao(missao3)

    # Lista as missões do personagem
    heroi_missao.listar_missoes()

    # Demonstra que as missões existem independentemente do personagem
    print("\n--- Verificando se as missões ainda existem independentemente ---")
    print(f"A missão '{missao1.nome}' ainda pode ser acessada: {missao1.descricao}")

    # Se o personagem for deletado, as missões ainda existiriam.
    # Se uma missão for deletada, o personagem ainda existiria (mas sem aquela missão em sua lista).

    print("\nTeste de q47.py concluído!")
