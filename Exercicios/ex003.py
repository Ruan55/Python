import os
os.system('cls || clear')

# Solicitando os dados do usuario
primeiroNumero = int(input('Digite o primeiro numero: '))
segundoNumero = int(input('Digite o segundo numero: '))

# Somando os numeros
soma = primeiroNumero + segundoNumero

# Calculando o valor do produto
produto = primeiroNumero * segundoNumero

# Calculando a media
media = soma / 2

# Exibindo o resultado no terminal
print(f'Media: {media}')
print(f'soma: {soma}')
print(f'Produto: {produto}')

# Verificando qual é o maior e o menor numero
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
