import os
os.system('cls || clear')

nome = str(input('Digite o seu nome: '))
sexo = str(input('Digite o seu sexo: '))
estadoCivil = str(input('Digite o seu estado civil: '))

if sexo == 'f' or sexo == 'F' and estadoCivil == 'casada' or estadoCivil == 'Casada':

    anos = int(input('Digite a quanto tempo está comprometida: '))

print(f'Nome: {nome}')
print(f'Sexo: {sexo}')
print(f'Estado civil: {estadoCivil}')
print(f'Esta comprometida há: {anos} anos')