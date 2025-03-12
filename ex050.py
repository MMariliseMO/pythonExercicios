# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar desconsidere-o.

soma = 0 #acumulador
cont = 0 #contador
for i in range(1, 7):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Dos 6 números digitados, {cont} são pares e a soma entre eles é: {soma}')

    
        