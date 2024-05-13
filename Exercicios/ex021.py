import os
os.system('cls || clear')

soma = 0
quantidadeDeNotas = 0

while True:

    nota = int(input('Digite uma nota: '))

    resposta = (input('Deseja inserir mais uma nota?: '))
   
    soma += nota
    quantidadeDeNotas += 1

    if resposta == 'N':
        break

media = soma / quantidadeDeNotas

print(f'Sua media: {media}')

if media >= 7:
    print('Aprovado!')
elif media >= 5:
    print('Recuperação!')
else:
    print('Reprovado!')

            