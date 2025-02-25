#Crie um programa que ler 2 números e dar a soma entre eles.

# usando o int() e o f-string
'''n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
s = n1 + n2

print(f'A soma do número {n1} + {n2} é igual a: {s}')
'''

# usando o float() e o .format()
'''num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
soma = num1 + num2

print('A soma do número {} + {} é igual a: {} ' .format(num1, num2, soma))
'''

# sem declarar a variável soma
'''n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))

print('A soma do número {} + o número {} é igual a: {:.2f}' .format(n1, n2, n1 + n2))
'''