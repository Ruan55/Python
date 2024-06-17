import os
from dataclasses import dataclass

os.system('cls || clear')

# Solicitar dados para o usuario
# usuario = (nome e idade)
# Estrutura de dados

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    nome: str
    idade: int

alunos = []

for i in range(QUANTIDADE_ALUNOS):

    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    aluno = Aluno(nome = nome, idade = idade)
    alunos.append(aluno)

for dados_alunos in alunos:
    print(f'Nome: {dados_alunos.nome}')
    print(f'Idade: {dados_alunos.idade}')

print('Salvando dados em um arquivo')

# Nome do arquivo
nome_arquivo = 'cadastro_de_alunos.txt'

# Gravando dados no arquivo
with open(nome_arquivo, "w") as arquivo:
    for dados_alunos in alunos:
        arquivo.write(f'{dados_alunos.nome}, {dados_alunos.idade}')

print('Dados salvos com sucesso!!!')

input('Lendo dados em um arquivo')
listar_alunos = []

# Lendo dados do arquivo
with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        nome, idade = linha.strip().split(',')
        listar_alunos.append(Aluno(nome = nome, idade = int(idade)))

# Exibindo dados
for aluno in listar_alunos:
    print(f'Nome: {aluno.nome}')
    print(f'Idade: {aluno.idade}')
