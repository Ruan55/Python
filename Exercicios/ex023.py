import os
os.system('cls || clear')

notas = []
soma = 0

for i in range(3):

    nota = float(input(f'Digite a {i+1}º nota: '))
    notas.append(nota)
    soma += notas[i]

for i in range(3):

    print(f'{i+1}º Nota: {notas[i]}')

media = soma / 3
print(f'Sua media: {media:.2f}')
