from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O angulo de {angulo} tem o seno de {seno:.2f}')
print(f'O angulo de {angulo} tem o cosseno de {cosseno:.2f}')
print(f'O angulo de {angulo} tem o tangente de {tangente:.2f}')
