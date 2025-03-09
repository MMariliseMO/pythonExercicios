#elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 
# A vista, dinheiro ou cheque: 10% de desconto; 
# A vista no cartão: 5% de desconto;  
# Em até 2x no cartão: preço normal; 
# 3x ou mais no cartão: 20% de juros.

valor_produto = float(input('Informe o valor do produto: '))
pagamento = input('Informe como deseja pagar: \n1 - À vista, dinheiro ou cheque; \n2 - À vista no cartão; \n3 - Em até 2x no cartão; \n4 - 3x ou mais no cartão. \n')

if pagamento == "1":
    print(f'O valor com 10% de desconto fica de: R$ {valor_produto - (valor_produto * 0.10):.2f}') 
elif pagamento == "2":
    print(f'O valor do produto com 5% de desconto fica de: R$ {valor_produto - (valor_produto * 0.05):.2f}')
elif pagamento == "3":
    print(f'O produto fica no valor normal sem desconto. Valor de: R${valor_produto:.2f}')
elif pagamento == "4":
    print(f'O produto com juros de 20% fica de: R$ {valor_produto + (valor_produto * 0.20):.2f}')
else:
    print('Opção de pagamento inválida!')


valor_produto = float(input('Informe o valor do produto: '))
pagamento = input('''Informe como deseja pagar: 
1 - À vista, dinheiro ou cheque; 
2 - À vista no cartão; 
3 - Em até 2x no cartão; 
4 - 3x ou mais no cartão. ''')

if pagamento == "1":
    valor_com_desconto = valor_produto - (valor_produto * 0.10)
    print(f'O produto com 10% de desconto fica de: R$ {valor_com_desconto:.2f}')
elif pagamento == "2":
    valor_com_desconto = valor_produto - (valor_produto * 0.05)
    print(f'O valor com 5% de desconto fica de: R$ {valor_com_desconto:.2f}')
elif pagamento == "3":
    print(f'O produto fica de R$ {valor_produto:.2f}, pois não tem desconto.')
elif pagamento == "4":
    valor_com_juros = valor_produto + (valor_produto * 0.20)
    print(f'O produto com 20% de juros fica de: R$ {valor_com_juros:.2f}')
else:
    print('Opção inválida. Por favor, escolha uma opção válida.')