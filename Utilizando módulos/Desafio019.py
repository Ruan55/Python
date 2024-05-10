from random import choice
primeiroAluno = input('Primeiro aluno: ')
segundoAluno = input('Segundo aluno: ')
terceiroAluno = input('Terceiro aluno: ')
quartaAluno = input('Quarto aluno: ')
sorteio = [primeiroAluno, segundoAluno, terceiroAluno, quartaAluno]
sorteado = choice(sorteio)
print(f'O aluno escolhido foi {sorteado}')
