salario = float(input('Digite o seu salario atual: '))

if salario > 1250:
    aumentoSalario = salario * 0.10
    novoSalario = salario + aumentoSalario
    print(f'Quem ganhava {salario}R$ passa a ganhar {novoSalario}R$')
if salario <= 1250:
    aumentoSalario = salario * 0.15
    novoSalario = salario + aumentoSalario
    print(f'Quem ganhava {salario}R$ passa a ganhar {novoSalario}R$')

