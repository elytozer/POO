# Arquivo capitulo_2/q58.py (ou capitulo_3/q58.py, dependendo da sua estrutura)

class Jogo:
    """
    Representa um jogo.
    Inclui um atributo de classe para a dificuldade global (Q58),
    que pode ser acessado e alterado por todas as instâncias da classe.
    """
    # Q58: Atributo de classe para a dificuldade global.
    # Este atributo pertence à classe Jogo, não a instâncias individuais.
    dificuldade_global = 1 # Valor padrão da dificuldade global (1: Fácil, 2: Normal, 3: Difícil)

    def __init__(self, titulo="Meu Jogo"):
        """
        Inicializa um novo jogo.
        :param titulo: O título do jogo.
        """
        self.titulo = titulo
        #A instância pode usar a dificuldade global no momento de sua criação,
        #ou pode ter sua própria dificuldade de instância se for necessário.
        #Para esta questão, vamos mostrar como ela acessa a global.
        self.dificuldade_instancia_no_momento_da_criacao = Jogo.dificuldade_global
        print(f"Jogo '{self.titulo}' criado. Dificuldade de instância (no momento da criação): {self.dificuldade_instancia_no_momento_da_criacao}")

    def iniciar(self):
        """
        Inicia o jogo, exibindo a dificuldade global atual.
        """
        print(f"O jogo '{self.titulo}' começou com dificuldade GLOBAL: {Jogo.dificuldade_global}!")

    @classmethod #método de classe para alterar o atributo de classe de forma controlada.
    def alterar_dificuldade_global(cls, nova_dificuldade):
        """
        Altera a dificuldade global do jogo.
        Este método de classe afeta o atributo 'dificuldade_global' da classe Jogo.
        :param nova_dificuldade: O novo valor para a dificuldade global (deve ser entre 1 e 3).
        """
        if 1 <= nova_dificuldade <= 3:
            cls.dificuldade_global = nova_dificuldade
            print(f"Dificuldade global do jogo alterada para: {cls.dificuldade_global}")
        else:
            print(f"Valor inválido para dificuldade global: {nova_dificuldade}. A dificuldade deve ser entre 1 e 3.")

#Exemplo de Uso
if __name__ == "__main__":
    print("--- Questão 58: Dificuldade Global do Jogo ---")

    #Criação de instâncias de Jogo. Elas refletem a dificuldade global inicial.
    print("\nCriando jogos com a dificuldade global padrão (1):")
    jogo_aventura = Jogo("Aventura Mágica")
    jogo_rpg = Jogo("RPG Épico")

    print(f"\nDificuldade global atual (acesso direto à classe): {Jogo.dificuldade_global}")
    print(f"Dificuldade de instância de '{jogo_aventura.titulo}': {jogo_aventura.dificuldade_instancia_no_momento_da_criacao}")
    print(f"Dificuldade de instância de '{jogo_rpg.titulo}': {jogo_rpg.dificuldade_instancia_no_momento_da_criacao}")

    #Alterando a dificuldade global usando o método de classe.
    print("\nAlterando a dificuldade global para 3 (Difícil):")
    Jogo.alterar_dificuldade_global(3) # Isso muda Jogo.dificuldade_global

    print(f"Nova dificuldade global: {Jogo.dificuldade_global}")

    #Criando uma nova instância de Jogo. Ela pegará a nova dificuldade global.
    print("\nCriando um novo jogo após a alteração da dificuldade global:")
    jogo_novo = Jogo("Jogo Rápido")
    jogo_novo.iniciar() # Este jogo será iniciado com a nova dificuldade global

    #As instâncias antigas também veem a mudança se acessarem o atributo de classe.
    print("\nIniciando jogos antigos para ver a dificuldade global atualizada:")
    jogo_aventura.iniciar()
    jogo_rpg.iniciar()

    #Tentando definir uma dificuldade inválida
    print("\nTentando alterar a dificuldade global para um valor inválido (5):")
    Jogo.alterar_dificuldade_global(5)
    print(f"Dificuldade global permanece: {Jogo.dificuldade_global}")

    print("\nTeste de q58.py concluído!")
