# Arquivo capitulo_2\q31.py

import random # Necessário para gerar dano aleatório

class Arma:
    """
    Classe base para armas.
    Define a estrutura básica para qualquer arma no jogo.
    """
    def __init__(self, nome, dano_base):
        """
        Inicializa uma nova arma.
        :param nome: O nome da arma (ex: "Espada Longa", "Arco Curto").
        :param dano_base: O valor base de dano que a arma causa.
        """
        self.nome = nome
        self.dano_base = dano_base

    def usar(self):
        """
        Método para usar a arma e retornar o dano causado.
        Este é um método abstrato que deve ser implementado por todas as subclasses.
        Levanta um erro se não for sobrescrito.
        """
        raise NotImplementedError("O método 'usar' deve ser implementado pelas subclasses.")

class Espada(Arma):
    """
    Representa uma espada, que herda da classe Arma.
    Caracteriza-se por um ataque de golpe corpo a corpo com variação de dano.
    """
    def __init__(self, nome="Espada Curta", dano_base=15):
        """
        Inicializa uma espada, chamando o construtor da classe base (Arma).
        Define um nome e um dano base padrão para a espada.
        """
        super().__init__(nome, dano_base)

    def usar(self):
        """
        Implementa o método 'usar' para a espada.
        Calcula um dano aleatório baseado no dano base da espada,
        simulando a variação de um golpe.
        """
        dano = random.randint(self.dano_base - 5, self.dano_base + 5)
        print(f"Você golpeou com a {self.nome} causando {dano} de dano!")
        return dano

class Arco(Arma):
    """
    Representa um arco, que herda da classe Arma.
    Caracteriza-se por um ataque à distância com variação de dano e chance de acerto crítico.
    """
    def __init__(self, nome="Arco Longo", dano_base=10):
        """
        Inicializa um arco, chamando o construtor da classe base (Arma).
        Define um nome e um dano base padrão para o arco.
        """
        super().__init__(nome, dano_base)

    def usar(self):
        """
        Implementa o método 'usar' para o arco.
        Calcula um dano aleatório e tem uma chance de 20% de causar um acerto crítico,
        dobrando o dano.
        """
        dano = random.randint(self.dano_base - 3, self.dano_base + 7)
        if random.random() < 0.2: # 20% de chance de crítico
            dano *= 2
            print(f"Você disparou uma flecha com o {self.nome}! ACERTO CRÍTICO! Causando {dano} de dano!")
        else:
            print(f"Você disparou uma flecha com o {self.nome} causando {dano} de dano.")
        return dano

# --- Exemplo de Uso (Questão 31) ---
if __name__ == "__main__":
    print("--- Questão 31: Classe Arma e subclasses (Espada e Arco) ---")

    # Cria instâncias das subclasses de Arma
    espada_ferro = Espada("Espada de Ferro", dano_base=20)
    arco_caca = Arco("Arco de Caça", dano_base=12)

    print(f"\nTestando a {espada_ferro.nome}:")
    dano_espada = espada_ferro.usar()
    print(f"Dano causado pela espada: {dano_espada}")

    print(f"\nTestando o {arco_caca.nome}:")
    dano_arco = arco_caca.usar()
    print(f"Dano causado pelo arco: {dano_arco}")

    print("\nTestando múltiplos ataques com o arco para observar acertos críticos:")
    for i in range(5):
        print(f"Ataque {i+1}: ", end="")
        arco_caca.usar()

    print("\nTeste de q31.py concluído!")
