import os

from dataclasses import dataclass

@dataclass
class Veiculo:
    placa: str
    cor: str
    numeroDePassageiros: int
    capacidadeDeTanque: int
    velocidadeMaxima: int
    consumoMedio: int

@dataclass
class Cliente:
    nome: str
    idade: int
    cpf: int
    endereco: str
    telefone: int

veiculos = []
clientes = []

os.system('cls || clear')
placa = input('Digite a sua placa: ')
cor = input('Digite a sua cor: ')
numeroDePassageiros = int(input('Digite a quantidade de passageiros: '))
capacidadeDeTanque = int(input('Digite a capacidade do tanque: '))
velocidadeMaxima = int(input('Digite a velocidade máxima: '))
consumoMedio = int(input('Digite o consumo médio: '))

veiculo = Veiculo(placa = placa, cor = cor, numeroDePassageiros = numeroDePassageiros, capacidadeDeTanque = capacidadeDeTanque, velocidadeMaxima = velocidadeMaxima, consumoMedio = consumoMedio)
veiculos.append(veiculo)

os.system('cls || clear')
nome = input('Digite seu nome: ')
idade = int(input('Digite a sua idade: '))
cpf = int(input('Digite o seu cpf: '))
endereco = input('Digite o seu endereço: ')
telefone = int(input('Digite o seu número de telefone: '))

cliente = Cliente(nome = nome, idade = idade, cpf = cpf, endereco = endereco, telefone = telefone)
clientes.append(cliente)

os.system('cls || clear')
print(f'Placa: {placa}')
print(f'Cor: {cor}')
print(f'Numero de passageiros: {numeroDePassageiros}')
print(f'Capacidade de tanque: {capacidadeDeTanque}')
print(f'Velocidade máxima: {velocidadeMaxima}')
print(f'Consumo médio: {consumoMedio}')

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Cpf: {cpf}')
print(f'Endereço: {endereco}')
print(f'Telefone: {telefone}')
