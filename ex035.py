#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

num1 = float(input('Digite o valor da 1º reta: '))
num2 = float(input('Digite o valor da 2º reta: '))
num3 = float(input('Digite o valor da 3º reta: '))
triangulo = num1 + num2 #para formar o triângulo é necessário verificar se a soma de dois lados é maior que o terceiro lado

if triangulo > num3:
    print('O valores das retas formam um triângulo!')
else:
    print('Os valores das retas não formam um triângulo!')


num1 = float(input('Digite o valor da 1º reta: '))
num2 = float(input('Digite o valor da 2º reta: '))
num3 = float(input('Digite o valor da 3º reta: '))
if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print('O valores das retas podem formar triângulos.')
else:
    print('Os valores das retas não podem formar triângulos.')
