from random import shuffle
primeiroAluno = input('Primeiro aluno: ')
segundoAluno = input('Segundo aluno: ')
terceiroAluno = input('Terceiro aluno: ')
quartoAluno = input('Quarto aluno: ')
sorteio = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
shuffle(sorteio)
print(f'A ordem de apresentação será: {sorteio}')
