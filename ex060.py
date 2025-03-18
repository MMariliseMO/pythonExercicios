# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial
import time
num = int(input('Informe um número qualquer: '))
fatorial = factorial(num)
print(f'Calculando ...')
time.sleep(1)
print(f'{num}! = {fatorial}')

#Guanabara
n = int(input('Informe um número: '))
c = n # c é a variável contador
f = 1
print('Calculando {}! = ' .format(n), end = '')
while c > 0: #enquanto o contador for maior que 0
    print('{}' .format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print('{}' .format(f))



    








