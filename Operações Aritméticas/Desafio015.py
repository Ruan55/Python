aluguelDias = int(input('Quantos dias alugado?: '))
kmRodados = float(input('Quantos Km rodados?: '))
precoFinal = (aluguelDias * 60) + (kmRodados * 0.15)
print(f'O total a pagar é de {precoFinal:.2f}')
