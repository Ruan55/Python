import os
os.system('cls || clear')

primeiroNumero = int(input('Digite o primeiro numero: '))
segundoNumero = int(input('Digite o segundo numero: '))
soma = primeiroNumero + segundoNumero
produto = primeiroNumero * segundoNumero

media = soma / 2

print(f'Media: {media}')
print(f'soma: {soma}')
print(f'Produto: {produto}')

if primeiroNumero > segundoNumero:
    print(f'O maior numero é: {primeiroNumero}')
else:
     print(f'O maior numero é: {segundoNumero}')

if primeiroNumero < segundoNumero:
    print(f'O menor numero é:{primeiroNumero}')
else:
    print(f'O menor numero é:{segundoNumero}')

if primeiroNumero == segundoNumero:
    print('Os 2 numeros são iguais')
