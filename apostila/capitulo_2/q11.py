# Arquivo capitulo_2\q11.py

import random # Necessário para gerar dano aleatório
import time   # Adicionado para pausas na simulação de combate

# Classe Personagem (consolidada das Questões 6, 8 e atualizada para a Questão 11)
class Personagem:
    """
    Representa um personagem no jogo com nome e vida.
    Capaz de dizer o nome, tomar dano e atacar.
    """
    def __init__(self, nome, vida=100): # Q22 (antecipado): Construtor com nome e vida
        self.nome = nome
        self.vida = vida  # Vida inicializada em 100

    def dizer_nome(self): # Q6
        """
        Imprime o nome do personagem.
        """
        print(f"Meu nome é {self.nome}.")

    def tomar_dano(self, dano): # Q8
        """
        Reduz a vida do personagem pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Game Over!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0 # Garante que a vida não seja negativa
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

    def atacar(self, alvo): # Q11
        """
        Ataca um alvo (Personagem ou Inimigo), causando dano aleatório entre 5 e 20.
        :param alvo: O objeto Personagem ou Inimigo a ser atacado.
        """
        dano = random.randint(5, 20) # Dano aleatório entre 5 e 20
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
        alvo.tomar_dano(dano) # Chama o método tomar_dano do alvo

# Classe Inimigo (consolidada das Questões 3, 10 e atualizada para a Questão 11)
class Inimigo:
    """
    Representa um inimigo no jogo com nome e vida.
    Capaz de atacar um Personagem ou outro Inimigo.
    """
    def __init__(self, nome, vida=100): # Q23 (antecipado): Construtor com nome e vida
        self.nome = nome
        self.vida = vida  # Vida inicializada em 100

    def tomar_dano(self, dano): # Reutilizado de Personagem para Inimigo também
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

    def atacar(self, alvo): # Q11 (dano aleatório)
        """
        Ataca um alvo (Personagem ou Inimigo), causando dano aleatório entre 5 e 20.
        :param alvo: O objeto Personagem ou Inimigo a ser atacado.
        """
        dano = random.randint(5, 20) # Dano aleatório entre 5 e 20
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
        alvo.tomar_dano(dano) # Chama o método tomar_dano do alvo

# --- Simulação de Combate (Questão 11) ---
if __name__ == "__main__":
    print("--- Simulação de Combate entre Personagem e Inimigo (Questão 11) ---")

    personagem_combate = Personagem("Cavaleiro")
    inimigo_combate = Inimigo("Dragão")

    print(f"Início da Batalha: {personagem_combate.nome} (Vida: {personagem_combate.vida}) vs {inimigo_combate.nome} (Vida: {inimigo_combate.vida})")
    print("-" * 30)

    turno = 1
    while personagem_combate.vida > 0 and inimigo_combate.vida > 0:
        print(f"\n--- Turno {turno} ---")
        # Personagem ataca primeiro
        if personagem_combate.vida > 0: # Verifica se o personagem ainda está vivo para atacar
            personagem_combate.atacar(inimigo_combate)
            if inimigo_combate.vida <= 0:
                print(f"{inimigo_combate.nome} foi derrotado!")
                break # Sai do loop se o inimigo for derrotado

        time.sleep(0.5) # Pausa para melhor visualização da simulação

        # Inimigo ataca em seguida
        if inimigo_combate.vida > 0: # Verifica se o inimigo ainda está vivo para atacar
            inimigo_combate.atacar(personagem_combate)
            if personagem_combate.vida <= 0:
                print(f"{personagem_combate.nome} foi derrotado!")
                break # Sai do loop se o personagem for derrotado

        time.sleep(0.5) # Pausa para melhor visualização da simulação
        turno += 1

    print("-" * 30)
    if personagem_combate.vida > 0:
        print(f"Vitória! {personagem_combate.nome} venceu a batalha com {personagem_combate.vida} de vida restante.")
    else:
        print(f"Derrota! {inimigo_combate.nome} venceu a batalha com {inimigo_combate.vida} de vida restante.")

    print("Teste de q11.py concluído!")
