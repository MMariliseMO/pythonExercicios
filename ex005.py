# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# usando o f-string 
'''num = int(input('Digite um número: '))
sucessor = num + 1
antecessor = num - 1

print(f'O número {num}, tem como sucessor o {sucessor} e como antecessor o {antecessor}.')
'''

# usando a f-string, porém declarando apenas a variável num
'''num = int(input('Digite um número: '))
print(f'O número {num}, tem como sucessor {num + 1} e como antecessor {num -1}')
'''

# usando o .format() e declarando apenas a variável n para número
'''n = int(input('Digite um número: '))
print('O número {}, tem como sucessor o {} e como antecessor o {}' .format(n, n + 1, n - 1))
'''