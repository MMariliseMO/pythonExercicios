#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados são iguais; 
# Isósceles: dois lados iguais; 
# Escaleno: todos os lados diferentes.

#enunciado do exercício ex035.py: #Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

lado1 = float(input('Informe o valor do 1º lado: '))
lado2 = float(input('Informe o valor do 2º lado: '))
lado3 = float(input('Informe o valor do 3º lado: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2: #o critério para os valores darem um triângulo é: A soma dos dois lados tem que ser maior que o valor do terceiro lado
    print(f'Os valores {lado1}, {lado2}, {lado3} formam um triângulo!')
    if lado1 == lado2 == lado3:
        print('Triângulo Equilátero.')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('Triângulo Isóceles.')
    else:
        print('Trângulo Escaleno.')
else:
    print('Os valores não formam um triângulo.')

    
