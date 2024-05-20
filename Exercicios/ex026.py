import os
os.system('cls || clear')

soma = 0
notas = []

for i in range(4):

    nota = float(input(f'Digite a {i+1}º nota: '))
    notas.append(nota)
    soma += notas[i]

for i in range(4):

    print(f'{i + 1}Notas: {notas[i]}')

media = soma / 4
print(f'Sua media: {media:.2f}')

if media >= 7:
    print('Aprovado!')
elif media >= 5 and media <= 6.9:
    print('Recuperação!')
else:
    print('Reprovado!')


