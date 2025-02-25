# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. (Considere US$1,00 = R$3,27)

# declarando apenas 1 variável e usando o f-string
'''din = float(input('Qual o valor que você tem na carteira em Reais(R$): '))

print(f'Com o valor: R${din:.2f} você pode comprar: US${din / 3.27:.2f}.')
'''

# declarar a variável dinheiro e fazer o cálculo do cambio em variável separada, usando o .format()
'''din = float(input('Digite o valor que você tem na carteira em Reais(R$): '))
cambio = din / 3.27

print('Com o valor: R${}, você pode comprar US${:.2f}' .format(din, cambio))
'''

