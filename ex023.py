#Faça um programa que leia um número 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex: Digite um número: 1834. Unidade: 3 Dezena: 3. Centena: 8. Milhar: 1

num = int(input('Digite um número: '))
unid = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print(f'O número {num}, tem: \nUnidade: {unid}; \nDezena: {dez}; \nCentena: {cen}; \nMilhar: {mil}')