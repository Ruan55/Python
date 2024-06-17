import os
from dataclasses import dataclass

os.system('cls || clear')

# Solicitar dados para o usuario
# usuario = (nome e idade)
# Estrutura de dados

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

alunos = []

for i in range(QUANTIDADE_ALUNOS):

    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    aluno = Aluno(nome = nome, idade = idade)
    alunos.append(aluno)

for dados_alunos in alunos:
    print(f'Nome: {dados_alunos.nome}')
    print(f'Idade: {dados_alunos.idade}')
