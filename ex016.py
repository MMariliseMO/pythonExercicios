#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

#biblioteca completa
'''import math 
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {math.trunc(num)}.')
'''

#apenas a função trunc para mostrar a parte inteira
'''from math import trunc 
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}.') # não precisa da referência math
'''

#sem a necessidade de importar a biblioteca
'''num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {int(num)}') # a variável num foi convertida para inteiro
'''

#https://docs.python.org/3/library/math.html