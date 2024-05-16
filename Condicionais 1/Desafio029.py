velocidade = int(input('Qual foi a velocidade do seu carro?: '))
limite = 80
multa = (velocidade-80) * 7

if velocidade > limite:
    print(f'{velocidade}KM')
    print('Limite de velocidade excedido!!! Você foi multado!')
    print(f'Sua multa esta no valor de {multa:.2f}R$')
else:
    print(f'{velocidade}KM')
    print('Velocidade dentro do limite! Tenha um ótimo dia!')
