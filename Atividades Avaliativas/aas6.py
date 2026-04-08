# Primeira tentativa da Atividade Avaliativa da Semana 6 de Algoritmos e Programação de Computadores I

# Questão 2
for x in range(10):
    print(x)

# %% Questão 4 - Teste 1: Criando o menu de comando usando while
i = 0
while i <= 4:
     i += 1
     if i == 1:
        print(i,' Cadastrar produtos.', sep=".")
     if i == 2:
         print(i,' Consultar produtos.', sep=".")
     if i == 3:
         print(i,' Alterar produtos.', sep=".")
     if i == 4:
         print(i,' Excluir produtos.', sep=".")
     if i == 5:
         print(i,' Sair do programa.', sep=".")

# %% Questão 4 - Teste 2: criando um menu utilizando while True
i = 0
while True:
     i += 1
     if i == 1:
        print(i,' Cadastrar produtos.', sep=".")
     if i == 2:
         print(i,' Consultar produtos.', sep=".")
     if i == 3:
         print(i,' Alterar produtos.', sep=".")
     if i == 4:
         print(i,' Excluir produtos.', sep=".")
     if i == 5:
         print(i,' Sair do programa.', sep=".")

# %% Questão 4 - Teste 3: Opção de solução "while operacao != 5"
operacao = 0
while operacao != 5:
     operacao += 1
     if operacao == 1:
        print(operacao,' Cadastrar produtos.', sep=".")
     if operacao == 2:
         print(operacao,' Consultar produtos.', sep=".")
     if operacao == 3:
         print(operacao,' Alterar produtos.', sep=".")
     if operacao == 4:
         print(operacao,' Excluir produtos.', sep=".")
     if operacao == 5:
         print(operacao,' Sair do programa.', sep=".")

# %% Questão 4 - Teste 4: O modelo de loop mais indicado é o laço "for"
operacao = 0
for operacao in range(5):
    operacao += 1
    if operacao == 1:
        print(operacao, ' Cadastrar produtos.', sep=".")
    if operacao == 2:
        print(operacao, ' Consultar produtos.', sep=".")
    if operacao == 3:
        print(operacao, ' Alterar produtos.', sep=".")
    if operacao == 4:
        print(operacao, ' Excluir produtos.', sep=".")
    if operacao == 5:
        print(operacao, ' Sair do programa.', sep=".")

# %% Questão 6

while True:
    n1 = eval(input('Digite o primeiro número:'))
    n2 = eval(input('Digite o segundo número:'))
    operacao = eval(input('Opções: \n\n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Sair \n\n'))

    if operacao == 1:
        resultado = n1 + n2 # soma(n1,n2)
        print('O resultado é', resultado)
    if operacao == 2:
        resultado = n1 - n2 # subtracao(n1,n2)
        print('O resultado é', resultado)
    if operacao == 3:
        resultado = n1 * n2 #multiplicacao(n1,n2)
        print('O resultado é', resultado)
    if operacao == 4:
        resultado = n1 / n2 #divisao(n1,n2)
        print('O resultado é', resultado)
    if operacao == 5:
        print("Fim!") # Adição minha.
        break

