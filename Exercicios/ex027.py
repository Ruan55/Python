import os
os.system('cls || clear')

numeros = []
maiorNumero = 0
menorNumero = 5000

for i in range(5):

    numero = int(input(f'Digite o {i + 1}º numero: '))
    numeros.append(numero)

    maiorNumero = max(maiorNumero, numeros[i])
    menorNumero = min(menorNumero, numeros[i])

for i in range(5):

    print(f'{i + 1}º numero: {numeros[i]}')

print(f'Maior numero: {maiorNumero}')
print(f'Menor numero: {menorNumero}')
