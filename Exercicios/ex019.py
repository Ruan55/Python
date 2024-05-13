import os
os.system('cls || clear')

soma = 0

for i in range (2):

    while True: 

        nota = int(input('Digite uma nota: '))
       
        if nota < 0 or nota > 10:
            print('Nota invalida!')
        else:
            soma += nota
            break

media = soma / 2
print(f'Sua media: {media:.2f}')