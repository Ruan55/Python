import os
os.system('cls || clear')

numeros = []
par = 0
impar = 0

for i in range(6):

    numero = int(input(f'Digite o {i+1}º numero: '))
    numeros.append(numero)

    if numeros[i] % 2 == 0:
        par += 1
    if numeros[i] % 2 == 1:
        impar += 1

print(f'Quantidade de pares: {par}')
print(f'Quantiade de impares: {impar}')