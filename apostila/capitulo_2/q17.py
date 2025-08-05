# Arquivo capitulo_2\q17.py

class Jogador:
    """
    Representa um jogador com atributo energia privado e métodos para gerenciar energia.
    """
    def __init__(self, nome, energia=50):
        self.nome = nome
        self.__energia = self._validar_energia(energia) # Q17: Atributo energia privado

    def _validar_energia(self, energia): # Método auxiliar para garantir range 0-100
        if not 0 <= energia <= 100:
            print("Energia deve ser entre 0 e 100. Ajustando valor.")
            return max(0, min(100, energia)) # Garante que fique entre 0 e 100
        return energia

    def recuperar_energia(self, quantidade): # Q17: Garante valor entre 0 e 100
        """
        Aumenta a energia do jogador pela quantidade especificada.
        A energia não pode exceder 100.
        :param quantidade: A quantidade de energia a ser recuperada.
        """
        nova_energia = self.__energia + quantidade
        self.__energia = self._validar_energia(nova_energia)
        print(f"{self.nome} recuperou {quantidade} de energia. Energia atual: {self.__energia}")

    def usar_energia(self, quantidade): # Q17: Garante valor entre 0 e 100
        """
        Reduz a energia do jogador pela quantidade especificada.
        Se não houver energia suficiente, imprime uma mensagem de aviso.
        :param quantidade: A quantidade de energia a ser usada.
        :return: True se a energia foi usada com sucesso, False caso contrário.
        """
        if self.__energia >= quantidade:
            nova_energia = self.__energia - quantidade
            self.__energia = self._validar_energia(nova_energia)
            print(f"{self.nome} usou {quantidade} de energia. Energia restante: {self.__energia}")
            return True
        else:
            print(f"{self.nome} sem energia suficiente! Energia atual: {self.__energia}")
            return False

    def mostrar_energia(self): # Método auxiliar para demonstração
        """
        Retorna a energia atual do jogador.
        """
        return self.__energia

# --- Exemplo de Uso (Questão 17) ---
if __name__ == "__main__":
    print("--- Questão 17: Ajuste na classe Jogador (Encapsulamento) ---")

    jogador_teste = Jogador("Explorador", energia=70)
    print(f"Energia inicial de {jogador_teste.nome}: {jogador_teste.mostrar_energia()}")

    jogador_teste.usar_energia(30) # 70 - 30 = 40
    jogador_teste.recuperar_energia(20) # 40 + 20 = 60
    jogador_teste.usar_energia(70) # 60 - 70 = -10 (deve avisar e manter em 0)
    print(f"Energia após tentativa de uso excessivo: {jogador_teste.mostrar_energia()}")

    jogador_teste.recuperar_energia(150) # 0 + 150 = 150 (deve limitar a 100)
    print(f"Energia após recuperação excessiva: {jogador_teste.mostrar_energia()}")

    print("Teste de q17.py concluído!")
