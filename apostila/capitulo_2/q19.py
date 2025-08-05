# Arquivo capitulo_2\q19.py

class Pontuacao:
    """
    Representa a pontuação do jogo com um setter @pontos.setter que impede valores negativos.
    """
    def __init__(self, pontos=0):
        self.__pontos = pontos # Atributo privado

    @property # Getter para pontos
    def pontos(self):
        """
        Retorna a pontuação atual.
        """
        return self.__pontos

    @pontos.setter # Q19: Setter para pontos, impede valores negativos
    def pontos(self, valor):
        if valor < 0:
            print("Pontuação não pode ser negativa. Mantendo o valor atual ou zerando.")
            self.__pontos = 0 # Define como 0 se tentar ser negativo
        else:
            self.__pontos = valor
        print(f"Pontuação ajustada para: {self.__pontos}")

    def adicionar_pontos(self, quantidade):
        """
        Adiciona uma quantidade específica de pontos à pontuação total.
        :param quantidade: O número de pontos a ser adicionado.
        """
        self.pontos += quantidade # Isso usará o setter

    def zerar_pontos(self):
        """
        Zera a pontuação.
        """
        self.pontos = 0 # Isso usará o setter
        print("Pontuação zerada!")

# --- Exemplo de Uso (Questão 19) ---
if __name__ == "__main__":
    print("--- Questão 19: Ajuste na classe Pontuacao (Getters e Setters) ---")

    placar_setter = Pontuacao(100)
    print(f"Pontuação inicial: {placar_setter.pontos}")

    placar_setter.adicionar_pontos(50) # Adiciona 50, total 150
    print(f"Pontuação após adicionar 50: {placar_setter.pontos}")

    placar_setter.pontos = -20 # Tentativa de definir valor negativo, deve ser ajustado para 0
    print(f"Pontuação após tentativa de negativo: {placar_setter.pontos}")

    placar_setter.pontos = 75 # Define diretamente para 75
    print(f"Pontuação após definir para 75: {placar_setter.pontos}")

    placar_setter.zerar_pontos()
    print(f"Pontuação após zerar: {placar_setter.pontos}")

    print("Teste de q19.py concluído!")
