import os
os.system('cls || clear')

login = str(input('Digite o seu nome de usuario: '))
senha = str(input('Digite a sua senha: '))
loginSalvo = 'Ruan'
senhaSalva = '123'

if login == loginSalvo and senha == senhaSalva:
    print('Acesso liberado!')
else:
    print('Acesso negado!')
    