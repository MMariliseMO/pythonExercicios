#Crie um programa que leia o nome completo de uma pessoa e mostre: *O nome com todas as letras maiúsculas. *O nome com todas as letras minúsculas. *Quantas letras ao todo(sem contar os espaços). *Quantas letras tem o seu primeiro nome. 


nome = str(input('Digite o nome completo: '))
print(f'Letras Maiúsculas: {nome.upper()}')
print(f'Letras Minúsculas: {nome.lower()}')
print(f'Tem um total de: {len(nome) - nome.count(" ")} letras') #contei os nomes len(nome) depois tirei os espaços com o -(menos) nome.count(" ")
print(f'O 1º nome é: {nome.split()[0]} e tem {len(nome.split()[0])} letras.') 


nome = input('Digite o nome completo: ')
print(f'Nome em maiúsculo: {nome.upper()}')
print(f'Nome em minúsculo: {nome.lower()}')
print(f'Quantidade de letras sem espaços: {len(nome.replace(" ", ""))} letras') #a função len(variável) conta as letras e o replace (" ", "") substitui os espaços " " por uma string vazia (""), ou seja, remove os espaços
print(f'Seu 1º nome é: {nome.split()[0]}.  Ele tem: {len(nome.split()[0])} letras') #o split() divide um string em uma lista de palavras, quando eu coloco o nome.split()[0] eu estou pedindo para ele retornar o primeiro elemento da lista que é o primeiro nome. Adicionei o len(), pois quero que informe também a quantidade de letras


nome = str(input('Digite seu nome completo: ')).strip() #especificou que quer uma string str e no final removeu os espaços em branco com o .strip(). Os espaços antes e depois do nome
print('O nome maiúsculo é: {}' .format(nome.upper()))
print('O nome minúsculo é: {}' .format(nome.lower()))
print('Quantidade de letras sem espaços: {}' .format(len(nome) - nome.count(' '))) #(len(nome) - nome.count(' '))) ler a quantidade de letras da variável nome e depois retira os espaços em branco - nome.count(' ') 
print('Seu nome tem ao todo {} letras' .format(nome.find(' '))) #o find(' ') localiza a o primeiro espaço no nome, ou seja, a posição do 1º espaço
separa = nome.split() #joga dentro de uma lista os nomes
print('Seu primeiro nome é: {}. Ele tem: {} letras' .format(separa[0], len(separa[0]))) #separa[0] separa o 1º nome e o len(separa[0] conta as letras do 1º nome
