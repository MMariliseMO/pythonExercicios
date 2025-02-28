#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

#bibliotecas para cos(x) - cosseno, sin(x) seno e tang(x) tangente
from math import cos, sin, tan, radians 
num = float(input('Digite um número de um ângulo qualquer: '))
num_rad = radians(num) #o valor solicitado ao usuário vem em graus, porém as funções cos(), sin() e tan() retorna em radianos. O num_rad = radians(num) é uma variável que converte o número em graus para radiano

print(f'O valor {num}, tem como seno: {sin(num_rad):.2f}, cosseno: {cos(num_rad):.2f} e tangente: {tan(num_rad):.2f}')


#.format()
from math import cos, sin, tan, radians
num = float(input('Digite um número de um ângulo qualquer: '))
num_rad = radians(num)

print('O valor {}, tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.' .format(num, sin(num_rad), cos(num_rad), tan(num_rad)))


#importei toda a biblioteca math
import math
num = float(input('Digite um ângulo qualquer: '))
num_rad = math.radians(num)
print(f'O valor {num}, tem como seno {math.sin(num_rad):.2f}, cosseno {math.cos(num_rad):.2f} e tangente {math.tan(num_rad):.2f}')
