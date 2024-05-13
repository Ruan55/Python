import os, time
os.system('cls || clear')

soma = 0
quantidadeDeNotas = 0

nota = int(input('Digite uma nota: '))

while True:

    print('S - Inserir mais uma nota\n')
    print('P - Ver quantas notas foram inseridas\n')
    print('N - Calcular a media aritmética das notas informadas\n')
    opcao = (input('Selecione uma opção acima: '))

    match opcao:

        case 'S':
            os.system('cls || clear')
            notaExtra = int(input('Digite mais uma nota: '))
            quantidadeDeNotas += 1
            soma += nota

        case 'P':
            os.system('cls || clear')
            print(f'Quantidade de notas inseridas: {quantidadeDeNotas}')
            
        
        case 'N':
            os.system('cls || clear')
            quantidadeDeNotas == 0
            media = soma / quantidadeDeNotas
            print(f'Sua media: {media:.2f}')

        case _:
            break







        
    
