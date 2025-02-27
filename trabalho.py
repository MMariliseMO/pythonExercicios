#O professor de Modelagem de Negócios e Requisitos passou um trabalho em grupo. O grupo é de até  5 alunos e no nosso círculo de amizades, temos 10 pessoas. Criar um programa em python que solicite o nome dos amigos e faça um sorteio mostrando na tela a equipe1 e equipe2 cada um com 5 integrantes

from random import shuffle

amigos = [] #lista de amigos
for i in range(1, 11): #são 10 amigos
    nomes = input(f'Digite o nome do {i}º amigo: ') #variável para receber o nome dos amigos
    amigos.append(nomes) #a cada interação do usuário o método append adiciona o nome digitado ao final da minha lista

shuffle(amigos) #embaralhando os amigos, pois é a lista amigos que precisa sem abaralhada

#divisão das equipes (fatiamento das equipes)
sorteio1 = amigos[:5] #sorteio1 é uma variável a partir da lista amigos. Digo que o 1º sorteio contém os 5 primeiros nomes (vai do índice 0 até o 4) 
sorteio2 = amigos[5:] #sorteio2 é uma variável a partir da lista amigos. Digo que o 2º sorteio vai do 5º índice para o final (vai do índice 5 até o final da lista)

#equipes
print(f'A 1ª equipe é: {sorteio1}')
print(f'A 2ª equipe é: {sorteio2}')

#sobre o fatiamento: https://docs.python.org/3/tutorial/introduction.html#more-on-lists
#listas e append: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range