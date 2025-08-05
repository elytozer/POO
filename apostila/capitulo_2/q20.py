# Arquivo capitulo_2\q20.py

class Jogo:
    """
    Representa um jogo com um atributo de dificuldade privado e getters/setters.
    """
    def __init__(self, titulo="Meu Jogo", dificuldade=1):
        self.titulo = titulo
        self._dificuldade = self._validar_dificuldade(dificuldade) # Atributo privado

    def _validar_dificuldade(self, dificuldade): # Método auxiliar para validação
        if not 1 <= dificuldade <= 3:
            print("A dificuldade deve ser um valor entre 1 e 3. Definindo como 1.")
            return 1
        return dificuldade

    @property # Q20: Getter para dificuldade
    def dificuldade(self):
        """
        Retorna o nível de dificuldade atual.
        """
        return self._dificuldade

    @dificuldade.setter # Q20: Setter para dificuldade, aceita apenas 1 a 3
    def dificuldade(self, valor):
        self._dificuldade = self._validar_dificuldade(valor)
        print(f"Dificuldade do jogo ajustada para: {self._dificuldade}")

    def iniciar(self):
        """
        Imprime uma mensagem indicando que o jogo começou.
        """
        print(f"O jogo '{self.titulo}' começou com dificuldade {self.dificuldade}!")

# --- Exemplo de Uso (Questão 20) ---
if __name__ == "__main__":
    print("--- Questão 20: Ajuste na classe Jogo (Getters e Setters) ---")

    meu_jogo = Jogo("Aventura Mística", dificuldade=2)
    print(f"Dificuldade inicial: {meu_jogo.dificuldade}")

    meu_jogo.dificuldade = 3 # Define dificuldade para 3 (válido)
    print(f"Nova dificuldade: {meu_jogo.dificuldade}")

    meu_jogo.dificuldade = 5 # Tenta definir dificuldade inválida (deve ser 1)
    print(f"Dificuldade após tentativa inválida: {meu_jogo.dificuldade}")

    meu_jogo.dificuldade = 0 # Tenta definir dificuldade inválida (deve ser 1)
    print(f"Dificuldade após outra tentativa inválida: {meu_jogo.dificuldade}")

    meu_jogo.iniciar()

    print("Teste de q20.py concluído!")
