nomeCompleto = str(input('Digite seu nome completo: ')).strip()
nome = nomeCompleto.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[len(nome)-1]}')
