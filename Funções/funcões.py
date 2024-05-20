import os
os.system('cls || clear')

def cabecalho():

    os.system('cls || clear')
    print('='*10)
    print('Senai')
    print('='*10)

cabecalho()
nome = input('Digite o seu nome: ')

cabecalho()
idade = int(input('Digite a sua idade: '))

print(f'Nome: {nome}')
print(f'Idade: {idade}')