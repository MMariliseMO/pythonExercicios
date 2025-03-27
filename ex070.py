# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

'''total_compra = total_produto = produto_mil = 0
nome_produto_barato = ''
preco_produto_barato = float('inf')

while True:
    nome_produto = str(input('Informe o nome do produto: ')).strip()
    preco_produto = float(input('Informe o preço do produto: '))
    
    total_produto += preco_produto
    
    if preco_produto > 1000:
        produto_mil += 1
    
    if preco_produto < preco_produto_barato:
        preco_produto_barato = preco_produto
        nome_produto_barato = nome_produto 
    

    cadastro = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if cadastro == 'N':
        break

print(f'O total gasto na compra foi de: {total_produto}.')
print(f'{produto_mil} produtos custam mais de R$1000.00. ')
print(f'{nome_produto_barato} foi o produto mais barato.')'''

###########################################
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break

print('{:-^40}' .format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')



