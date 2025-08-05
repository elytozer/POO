# Arquivo capitulo_2/q49.py
# Solução para a Questão 49: Composição entre Fase e Inimigos.

# Classe Inimigo (componente da composição)
class Inimigo:
    """
    Representa um inimigo que é um componente de uma fase.
    """
    def __init__(self, nome, vida=100):
        """
        Inicializa um novo inimigo.
        :param nome: O nome do inimigo.
        :param vida: A vida inicial do inimigo.
        """
        self.nome = nome
        self.vida = vida
        print(f"Inimigo '{self.nome}' foi CRIADO.")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Inimigo é destruído.
        Demonstra que o Inimigo é destruído junto com a Fase que o compõe.
        """
        print(f"Inimigo '{self.nome}' foi DESTRUÍDO.")

class Fase:
    """
    Representa uma fase do jogo que COMPÕE um conjunto de Inimigos.
    Isso significa que os Inimigos são partes integrais da Fase e seus ciclos de vida
    estão diretamente ligados ao ciclo de vida da Fase.
    """
    def __init__(self, nome, descricao, num_inimigos=3):
        """
        Inicializa uma nova fase.
        :param nome: O nome da fase.
        :param descricao: Uma breve descrição da fase.
        :param num_inimigos: O número de inimigos a serem criados para esta fase.
        """
        self.nome = nome
        self.descricao = descricao
        self.inimigos_da_fase = [] # Q49: Composição - Inimigos são criados e destruídos com a fase
        self._gerar_inimigos(num_inimigos) # Cria os inimigos na inicialização da fase
        print(f"Fase '{self.nome}' foi CRIADA.")

    def _gerar_inimigos(self, quantidade):
        """
        Cria e adiciona inimigos à lista de inimigos da fase.
        Estes inimigos são compostos pela fase.
        :param quantidade: O número de inimigos a serem gerados.
        """
        print(f"Gerando {quantidade} inimigos para a fase {self.nome}...")
        for i in range(quantidade):
            # O objeto Inimigo é criado DENTRO da Fase
            self.inimigos_da_fase.append(Inimigo(f"Inimigo da {self.nome} {i+1}"))
        print(f"Inimigos gerados: {[inimigo.nome for inimigo in self.inimigos_da_fase]}")

    def entrar(self):
        """
        Imprime uma mensagem ao entrar na fase e lista os inimigos presentes.
        """
        print(f"Você entrou na {self.nome}: {self.descricao}")
        print(f"Inimigos presentes: {[inimigo.nome for inimigo in self.inimigos_da_fase]}")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Fase é destruído.
        Quando a Fase é destruída, os Inimigos que ela compõe também são automaticamente destruídos,
        pois não há outras referências a eles fora do objeto Fase.
        """
        print(f"Fase '{self.nome}' foi DESTRUÍDA.")
        # Não é necessário chamar 'del inimigo' explicitamente para cada inimigo,
        # pois o coletor de lixo do Python cuidará disso quando as referências
        # na lista 'self.inimigos_da_fase' forem removidas (quando o objeto Fase for destruído).

# --- Exemplo de Uso (Questão 49) ---
if __name__ == "__main__":
    print("--- Questão 49: Composição entre Fase e Inimigos ---")

    # Cria uma instância de Fase. Isso automaticamente cria instâncias de Inimigo.
    fase_caverna = Fase("Caverna Sombria", "Uma caverna escura e úmida.", num_inimigos=2)

    print("\nEntrando na fase:")
    fase_caverna.entrar()

    print("\nDeletando a fase (observe que os inimigos também serão destruídos):")
    # Força a destruição do objeto 'fase_caverna'.
    # Isso acionará o __del__ de Fase, e consequentemente, o __del__ de cada Inimigo composto.
    del fase_caverna

    print("\nTeste de q49.py concluído!")
    # Após a execução, você verá as mensagens de criação e destruição,
    # demonstrando o ciclo de vida acoplado na composição.
