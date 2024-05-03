import os
os.system('cls || clear')

# Solicitando os dados do usuario
nome = input('Qual é o seu nome?: ')
idade = input('Qual a sua idade?: ')
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))

# Somando as notas
soma = nota1 + nota2 + nota3

# Calculando a media
media = soma / 3

# Exibindo o resultado no terminal
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Primeira nota: {nota1}')
print(f'Segunda nota: {nota2}')
print(f'Terceira nota: {nota3}')
print(f'Sua media: {media}')

# Verificando a media do aluno
if media < 7:
    print('Reprovado')
else:
    print('Aprovado')
