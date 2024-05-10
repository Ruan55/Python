import os
os.system('cls || clear')

soma = 0

for i in range(1, 5):

    notas = int(input(f'Digite a {i}º nota: '))

    soma += notas

media = soma / 4
print(f'A sua média é: {media}')