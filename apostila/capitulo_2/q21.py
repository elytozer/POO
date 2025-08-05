# Arquivo capitulo_2\q21.py

class Personagem:
    """
    Representa um personagem com atributo de defesa privado e getters/setters.
    """
    def __init__(self, nome, vida=100, defesa=50):
        self.nome = nome
        self.__vida = vida # Mantido privado para consistência com Q14
        self.__defesa = self._validar_defesa(defesa) # Q21: Atributo defesa privado

    def _validar_defesa(self, defesa): # Método auxiliar para validar defesa
        if not 0 <= defesa <= 100:
            print("Defesa deve ser entre 0 e 100. Definindo como 50.")
            return 50
        return defesa

    @property # Getter para vida (de Q18)
    def vida(self):
        return self.__vida

    @vida.setter # Setter para vida (de Q18, se necessário)
    def vida(self, valor):
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor

    @property # Q21: Getter para defesa
    def defesa(self):
        """
        Retorna o valor da defesa do personagem.
        """
        return self.__defesa

    @defesa.setter # Q21: Setter para defesa, garante valor entre 0 e 100
    def defesa(self, valor):
        self.__defesa = self._validar_defesa(valor)
        print(f"Defesa de {self.nome} ajustada para: {self.__defesa}")

    def tomar_dano(self, dano):
        """
        Reduz a vida do personagem pelo valor do dano, considerando a defesa.
        """
        dano_real = max(0, dano - (self.defesa // 2)) # Usa o getter de defesa
        self.vida -= dano_real # Usa o setter de vida
        if self.vida <= 0:
            print(f"{self.nome} recebeu {dano_real} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano_real} de dano. Vida restante: {self.vida}.")

# --- Exemplo de Uso (Questão 21) ---
if __name__ == "__main__":
    print("--- Questão 21: Ajuste na classe Personagem (Getters e Setters para Defesa) ---")

    guerreiro = Personagem("Defensor", defesa=70)
    print(f"Defesa inicial de {guerreiro.nome}: {guerreiro.defesa}")

    guerreiro.defesa = 90 # Define defesa válida
    print(f"Nova defesa: {guerreiro.defesa}")

    guerreiro.defesa = 120 # Tenta definir defesa inválida (deve ser 50)
    print(f"Defesa após tentativa inválida (>100): {guerreiro.defesa}")

    guerreiro.defesa = -10 # Tenta definir defesa inválida (<0)
    print(f"Defesa após outra tentativa inválida (<0): {guerreiro.defesa}")

    print("\nTestando dano com defesa:")
    print(f"Vida inicial de {guerreiro.nome}: {guerreiro.vida}")
    guerreiro.tomar_dano(50) # Dano de 50, defesa de 50 (dano real 50 - 25 = 25)
    print(f"Vida após dano: {guerreiro.vida}")

    print("Teste de q21.py concluído!")
