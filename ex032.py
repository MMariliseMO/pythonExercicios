#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date #para a data atual
ano = int(input('Qual o ano que deseja saber se é ou não Bissexto? Digite o 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year #pega a data de hoje, porém só o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print('O ano não é BISSEXTO.')
