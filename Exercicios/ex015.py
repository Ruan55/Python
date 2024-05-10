import os
os.system('cls || clear')

nome = str(input('Digite o nome do aluno: '))
idade = int(input('Digite a sua idade: '))

soma = 0

for i in range(3):

    notas = int(input(f'Digite a {i + 1}º nota: '))
    soma += notas

media = soma / 3
print(f'Sua media: {media:.2f}')

if media >= 7:
    print('Aprovado!')
elif media >= 5 and media <= 6.9:
    print('Recuperação!')
else:
    print('Reprovado!')

