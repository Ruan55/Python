import os
os.system('cls || clear')

operador = str(input('Escolha a operação que deseja: +, -, *, / : '))
primeiroNumero = int(input('Digite o primeiro numero: '))
segundoNumero = int(input('Digite o segundo numero: '))

match(operador):

    case '+':
        resultado = primeiroNumero + segundoNumero
    case '-':
        resultado = primeiroNumero - segundoNumero
    case '*':
        resultado = primeiroNumero * segundoNumero
    case '/':
        resultado = primeiroNumero / segundoNumero
    case _:
        resultado = 0

print(f'Resultado: {primeiroNumero} {operador} {segundoNumero} = {resultado}')
