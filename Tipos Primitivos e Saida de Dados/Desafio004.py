print('=== DESAFIO 004 ===')
n = input('Digite algo: ')
print(f'Possui apenas letras maiusculas?{n.isupper()}')
print(f'Possui apenas letras minusculas?{n.islower()}')
print(f'Possui apenas numeros?{n.isnumeric()}')
print(f'Possui apenas letras?{n.isalpha()}')
print(f'Possui letras e numeros?{n.isalnum()}')
print(f'Possui apenas numeros decimais?{n.isdecimal()}')
print(f'Possui espaço?{n.isspace()}')