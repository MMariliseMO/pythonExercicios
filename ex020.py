#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

'''import random
alunos = []
for i in range(1, 5):
    nome = input('Digite o nome dos alunos: ')
    alunos.append(nome)

random.shuffle(alunos) #chamei o random.shuffle(), pois ele precisa embaralhar a lista de nomes.

print(f'A sequência de alunos para apresentação é: {alunos}')   
'''