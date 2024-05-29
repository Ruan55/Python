import os

# Declarando as variáveis
preco = 0
subtotal = 0
totalPagar = 0
pratos_escolhidos = []

while True:

    os.system('cls || clear')
    # Opções para o menu do restaurante
    print('1 - BIG DOUGLAS 10R$')
    print('2 - CHEESE PICANHA 15R$')
    print('3 - BIG CHEEDAR 20R$')
    print('4 - CHICKEN PREMIUM 25R$')
    print('5 - BIG JUMBO 30R$')
    print('6 - BIG BACON 35R$')
    print('7 - BIG ING 40R$')
    opcao = int(input('Escolha uma das opções acima: '))

    # Configurando as opções
    match opcao:

        case 1:
            print('1 - BIG DOUGLAS')
            preco = 10
            repetir = str(input(r'Deseja inserir mais um prato?: (s\n)'))
            pratos_escolhidos.append('1 - BIG DOUGLAS')
        case 2:
            print('2 - CHEESE PICANHA')
            preco = 15
            repetir = str(input(r'Deseja inserir mais um prato?: (s\n)'))
            pratos_escolhidos.append('2 - CHEESE PICANHA')
        case 3:
            print('3 - BIG CHEEDAR')
            preco = 20
            repetir = str(input(r'Deseja inserir mais um prato?: (s\n)'))
            pratos_escolhidos.append('3 - BIG CHEEDAR')
        case 4:
            print('4 - CHICKEN PREMIUM')
            preco = 25
            repetir = str(input(r'Deseja inserir mais um prato?: (s\n)'))
            pratos_escolhidos.append('4 - CHICKEN PREMIUM')
        case 5:
            print('5 - BIG JUMBO')
            preco = 30
            repetir = str(input(r'Deseja inserir mais um prato?: (s\n)'))
            pratos_escolhidos.append('5 - BIG JUMBO')
        case 6:
            print('6 - BIG BACON')
            preco = 35
            repetir = str(input(r'Deseja inserir mais um prato?: (s\n)'))
            pratos_escolhidos.append('6 - BIG BACON')
        case 7:
            print('7 - BIG ING')
            preco = 40
            repetir = str(input(r'Deseja inserir mais um prato?: (s\n)'))
            pratos_escolhidos.append('7 - BIG ING')

        case 0:
            break
    
    # Calculando o subtotal
    subtotal += preco

os.system('cls || clear')
while True:

    # Opções de pagamento
    print('1 - Pagamento a vista')
    print('2 - Pagamento a prazo')
    formaDePagamento = int(input('Selecione uma das forma de pagamento acima: '))

    match formaDePagamento:

        case 1:
            desconto = subtotal * 0.10
            totalPagar = subtotal - desconto
            print(pratos_escolhidos)
            print('Você escolheu o pagamento a vista!')
            print(f'Valor do desconto: {desconto}')
            print(f'Subtotal: {subtotal}')
            print(f'Total a pagar: {totalPagar:.2f}')
            break
        case 2:
            taxa = subtotal * 0.10
            totalPagar = subtotal + taxa
            print(pratos_escolhidos)
            print('Você escolheu o pagamento a prazo!')
            print(f'Valor da taxa: {taxa}')
            print(f'Subtotal: {subtotal}')
            print(f'Total a pagar: {totalPagar:.2f}')
            break