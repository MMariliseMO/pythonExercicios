# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

# usando o f-string com cálculo feito no print 
'''prod = float(input('Qual o valor do produto? '))

print(f'O produto no valor de: {prod} com 5% de desconto fica: {prod * 0.95:.2f}') #0.95 foi retirado os 5% dos 100%, quanto tira os 5% o cliente paga 95% do produto original.
'''

#variáveis decladar individualmente e o .format() usado
'''prod = float(input('Qual o valor do produto? '))
desc = prod * 0.05
preco_final = prod - desc

print('O produto {} com desconto de 5%, fica: {:.2f}' .format(prod, preco_final))
'''