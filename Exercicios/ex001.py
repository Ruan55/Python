import os
os.system('cls || clear')

nome = input('Qual é o seu nome?: ')
idade = input('Qual é a sua idade?: ')
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
soma = nota1 + nota2
media = soma / 2

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Primeira nota: {nota1}')
print(f'Segunda nota: {nota2}')
print(f'Sua media: {media}')


