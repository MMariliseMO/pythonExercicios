#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal, 3 para hexadecimal.

num = int(input('Digite um número inteiro qualquer: '))
base = int(input('Qual a base que deseja usar para conversão? \n1 para binário; \n2 para octal; \n3 para hexadecimal. '))

if base == 1:
    print(f'O número {num} na base binária é igual a: {bin(num)}.')
elif base == 2:
    print(f'O número {num} na base octal é igual a: {oct(num)}.')
elif base == 3:
    print(f'O número {num} na base hexadecimal é igual a: {hex(num)}')
else:
    print('Opção inválida')


    #https://docs.python.org/pt-br/3.10/library/functions.html#oct