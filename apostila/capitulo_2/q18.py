# Arquivo capitulo_2\q18.py

class Personagem:
    """
    Representa um personagem com atributo de vida privado e um getter @property.
    """
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.__vida = vida  # Atributo privado

    @property # Q18: Getter para vida
    def vida(self):
        """
        Retorna a vida atual do personagem.
        """
        return self.__vida

    # Opcional: Um setter para vida, se permitido (não pedido na Q18, mas útil)
    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor
        print(f"Vida de {self.nome} ajustada para {self.__vida}.")

    def tomar_dano(self, dano):
        """
        Reduz a vida do personagem pelo valor do dano.
        """
        self.vida -= dano # Usa o setter implícito se definido, ou acessa diretamente __vida
        if self.vida <= 0: # Usa o getter para verificar
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

# --- Exemplo de Uso (Questão 18) ---
if __name__ == "__main__":
    print("--- Questão 18: Ajuste na classe Personagem (Getters e Setters) ---")

    heroi_getter = Personagem("Lutador")
    print(f"Vida de {heroi_getter.nome} (via getter): {heroi_getter.vida}") # Acessa como atributo

    heroi_getter.tomar_dano(40)
    print(f"Vida de {heroi_getter.nome} após dano: {heroi_getter.vida}")

    # Exemplo de uso do setter (se implementado)
    heroi_getter.vida = 100 # Isso chamaria o setter se ele existisse
    print(f"Vida de {heroi_getter.nome} após ajuste: {heroi_getter.vida}")

    print("Teste de q18.py concluído!")
