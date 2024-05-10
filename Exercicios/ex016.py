import os
os.system('cls || clear')

kgMorango = float(input('Digite o kg do morango: '))
kgMaca = float(input('Digite o kg da maçã: '))

if kgMorango <= 5:
    valorMorango = kgMorango * 2.50
else:
    valorMorango = kgMorango * 2.20

if kgMaca <= 5:
    valorMaca = kgMaca * 1.80
else:
    valorMaca = kgMaca * 1.50

total = valorMorango + valorMaca

if kgMorango + kgMaca > 8 or total > 25:
    desconto = total * 0.10
    total = total - desconto

print(f'O valor total que o cliente deve pagar é de: {total:.2f} R$')