# Arquivo capitulo_2/q34.py
# Solução para a Questão 34: Classe Fase e subclasses (FaseFloresta e FaseDeserto).
# Inclui a sobrescrita do método gerar_inimigos() para a Questão 41.

import random # Necessário para gerar inimigos aleatórios

# Classe Inimigo (necessária para Fase.gerar_inimigos)
# Uma classe simples para representar inimigos que podem ser gerados nas fases.
class Inimigo:
    """
    Representa um inimigo simples com nome, vida e força.
    """
    def __init__(self, nome, vida=100, forca=15):
        """
        Inicializa um novo inimigo.
        :param nome: The name of the enemy.
        :param vida: The initial health of the enemy.
        :param forca: The strength of the enemy.
        """
        self.nome = nome
        self.vida = vida
        self.forca = forca # Simplified for this question

    def tomar_dano(self, dano):
        """
        Reduz a vida do inimigo pelo valor do dano.
        :param dano: The amount of damage to apply.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

class Fase:
    """
    Classe base para fases do jogo.
    Define a estrutura comum e o comportamento básico para todas as fases.
    """
    def __init__(self, nome, descricao):
        """
        Inicializa uma nova fase.
        :param nome: The name of the phase.
        :param descricao: A brief description of the phase.
        """
        self.nome = nome
        self.descricao = descricao
        self.inimigos_da_fase = [] # Q49 (antecipado): Composição - Fase tem um conjunto de Inimigos

    def gerar_inimigos(self, quantidade): # Q41 (antecipado): base para sobrescrita
        """
        Gera inimigos genéricos para a fase.
        :param quantidade: The number of enemies to generate.
        """
        print(f"Gerando {quantidade} inimigos genéricos para a fase {self.nome}...")
        for i in range(quantidade):
            self.inimigos_da_fase.append(Inimigo(f"Inimigo Genérico {i+1}"))
        print(f"Inimigos gerados: {[inimigo.nome for inimigo in self.inimigos_da_fase]}")

    def entrar(self):
        """
        Prints a message when entering the phase.
        """
        print(f"Você entrou na {self.nome}: {self.descricao}")

class FaseFloresta(Fase):
    """
    Representa uma fase de floresta, que herda da classe Fase.
    """
    def __init__(self, nome="Floresta Encantada", descricao="Uma floresta densa e misteriosa."):
        """
        Inicializa uma fase de floresta, chamando o construtor da classe base.
        """
        super().__init__(nome, descricao)

class FaseDeserto(Fase):
    """
    Representa uma fase de deserto, que herda da classe Fase.
    Sobrescreve o método gerar_inimigos() para adicionar inimigos específicos do deserto.
    """
    def __init__(self, nome="Deserto Escalante", descricao="Um deserto vasto e implacável."):
        """
        Inicializa uma fase de deserto, chamando o construtor da classe base.
        """
        super().__init__(nome, descricao)

    def gerar_inimigos(self, quantidade): # Q41: Sobrescrita para inimigos específicos
        """
        Gera inimigos específicos para o ambiente de deserto.
        :param quantidade: The number of enemies to generate.
        """
        print(f"Gerando {quantidade} inimigos do deserto para a fase {self.nome}...")
        for i in range(quantidade):
            # Example of specific desert enemies with varied stats
            inimigo_tipo = random.choice(["Escorpião Gigante", "Serpente do Deserto", "Bandido do Saara"])
            self.inimigos_da_fase.append(Inimigo(f"{inimigo_tipo} {i+1}", vida=random.randint(60, 120), forca=random.randint(15, 25)))
        print(f"Inimigos gerados: {[inimigo.nome for inimigo in self.inimigos_da_fase]}")

# --- Exemplo de Uso (Questão 34 e 41) ---
if __name__ == "__main__":
    print("--- Questão 34: Classe Fase e subclasses (FaseFloresta e FaseDeserto) ---")
    print("--- E Questão 41: Modifique a classe FaseDeserto (Reescrita e Polimorfismo) ---")

    # Exemplo de uso da classe base Fase
    fase_generica = Fase("Planície Aberta", "Uma planície verdejante e vasta.")
    print("\n--- Entrando na Fase Genérica ---")
    fase_generica.entrar()
    fase_generica.gerar_inimigos(2) # Generates generic enemies

    print("\n" + "=" * 40 + "\n")

    # Exemplo de uso da subclasse FaseFloresta
    fase_floresta = FaseFloresta()
    print("\n--- Entrando na Fase Floresta ---")
    fase_floresta.entrar()
    fase_floresta.gerar_inimigos(3) # Generates generic enemies (as FaseFloresta doesn't override it)

    print("\n" + "=" * 40 + "\n")

    # Exemplo de uso da subclasse FaseDeserto (com método sobrescrito)
    fase_deserto = FaseDeserto()
    print("\n--- Entrando na Fase Deserto ---")
    fase_deserto.entrar()
    fase_deserto.gerar_inimigos(4) # Calls the overridden method, generating desert-specific enemies

    print("\nTeste de q34.py e q41.py concluído!")
