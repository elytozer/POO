# Arquivo capitulo_2/q53.py
# Solução para a Questão 53: Agregação entre Loja e Itens.

# Classe Item (base para a agregação)
class Item:
    """
    Representa um item no jogo.
    Neste contexto de agregação, os objetos Item existem independentemente
    da Loja.
    """
    def __init__(self, nome, preco):
        """
        Inicializa um novo item.
        :param nome: O nome do item.
        :param preco: O preço do item.
        """
        self.nome = nome
        self.preco = preco
        print(f"Item '{self.nome}' (Preço: {self.preco}) foi CRIADO.")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Item é destruído.
        Isso nos ajuda a observar o ciclo de vida independente dos itens.
        """
        print(f"Item '{self.nome}' foi DESTRUÍDO.")

class Loja:
    """
    Representa uma loja que AGREGA uma lista de Itens para venda.
    Na agregação, a Loja contém referências aos objetos Item, mas não é
    responsável pela sua criação ou destruição. Os Itens podem existir
    antes e depois da Loja.
    """
    def __init__(self, nome):
        """
        Inicializa uma nova loja.
        :param nome: O nome da loja.
        """
        self.nome = nome
        self.estoque = [] # Q53: Agregação - Itens no estoque são agregados
        print(f"Loja '{self.nome}' foi CRIADA.")

    def adicionar_item_estoque(self, item): # Q53: Método para adicionar um item ao estoque
        """
        Adiciona um item ao estoque da loja.
        :param item: O objeto Item a ser adicionado.
        """
        self.estoque.append(item)
        print(f"Item '{item.nome}' adicionado ao estoque da loja '{self.nome}'.")

    def remover_item_estoque(self, item):
        """
        Remove um item do estoque da loja.
        :param item: O objeto Item a ser removido.
        """
        if item in self.estoque:
            self.estoque.remove(item)
            print(f"Item '{item.nome}' removido do estoque da loja '{self.nome}'.")
        else:
            print(f"Item '{item.nome}' não encontrado no estoque da loja '{self.nome}'.")

    def listar_itens(self): # Q53: Método para listar itens
        """
        Lista os itens disponíveis na loja.
        """
        print(f"\n--- Itens na Loja '{self.nome}' ---")
        if not self.estoque:
            print("Nenhum item no estoque.")
        else:
            for i, item in enumerate(self.estoque):
                print(f"{i+1}. {item.nome} - {item.preco} moedas")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Loja é destruído.
        Na agregação, os objetos Item NÃO são destruídos com a Loja,
        pois eles existem independentemente.
        """
        print(f"Loja '{self.nome}' foi DESTRUÍDA.")
        # Não é necessário limpar a lista self.estoque, pois os objetos Item
        # continuarão a existir se ainda houver outras referências a eles.

# --- Exemplo de Uso (Questão 53) ---
if __name__ == "__main__":
    print("--- Questão 53: Agregação entre Loja e Itens ---")

    # 1. Criação de objetos Item independentemente da Loja
    pocao_cura = Item("Poção de Cura", 50)
    espada_ferro = Item("Espada de Ferro", 150)
    armadura_couro = Item("Armadura de Couro", 100)

    # 2. Criação da Loja
    loja_do_ferreiro = Loja("Ferreiro Local")

    # 3. Adiciona itens ao estoque da loja (agregação)
    print("\n--- Adicionando itens ao estoque da loja ---")
    loja_do_ferreiro.adicionar_item_estoque(pocao_cura)
    loja_do_ferreiro.adicionar_item_estoque(espada_ferro)
    loja_do_ferreiro.listar_itens()

    # 4. Remove um item do estoque da loja
    print("\n--- Removendo a espada do estoque ---")
    loja_do_ferreiro.remover_item_estoque(espada_ferro)
    loja_do_ferreiro.listar_itens()

    # 5. Deleta a loja
    print("\n--- Deletando a loja (observe que os itens NÃO serão destruídos) ---")
    del loja_do_ferreiro

    # 6. Demonstra que os itens ainda existem após a loja ser deletada
    print("\n--- Verificando se os itens ainda existem ---")
    print(f"Item '{pocao_cura.nome}' ainda existe.")
    print(f"Item '{espada_ferro.nome}' ainda existe (mesmo após ser removido da loja).")
    print(f"Item '{armadura_couro.nome}' ainda existe (nunca esteve na loja).")

    # Para realmente deletar os itens, suas referências externas precisariam ser removidas.
    # Ex: del pocao_cura, del espada_ferro, del armadura_couro

    print("\nTeste de q53.py concluído!")
