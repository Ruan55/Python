algo = str(input('Digite algo: ')).upper().strip()
print(f'A letra A aparece {algo.count('A')} vezes')
print(f'A primeira letra A apareceu na posição: {algo.find('A')+1}')
print(f'A ultima letra A apareceu na posição: {algo.rfind('A')+1}')


