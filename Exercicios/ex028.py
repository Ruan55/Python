import os
os.system('cls || clear')

numeros = []
qntdNegativos = 0
somaPositivos = 0

for i in range(10):

    numero = int(input(f'Digite {i+1}º numero: '))
    numeros.append(numero)

    if numeros[i] < 0:
        qntdNegativos += 1
    if numeros[i] > 0:
        somaPositivos += numeros[i]
    
for i in range(10):

    print(f'{i+1}º Numero: {numeros[i]}')

print(f'Quantidade de numeros negativos: {qntdNegativos}')
print(f'Soma dos numeros positivos: {somaPositivos}')