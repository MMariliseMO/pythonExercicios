#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR o ÍMPAR.

num = int(input('Digite um número qualquer: '))
par = num % 2 #o número par tem resto 0 e número impar tem resto 1
if par == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é impar.')


num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'O número {num} é par.')
else: 
    print(f'O número {num} é impar. ')