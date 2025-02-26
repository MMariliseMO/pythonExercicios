#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

 # importei a biblioteca hypot, usada para calcular a hipotenusa
'''from math import hypot
cateto_oposto = float(input('Digite o valor do Cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do Cateto adjacente: '))

print(f'O comprimento da hipotenusa é: {hypot(cateto_oposto, cateto_adjacente):.2f}')
'''

# importei o sqrt retorna a raiz quadrada do número
'''from math import sqrt
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = sqrt(cateto_oposto*cateto_oposto + cateto_adjacente*cateto_adjacente)

print(f'A hipotenusa é: {hipotenusa:.2f}')
'''
# a documentação dá a seguinte expressão (x, y)sqrt(x*x + y*y), ou seja, posso usar o hypot(x, y) com os catetos (1º código) oou posso usar o sqrt(x*x + y*y) (2º código). Lembrando de importar a biblioteca especifica
 
