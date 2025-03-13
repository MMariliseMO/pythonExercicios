# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    ano_nascimento = int(input(f'Ano de nascimento da {i}º pessoa: '))
    idade = ano_atual - ano_nascimento
    if idade > 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} maiores de idade.')
print(f'Ao todo tivemos {menor} menores de idade.')

    