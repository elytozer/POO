# Arquivo capitulo_2/q51.py
# Solução para a Questão 51: Agregação entre Guilda e Jogadores.

# Classe Jogador (base para a agregação)
class Jogador:
    """
    Representa um jogador no jogo.
    Neste contexto de agregação, os objetos Jogador existem independentemente
    da Guilda.
    """
    def __init__(self, nome):
        """
        Inicializa um novo jogador.
        :param nome: O nome do jogador.
        """
        self.nome = nome
        print(f"Jogador '{self.nome}' foi CRIADO.")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Jogador é destruído.
        Isso nos ajuda a observar o ciclo de vida independente dos jogadores.
        """
        print(f"Jogador '{self.nome}' foi DESTRUÍDO.")

class Guilda:
    """
    Representa uma guilda que AGREGA vários Jogadores.
    Na agregação, a Guilda contém referências aos objetos Jogador, mas não é
    responsável pela sua criação ou destruição. Os Jogadores podem existir
    antes e depois da Guilda.
    """
    def __init__(self, nome):
        """
        Inicializa uma nova guilda.
        :param nome: O nome da guilda.
        """
        self.nome = nome
        self.membros = [] # Q51: Agregação - Membros (Jogadores) são agregados
        print(f"Guilda '{self.nome}' foi CRIADA.")

    def adicionar_membro(self, jogador): # Q51: Método para adicionar um membro
        """
        Adiciona um jogador como membro da guilda.
        :param jogador: O objeto Jogador a ser adicionado.
        """
        if jogador not in self.membros:
            self.membros.append(jogador)
            print(f"{jogador.nome} se juntou à guilda '{self.nome}'.")
        else:
            print(f"{jogador.nome} já é membro da guilda '{self.nome}'.")

    def remover_membro(self, jogador): # Q51: Método para remover um membro
        """
        Remove um jogador da guilda.
        :param jogador: O objeto Jogador a ser removido.
        """
        if jogador in self.membros:
            self.membros.remove(jogador)
            print(f"{jogador.nome} saiu da guilda '{self.nome}'.")
        else:
            print(f"{jogador.nome} não é membro da guilda '{self.nome}'.")

    def listar_membros(self):
        """
        Lista todos os membros atualmente na guilda.
        """
        print(f"\n--- Membros da Guilda '{self.nome}' ---")
        if not self.membros:
            print("Nenhum membro na guilda.")
        else:
            for membro in self.membros:
                print(f"- {membro.nome}")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Guilda é destruído.
        Na agregação, os objetos Jogador NÃO são destruídos com a Guilda,
        pois eles existem independentemente.
        """
        print(f"Guilda '{self.nome}' foi DESTRUÍDA.")
        # Não é necessário limpar a lista self.membros, pois os objetos Jogador
        # continuarão a existir se ainda houver outras referências a eles.

# --- Exemplo de Uso (Questão 51) ---
if __name__ == "__main__":
    print("--- Questão 51: Agregação entre Guilda e Jogadores ---")

    # 1. Criação de objetos Jogador independentemente da Guilda
    jogador_a = Jogador("Alice")
    jogador_b = Jogador("Bruno")
    jogador_c = Jogador("Carlos")

    # 2. Criação da Guilda
    guilda_dos_herois = Guilda("Heróis da Luz")

    # 3. Adiciona jogadores à guilda (agregação)
    print("\n--- Adicionando membros à guilda ---")
    guilda_dos_herois.adicionar_membro(jogador_a)
    guilda_dos_herois.adicionar_membro(jogador_b)
    guilda_dos_herois.listar_membros()

    # 4. Remove um jogador da guilda
    print("\n--- Removendo Bruno da guilda ---")
    guilda_dos_herois.remover_membro(jogador_b)
    guilda_dos_herois.listar_membros()

    # 5. Deleta a guilda
    print("\n--- Deletando a guilda (observe que os jogadores NÃO serão destruídos) ---")
    del guilda_dos_herois

    # 6. Demonstra que os jogadores ainda existem após a guilda ser deletada
    print("\n--- Verificando se os jogadores ainda existem ---")
    print(f"Jogador '{jogador_a.nome}' ainda existe.")
    print(f"Jogador '{jogador_b.nome}' ainda existe (mesmo após ser removido da guilda).")
    print(f"Jogador '{jogador_c.nome}' ainda existe (nunca esteve na guilda).")

    # Para realmente deletar os jogadores, suas referências externas precisariam ser removidas.
    # Ex: del jogador_a, del jogador_b, del jogador_c

    print("\nTeste de q51.py concluído!")
