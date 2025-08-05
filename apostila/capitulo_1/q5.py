# Arquivo capitulo_1\q5.py

class Menu:
    """
    Representa um menu com opções de iniciar jogo, mostrar opções e sair.
    """
    def iniciar_jogo(self):
        """
        Imprime uma mensagem para iniciar o jogo.
        """
        print("Iniciando o jogo...")

    def mostrar_opcoes(self):
        """
        Imprime as opções disponíveis no menu.
        """
        print("Opções do Menu: Som, Controles, Dificuldade.")

    def sair(self):
        """
        Imprime uma mensagem de saída do jogo.
        """
        print("Saindo do jogo. Até a próxima!")

#Instancia a classe Menu e testa seus métodos
if __name__ == "__main__":
    menu_principal = Menu()
    menu_principal.iniciar_jogo()
    menu_principal.mostrar_opcoes()
    menu_principal.sair()

