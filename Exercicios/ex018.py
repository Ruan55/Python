import os
os.system('cls || clear')

nota1 = -1
nota2 = -2

while(nota1 < 0 or nota1 > 10):
    nota1 = int(input('Digite uma nota: '))

while(nota2 < 0 or nota2 > 10):
    nota2 = int(input('Digite uma nota: '))

media = (nota1 + nota2) / 2

print(f'Primeira nota informada: {nota1}')
print(f'Segunda nota informada: {nota2}')
print(f'Sua media: {media:.2f}')




