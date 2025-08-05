# Arquivo capitulo_2/q33.py
# Solução para a Questão 33: Classe Item e subclasses (Pocao e Equipamento).

# Classe Personagem (necessária para testar Item.usar, com setters para vida e defesa)
class Personagem:
    """
    Representa um personagem simples para ser alvo de itens como poções e equipamentos.
    Possui atributos de vida e defesa com validação e limites.
    """
    def __init__(self, nome, vida=100, defesa=50):
        self.nome = nome
        self.__vida = vida
        self.__defesa = defesa

    @property
    def vida(self):
        """
        Getter para o atributo de vida.
        """
        return self.__vida

    @vida.setter
    def vida(self, valor):
        """
        Setter para o atributo de vida, garantindo que não seja negativo e não exceda 100.
        """
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor
        if self.__vida > 100: # Limite de vida para cura
            self.__vida = 100

    @property
    def defesa(self):
        """
        Getter para o atributo de defesa.
        """
        return self.__defesa

    @defesa.setter
    def defesa(self, valor):
        """
        Setter para o atributo de defesa, garantindo que o valor fique entre 0 e 100.
        """
        if not 0 <= valor <= 100:
            print("Defesa deve ser entre 0 e 100. Ajustando para 50.")
            self.__defesa = 50
        else:
            self.__defesa = valor
        if self.__defesa > 100: # Limite de defesa para equipamento
            self.__defesa = 100

    def mostrar_status(self):
        """
        Imprime o status atual do personagem (vida e defesa).
        """
        print(f"{self.nome}: Vida = {self.vida}, Defesa = {self.defesa}")

class Item:
    """
    Classe base para todos os itens do jogo.
    Define propriedades comuns a todos os itens.
    """
    def __init__(self, nome, descricao):
        """
        Inicializa um novo item.
        :param nome: O nome do item (ex: "Poção de Cura", "Espada").
        :param descricao: Uma breve descrição do item.
        """
        self.nome = nome
        self.descricao = descricao

    def usar(self, alvo):
        """
        Método para usar o item em um alvo.
        Este é um método abstrato que deve ser implementado por todas as subclasses de Item.
        Levanta um erro se não for sobrescrito.
        :param alvo: O objeto (ex: Personagem, Jogador) no qual o item será usado.
        """
        raise NotImplementedError("O método 'usar' deve ser implementado pelas subclasses.")

class Pocao(Item):
    """
    Representa uma poção, que herda da classe Item.
    Poções são itens consumíveis que geralmente restauram vida ou energia.
    """
    def __init__(self, nome="Poção de Cura", descricao="Restaura vida", valor_cura=30):
        """
        Inicializa uma poção, chamando o construtor da classe base (Item).
        :param nome: O nome da poção.
        :param descricao: A descrição da poção.
        :param valor_cura: A quantidade de vida que a poção restaura.
        """
        super().__init__(nome, descricao)
        self.valor_cura = valor_cura

    def usar(self, alvo):
        """
        Usa a poção para curar um alvo.
        :param alvo: O objeto Personagem ou Jogador a ser curado.
        """
        print(f"{alvo.nome} usou {self.nome} e recuperou {self.valor_cura} de vida.")
        alvo.vida += self.valor_cura # Assume que o alvo tem um atributo 'vida' com setter

class Equipamento(Item):
    """
    Representa um equipamento, que herda da classe Item.
    Equipamentos são itens que podem ser vestidos ou equipados para conceder bônus.
    """
    def __init__(self, nome="Armadura Leve", descricao="Aumenta defesa", bonus_defesa=10):
        """
        Inicializa um equipamento, chamando o construtor da classe base (Item).
        :param nome: O nome do equipamento.
        :param descricao: A descrição do equipamento.
        :param bonus_defesa: A quantidade de defesa que o equipamento concede.
        """
        super().__init__(nome, descricao)
        self.bonus_defesa = bonus_defesa

    def usar(self, alvo):
        """
        Equipa o item para aumentar a defesa do alvo.
        :param alvo: O objeto Personagem ou Jogador a ser equipado.
        """
        print(f"{alvo.nome} equipou {self.nome} e ganhou {self.bonus_defesa} de defesa.")
        alvo.defesa += self.bonus_defesa # Assume que o alvo tem um atributo 'defesa' com setter

# --- Exemplo de Uso (Questão 33) ---
if __name__ == "__main__":
    print("--- Questão 33: Classe Item e subclasses (Pocao e Equipamento) ---")

    # Cria uma instância de Personagem para testar os itens
    heroi_item = Personagem("Aventureiro Teste", vida=50, defesa=30)
    print("Status inicial do herói:")
    heroi_item.mostrar_status()

    # Cria instâncias de Poção e Equipamento
    pocao_pequena = Pocao("Poção Pequena de Cura", valor_cura=20)
    armadura_placa = Equipamento("Armadura de Placa", bonus_defesa=25)

    print("\n--- Usando Poção de Cura ---")
    pocao_pequena.usar(heroi_item)
    print("Status do herói após usar poção:")
    heroi_item.mostrar_status()

    print("\n--- Usando Equipamento (Armadura) ---")
    armadura_placa.usar(heroi_item)
    print("Status do herói após equipar armadura:")
    heroi_item.mostrar_status()

    # Testando os limites de vida e defesa
    print("\n--- Testando limites (vida e defesa) ---")
    heroi_item.vida = 90 # Define vida próxima do máximo
    heroi_item.defesa = 90 # Define defesa próxima do máximo
    print("Status do herói antes de testar limites:")
    heroi_item.mostrar_status()

    pocao_grande = Pocao("Poção Grande de Cura", valor_cura=50)
    armadura_lendaria = Equipamento("Armadura Lendária", bonus_defesa=30)

    print("\nUsando Poção Grande (deve limitar a vida a 100):")
    pocao_grande.usar(heroi_item)
    print("Status do herói após poção grande:")
    heroi_item.mostrar_status()

    print("\nUsando Armadura Lendária (deve limitar a defesa a 100):")
    armadura_lendaria.usar(heroi_item)
    print("Status do herói após armadura lendária:")
    heroi_item.mostrar_status()

    print("\nTeste de q33.py concluído!")
