#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# usando apenas 1 variável.
'''num = float(input('Digite o valor em metros: '))

print(f'O valor {num} em centímetros é {num * 100:.1f} e em milímetros é {num * 1000:.1f}.')
'''

# declarando uma variável para centrímetros e milímetros usando o .format()
'''n = float(input('Digite um valor em metros: '))
c = n * 100
m = n * 1000

print('O número: {} em centímetros é: {} e em milímetros é: {}' .format(n, c, m))
'''

# usando o .format()
'''num = float(input('Digite um valor em metros: '))

print('O valor: {}, equivale a: {} em centímetros e: {} em milímetros' .format(num, num * 100, num * 1000))
'''