import os
os.system('cls || clear')

def cabecalho():

    os.system('cls || clear')
    print('='*10)
    print('SENAI')
    print('='*10)

def somar(primeiroNumero, segundoNumero):
    soma = primeiroNumero + segundoNumero
    return soma

def subtrair(primeiroNumero, segundoNumero):
    subtracao = primeiroNumero - segundoNumero
    return subtracao

def multiplicar(primeiroNumero, segundoNumero):
    multiplicao = primeiroNumero * segundoNumero
    return multiplicao

def dividir(primeiroNumero, segundoNumero):
    divisao = primeiroNumero / segundoNumero
    return divisao

cabecalho()
primeiroNumero = int(input('Digite o primeiro numero: '))
segundoNumero = int(input('Digite o segundo numero: '))

somaResultado = somar(primeiroNumero, segundoNumero)
subtracaoResultado = subtrair(primeiroNumero, segundoNumero)
multiplicacaoResultado = multiplicar(primeiroNumero, segundoNumero)
divisaoResultado = dividir(primeiroNumero, segundoNumero)

print(f'Primeiro Numero: {primeiroNumero}')
print(f'Segundo Numero: {segundoNumero}')
print(f'Soma: {somaResultado}')
print(f'Subtração: {subtracaoResultado}')
print(f'Multiplicação: {multiplicacaoResultado}')
print(f'Divisão: {divisaoResultado}')

