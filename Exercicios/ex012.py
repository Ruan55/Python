import os
os.system('cls || clear')

soma = 0

for i in range(1, 6):
    numero = int(input(f'Digite o {i}º numero: '))
    soma += numero


print(f'Resultado: {soma}')