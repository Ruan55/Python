import os
os.system('cls || clear')

par = 0
impar = 0

for i in range(5):

    numero = int(input(f'Digite o {i+1}º numero: '))

    if numero % 2 == 0:
         par += 1
    
    if numero % 2 == 1:
        impar += 1
        
print(f'Numero pares: {par}')
print(f'Numeros impares: {impar}')