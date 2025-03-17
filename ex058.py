# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

#Exercício 28: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint #importei a função randint que gera números aleatórios
palpites = 1 #a contagem dos palpites
computador = randint(0, 3) # a variável computador para armazenar o número que o randint gerou

jogador = int(input('Informe um número inteiro qualquer entre 0 e 10: ')) # peço ao usuário o palpite dele

while jogador != computador: # inicio o while com a condição do palpite do jogador ser diferente do palpite do computador
    jogador = int(input('Você errou! Tente mais uma vez. ')) # quando o paplpite for diferente a mensagem de erro aparece e solicita uma nova entrada 
    palpites += 1 #contagem dos palpites

print(f'Parabéns você conseguiu acertar com {palpites} palpites. O número escolhido pelo computador foi: {computador} e o número escolhido pelo jogador foi: {jogador}') #quando o jogador acerta o mesmo número do computador


#Guanabara

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10. ')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais! ... Tente mais uma vez.')
        else:
            print('Menos!... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!' .format(palpites))
        

