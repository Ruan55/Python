import os
os.system('cls || clear')

soma = 0

for i in range(3):

    while True:

        nota = int(input('Digite um nota: '))

        if nota < 0 or nota > 10:
            print('Nota invalida!')
        else:
            soma += nota
            break
        
media = soma / 3
print(f'Sua media: {media}')

if media >= 7:
    print('Aprovado!')
elif media >= 5 and media <= 6.9:
    print('Recuperação!')
else:
    print('Reprovado!')