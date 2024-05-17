import os
os.system('cls || clear')

notas = []

while True:
    nota = float(input('Digite a nota do aluno: '))
    notas.append(nota)

    continuar = input(r'Deseja digitar uma outra nota?: (s/n)')
    if continuar == 'n':
     break

print(f'Notas: {notas}')
