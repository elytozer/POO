# Arquivo capitulo_2/q55.py
# Solução para a Questão 55: Composição onde a classe SistemaCombate gerencia um Personagem e um Inimigo.

import random # Necessário para gerar dano aleatório
import time   # Necessário para pausas na simulação

# Classe Personagem (componente da composição)
# Esta classe representa um combatente que será gerenciado pelo SistemaCombate.
class Personagem:
    """
    Representa um personagem que participa de um combate.
    É um componente da classe SistemaCombate.
    """
    def __init__(self, nome, vida=100):
        """
        Inicializa um novo personagem.
        :param nome: O nome do personagem.
        :param vida: A vida inicial do personagem.
        """
        self.nome = nome
        self.vida = vida
        print(f"Personagem '{self.nome}' foi CRIADO.")

    def tomar_dano(self, dano):
        """
        Reduz a vida do personagem pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Game Over!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

    def atacar(self, alvo):
        """
        Ataca um alvo, causando um dano aleatório.
        :param alvo: O objeto a ser atacado (Inimigo ou outro Personagem).
        """
        dano = random.randint(10, 20) # Dano base do personagem
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
        alvo.tomar_dano(dano)

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Personagem é destruído.
        Demonstra que o Personagem é destruído junto com o SistemaCombate que o compõe.
        """
        print(f"Personagem '{self.nome}' foi DESTRUÍDO.")

# Classe Inimigo (componente da composição)
# Esta classe representa um combatente que será gerenciado pelo SistemaCombate.
class Inimigo:
    """
    Representa um inimigo que participa de um combate.
    É um componente da classe SistemaCombate.
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

    def tomar_dano(self, dano):
        """
        Reduz a vida do inimigo pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Inimigo derrotado!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. {self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

    def atacar(self, alvo):
        """
        Ataca um alvo, causando um dano aleatório.
        :param alvo: O objeto a ser atacado (Personagem ou outro Inimigo).
        """
        dano = random.randint(5, 15) # Dano base do inimigo
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
        alvo.tomar_dano(dano)

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto Inimigo é destruído.
        Demonstra que o Inimigo é destruído junto com o SistemaCombate que o compõe.
        """
        print(f"Inimigo '{self.nome}' foi DESTRUÍDO.")

# Classe SistemaCombate (compondo Personagem e Inimigo)
class SistemaCombate:
    """
    Gerencia um combate entre um Personagem e um Inimigo.
    Utiliza composição: o Personagem e Inimigo são criados e destruídos
    junto com o SistemaCombate, indicando que a batalha termina quando
    o sistema de combate é encerrado.
    """
    def __init__(self, nome_personagem, nome_inimigo):
        """
        Inicializa o sistema de combate, criando e compondo um Personagem e um Inimigo.
        :param nome_personagem: O nome para o Personagem.
        :param nome_inimigo: O nome para o Inimigo.
        """
        # Q55: Composição - Os objetos Personagem e Inimigo são criados DENTRO
        # do construtor de SistemaCombate. Isso significa que eles não podem
        # existir sem o SistemaCombate.
        self.personagem = Personagem(nome_personagem)
        self.inimigo = Inimigo(nome_inimigo)
        print(f"\n--- SISTEMA DE COMBATE CRIADO para {self.personagem.nome} vs {self.inimigo.nome} ---")

    def iniciar_batalha(self):
        """
        Inicia a simulação de batalha, onde o Personagem e o Inimigo
        se atacam alternadamente até que um deles seja derrotado.
        """
        print(f"Início da Batalha: {self.personagem.nome} (Vida: {self.personagem.vida}) vs {self.inimigo.nome} (Vida: {self.inimigo.vida})")
        turno = 1
        while self.personagem.vida > 0 and self.inimigo.vida > 0:
            print(f"\n--- Turno {turno} ---")
            # Personagem ataca primeiro
            if self.personagem.vida > 0:
                self.personagem.atacar(self.inimigo)
                if self.inimigo.vida <= 0:
                    print(f"{self.inimigo.nome} foi derrotado!")
                    break # Sai do loop se o inimigo for derrotado

            time.sleep(0.5) # Pequena pausa para melhor visualização

            # Inimigo ataca em seguida (se ainda estiver vivo)
            if self.inimigo.vida > 0:
                self.inimigo.atacar(self.personagem)
                if self.personagem.vida <= 0:
                    print(f"{self.personagem.nome} foi derrotado!")
                    break # Sai do loop se o personagem for derrotado

            time.sleep(0.5) # Pequena pausa para melhor visualização
            turno += 1

        print("\n--- BATALHA ENCERRADA ---")
        if self.personagem.vida > 0:
            print(f"Vencedor: {self.personagem.nome} com {self.personagem.vida} de vida restante.")
        else:
            print(f"Vencedor: {self.inimigo.nome} com {self.inimigo.vida} de vida restante.")

    def __del__(self):
        """
        Método destrutor, chamado quando o objeto SistemaCombate é destruído.
        Quando o SistemaCombate é destruído, os objetos Personagem e Inimigo
        que ele compõe também são automaticamente destruídos, pois não há
        outras referências a eles fora do objeto SistemaCombate.
        """
        print(f"--- SISTEMA DE COMBATE DESTRUÍDO ---")
        # Não é necessário chamar 'del self.personagem' ou 'del self.inimigo' explicitamente,
        # pois o coletor de lixo do Python cuidará disso quando as referências
        # dentro de SistemaCombate forem removidas (quando o objeto SistemaCombate for destruído).

# --- Exemplo de Uso (Questão 55) ---
if __name__ == "__main__":
    print("--- Questão 55: Composição - SistemaCombate gerencia Personagem e Inimigo ---")

    # 1. Cria uma instância de SistemaCombate.
    # Ao fazer isso, os objetos Personagem e Inimigo são CRIADOS automaticamente
    # como parte do SistemaCombate.
    batalha_epica = SistemaCombate("Herói Corajoso", "Lich Maligno")

    # 2. Inicia a simulação da batalha
    print("\nIniciando a batalha:")
    batalha_epica.iniciar_batalha()

    # 3. Deleta a instância de SistemaCombate.
    # Ao fazer isso, os objetos Personagem e Inimigo que foram compostos por ele
    # também serão DESTRUÍDOS automaticamente.
    print("\nDeletando o sistema de combate (personagem e inimigo também devem ser destruídos):")
    del batalha_epica

    print("\nTeste de q55.py concluído!")
    # Observe as mensagens de criação e destruição para entender o ciclo de vida
    # dos objetos na relação de composição.
