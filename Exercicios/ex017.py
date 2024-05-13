import os
os.system('cls || clear')

nota = -1

while(nota < 0 or nota > 10):
    nota = int(input('Digite a sua nota: '))

print(f'Nota informada: {nota}')