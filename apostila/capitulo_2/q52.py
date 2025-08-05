# Arquivo capitulo_2/q52.py
# Solução para a Questão 52: Agregação entre Mapa e Fases.

# Classe Fase (base para a agregação)
class Fase:
    """
    Representa uma fase do jogo.
    Neste contexto de agregação, os objetos Fase existem independentemente
    do Mapa.
    """
    def __init__(self, nome, descricao):
        """
        Inicializa uma nova fase.
        :param nome: O nome da fase.
        :param descricao: Uma breve descrição da fase.
        """
        self.nome = nome
        self.descricao = descricao
        print(f"Fase '{self.nome}' foi CRIADA.")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Fase é destruído.
        Isso nos ajuda a observar o ciclo de vida independente das fases.
        """
        print(f"Fase '{self.nome}' foi DESTRUÍDA.")

class Mapa:
    """
    Representa um mapa que AGREGA várias Fases.
    Na agregação, o Mapa contém referências aos objetos Fase, mas não é
    responsável pela sua criação ou destruição. As Fases podem existir
    antes e depois do Mapa.
    """
    def __init__(self, nome):
        """
        Inicializa um novo mapa.
        :param nome: O nome do mapa.
        """
        self.nome = nome
        self.fases = [] # Q52: Agregação - Fases são agregadas
        print(f"Mapa '{self.nome}' foi CRIADO.")

    def adicionar_fase(self, fase): # Q52: Método para adicionar uma fase
        """
        Adiciona uma fase ao mapa.
        :param fase: O objeto Fase a ser adicionado.
        """
        self.fases.append(fase)
        print(f"Fase '{fase.nome}' adicionada ao mapa '{self.nome}'.")

    def remover_fase(self, fase): # Q52: Método para remover uma fase
        """
        Remove uma fase do mapa.
        :param fase: O objeto Fase a ser removido.
        """
        if fase in self.fases:
            self.fases.remove(fase)
            print(f"Fase '{fase.nome}' removida do mapa '{self.nome}'.")
        else:
            print(f"Fase '{fase.nome}' não encontrada no mapa '{self.nome}'.")

    def listar_fases(self):
        """
        Lista todas as fases atualmente no mapa.
        """
        print(f"\n--- Fases no Mapa '{self.nome}' ---")
        if not self.fases:
            print("Nenhuma fase no mapa.")
        else:
            for fase in self.fases:
                print(f"- {fase.nome} ({fase.descricao})")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Mapa é destruído.
        Na agregação, os objetos Fase NÃO são destruídos com o Mapa,
        pois eles existem independentemente.
        """
        print(f"Mapa '{self.nome}' foi DESTRUÍDO.")
        # Não é necessário limpar a lista self.fases, pois os objetos Fase
        # continuarão a existir se ainda houver outras referências a eles.

# --- Exemplo de Uso (Questão 52) ---
if __name__ == "__main__":
    print("--- Questão 52: Agregação entre Mapa e Fases ---")

    # 1. Criação de objetos Fase independentemente do Mapa
    fase_floresta = Fase("Floresta Verde", "Uma área cheia de árvores e animais.")
    fase_montanha = Fase("Pico Nevado", "Uma montanha alta e perigosa.")
    fase_vila = Fase("Vila Pacífica", "Um pequeno assentamento humano.")

    # 2. Criação do Mapa
    mapa_mundi = Mapa("Terra de Aethel")

    # 3. Adiciona fases ao mapa (agregação)
    print("\n--- Adicionando fases ao mapa ---")
    mapa_mundi.adicionar_fase(fase_floresta)
    mapa_mundi.adicionar_fase(fase_montanha)
    mapa_mundi.listar_fases()

    # 4. Remove uma fase do mapa
    print("\n--- Removendo a Fase Floresta do mapa ---")
    mapa_mundi.remover_fase(fase_floresta)
    mapa_mundi.listar_fases()

    # 5. Deleta o mapa
    print("\n--- Deletando o mapa (observe que as fases NÃO serão destruídas) ---")
    del mapa_mundi

    # 6. Demonstra que as fases ainda existem após o mapa ser deletado
    print("\n--- Verificando se as fases ainda existem ---")
    print(f"Fase '{fase_floresta.nome}' ainda existe.")
    print(f"Fase '{fase_montanha.nome}' ainda existe (mesmo após ser removida do mapa).")
    print(f"Fase '{fase_vila.nome}' ainda existe (nunca esteve no mapa).")

    # Para realmente deletar as fases, suas referências externas precisariam ser removidas.
    # Ex: del fase_floresta, del fase_montanha, del fase_vila

    print("\nTeste de q52.py concluído!")
