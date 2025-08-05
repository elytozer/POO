# Arquivo capitulo_2\q12.py

import random 
import time

# Classe Pontuacao (consolidada das Questões 4, 7 e atualizada para a Questão 12)
class Pontuacao:
    """
    Representa a pontuação do jogo com métodos para zerar, adicionar e mostrar pontos.
    """
    def __init__(self, pontos=0): # Q7
        self.pontos = pontos

    def zerar_pontos(self): # Q4
        """
        Zera a pontuação.
        """
        self.pontos = 0
        print("Pontuação zerada!")

    def adicionar_pontos(self, quantidade): # Q7
        """
        Adiciona uma quantidade específica de pontos à pontuação total.
        :param quantidade: O número de pontos a ser adicionado.
        """
        self.pontos += quantidade
        print(f"Adicionados {quantidade} pontos. Pontuação atual: {self.pontos}")

    def mostrar_pontos(self): # Q7
        """
        Imprime a pontuação atual.
        """
        print(f"Pontuação atual: {self.pontos}")

# Classe Inimigo (consolidada das Questões 3, 10, 11 e atualizada para a Questão 12)
class Inimigo:
    """
    Representa um inimigo no jogo com nome e vida.
    Capaz de atacar um Jogador.
    """
    def __init__(self, nome, vida=100): # Q10
        self.nome = nome
        self.vida = vida

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

    def atacar(self, alvo): # Q11 (dano aleatório)
        """
        Ataca um alvo (Jogador), causando dano aleatório entre 5 e 20.
        :param alvo: O objeto Jogador a ser atacado.
        """
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
        alvo.tomar_dano(dano) # Assumindo que Jogador tem tomar_dano

# Classe Jogador (consolidada das Questões 9 e atualizada para a Questão 12)
class Jogador:
    """
    Representa um jogador com atributos nome, energia e pontos.
    Capaz de recuperar e usar energia, adicionar pontos, e atacar inimigos.
    """
    def __init__(self, nome, energia=50, pontos=0): # Q9, Q24 (antecipado)
        self.nome = nome
        self.energia = energia
        self.pontuacao = Pontuacao(pontos) # Q12: Usa a classe Pontuacao
        self.vida = 100 # Adicionado para que o inimigo possa atacar o jogador

    def tomar_dano(self, dano): # Necessário para ser atacado por Inimigo
        """
        Reduz a vida do jogador pelo valor do dano.
        Se a vida chegar a 0 ou menos, imprime "Game Over!".
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}. Game Over!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

    def recuperar_energia(self, quantidade): # Q9
        """
        Aumenta a energia do jogador pela quantidade especificada.
        A energia não pode exceder 100.
        :param quantidade: A quantidade de energia a ser recuperada.
        """
        self.energia += quantidade
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nome} recuperou {quantidade} de energia. Energia atual: {self.energia}")

    def usar_energia(self, quantidade): # Q9
        """
        Reduz a energia do jogador pela quantidade especificada.
        Se não houver energia suficiente, imprime uma mensagem de aviso.
        :param quantidade: A quantidade de energia a ser usada.
        :return: True se a energia foi usada com sucesso, False caso contrário.
        """
        if self.energia >= quantidade:
            self.energia -= quantidade
            print(f"{self.nome} usou {quantidade} de energia. Energia restante: {self.energia}")
            return True
        else:
            print(f"{self.nome} sem energia suficiente para esta ação! Energia atual: {self.energia}")
            return False

    def atacar(self, inimigo): # Q12
        """
        O jogador ataca um inimigo, reduzindo sua vida. Perde 10 de energia por ataque.
        :param inimigo: O objeto Inimigo a ser atacado.
        """
        if not self.usar_energia(10): # Custo de energia por ataque
            return False # Não pode atacar sem energia

        dano = random.randint(10, 25) # Dano base do jogador
        print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano.")
        inimigo.tomar_dano(dano)

        if inimigo.vida <= 0:
            self.pontuacao.adicionar_pontos(10) # Q12: Ganha 10 pontos ao derrotar inimigo
            print(f"{self.nome} derrotou {inimigo.nome} e ganhou 10 pontos!")
        return True

    def descansar(self): # Q12
        """
        Recupera 20 de energia para o jogador, não excedendo 100.
        """
        self.recuperar_energia(20)
        print(f"{self.nome} descansou e recuperou energia.")

# --- Exemplo de Uso (Questão 12) ---
if __name__ == "__main__":
    print("--- Questão 12: Sistema de Pontuação e Energia no Jogo ---")

    jogador_q12 = Jogador("Aventureiro Corajoso", energia=100, pontos=0)
    inimigo_fraco = Inimigo("Goblin", vida=30)
    inimigo_medio = Inimigo("Orc", vida=70)

    print(f"\nEstado inicial de {jogador_q12.nome}:")
    print(f"Vida: {jogador_q12.vida}, Energia: {jogador_q12.energia}, Pontos: {jogador_q12.pontuacao.pontos}")
    print("-" * 30)

    print(f"\n{jogador_q12.nome} enfrenta {inimigo_fraco.nome} (Vida: {inimigo_fraco.vida})")
    while inimigo_fraco.vida > 0 and jogador_q12.vida > 0:
        if not jogador_q12.atacar(inimigo_fraco):
            print(f"{jogador_q12.nome} precisa descansar antes de atacar novamente!")
            jogador_q12.descansar()
            time.sleep(1)
            # Se ainda não tiver energia suficiente após descansar, sai do loop
            if not jogador_q12.usar_energia(10): # Tenta usar energia para verificar
                print(f"{jogador_q12.nome} está exausto e não pode continuar o combate.")
                break
            else:
                # Se recuperou e pode atacar, remove o custo de energia da verificação
                jogador_q12.energia += 10 # Reverte o custo da verificação
                continue # Tenta atacar novamente

        if inimigo_fraco.vida > 0:
            inimigo_fraco.atacar(jogador_q12)
        time.sleep(0.5)

    if jogador_q12.vida <= 0:
        print(f"\n{jogador_q12.nome} foi derrotado! Fim de jogo.")
    elif inimigo_fraco.vida <= 0:
        print(f"\n{inimigo_fraco.nome} foi derrotado! {jogador_q12.nome} tem {jogador_q12.vida} de vida e {jogador_q12.energia} de energia.")
        jogador_q12.pontuacao.mostrar_pontos()

    print("-" * 30)
    print(f"\n{jogador_q12.nome} agora enfrenta {inimigo_medio.nome} (Vida: {inimigo_medio.vida})")
    while inimigo_medio.vida > 0 and jogador_q12.vida > 0:
        if not jogador_q12.atacar(inimigo_medio):
            print(f"{jogador_q12.nome} precisa descansar antes de atacar novamente!")
            jogador_q12.descansar()
            time.sleep(1)
            if not jogador_q12.usar_energia(10):
                print(f"{jogador_q12.nome} está exausto e não pode continuar o combate.")
                break
            else:
                jogador_q12.energia += 10
                continue

        if inimigo_medio.vida > 0:
            inimigo_medio.atacar(jogador_q12)
        time.sleep(0.5)

    if jogador_q12.vida <= 0:
        print(f"\n{jogador_q12.nome} foi derrotado! Fim de jogo.")
    elif inimigo_medio.vida <= 0:
        print(f"\n{inimigo_medio.nome} foi derrotado! {jogador_q12.nome} tem {jogador_q12.vida} de vida e {jogador_q12.energia} de energia.")
        jogador_q12.pontuacao.mostrar_pontos()

    print("\nTeste de q12.py concluído!")
