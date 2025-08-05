# Arquivo capitulo_2\q16.py

import random # Para dano aleatório

# Classe Personagem (necessária para Inimigo.atacar)
class Personagem:
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

class Inimigo:
    """
    Representa um inimigo com atributo força privado e método atacar modificado.
    """
    def __init__(self, nome, vida=100, forca=15):
        self.nome = nome
        self.vida = vida
        self.__forca = forca # Q16: Atributo forca privado

    def atacar(self, alvo): # Q16: Exibe a força sem acesso direto a __forca
        """
        Ataca um alvo, exibindo a força do ataque.
        :param alvo: O objeto a ser atacado (Personagem).
        """
        dano = random.randint(self.__forca - 5, self.__forca + 5) # Usa __forca internamente
        print(f"{self.nome} atacou {alvo.nome} com força base {self.__forca} causando {dano} de dano.") # Q16
        alvo.tomar_dano(dano)

    def mostrar_forca_inimigo(self): # Método auxiliar para demonstração
        """
        Retorna a força do inimigo (para fins de teste/depuração).
        """
        return self.__forca

# --- Exemplo de Uso (Questão 16) ---
if __name__ == "__main__":
    print("--- Questão 16: Ajuste na classe Inimigo (Encapsulamento) ---")

    inimigo_orc = Inimigo("Orc Bruto", forca=20)
    heroi_alvo = Personagem("Cavaleiro")

    print(f"Força do {inimigo_orc.nome} (via método auxiliar): {inimigo_orc.mostrar_forca_inimigo()}")
    print(f"Vida inicial de {heroi_alvo.nome}: {heroi_alvo.vida}")

    inimigo_orc.atacar(heroi_alvo)
    inimigo_orc.atacar(heroi_alvo)
    inimigo_orc.atacar(heroi_alvo)

    print(f"Vida final de {heroi_alvo.nome}: {heroi_alvo.vida}")

    print("Teste de q16.py concluído!")
