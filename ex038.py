#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: - O primeiro valor é maior; - O segundo valor é maior; ou o - Não existe valor maior, os dois são iguais.

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))

if num1 > num2:
    print('O 1º valor é maior.')
elif num2 > num1:
    print('O 2º valor é maior.')
else:
    print('Os valores são iguais.')
