# Arquivo capitulo_2/q59.py (ou capitulo_3/q59.py, dependendo da sua estrutura).

import random # Necessário para gerar um valor aleatório para o dano

class Personagem:
    """
    Representa um personagem básico no jogo.
    Inclui um método estático para calcular dano base (Q59).
    """
    def __init__(self, nome, vida=100, defesa=50):
        """
        Inicializa um novo personagem.
        :param nome: O nome do personagem.
        :param vida: A vida inicial do personagem.
        :param defesa: A defesa inicial do personagem.
        """
        self.nome = nome
        self.vida = vida
        self.defesa = defesa
        print(f"Personagem '{self.nome}' criado.")

    def tomar_dano(self, dano):
        """
        Reduz a vida do personagem pelo valor do dano.
        (Simplificado para esta questão).
        :param dano: A quantidade de dano a ser aplicada.
        """
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}.")

    @staticmethod # Q59: Decorador que indica que este é um método estático.
    def calcular_dano_base(forca):
        """
        Calcula o dano base de um ataque usando a força fornecida.
        Este método não precisa de acesso a nenhum atributo da instância (self)
        nem da classe (cls), operando apenas com os parâmetros que recebe.
        :param forca: A força do atacante.
        :return: O dano base calculado.
        """
        #Exemplo simples
        dano = forca + random.randint(1, 5)
        print(f"Método estático: Calculando dano base para força {forca} -> Dano: {dano}")
        return dano

#Exemplo de Uso
if __name__ == "__main__":
    print("--- Questão 59: Método Estático calcular_dano_base() ---")

    #Chamando o método estático diretamente na CLASSE Personagem.
    #Não é necessário criar uma instância de Personagem para usar este método.
    print("\nChamando Personagem.calcular_dano_base(10):")
    dano_ataque_leve = Personagem.calcular_dano_base(10)
    print(f"Dano para um ataque leve: {dano_ataque_leve}")

    print("\nChamando Personagem.calcular_dano_base(50):")
    dano_ataque_forte = Personagem.calcular_dano_base(50)
    print(f"Dano para um ataque forte: {dano_ataque_forte}")

    #Podemos até criar uma instância, mas o método estático ainda é chamado da mesma forma.
    print("\nCriando uma instância de Personagem e chamando o método estático através dela (não recomendado):")
    guerreiro = Personagem("Conan", vida=150, defesa=40)
    #chamar métodos estáticos diretamente na classe.
    dano_guerreiro = guerreiro.calcular_dano_base(guerreiro.vida // 10)
    print(f"Dano calculado para Conan: {dano_guerreiro}")

    print("\nTeste de q59.py concluído!")
