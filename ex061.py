# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

#Exercício 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro_termo #mostra o termo
i = 1 #contar os termos
while i <= 10:
    print(f'{termo}', end = ' ')
    termo += razao
    i += 1
