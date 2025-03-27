#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for i in range(1, 51):
    if i % 2 == 0: #o número i será dividido por 2 com resto 0
        print(i, end = ' ')

for i in range(2, 51, 2): #começa no índice 2 e pula de dois em dois números
    print(i, end = ' ') #O uso do parametro "end = ' '" no print faz com que os valores sejam impressos na mesma linha, e separados por espaço.