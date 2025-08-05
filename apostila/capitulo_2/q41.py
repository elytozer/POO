# Arquivo capitulo_2/q41.py
# Solução para a Questão 41: Modifique a classe FaseDeserto (Reescrita e Polimorfismo).

import random # Necessário para gerar inimigos aleatórios

# Classe Inimigo (base para Fase.gerar_inimigos)
# Uma classe simples para representar inimigos que podem ser gerados nas fases.
class Inimigo:
    """
    Representa um inimigo simples com nome, vida e força.
    """
    def __init__(self, nome, vida=100, forca=15):
        """
        Inicializa um novo inimigo.
        :param nome: O nome do inimigo.
        :param vida: A vida inicial do inimigo.
        :param forca: A força do inimigo.
        """
        self.nome = nome
        self.vida = vida
        self.forca = forca # Simplificado para esta questão

    def tomar_dano(self, dano):
        """
        Reduz a vida do inimigo pelo valor do dano.
        :param dano: A quantidade de dano a ser aplicada.
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
        :param nome: O nome da fase.
        :param descricao: Uma breve descrição da fase.
        """
        self.nome = nome
        self.descricao = descricao
        self.inimigos_da_fase = [] # Lista para armazenar inimigos (composição, Q49 antecipada)

    def gerar_inimigos(self, quantidade): # Método base a ser sobrescrito
        """
        Gera inimigos genéricos para a fase.
        :param quantidade: O número de inimigos a gerar.
        """
        print(f"Gerando {quantidade} inimigos genéricos para a fase {self.nome}...")
        for i in range(quantidade):
            self.inimigos_da_fase.append(Inimigo(f"Inimigo Genérico {i+1}"))
        print(f"Inimigos gerados: {[inimigo.nome for inimigo in self.inimigos_da_fase]}")

    def entrar(self):
        """
        Imprime uma mensagem ao entrar na fase.
        """
        print(f"Você entrou na {self.nome}: {self.descricao}")

# Classe FaseDeserto (Q34, Q41: herda de Fase, sobrescreve gerar_inimigos())
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

    def gerar_inimigos(self, quantidade): # Q41: Sobrescrita do método 'gerar_inimigos()'
        """
        Gera inimigos específicos para o ambiente de deserto.
        Demonstra o polimorfismo ao substituir o comportamento do método da classe base.
        :param quantidade: O número de inimigos a gerar.
        """
        print(f"Gerando {quantidade} inimigos do deserto para a fase {self.nome}...")
        for i in range(quantidade):
            # Exemplo de inimigos específicos do deserto com estatísticas variadas
            inimigo_tipo = random.choice(["Escorpião Gigante", "Serpente do Deserto", "Bandido do Saara"])
            self.inimigos_da_fase.append(Inimigo(f"{inimigo_tipo} {i+1}", vida=random.randint(60, 120), forca=random.randint(15, 25)))
        print(f"Inimigos gerados: {[inimigo.nome for inimigo in self.inimigos_da_fase]}")

# --- Exemplo de Uso (Questão 41) ---
if __name__ == "__main__":
    print("--- Questão 41: Modifique a classe FaseDeserto (Reescrita e Polimorfismo) ---")

    # Exemplo de uso da classe base Fase
    fase_generica = Fase("Planície Aberta", "Uma planície verdejante e vasta.")
    print("\n--- Entrando na Fase Genérica ---")
    fase_generica.entrar()
    fase_generica.gerar_inimigos(2) # Gera inimigos genéricos

    print("\n" + "=" * 40 + "\n")

    # Exemplo de uso da subclasse FaseDeserto (com método sobrescrito)
    fase_deserto = FaseDeserto()
    print("\n--- Entrando na Fase Deserto ---")
    fase_deserto.entrar()
    fase_deserto.gerar_inimigos(3) # Chama o método 'gerar_inimigos' sobrescrito, gerando inimigos específicos do deserto

    print("\nTeste de q41.py concluído!")
