# Arquivo capitulo_2\q24.py

class Jogador:
    """
    Representa um jogador com um construtor modificado para aceitar nome, energia e pontos.
    """
    def __init__(self, nome, energia=50, pontos=0): # Q24: nome, energia e pontos como parâmetros
        self.nome = nome
        # O atributo energia é encapsulado para consistência com a Questão 17.
        # O setter e o método auxiliar _validar_energia garantem que a energia esteja entre 0 e 100.
        self.__energia = self._validar_energia(energia)
        self.__pontos = pontos # Mantido como um atributo simples para esta questão

    def _validar_energia(self, energia):
        """
        Método auxiliar para garantir que o valor da energia esteja entre 0 e 100.
        """
        if not 0 <= energia <= 100:
            print("Energia deve ser entre 0 e 100. Ajustando valor.")
            return max(0, min(100, energia)) # Garante que fique entre 0 e 100
        return energia

    @property
    def energia(self):
        """
        Getter para o atributo de energia.
        """
        return self.__energia

    @energia.setter
    def energia(self, valor):
        """
        Setter para o atributo de energia, usando o método de validação.
        """
        self.__energia = self._validar_energia(valor)

    def mostrar_status(self):
        """
        Mostra o status atual do jogador, incluindo nome, energia e pontos.
        """
        print(f"Jogador: {self.nome}, Energia: {self.energia}, Pontos: {self.__pontos}")

# --- Exemplo de Uso (Questão 24) ---
if __name__ == "__main__":
    print("--- Questão 24: Ajuste na classe Jogador (Construtores) ---")

    # Criando um jogador com todos os parâmetros especificados
    jogador1 = Jogador("Mestre Aventureiro", energia=80, pontos=500)
    jogador1.mostrar_status()

    print("\n" + "-" * 30 + "\n")

    # Criando um jogador usando os valores padrão para energia e pontos
    jogador2 = Jogador("Novato Explorador")
    jogador2.mostrar_status()

    print("\n" + "-" * 30 + "\n")

    # Criando um jogador com valores que testam a validação da energia
    # A energia 120 deve ser ajustada para 100.
    # Os pontos -100 serão aceitos, pois a validação de pontos não foi solicitada nesta questão.
    jogador3 = Jogador("Veterano Cansado", energia=120, pontos=-100)
    jogador3.mostrar_status()

    print("\nTeste de q24.py concluído!")
