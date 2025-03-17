# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 0 #inicia com 0 para garantir que seja executada pelo menos uma vez
num1 = float(input('Informe um número qualquer: '))
num2 = float(input('Informe outro número qualquer: '))

while opcao != 5:
    opcao = int(input('''Escolha uma das opções abaixo:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa: \n'''))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma dos números {num1} + {num2} é = {soma}.\n')
    elif opcao == 2:
        multiplicar = num1 * num2
        print(f'A multiplicação dos números {num1} * {num2} é = {multiplicar}.\n')
    elif opcao == 3:
        if num1 > num2:
            print(f'O número {num1} é maior que {num2}.\n')
        elif num2 > num1:
            print(f'O número {num2} é maior que {num1}.\n')
        else:
            print('Números iguais! \n')
    elif opcao == 4:
        print('Escolha novos números! ')
        num1 = float(input('Informe um número qualquer: '))
        num2 = float(input('Informe um outro número qualquer: \n'))
    elif opcao == 5:
        print(' \033[7;30mHasta la vista, baby!\033[m')
    else:
        print('Opção inválida! Volte e escolha uma opção válida!')
    


