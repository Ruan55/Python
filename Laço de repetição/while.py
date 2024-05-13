import os
os.system('cls || clear')

while True:

    nota = int(input('Digite a sua nota: '))

    if nota < 0 or nota > 10:
        print('Nota invalida!')
    else:
        break

print(f'Nota informada: {nota}')