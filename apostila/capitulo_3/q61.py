# Arquivo capitulo_2/q61.py (ou capitulo_3/q61.py, dependendo da sua estrutura)

class Fase:
    """
    Representa uma fase do jogo.
    Inclui um atributo de classe para o tempo máximo de conclusão
    que é compartilhado por todas as instâncias da classe.
    """
    # Q61: Atributo de classe para o tempo máximo global.
    # Este atributo pertence à classe Fase, não a instâncias individuais.
    tempo_maximo = 60 # Valor padrão em segundos (ex: 60 segundos = 1 minuto)

    def __init__(self, nome, descricao):
        """
        Inicializa uma nova fase.
        :param nome: O nome da fase.
        :param descricao: Uma breve descrição da fase.
        """
        self.nome = nome
        self.descricao = descricao
        # A instância da fase pode acessar o tempo máximo global diretamente.
        print(f"Fase '{self.nome}' criada. Tempo máximo para esta fase: {Fase.tempo_maximo} segundos.")

    def iniciar_fase(self):
        """
        Inicia a fase, exibindo o tempo máximo permitido para completá-la.
        """
        print(f"Entrando na fase: {self.nome}. Você tem {Fase.tempo_maximo} segundos para completar!")

    @classmethod # Decorador que indica que este é um método de classe.
    # O primeiro parâmetro é 'cls' (convenção), que se refere à própria classe (Fase).
    def definir_tempo_maximo_global(cls, novo_tempo):
        """
        Define um novo tempo máximo global para todas as fases.
        Este método de classe altera o atributo 'tempo_maximo' da classe Fase.
        :param novo_tempo: O novo tempo máximo em segundos (deve ser um valor positivo).
        """
        if novo_tempo > 0:
            cls.tempo_maximo = novo_tempo
            print(f"Tempo máximo global para fases alterado para: {cls.tempo_maximo} segundos.")
        else:
            print(f"Valor inválido para tempo máximo: {novo_tempo}. O tempo máximo deve ser um valor positivo.")


if __name__ == "__main__":
    print("--- Questão 61: Tempo Máximo Global da Fase ---")

    #Criação de instâncias de Fase. Ela reflete o tempo maximo global inicial.
    print("\nCriando fases com o tempo máximo global padrão (60 segundos):")
    fase_inicial = Fase("Floresta Sombria", "Uma fase de introdução com desafios simples.")
    fase_desafio = Fase("Torre do Mago", "Um desafio vertical com inimigos poderosos.")

    print(f"\nTempo máximo global atual (acesso direto à classe): {Fase.tempo_maximo} segundos")
    print(f"Tempo máximo da '{fase_inicial.nome}': {fase_inicial.tempo_maximo} segundos")
    print(f"Tempo máximo da '{fase_desafio.nome}': {fase_desafio.tempo_maximo} segundos")

    #Altera o tempo máximo global usando o método de classe.
    print("\nAlterando o tempo máximo global para 90 segundos:")
    Fase.definir_tempo_maximo_global(90) # Isso muda Fase.tempo_maximo

    print(f"Novo tempo máximo global: {Fase.tempo_maximo} segundos")

    #Cria uma nova instância de Fase. Ela pegará o novo tempo máximo global.
    print("\nCriando uma nova fase após a alteração do tempo máximo global:")
    fase_nova = Fase("Caverna Congelada", "Um ambiente hostil e escorregadio.")
    fase_nova.iniciar_fase() # Esta fase será iniciada com o novo tempo máximo global

    #instâncias antigas também veem a mudança se acessarem o atributo classe.
    print("\nIniciando fases antigas para ver o tempo máximo global atualizado:")
    fase_inicial.iniciar_fase()
    fase_desafio.iniciar_fase()

    #define um tempo máximo inválido
    print("\nTentando alterar o tempo máximo global para um valor inválido (0):")
    Fase.definir_tempo_maximo_global(0)
    print(f"Tempo máximo global permanece: {Fase.tempo_maximo} segundos")

    print("\nTeste de q61.py concluído!")
