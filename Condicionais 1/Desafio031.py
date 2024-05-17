distancia = int(input('Digite a distância da viagem: '))

if distancia <= 200:
    viagemCurta = distancia * 0.50
    print(f'Você esta prestes a começar uma viagem de {distancia}KM')
    print(f'E o preço da sua passagem será de {viagemCurta:.2f}R$')

else:
    viagemLonga = distancia * 0.45
    print(f'Você esta prestes a começar uma viagem de {distancia}KM')
    print(f'E o preço da sua passagem será de {viagemLonga:.2f}R$')


