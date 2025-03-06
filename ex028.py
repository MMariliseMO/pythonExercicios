#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
num_usuario = int(input('Digite um número inteiro de 0 a 5: '))
num_computador = randint(0, 5) #retorna um número aleatório de 0 a 5

if num_usuario == num_computador:
    print(f'Parabéns, você venceu. O número que eu escolhei foi: {num_computador}.')
else:
    print(f'Que pena! Você perdeu, pois o número que eu escolhi foi: {num_computador}.')
