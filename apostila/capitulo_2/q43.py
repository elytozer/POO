# Arquivo capitulo_2/q43.py
# Solução para a Questão 43: Classe Curador e Paladino (Herança Múltipla).

import random # Necessário para o ataque do Guerreiro (simulação)

# Classe Personagem (base para Aliado/Guerreiro, com setters de vida para cura)
# Incluída para garantir que o arquivo q43.py seja autônomo.
class Personagem:
    """
    Representa um personagem básico com nome, vida e defesa.
    Inclui getters e setters para atributos encapsulados, permitindo
    interações como cura e aumento de defesa por itens ou habilidades.
    """
    def __init__(self, nome, vida=100, defesa=50):
        """
        Inicializa um novo personagem.
        :param nome: O nome do personagem.
        :param vida: A vida inicial do personagem.
        :param defesa: A defesa inicial do personagem.
        """
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
        Setter para o atributo de vida, garantindo que não seja negativo
        e não exceda 100 (limite comum para personagens).
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
            print("Defesa deve ser entre 0 e 100. Definindo como 50.")
            self.__defesa = 50
        else:
            self.__defesa = valor
        if self.__defesa > 100: # Limite de defesa para equipamento
            self.__defesa = 100

    def tomar_dano(self, dano):
        """
        Reduz a vida do personagem pelo valor do dano, considerando a defesa.
        :param dano: A quantidade de dano a ser aplicada.
        """
        dano_real = max(0, dano - (self.defesa // 2)) # Reduz dano pela metade da defesa
        self.vida -= dano_real # Usa o setter de vida
        if self.vida <= 0:
            print(f"{self.nome} recebeu {dano_real} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano_real} de dano. Vida restante: {self.vida}.")

    def atacar(self, alvo):
        """
        Método de ataque padrão.
        :param alvo: O objeto a ser atacado.
        """
        dano = random.randint(10, 20)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
        alvo.tomar_dano(dano)

# Classe Aliado (base para Guerreiro)
class Aliado(Personagem):
    """
    Classe base para aliados, herda de Personagem.
    """
    def __init__(self, nome, vida=100, defesa=50):
        """
        Inicializa um novo aliado.
        :param nome: O nome do aliado.
        :param vida: A vida inicial do aliado.
        :param defesa: A defesa inicial do aliado.
        """
        super().__init__(nome, vida, defesa)

    def habilidade_especial(self):
        """
        Método abstrato para a habilidade especial do aliado.
        Deve ser implementado por todas as subclasses de Aliado.
        """
        raise NotImplementedError("Habilidade especial deve ser implementada pelas subclasses.")

# Classe Guerreiro (base para Paladino)
class Guerreiro(Aliado):
    """
    Representa um Guerreiro, herda de Aliado.
    """
    def __init__(self, nome="Guerreiro", vida=120, defesa=70):
        """
        Inicializa um novo Guerreiro.
        :param nome: O nome do guerreiro.
        :param vida: A vida inicial do guerreiro.
        :param defesa: A defesa inicial do guerreiro.
        """
        super().__init__(nome, vida, defesa)

    def habilidade_especial(self):
        """
        Guerreiro usa um golpe poderoso.
        """
        print(f"{self.nome} usou um golpe poderoso!")

# Classe Curador (Q43)
class Curador:
    """
    Classe para entidades que podem curar.
    """
    def curar(self, alvo, quantidade_cura=25):
        """
        Cura um alvo, restaurando sua vida.
        :param alvo: O objeto (Personagem ou Jogador) a ser curado.
        :param quantidade_cura: A quantidade de vida a ser restaurada.
        """
        print(f"{self.nome} curou {alvo.nome} em {quantidade_cura} pontos de vida!")
        # Assume que o alvo tem um atributo 'vida' com setter
        alvo.vida += quantidade_cura

# Classe Paladino (Q43: herda de Guerreiro e Curador)
class Paladino(Guerreiro, Curador):
    """
    Representa um Paladino que herda de Guerreiro e Curador.
    Pode atacar (como Guerreiro) e curar aliados (como Curador).
    """
    def __init__(self, nome="Sir Lancelot", vida=150, defesa=80):
        """
        Inicializa um novo Paladino.
        Chama o construtor da classe Guerreiro para inicializar atributos de guerreiro.
        :param nome: O nome do paladino.
        :param vida: A vida inicial do paladino.
        :param defesa: A defesa inicial do paladino.
        """
        # Chama o construtor da primeira classe pai na MRO (Method Resolution Order)
        Guerreiro.__init__(self, nome, vida, defesa)
        # A classe Curador não tem um construtor que precise ser chamado com super()
        # ou explicitamente neste exemplo.
        print(f"Paladino {self.nome} criado. Vida: {self.vida}, Defesa: {self.defesa}.")

    def habilidade_especial(self): # Sobrescrita da habilidade especial do Guerreiro
        """
        Paladino usa sua aura sagrada, curando a si mesmo.
        """
        print(f"{self.nome} usa sua aura sagrada!")
        self.curar(self, 20) # Cura a si mesmo em 20 pontos de vida

# --- Exemplo de Uso (Questão 43) ---
if __name__ == "__main__":
    print("--- Questão 43: Classe Curador e Paladino (Herança Múltipla) ---")

    # Cria uma instância de Paladino com vida reduzida para testar a cura
    paladino_sagrado = Paladino("Arthur", vida=80)
    print(f"Vida inicial do {paladino_sagrado.nome}: {paladino_sagrado.vida}")

    # Cria um inimigo para o Paladino atacar
    inimigo_teste = Personagem("Espectro", vida=50)
    print(f"Vida inicial do {inimigo_teste.nome}: {inimigo_teste.vida}")

    print("\n--- Paladino Ataca ---")
    paladino_sagrado.atacar(inimigo_teste) # Ataca como Guerreiro
    print(f"Vida do {inimigo_teste.nome} após ataque: {inimigo_teste.vida}")

    print(f"\n--- Paladino usa Habilidade Especial (Cura a si mesmo) ---")
    paladino_sagrado.habilidade_especial() # Usa habilidade especial (cura a si mesmo)
    print(f"Vida do {paladino_sagrado.nome} após habilidade: {paladino_sagrado.vida}")

    # Cria um aliado ferido para o Paladino curar
    aliado_ferido = Personagem("Mago Ferido", vida=30)
    print(f"\nVida do {aliado_ferido.nome} antes da cura: {aliado_ferido.vida}")

    print(f"--- {paladino_sagrado.nome} cura {aliado_ferido.nome} ---")
    paladino_sagrado.curar(aliado_ferido, 40) # Cura outro personagem como Curador
    print(f"Vida do {aliado_ferido.nome} após cura: {aliado_ferido.vida}")

    print("\nTeste de q43.py concluído!")
