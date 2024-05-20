import os
os.system('cls || clear')

def cabecalho():

    os.system('cls || clear')
    print('='*10)
    print('SENAI')
    print('='*10)

numeros = []

for i in range(5):

    cabecalho()
    numero = int(input(f'Digite o {i+1}º numero: '))
    numeros.append(numero)

    if numeros[i] < 0:
        numeros[i] = 0

cabecalho()
for i in range(5):

    print(f'{i+1}º Numero: {numeros[i]}')