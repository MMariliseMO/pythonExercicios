#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# usando o f-string e declarando apenas a variável num
'''num = float(input('Digite um número: '))
print(f'O número {num}, tem como o dobro {num * 2}, triplo {num * 3} e raiz quadrada {num ** 0.5:.2f}') # o ** 0.5:.2f, quer dizer: O ** 0.5 calcula a raiz quadrada do número, pois elevar o número a 1/2 é o mesmo que calcular a raiz quadrada e :.2f é que quero apenas 2 casas decimais.
'''

# declarando as variáveis e usando o .format()
'''n = float(input('Digite um número: '))
dobro = n * 2 
triplo = n * 3
raiz = n ** 0.5

print('O número {}, tem como o dobro {}, triplo {} e raiz quadrada {:.2f}' .format(n, dobro, triplo, raiz))
'''

# usando apenas o .format()
'''num = float(input('Digite um número: '))
print('O numero {}, possui como dobro {}, triplo {} e raiz quadrada {:.2f}' .format(num, num * 2, num * 3, num ** 0.5))
'''