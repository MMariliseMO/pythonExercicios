#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0: #é ímpar e múltiplo de 3
        soma = soma + i
print(f'A soma entre eles é de: {soma}')


soma = 0 #acumulador para somar os valores
cont = 0 #contador
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i  # = soma += i
        cont = cont + 1 #conta o número que achei + 1 - cont += 1
print(f'A soma de todos os {cont} valores solicitados é de: {soma}')

          