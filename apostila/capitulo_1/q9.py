# Arquivo capitulo_1\q9.py

class Jogador:
    """
    Representa um jogador com atributo energia e métodos para recuperar e usar energia.
    """
    def __init__(self):
        """
        Inicializa a energia do jogador em 50.
        """
        self.energia = 50

    def recuperar_energia(self, quantidade):
        """
        Aumenta a energia do jogador pela quantidade especificada.
        A energia não pode exceder 100.
        :param quantidade: A quantidade de energia a ser recuperada.
        """
        self.energia += quantidade
        if self.energia > 100:
            self.energia = 100
        print(f"Energia recuperada em {quantidade}. Energia atual: {self.energia}")

    def usar_energia(self, quantidade):
        """
        Reduz a energia do jogador pela quantidade especificada.
        Se não houver energia suficiente, imprime uma mensagem de aviso.
        :param quantidade: A quantidade de energia a ser usada.
        :return: True se a energia foi usada com sucesso, False caso contrário.
        """
        if self.energia >= quantidade:
            self.energia -= quantidade
            print(f"Energia usada: {quantidade}. Energia restante: {self.energia}")
            return True
        else:
            print("Sem energia suficiente!")
            return False

#Instancia a classe Jogador e testa seus métodos
if __name__ == "__main__":
    meu_jogador = Jogador()
    print(f"Energia inicial do jogador: {meu_jogador.energia}")

    meu_jogador.usar_energia(20)
    meu_jogador.recuperar_energia(30)
    meu_jogador.usar_energia(70) #Deve imprimir "Sem energia suficiente!"
    meu_jogador.usar_energia(40)
    meu_jogador.recuperar_energia(100) #Deve recuperar até 100
    print(f"Energia final do jogador: {meu_jogador.energia}")
