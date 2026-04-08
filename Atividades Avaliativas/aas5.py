# Atividade Avaliativa da Semana 5 de Algoritmos e Programação de Computadores I

# %% Questão 1
print('Você tem que digitar a sua nacionalidade')
nacionalid = input("Coloque b (brasileiro) ou q (caso não seja)")
if (nacionalid == 'q'):
    print('Você não pode votar')
else:
    idade = eval(input("Digite sua idade: "))
    if idade < 16:
        print("Você não é eleitor")
    elif idade >= 18 and idade < 65:
        print("Você é eleitor obrigatório")
    elif (idade >= 16 and idade < 18) or idade > 65:
        print("Você é eleitor facultativo")
    else:
        print("Erro")
print("Obrigada por usar nossos serviços")

# %% Questão 6
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 * 4 + nota2 * 6) / 2 # A divisão deve ser feita pelo total dos pesos

if media >= 5:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"
print("O aluno foi", resultado)

# %% Questão 7
n1 = 7.0
n2 = 8.5
n3 = 3.0
n4 = 5.0

media = (n1 + n2 + n3 + n4) / 4

if media < 3:
    print('Média:', media,'. Situação: Reprovado')
elif media < 7:
    print('Média:', media,'. Situação: Exame')
else:
    print('Média:', media,'. Situação: Aprovado')
