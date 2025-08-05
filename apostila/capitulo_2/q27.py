# Arquivo capitulo_2\q27.py

import random # Necessário para gerar dano aleatório

# Classe Inimigo (base para herança da classe Chefe)
# Inclui encapsulamento para 'vida' e 'forca' e métodos para tomar dano e atacar.
class Inimigo:
    """
    Representa um inimigo no jogo com nome, vida e força.
    """
    def __init__(self, nome, vida=100, forca=15):
        self.nome = nome
        self.__vida = vida    # Atributo privado para vida
        self.__forca = forca  # Atributo privado para força

    @property # Getter para 'vida'
    def vida(self):
        """
        Retorna a vida atual do inimigo.
        """
        return self.__vida

    @vida.setter # Setter para 'vida'
    def vida(self, valor):
        """
        Define a vida do inimigo, garantindo que não seja negativa.
        """
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor

    # Getter para 'forca' (não pedido explicitamente, mas útil para demonstração e subclasses)
    @property
    def forca(self):
        """
        Retorna a força do inimigo.
        """
        return self.__forca

    def tomar_dano(self, dano):
        """
        Reduz a vida do inimigo pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Inimigo derrotado!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano # Usa o setter de vida
        if self.vida <= 0:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. {self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

    def atacar(self, alvo):
        """
        Ataca um alvo, causando dano baseado na força do inimigo.
        :param alvo: O objeto a ser atacado (Personagem ou outro Inimigo).
        """
        dano = random.randint(self.__forca - 5, self.__forca + 5) # Usa o atributo privado __forca
        print(f"{self.nome} (Força: {self.__forca}) atacou {alvo.nome} causando {dano} de dano.")
        alvo.tomar_dano(dano) # Assume que o alvo tem um método tomar_dano

# Classe Personagem (necessária para que o método atacar() do Inimigo/Chefe funcione)
# Inclui um método básico para tomar dano.
class Personagem:
    """
    Representa um personagem simples para ser alvo de ataques.
    """
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida # Não encapsulado para simplicidade, mas Personagem em outras Qs tem encapsulamento

    def tomar_dano(self, dano):
        """
        Reduz a vida do personagem pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Game Over!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

# Classe Chefe (Q27: herda de Inimigo, dobro de vida e força)
# Sobrescreve o método atacar() para a Questão 37.
class Chefe(Inimigo):
    """
    Representa um Chefe que herda de Inimigo, com o dobro de vida e força.
    Possui um ataque especial que causa dano extra.
    """
    def __init__(self, nome, vida_base=100, forca_base=15):
        # Q27: Chama o construtor da classe base (Inimigo) com vida e força dobradas.
        super().__init__(nome, vida_base * 2, forca_base * 2)
        print(f"Chefe {self.nome} criado com {self.vida} de vida e {self.forca} de força.")

    def atacar(self, alvo): # Q37: Sobrescrita do método atacar() para golpe especial
        """
        Chefe ataca com um golpe especial que causa dano extra.
        :param alvo: O objeto Personagem ou Inimigo a ser atacado.
        """
        # Acessa a força via getter, ou diretamente se necessário (ex: self._Inimigo__forca)
        dano_base = random.randint(self.forca - 5, self.forca + 5)
        dano_extra = random.randint(10, 25) # Dano extra do golpe especial
        dano_total = dano_base + dano_extra
        print(f"{self.nome} (Chefe) usou um GOLPE ESPECIAL em {alvo.nome} causando {dano_total} de dano!")
        alvo.tomar_dano(dano_total)

# --- Exemplo de Uso (Questão 27 e 37) ---
if __name__ == "__main__":
    print("--- Questão 27: Classe Chefe (Herança) ---")
    print("--- E Questão 37: Modifique a classe Chefe (Reescrita e Polimorfismo) ---")

    # Cria um inimigo comum para comparação
    inimigo_comum = Inimigo("Goblin", vida=50, forca=10)
    print(f"\nStatus do Inimigo Comum: {inimigo_comum.nome}, Vida: {inimigo_comum.vida}, Força: {inimigo_comum.forca}")

    # Cria um chefe, passando os valores base que serão dobrados no construtor
    chefe_maldoso = Chefe("Lorde das Sombras", vida_base=100, forca_base=25)
    # Note que o print no construtor do Chefe já mostra os valores dobrados.

    # Cria um herói para ser o alvo dos ataques
    heroi = Personagem("Aventureiro Corajoso", vida=200) # Herói com mais vida para o teste de chefe
    print(f"\nVida inicial de {heroi.nome}: {heroi.vida}")

    print("\n--- Inimigo Comum Ataca ---")
    inimigo_comum.atacar(heroi)
    print(f"Vida de {heroi.nome} após ataque comum: {heroi.vida}")

    print("\n--- Chefe Ataca com Golpe Especial ---")
    chefe_maldoso.atacar(heroi) # Chama o método sobrescrito do Chefe
    print(f"Vida de {heroi.nome} após golpe especial: {heroi.vida}")

    chefe_maldoso.atacar(heroi) # Mais um ataque do chefe
    print(f"Vida de {heroi.nome} após segundo golpe especial: {heroi.vida}")

    print("\nTeste de q27.py e q37.py concluído!")
