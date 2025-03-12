# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Informe um número: '))
cont_dividor = 0 #contador
if num < 2:
    print(f'O número {num} não é primo!')
else:
    for i in range(1, num + 1):
        if num % i == 0:
            cont_dividor += 1
    if cont_dividor == 2:
        print(f'O número {num} é primo!')
    else: 
        print(f'O número {num} não é primo!')


num = int(input('Informe um número: '))
tot = 0
for c in range(1, num +1): #o for vai do número 1 até o número digitado pelo usuário + 1, pois o python conta 1 a menos no for.
    if num % c == 0:
        print('\033[33m', end = ' ')
        tot += 1
    else:
        print('\033[31m', end = ' ')
    print(f'{c}', end = ' ')
print('\n\033[mO número {} foi divisível {} vezes'. format(num, tot))
if tot == 2:
    print('O número é primo!')
else:
    print('O número não primo!')



