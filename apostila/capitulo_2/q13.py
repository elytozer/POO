# Arquivo capitulo_2\q13.py

import random # Necessário para selecionar inimigos aleatoriamente
import time   # Para simulação de pausas

# Classe Menu (consolidada das Questões 5 e atualizada para a Questão 13)
class Menu:
    """
    Representa um menu com opções de iniciar jogo, mostrar opções e sair.
    """
    def __init__(self, titulo="Menu Principal"): # Q25 (antecipado): Construtor com título
        self.titulo = titulo

    def iniciar_jogo(self): # Q5
        """
        Imprime uma mensagem para iniciar o jogo.
        """
        print("Iniciando o jogo...")

    def mostrar_opcoes(self): # Q5, Q13
        """
        Imprime as opções disponíveis no menu.
        """
        print(f"\n--- {self.titulo} ---")
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")

    def sair(self): # Q5
        """
        Imprime uma mensagem de saída do jogo.
        """
        print("Saindo do jogo. Até a próxima!")

# Classe Inimigo (consolidada das Questões 3, 10, 11 e 12)
class Inimigo:
    """
    Representa um inimigo no jogo com nome e vida.
    Capaz de atacar um Jogador.
    """
    def __init__(self, nome, vida=100):
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

    def atacar(self, alvo):
        """
        Ataca um alvo (Jogador), causando dano aleatório entre 5 e 20.
        :param alvo: O objeto Jogador a ser atacado.
        """
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano.")
        alvo.tomar_dano(dano)

# Classe Jogador (consolidada das Questões 9 e 12)
class Jogador:
    """
    Representa um jogador com atributos nome, energia e pontos.
    Capaz de recuperar e usar energia, adicionar pontos, e atacar inimigos.
    """
    def __init__(self, nome, energia=50, pontos=0):
        self.nome = nome
        self.energia = energia
        self.pontuacao = 0 # Simplificado para int para esta questão
        self.vida = 100

    def tomar_dano(self, dano):
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

    def recuperar_energia(self, quantidade):
        """
        Aumenta a energia do jogador pela quantidade especificada.
        A energia não pode exceder 100.
        :param quantidade: A quantidade de energia a ser recuperada.
        """
        self.energia += quantidade
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nome} recuperou {quantidade} de energia. Energia atual: {self.energia}")

    def usar_energia(self, quantidade):
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

    def atacar(self, inimigo):
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
            self.pontuacao += 10 # Ganha 10 pontos ao derrotar inimigo
            print(f"{self.nome} derrotou {inimigo.nome} e ganhou 10 pontos!")
        return True

    def descansar(self):
        """
        Recupera 20 de energia para o jogador, não excedendo 100.
        """
        self.recuperar_energia(20)
        print(f"{self.nome} descansou e recuperou energia.")


# --- Sistema de Menu Interativo (Questão 13) ---
if __name__ == "__main__":
    print("--- Questão 13: Criando um Sistema de Menu Interativo ---")

    menu_principal = Menu("Menu do Jogo de Aventura")
    jogador_principal = Jogador("Herói Lendário", energia=100)

    while True:
        menu_principal.mostrar_opcoes()
        escolha = input("Escolha uma opção (1, 2 ou 3): ")

        if escolha == '1':
            menu_principal.iniciar_jogo()
            print(f"Vida do {jogador_principal.nome}: {jogador_principal.vida}, Energia: {jogador_principal.energia}")

            num_inimigos = random.randint(1, 3)
            print(f"\nVocê enfrentará {num_inimigos} inimigo(s)!")

            inimigos_derrotados = 0
            for i in range(num_inimigos):
                inimigo_partida = Inimigo(f"Monstro da Partida {i+1}", vida=random.randint(50, 100))
                print(f"\n--- Enfrentando {inimigo_partida.nome} (Vida: {inimigo_partida.vida}) ---")

                while inimigo_partida.vida > 0 and jogador_principal.vida > 0:
                    if not jogador_principal.atacar(inimigo_partida):
                        print("Herói está exausto e precisa descansar!")
                        jogador_principal.descansar()
                        time.sleep(1)
                        # Se ainda não tiver energia suficiente após descansar, sai do loop de combate
                        if not jogador_principal.usar_energia(10):
                            print(f"{jogador_principal.nome} está exausto e não pode continuar o combate.")
                            break
                        else:
                            jogador_principal.energia += 10 # Reverte o custo da verificação
                            continue # Tenta atacar novamente

                    if inimigo_partida.vida > 0:
                        inimigo_partida.atacar(jogador_principal)
                    time.sleep(0.5)

                if jogador_principal.vida <= 0:
                    print("\nVocê foi derrotado na partida! Game Over!")
                    break # Sai do loop de inimigos se o jogador for derrotado
                elif inimigo_partida.vida <= 0:
                    inimigos_derrotados += 1
                    print(f"Vida restante do {jogador_principal.nome}: {jogador_principal.vida}, Energia: {jogador_principal.energia}")

            if jogador_principal.vida > 0 and inimigos_derrotados == num_inimigos:
                print("\nPARABÉNS! Você venceu todos os inimigos da partida!")
                print(f"Sua pontuação total: {jogador_principal.pontuacao}")
            elif jogador_principal.vida <= 0:
                print(f"Pontuação final: {jogador_principal.pontuacao}")

        elif escolha == '2':
            print("\nOpções do Jogo:")
            print("- Dificuldade: Normal")
            print("- Som: Ligado")
            print("- Controles: Padrão")
            input("Pressione Enter para voltar ao menu...") # Pausa para o usuário ler

        elif escolha == '3':
            menu_principal.sair()
            break # Sai do loop principal do menu

        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
        time.sleep(1)

    print("\nTeste de q13.py concluído!")
