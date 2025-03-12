# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

#ex009.py - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.


num = int(input('Informe um número qualquer: '))
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')


