# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = [] #lista vazia para armazenar os pesos
for i in range(1, 6):
    peso = float(input(f'{i}º pessoa, informe o seu peso: '))
    pesos.append(peso) #o peso é inserido na lista pesos
print(f'O peso maior foi: {max(pesos)}Kg')
print(f'O peso menor foi: {min(pesos)}Kg')


maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}º pessoa: ' .format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de: {}Kg.' .format(maior))
print('O menor peso lido foi de: {}Kg.' .format(menor))
