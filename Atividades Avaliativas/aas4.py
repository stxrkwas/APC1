# Atividade Avaliativa da Semana 4 de Algoritmos e Programação de Computadores I

# %% Questão 3
def leNumero():
    numero = eval(input("Digite um número: "))
    print("números lidos")
    return numero

# %% Questão 5
base = eval(input("Digite a base: "))
altura = eval(input("Digite a altura: "))
area = (base * altura) / 2
print("A área é", area)

# %% Questão 6
import math
num = int(input("Digite um numero: "))
quadrado = math.pow(num,2)
cubo = math.pow(num,3)
raiz = math.sqrt(num)
print(f'O número ao quadrado é {quadrado} e ao cubo é {cubo}')
print(f'A raiz quadrada é {raiz:.2f}')

# %% Questão 7 - 1º quadro
def quadrado(x):
    return x * x
print(quadrado(4))   # Retorna o resultado

# %% Questão 7 - 2º quadro
def quadrado(): # Não tem parâmetro
    valor = x * x # Variável x não é reconhecida
    return valor
print(quadrado())

# %% Questão 8
n1 = input("Digite o número 1: ")
n2 = input("Digite o número 2: ")
print('O resultado é', int(n1) + int(n2))
