#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

'''from random import choice
alunos = ['Fatima', 'Olimpio', 'Messias', 'Marilise'] #são elementos separados da minha lista

print(choice(alunos))
'''

#solicitando os nomes dos alunos ao usuário
'''import random
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]

print(f'O aluno sorteado é: {random.choice(alunos)}')
'''

#usei o for
'''import random
alunos = [] #declarei uma lista
for i in range(1, 5): #são 4 alunos
    nome = input('Digite o nome do aluno: ')
    alunos.append(nome) # o list.append(x) adiciona um item ao final da lista

print(f'O aluno sorteado é: {random.choice(alunos)}')
'''

#https://docs.python.org/3/library/random.html