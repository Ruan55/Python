import os
os.system('cls || clear')

def cabecalho():

    os.system('cls || clear')
    print('='*10)
    print('Senai')
    print('='*10)

def somar(primeiroNumero, segundoNumero):
    resultado = primeiroNumero + segundoNumero
    return resultado

cabecalho()
primeiroNumero = int(input('Digite o primeiro numero: '))
segundoNumero = int(input('Digite o segundo numero: '))

soma = somar(primeiroNumero, segundoNumero)

print(f'Primeiro numero: {primeiroNumero}')
print(f'Segundo numero: {segundoNumero}')
print(f'Resultado: {soma}')