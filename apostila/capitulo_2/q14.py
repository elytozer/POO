# Arquivo capitulo_2\q14.py

class Personagem:
    """
    Representa um personagem no jogo com nome e vida (privada).
    """
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.__vida = vida  # Q14: Atributo vida privado

    def mostrar_vida(self): # Q14: Método público para retornar vida
        """
        Retorna a vida atual do personagem.
        """
        return self.__vida

    def tomar_dano(self, dano): # Mantido para funcionalidade
        """
        Reduz a vida do personagem pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Game Over!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.__vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.__vida}.")

# --- Exemplo de Uso (Questão 14) ---
if __name__ == "__main__":
    print("--- Questão 14: Ajuste na classe Personagem (Encapsulamento) ---")

    heroi = Personagem("Guardião")
    # Tentativa de acesso direto (não recomendado, mas Python permite)
    # print(f"Vida (acesso direto, não recomendado): {heroi.__vida}") # Isso geraria um AttributeError em uso real
    
    # Acesso via método público
    print(f"Vida de {heroi.nome} (via mostrar_vida()): {heroi.mostrar_vida()}")

    heroi.tomar_dano(30)
    print(f"Vida de {heroi.nome} após dano: {heroi.mostrar_vida()}")

    heroi.tomar_dano(80) # Leva a vida a 0
    print(f"Vida de {heroi.nome} após mais dano: {heroi.mostrar_vida()}")

    print("Teste de q14.py concluído!")
