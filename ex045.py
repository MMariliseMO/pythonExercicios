#Crie um programa que faça o computador jogar o Jokenpô com você.

from random import randint #importei a função randint() do módulo random para gerar números aleatórios
import time #o módulo time para o intervalo do tempo para a jogada
itens = ('Pedra', 'Papel', 'Tesoura') #tenho 3 elementos
jogador = int(input('''Qual opção você escolhe?
0 - Pedra;
1 - Papel;
2 - Tesoura. ''')) #escolha do jogador

print('PEDRA ...')
time.sleep(1) #pausa de 1 segundo entre as mensagens
print('PAPEL ... ')
time.sleep(1)
print('TESOOOOURA!')
time.sleep(1)

computador = randint(0, 2) #gera a escolha do computador. A função randint() vai gerar um número entre 0 e 2 e vai ficar armazenado na variável computador

if jogador in [0, 1, 2]: #verifica se a escolha do jogador está dentro das opções válidas
    print('-__-' * 10)
    print(f'Jogador escolheu: {itens[jogador]}')
    print(f'Computador escolheu: {itens[computador]}')

    if jogador == computador: #escolheram a mesma opção      
        print('\033[1;30;47mEmpate!\033[m')
    elif (jogador == 0 and computador == 1 ) or (jogador == 1 and computador == 2) or (jogador == 2 and computador == 0): #condições que o computador ganha
        print('\033[1;30;47mComputador Ganhou!\033[m')
    else: 
        print('\033[1;30;47mJogador Ganhou\033[m')
    print('-__-' * 10)    
else:
    print('Opção Inválida!')


