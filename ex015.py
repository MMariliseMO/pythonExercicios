# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

'''dias_alugado = int(input('Quantos dias alugados? '))
km_percorrido = float(input('Quantos km rodados? '))

print(f'O preço a pagar é de: {60 * dias_alugado} por dia alugado e {km_percorrido * 0.15} por Km rodado. O total a pagar é de: {dias_alugado * 60 + km_percorrido * 0.15}')
'''


#declarando as variáveis individualmente
'''dias_alugados = int(input('Quantos dias alugados? '))
km_percorrido = float(input('Quantos km rodados? '))

valor_dias_alugados = dias_alugados * 60
valor_km_percorrido = km_percorrido * 0.15
total = valor_dias_alugados + valor_km_percorrido

print('O preço a pagar por dias de aluguel é: {:.2f}. Por km rodado {:.2f}. O valor total a ser pago: {:.2f}' .format(valor_dias_alugados, valor_km_percorrido, total))
'''