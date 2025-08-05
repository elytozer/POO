#Arquivo capitulo_2/q57.py (ou capitulo_3/q57.py, dependendo da sua estrutura)
#Crie um método de classe exibir_total_jogadores() na classe
#Jogador, que retorna a quantidade total de jogadores instanciados.
#Inclui também a Questão 56, pois é um pré-requisito funcional.

class Jogador:
    """
    Representa um jogador no jogo.
    Inclui um atributo de classe para contar quantos jogadores foram criados (Q56)
    e um método de classe para exibir essa contagem (Q57).
    """
    #Atributo de classe para contar o total de jogadores instanciados.
    #Este atributo pertence à classe Jogador
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
        Q56 (complemento): Decrementa o contador de jogadores.
        """
        Jogador.total_jogadores -= 1
        print(f"Jogador '{self.nome}' deletado. Total de jogadores restantes: {Jogador.total_jogadores}")

    @classmethod #Q57: Decorador que indica que este é um método de classe.
    #O primeiro parâmetro é 'cls' (convenção), que se refere à própria classe (Jogador).
    def exibir_total_jogadores(cls):
        """
        Método de classe que retorna e imprime a quantidade total de jogadores instanciados.
        Acessa o atributo de classe 'total_jogadores' através de 'cls'.
        :return: A quantidade total de jogadores.
        """
        print(f"Total de jogadores instanciados: {cls.total_jogadores}")
        return cls.total_jogadores

#Exemplo de Uso
if __name__ == "__main__":
    print("--- Questão 57: Exibir Total de Jogadores (Método de Classe) ---")

    #Criação de jogadores
    print("\nCriando jogadores:")
    jogador_a = Jogador("Alice")
    jogador_b = Jogador("Bob")
    jogador_c = Jogador("Charlie")

    #Chamando o método de classe para exibir o total de jogadores (Q57)
    print("\nChamando o método de classe 'exibir_total_jogadores()':")
    total_atual = Jogador.exibir_total_jogadores()
    print(f"O método retornou: {total_atual}")

    #Deletando um jogador para ver o efeito na contagem
    print("\nDeletando 'jogador_a':")
    del jogador_a

    #Chamando o método de classe novamente para verificar a contagem atualizada
    print("\nVerificando o total de jogadores após a deleção:")
    Jogador.exibir_total_jogadores()

    #Criando mais um jogador
    print("\nCriando 'jogador_d':")
    jogador_d = Jogador("Diana")
    Jogador.exibir_total_jogadores()


    print("\nTeste de q57.py concluído!")
