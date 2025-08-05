# Arquivo capitulo_2\q22.py

class Personagem:
    """
    Representa um personagem com um construtor modificado para aceitar nome e vida.
    """
    def __init__(self, nome, vida=100, defesa=50): # Q22: nome e vida; Q21 (reutilizado): defesa
        self.nome = nome
        self.__vida = vida
        self.__defesa = defesa # Simplificado para esta questão, mas seria encapsulado em um cenário real

    @property
    def vida(self):
        """
        Retorna a vida atual do personagem.
        """
        return self.__vida

    @vida.setter
    def vida(self, valor):
        """
        Define a vida do personagem, garantindo que não seja negativa.
        """
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor

    @property
    def defesa(self):
        """
        Retorna o valor da defesa do personagem.
        """
        return self.__defesa

    @defesa.setter
    def defesa(self, valor):
        """
        Define a defesa do personagem, garantindo que o valor fique entre 0 e 100.
        """
        if not 0 <= valor <= 100:
            print("Defesa deve ser entre 0 e 100. Definindo como 50.")
            self.__defesa = 50
        else:
            self.__defesa = valor

    def dizer_nome(self):
        """
        Imprime o nome do personagem.
        """
        print(f"Meu nome é {self.nome}.")

    def tomar_dano(self, dano):
        """
        Reduz a vida do personagem pelo valor do dano, considerando a defesa.
        """
        dano_real = max(0, dano - (self.defesa // 2))
        self.vida -= dano_real
        if self.vida <= 0:
            print(f"{self.nome} recebeu {dano_real} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano_real} de dano. Vida restante: {self.vida}.")

# --- Exemplo de Uso (Questão 22) ---
if __name__ == "__main__":
    print("--- Questão 22: Ajuste na classe Personagem (Construtores) ---")

    personagem1 = Personagem("Arqueiro", vida=80)
    print(f"Personagem 1: {personagem1.nome}, Vida: {personagem1.vida}, Defesa: {personagem1.defesa}")

    personagem2 = Personagem("Bárbaro", vida=120, defesa=60)
    print(f"Personagem 2: {personagem2.nome}, Vida: {personagem2.vida}, Defesa: {personagem2.defesa}")

    personagem3 = Personagem("Mago") # Usa vida e defesa padrão
    print(f"Personagem 3: {personagem3.nome}, Vida: {personagem3.vida}, Defesa: {personagem3.defesa}")

    personagem2.tomar_dano(70)
    print(f"Vida de {personagem2.nome} após dano: {personagem2.vida}")

    print("Teste de q22.py concluído!")
