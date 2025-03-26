# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
contador = 0

while True:
    num_jogador = int(input('Informe um número: '))
    escolha = str(input('Você escolhe PAR ou ÍMPAR? ')) .upper() .strip()

    num_computador = randint(0, 11)
    resultado = num_jogador + num_computador

    print(f'O Jogador jogou {num_jogador} e o Computador jogou {num_computador}.')
    
    if resultado % 2 == 0:
        if escolha == 'PAR':
            print('JOGADOR VENCEU!!')
            contador += 1
        else:
            print('COMPUTADOR VENCEU!!')
            break
    else:
        if escolha == 'IMPAR':
            print('JOGADOR VENCEU!!')
            contador += 1
        else:
            print('COMPUTADOR VENCEU!!')
            break

print('-_-' * 10)
print('Fim de jogo! Você venceu {contador} vezes.')