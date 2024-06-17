import os

# Declarando as variáveis
qntdPares = 0
qntdImpares = 0
qntdPositivos = 0
qntdNegativos = 0
qntdGeral = 0
somaPar = 0
somaImpar = 0
somaGeral = 0
maiorNum = 0
menorNum = 5000
mediaPar = 0
mediaImpar = 0
mediaGeral = 0
numeros_invertidos = 0
numeros = []

# Contando os 5 numeros inseridos pelo usuario
for i in range(5):
    
    # Solicitando para o usuario inserir 5 numeros
    numero = int(input(f'Digite o {i+1}º numero: '))
    numeros.append(numero)

    # Verificando a quantidade de numeros pares
    if numero % 2 == 0:
        qntdPares += 1
        somaPar += numero
    # Verificando a quantidade de numeros impares
    if numero % 2 == 1:
        qntdImpares += 1
        somaImpar += numero
    
    # Verificando a quantidade de numeros positivos
    if numero > 0:
        qntdPositivos += 1
    # Verificando a quantidade de numeros negativos
    if numero < 0:
        qntdNegativos += 1

    # Verificando qual é o maior e o menor numero
    if numero > maiorNum:
        maiorNum = numero
    if numero < menorNum:
        menorNum = numero

    # Verificando a quantidade de numeros que o usuario inseriu
    qntdGeral += 1
    somaGeral += numero

# Calculando as médias
mediaPar = somaPar / qntdPares
mediaImpar = somaImpar / qntdImpares
mediaGeral = somaGeral / qntdGeral

# Invertendo a ordem dos numeros
numeros_invertidos = numeros[::-1]

# Imprimindo os resultados no terminal
os.system('cls || clear')
print(f'Quantidade de pares: {qntdPares}')
print(f'Quantidade de impares: {qntdImpares}')
print(f'Quantidade de positivos: {qntdPositivos}')
print(f'Quantidade de negativos: {qntdNegativos}')
print(f'Quantidadde de numeros inseridos: {qntdGeral}')
print(f'Maior numero: {maiorNum}')
print(f'Menor numero: {menorNum}')
print(f'Media pares: {mediaPar:.2f}')
print(f'Media impares: {mediaImpar:.2f}')
print(f'Media geral: {mediaGeral:.2f}')
print(numeros_invertidos)