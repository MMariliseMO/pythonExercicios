#Faça um programa que leia três números e mostre qual é o maior e qual é o menor entre eles.

num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
num3 = float(input('Digite o 3º número: '))

print(f'O menor número é: {min(num1, num2, num3)}')
print(f'O maior número é: {max(num1, num2, num3)}')


#https://docs.python.org/3/library/functions.html#min