#Resumo e exercícios das aulas

#1º desafio - receber o nome e imprimir na tela uma mensagem de boas vindas
'''nome = input('Qual o seu nome?')

print(f'Olá, {nome}!. Prazer em te conhecer!')
#o f é o f-string, pois eu adicionei a variável dentro do print, ou seja, precisei formatar a string para adicionar a variável nome
'''

#2º desafio - receber o dia, mês e ano do usuário e imprimir na tela
'''dia = input('Digite o dia do seu nascimento:')
mes = input('Digite o mês do seu nascimento: ')
ano = input('Digite o ano do seu nascimento: ')

print(f'Você nasceu no dia: {dia}/{mes}/{ano}, correto?')
'''

#3º desafio - ler 2 números e dar a soma entre eles
'''num1 = float(input('Digite o 1º número: ')) #digitei float, pois o input() só ler string então usamos float() para converter a entrada para número flutuante (decimal), posso usar também o int() para números inteiros
num2 = float(input('Digite o 2º número: '))
soma = num1 + num2
print('A soma do número {} + o número {} é = {}' .format(num1, num2, soma)) #usando o .format()
'''

'''num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
soma = num1 + num2
print(f'A soma do número {num1} + o número {num2} é = {soma}') #usando o f-string
'''

# 4º desafio - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''algo = input('Digite algo: ')
print(f'\n0 tipo primitivo desse valor é: {type(algo)}')
print(f'O valor contém apenas espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É uma combinação de letras e números? {algo.isalnum()}')
print(f'Todas as letras são maiúsculas? {algo.isupper()}')
print(f'Todas as letras são minúsculas? {algo.islower()}')
print(f'A 1º letra está maiúscula e o restante minúscula? {algo.istitle()}')
'''

#aula 08
'''import math #importa toda a biblioteca
num = int(input('Digite um número: '))
raiz = math.sqrt(num) #o math.sqrt faz o cálculo da raiz quadrada, tem o mesmo valor do **
print(f'A raiz de {num} é igual a {math.ceil(raiz)}.') #usei f-string e solicitei que arredonte o número para cima, {math.ceil(raiz)}
'''

'''from math import sqrt, ceil #importei apenas a raiz quadrada
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {ceil(raiz)}')
'''

'''from math import sqrt, ceil #raiz quadrada e arredondar para cima
num = int(input('Digite um número: '))
print(f'A raiz de {num} é igual a {ceil(sqrt(num))}') #mais enxuto, faz tudo em uma linha
'''

'''frase = ('Curso em Vídeo Python')
print(frase[9]) #V - é o índice 9

frase = ('Curso em Vídeo Python')
print(frase[9:13]) #vai do índice 9 até o 13, porém o 13 não conta

frase = ('Curso em Vídeo Python')
print(frase[9:21]) #vai do índice 9 até o 21, porém o 21 não conta

frase = ('Curso em Vídeo Python')
print(frase[9:21:2]) #começa do índice 9 e vai até o 21, porém o 21 não conta. O :2 quer dizer que vai pulando de 2 em 2

frase = ('Curso em Vídeo Python')
print(frase[:5]) #inicia no índice 0 e vai até o índice 5, porém o indice 5 não conta

frase = ('Curso em Vídeo Python')
print(frase[15:]) # índice 15 até o final

frase = ('Curso em Vídeo Python')
print(frase[9::3]) #vai começar no índice 9 e vai até o final, pulando de 3 em 3
'''

#Aula 10 - estuturas condicionais - exemplos dados durante a aula

'''nome = str(input('Qual é o seu nome? ' 
))
if nome == 'Marilise':
    print('Que nome lindo você tem!')
elif nome != 'Marilise':
    print('Seu nome é tão normal :/')'''

'''num1 = float(input('Digite a 1º nota: '))
num2 = float(input('Digite a 2º nota: '))
media = (num1 + num2) / 2

if media >= 7:
    print(f'Parabéns! Sua média foi: {media:.1f} e você está aprovado :)')
else:
    print(f'Que pena! Sua média foi: {media:.1f} e você está reprovado :/')'''

    #Aula 11 - Colocar cores no terminal

    #código ANSI \033[estilo da fonte, cor texto, cor do fundo + letra m

# print('\33[1;35;43mOlá Mundo\033[m')

#Aula 12 - Mundo 2 - Condições Aninhadas
'''nome = str(input('Digite seu nome: '))
if nome == 'Marilise' or nome == 'Messias' or nome == 'Olimpio' or nome == 'Fatima':
    print(f'Seu nome é lindo. Parabéns!:D')
else: 
    print('Vai dar certo. Se preocupa não, tá!')'''

#Aula 13 - Estrutura de repetição for

'''for i in range(6, 0, -1): # -1 ele fica decrescene
    print(i)
print('FIM')

for i in range(0, 7, 2): # de 0 ao 7 de 2 em 2
    print(i)
print('FIM')'''

'''n = int(input('Digite um número: '))
for i in range(0, n):
    print(i)
print('FIM')'''

'''inicio = int(input('Início: '))
final = int(input('Final: '))
passo = int(input('Passo: '))
print('-+-' * 5)
for i in range(inicio, final+1, passo):
    print(i)
print('-+-' * 5)'''

'''s = []
for i in range(0, 3):
    n = int(input('Digite um valor: ')) 
    s.append(n)
print(f'{s}')
print('-+-+- Fim -+-+- ')'''  

#Aula 14 - estrutura de repetição while
'''for c in range(1, 10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''



