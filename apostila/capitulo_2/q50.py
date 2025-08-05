# Arquivo capitulo_2/q50.py
# Solução para a Questão 50: Composição entre Inventario e Itens.

# Classe Item (componente da composição)
class Item:
    """
    Representa um item que é um componente de um inventário.
    """
    def __init__(self, nome, descricao):
        """
        Inicializa um novo item.
        :param nome: O nome do item.
        :param descricao: Uma breve descrição do item.
        """
        self.nome = nome
        self.descricao = descricao
        print(f"Item '{self.nome}' foi CRIADO.")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Item é destruído.
        Demonstra que o Item é destruído junto com o Inventario que o compõe.
        """
        print(f"Item '{self.nome}' foi DESTRUÍDO.")

class Inventario:
    """
    Representa um inventário que COMPÕE uma lista de Itens.
    Isso significa que os Itens são partes integrais do Inventario e seus ciclos de vida
    estão diretamente ligados ao ciclo de vida do Inventario.
    """
    def __init__(self, capacidade=5):
        """
        Inicializa um novo inventário.
        :param capacidade: A capacidade máxima de itens que o inventário pode conter.
        """
        self.capacidade = capacidade
        self.itens = [] # Q50: Composição - Itens pertencem exclusivamente ao inventário
        print(f"Inventário (capacidade: {self.capacidade}) foi CRIADO.")

    def adicionar_item(self, nome_item, descricao_item):
        """
        Cria e adiciona um item ao inventário.
        O item é criado internamente pelo inventário, reforçando a composição.
        :param nome_item: O nome do item a ser criado e adicionado.
        :param descricao_item: A descrição do item a ser criado e adicionado.
        """
        if len(self.itens) < self.capacidade:
            novo_item = Item(nome_item, descricao_item) # Item criado DENTRO do inventário
            self.itens.append(novo_item)
            print(f"Item '{nome_item}' adicionado ao inventário.")
        else:
            print("Inventário cheio! Não foi possível adicionar o item.")

    def remover_item(self, item_nome):
        """
        Remove um item do inventário pelo nome.
        :param item_nome: O nome do item a ser removido.
        :return: O objeto Item removido, ou None se não encontrado.
        """
        item_encontrado = None
        for item in self.itens:
            if item.nome == item_nome:
                item_encontrado = item
                break
        if item_encontrado:
            self.itens.remove(item_encontrado)
            print(f"Item '{item_nome}' removido do inventário.")
            return item_encontrado
        else:
            print(f"Item '{item_nome}' não encontrado no inventário.")
            return None

    def listar_itens(self):
        """
        Lista todos os itens atualmente no inventário.
        """
        print("\n--- Itens no Inventário ---")
        if not self.itens:
            print("Inventário vazio.")
        else:
            for item in self.itens:
                print(f"- {item.nome} ({item.descricao})")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Inventario é destruído.
        Quando o Inventario é destruído, os Itens que ele compõe também são automaticamente destruídos,
        pois não há outras referências a eles fora do objeto Inventario.
        """
        print(f"Inventário foi DESTRUÍDO.")
        # Não é necessário chamar 'del item' explicitamente para cada item,
        # pois o coletor de lixo do Python cuidará disso quando as referências
        # na lista 'self.itens' forem removidas (quando o objeto Inventario for destruído).

# --- Exemplo de Uso (Questão 50) ---
if __name__ == "__main__":
    print("--- Questão 50: Composição entre Inventario e Itens ---")

    # Cria uma instância de Inventario. Isso não cria itens imediatamente.
    inventario_heroi = Inventario(capacidade=3)

    # Adiciona itens ao inventário. Os itens são criados AQUI, dentro do método adicionar_item.
    print("\n--- Adicionando itens ao inventário ---")
    inventario_heroi.adicionar_item("Poção de Vida", "Restaura 50 de vida.")
    inventario_heroi.adicionar_item("Espada Curta", "Uma espada básica.")
    inventario_heroi.adicionar_item("Escudo de Madeira", "Protege contra ataques.")
    inventario_heroi.adicionar_item("Elmo de Ferro", "Um capacete de proteção.") # Deve falhar, inventário cheio

    inventario_heroi.listar_itens()

    print("\n--- Removendo um item do inventário ---")
    item_removido = inventario_heroi.remover_item("Espada Curta")
    if item_removido:
        # Note que 'item_removido' agora tem uma referência ao objeto Item,
        # então ele não será destruído até que essa referência também seja removida.
        print(f"Item '{item_removido.nome}' foi removido do inventário e ainda existe (temporariamente).")
        del item_removido # Força a destruição do item removido para demonstração
    inventario_heroi.listar_itens()

    print("\n--- Deletando o inventário (os itens restantes também serão destruídos) ---")
    # Força a destruição do objeto 'inventario_heroi'.
    # Isso acionará o __del__ de Inventario, e consequentemente, o __del__ de cada Item restante composto.
    del inventario_heroi

    print("\nTeste de q50.py concluído!")
    # Após a execução, você verá as mensagens de criação e destruição,
    # demonstrando o ciclo de vida acoplado na composição.
