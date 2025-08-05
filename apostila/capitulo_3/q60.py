#Arquivo capitulo_2/q60.py

class Item:
    """
    Representa um item no jogo com nome e preço.
    Usado como um objeto que a Loja irá gerenciar e cujos preços serão ajustados.
    """
    def __init__(self, nome, preco):
        """
        Inicializa um novo item.
        :param nome: O nome do item.
        :param preco: O preço atual do item.
        """
        self.nome = nome
        self.preco = preco
        print(f"Item '{self.nome}' criado com preço: {self.preco} moedas.")

    def __str__(self):
        """
        Retorna uma representação em string do item para fácil visualização.
        """
        return f"{self.nome} ({self.preco} moedas)"

class Loja:
    """
    Representa uma loja no jogo.
    Inclui um atributo de classe para um fator de inflação global e um método de classe
    para ajustar os preços dos itens em todas as lojas (Q60).
    """
    #Q60: Atributo de classe para o fator de inflação global.
    #Este atributo pertence à classe Loja e é compartilhado por todas as instâncias.
    fator_inflacao_global = 1.0 # Valor padrão (sem inflação)

    def __init__(self, nome):
        """
        Inicializa uma nova loja.
        :param nome: O nome da loja.
        """
        self.nome = nome
        self.estoque = [] #Lista para armazenar objetos Item
        print(f"Loja '{self.nome}' criada.")

    def adicionar_item(self, item):
        """
        Adiciona um item ao estoque da loja.
        :param item: O objeto Item a ser adicionado.
        """
        self.estoque.append(item)
        print(f"'{item.nome}' adicionado ao estoque da {self.nome}.")

    def listar_itens(self):
        """
        Lista os itens atualmente no estoque da loja, com seus preços.
        """
        print(f"\n--- Itens na Loja '{self.nome}' ---")
        if not self.estoque:
            print("Nenhum item no estoque.")
        else:
            for item in self.estoque:
                print(f"- {item}") #usa o método __str__ do Item

    @classmethod #Q60 Decorador que indica que este é um método de classe.
    #O primeiro parâmetro é 'cls' (convenção), que se refere à própria classe (Loja)
    def ajustar_preco_itens(cls, lojas, fator):
        """
        Altera o preço de todos os itens em todas as lojas fornecidas,
        com base em um fator global de ajuste
        Este método de classe acessa o atributo de classe 'fator_inflacao_global'
        e itera sobre uma lista de objetos Loja para modificar os preços de seus itens
        :param lojas: Uma lista de objetos Loja cujos itens terão os preços ajustados
        :param fator: O fator de ajuste
        """
        if fator <= 0:
            print("O fator de ajuste deve ser um valor positivo.")
            return

        cls.fator_inflacao_global = fator #Atualiza o fator de inflação global da classe
        print(f"\n--- Ajustando preços de itens com novo fator de inflação: {cls.fator_inflacao_global:.2f} ---")
        for loja in lojas:
            print(f"Ajustando itens na {loja.nome}:")
            for item in loja.estoque:
                preco_antigo = item.preco
                item.preco = int(item.preco * cls.fator_inflacao_global) #Ajusta o preço do item
                print(f"  - {item.nome}: {preco_antigo} -> {item.preco}")

#Exemplo de Uso
if __name__ == "__main__":
    print("--- Questão 60: Ajuste de Preços de Itens (Método de Classe) ---")

    #Criação de algumas lojas
    loja_ferreiro = Loja("Ferreiro da Vila")
    loja_mercado = Loja("Mercado Central")

    #Criação de alguns itens
    pocao = Item("Poção de Cura", 50)
    espada = Item("Espada de Ferro", 100)
    escudo = Item("Escudo de Madeira", 70)
    anel = Item("Anel de Ouro", 120)

    #Adiciona itens as lojas
    print("\n--- Adicionando itens às lojas ---")
    loja_ferreiro.adicionar_item(pocao)
    loja_ferreiro.adicionar_item(espada)
    loja_mercado.adicionar_item(escudo)
    loja_mercado.adicionar_item(anel)

    #Lista os itens nas lojas antes do ajuste
    print("\n--- Preços Iniciais dos Itens ---")
    loja_ferreiro.listar_itens()
    loja_mercado.listar_itens()

    #Ajusta os preços de todos os itens em  todas as lojas
    #lista de todas as lojas que queremos afetar.
    todas_as_lojas = [loja_ferreiro, loja_mercado]
    Loja.ajustar_preco_itens(todas_as_lojas, 1.2) # Aumento de 20% (fator 1.2)

    #Lista os itens nas lojas após o ajuste para verificar as mudanças
    print("\n--- Preços dos Itens Após Ajuste (20% de Aumento) ---")
    loja_ferreiro.listar_itens()
    loja_mercado.listar_itens()

    #Tenta ajustar com fator inválido
    print("\n--- Tentando ajustar preços com fator inválido (0.0) ---")
    Loja.ajustar_preco_itens(todas_as_lojas, 0.0)
    print(f"Fator de inflação global atual: {Loja.fator_inflacao_global:.2f}")


    print("\nTeste de q60.py concluído!")
