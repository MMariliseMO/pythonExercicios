# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = cont = soma = 0
contador = 0
num = int(input('Informe um número [999 para PARAR]: '))
while num != 999:
    contador += 1
    soma += num
    num = int(input('Informe um número [999 para PARAR]: '))
print(f'Foram digitados {contador} termos')
print(f'A soma entre eles é de: {soma}')

