import os
os.system('cls || clear')

# Vetor em Python
notas = []

for i in range(3):

    nota = float(input('Digite uma nota: '))
    notas.append(nota)

for i in range(3):

    print(f'Nota {i + 1}: {notas[i]}')


