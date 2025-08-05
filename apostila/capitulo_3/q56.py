#Arquivo capitulo_2/q56.py
#Crie um atributo de classe total_jogadores na classe Jogador,
#que conta quantos jogadores foram criados.

class Jogador:
    """
    Representa um jogador no jogo.
    Inclui um atributo de classe para contar quantos jogadores foram criados (Q56).
    """
    #Atributo de classe para contar o total de jogadores instanciados.
    #Este atributo pertence à classe Jogador, não a instâncias individuais.
    total_jogadores = 0

    def __init__(self, nome, energia=50, pontos=0):
        """
        Inicializa um novo jogador.
        :param nome: O nome do jogador.
        :param energia: A energia inicial do jogador.
        :param pontos: Os pontos iniciais do jogador.
        """
        self.nome = nome
        self.energia = energia
        self.pontos = pontos
        #Incrementa o contador de jogadores cada vez que uma nova instância é criada.
        Jogador.total_jogadores += 1
        print(f"Jogador '{self.nome}' criado. Total de jogadores: {Jogador.total_jogadores}")

    def __del__(self):
        """
        Método destrutor. É chamado quando uma instância do Jogador é deletada.
        Decrementa o contador de jogadores.
        """
        Jogador.total_jogadores -= 1
        print(f"Jogador '{self.nome}' deletado. Total de jogadores restantes: {Jogador.total_jogadores}")

#Exemplo de Uso
if __name__ == "__main__":
    print("--- Questão 56: Contador de Jogadores ---")

    #Criação de jogadores
    print("\nCriando jogadores:")
    jogador1 = Jogador("Alice")
    jogador2 = Jogador("Bob")
    jogador3 = Jogador("Charlie")

    #Acessando o atributo de classe diretamente (Q56)
    print(f"\nContagem direta de Jogador.total_jogadores: {Jogador.total_jogadores}")

    #Deletando um jogador para ver o contador diminuir
    print("\nDeletando 'jogador1':")
    del jogador1 # Isso acionará o método __del__

    #Verificando a contagem novamente após a deleção
    print(f"\nContagem direta de Jogador.total_jogadores após a deleção: {Jogador.total_jogadores}")

    #Criando mais um jogador
    print("\nCriando 'jogador4':")
    jogador4 = Jogador("Diana")
    print(f"Contagem direta de Jogador.total_jogadores: {Jogador.total_jogadores}")

    print("\nTeste de q56.py concluído!")
