from random import randint
numero = randint(0, 5) # A maquina sorteia um número entre 0 a 5
print('-' * 55)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' * 55)
usuario = int(input('Em que número eu pensei?: ')) # Perguntando ao usuario qual numero a máquina pensou
if usuario == numero:
    print(f'Eu pensei no numero: {numero}')
    print('PARABÉNS, você venceu!')
else:
    print(f'Eu pensei no numero: {numero}')
    print('Você errou, tente novamente...')




