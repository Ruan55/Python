import os
os.system('cls || clear')

def cabecalho():

    os.system('cls || clear')
    print('='*10)
    print('SENAI')
    print('='*10)

def Inflacao(preco):
    if preco < 100:
        inflacao = preco * 0.10
        precoFinal = preco + inflacao
        return precoFinal
    if preco >= 100:
        inflacao = preco * 0.20
        precoFinal = preco + inflacao
        return precoFinal
    
cabecalho()
preco = float(input('Digite o preço do produto: '))

precoFinal = Inflacao(preco)

print(f'Preço final: {precoFinal:.2f}')

    
