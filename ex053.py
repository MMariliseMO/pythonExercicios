#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# Exemplos de palíndromos:APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Infome uma frase: ')) .strip().lower() #.strip().lower() tirar espaços desnecesários e deixar a frase toda em letras minúsculas

frase = frase.replace(" ", "") #o replace() para substituir os " " espaços por "" sem espaõs
frase_invertida = frase[:: -1] #fatiei a string de tráspara frente independente do início e fim

if frase == frase_invertida: #a condição de frase ser igual a frase invertida
    print(f'A frase: {frase} lida ao contrário é: {frase_invertida}.')
    print('\033[1mÉ um palíndromo!\033[m')
else:
    print(f'A frase: {frase} lida ao contrário é: {frase_invertida}.')
    print('\033[1mNão é um palíndromo!\033[m')


frase = str(input('Informe a frase: ')) .strip().upper() #para desconsiderar os espaços e deixar tudo minúsculo

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}' .format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else: 
    print('A frase digitada não é um palíndromo')




