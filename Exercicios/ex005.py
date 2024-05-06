import os
os.system('cls || clear')

idade = int(input('Digite a sua idade: '))

if idade < 18 or idade > 65:
    print('Não é obrigado!')
else:
    print('É obrigado')
