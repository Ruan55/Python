primeiroNumero = int(input('Digite o primeiro numero: '))
segundoNumero = int(input('Digite o segundo numero: '))
terceiroNumero = int(input('Digite o terceiro numero: '))
maiorValor = primeiroNumero
menorValor = primeiroNumero

if segundoNumero < primeiroNumero and segundoNumero < terceiroNumero:
    menorValor = segundoNumero
if terceiroNumero < primeiroNumero and terceiroNumero < segundoNumero:
    menorValor = terceiroNumero

if segundoNumero > primeiroNumero and segundoNumero > terceiroNumero:
    maiorValor = segundoNumero
if terceiroNumero > primeiroNumero and terceiroNumero > segundoNumero:
    maiorValor = terceiroNumero

print(f'Menor valor: {menorValor}')
print(f'Maior valor: {maiorValor}')