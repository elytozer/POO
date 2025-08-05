# Arquivo: operacoes.py
# Módulo para a Questão 62, contendo funções básicas de matemática.

def somar(a, b):
    print(f"Somando {a} + {b}...")
    return a + b

def multiplicar(a, b):
    print(f"Multiplicando {a} * {b}...")
    return a * b

# Exemplo de uso interno
if __name__ == "__main__":
    print("Testando funções de operacoes.py:")
    print(f"2 + 3 = {somar(2, 3)}")
    print(f"4 * 5 = {multiplicar(4, 5)}")
