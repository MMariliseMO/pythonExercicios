#Crie um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

# usando o f-string
'''nome = input('Qual o seu nome? ')
print(f'Seja bem-vindo(a), {nome}!')
'''

# usando o .format()
'''nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!' .format(nome)) # .format(variável) vai inserir o valor da variável nome dentro do {}, porém usar o f-string é mais legível e mais prático.
'''