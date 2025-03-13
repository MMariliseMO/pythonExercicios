# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


num = int(input('Informe um número: '))
cont_dividor = 0 #contador para contar quantos divisores o num possui
if num < 2: #verifica se o número é menor que 2
    print(f'O número {num} não é primo!')
else: # se o número não for menor que 2 ele inicia a contagem
    for i in range(1, num + 1):
        if num % i == 0: # ao dividir o num por i e o resto for igual a 0, significa que i é divisor de num
            cont_dividor += 1 #incrementa o divisor 
    if cont_dividor == 2: #verifica se o divisor é igual a 2, pois o número primo só é dividido por 1 e por ele mesmo
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



