import os

from dataclasses import dataclass

os.system('cls || clear')

@dataclass
class Pet:
    nome: str
    idade: int
    raca: str
    porte: str
    alimentacao: str

pets = []

nome = input('Digite o nome do seu pet: ')
idade = int(input('Digite a idade do seu pet: '))
raca = input('Digite a raça do seu pet: ')
porte = input('Digite o porte do seu pet: ')
alimentacao = input('Digite a alimentação do seu pet: ')

pet = Pet(nome = nome, idade = idade, raca = raca, porte = porte, alimentacao = alimentacao)
pets.append(pet)

print(f'Nome do pet: {nome}')
print(f'Idade do pet: {idade}')
print(f'Raça do pet: {raca}')
print(f'Porte do pet: {porte}')
print(f'Alimentação do pet: {alimentacao}')
