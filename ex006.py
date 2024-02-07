# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:

import math

num = int(input('Digite um número: '))

print('Dobro de {} é {}'.format(num, num * 2))
print('Triplo de {} é {}'.format(num, num * 3))
print('Raiz quadrada de {} é {}'.format(num, math.sqrt(num)))