# Atividade Avaliativa da Semana 7 de Algoritmos e Programação de Computadores I

# Primeira tentativa -> Nota: 8.0

# Questão 1
matriz = []
for i in range(3):
    vetor =[]
    for j in range(3):
        vetor.append(j) # "append()" adiciona itens no final da lista "vetor"
    matriz.append(vetor)
print(matriz)

# %% Questão 2
def potencia(base, expoente):
    resultado = 1
    for numero in range(1, expoente + 1):
        resultado = resultado * base
    return resultado

numero = eval(input("Entre um número que quer calcular (base): "))
expoente = eval(input("Informe o expoente: "))
print('Potência: ',potencia(numero, expoente))

# %% Segunda tentativa (para prática) -> Nota: 8.0

# Questão 1 - Exemplo:

""" 
aluno1Notas = [7.5, 7.0, 8.7]
aluno2Notas = [8.0, 5.0, 9.0]

def calcula_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
        media = soma / len(aluno)
        return media

media = calcula_media(aluno1Notas)
print("A média do aluno 1 é: {:.2f}".format(media))

media = calcula_media(aluno2Notas)
print("A média do aluno 2 é: {:.2f}".format(media))
"""

# Alternativa E:
alunosNotas = [[7.5,7.0,8.7],[8.0,5.0,9.0]]

def calcula_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
        media = soma / len(aluno)
        return media

media = calcula_media(alunosNotas[0])
print("A média do aluno 1 é: {:.2f}".format(media))

media = calcula_media(alunosNotas[1])
print("A média do aluno 2 é: {:.2f}".format(media))

# %% Questão 5:

matrizNumeros=[[1,2,3,4],
               [1,3,5,7],
               [8,6,4,2],
               [7,5,3,1]]

for i in range(len(matrizNumeros)):
    for j in range(len(matrizNumeros[i])):
        print(matrizNumeros[i][j],end=" ")
