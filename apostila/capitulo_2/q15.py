# Arquivo capitulo_2\q15.py

class Pontuacao:
    """
    Representa a pontuação do jogo com um atributo privado e métodos para gerenciar pontos.
    """
    def __init__(self, pontos=0):
        self.__pontos = pontos # Q15: Atributo pontos privado

    def adicionar_pontos(self, quantidade): # Q15: Impede modificações diretas no atributo
        """
        Adiciona uma quantidade específica de pontos à pontuação total.
        :param quantidade: O número de pontos a ser adicionado.
        """
        if quantidade > 0:
            self.__pontos += quantidade
            print(f"Adicionados {quantidade} pontos. Pontuação atual: {self.__pontos}")
        else:
            print("Não é possível adicionar pontos negativos ou zero diretamente. Use um método específico para remover pontos se necessário.")

    def mostrar_pontos(self): # Mantido para visualização
        """
        Imprime a pontuação atual.
        """
        print(f"Pontuação atual: {self.__pontos}")

    def zerar_pontos(self): # Mantido para funcionalidade
        """
        Zera a pontuação.
        """
        self.__pontos = 0
        print("Pontuação zerada!")

# --- Exemplo de Uso (Questão 15) ---
if __name__ == "__main__":
    print("--- Questão 15: Ajuste na classe Pontuacao (Encapsulamento) ---")

    placar = Pontuacao()
    placar.mostrar_pontos() # 0

    placar.adicionar_pontos(50) # Adiciona 50
    placar.adicionar_pontos(25) # Adiciona 25
    placar.mostrar_pontos() # 75

    # Tentativa de "modificação direta" (via método, mas com validação)
    placar.adicionar_pontos(-10) # Deve ser rejeitado ou avisar
    placar.mostrar_pontos() # Ainda 75

    placar.zerar_pontos()
    placar.mostrar_pontos() # 0

    print("Teste de q15.py concluído!")
