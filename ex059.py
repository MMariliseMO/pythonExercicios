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
        print(f'\033[7;30mA soma dos números {num1} + {num2} é = {soma}.\033[m\n')
    elif opcao == 2:
        multiplicar = num1 * num2
        print(f'\033[7;30mA multiplicação dos números {num1} * {num2} é = {multiplicar}.\033[m\n')
    elif opcao == 3:
        if num1 > num2:
            print(f'\033[7;30mO número {num1} é maior que {num2}.\033[m\n')
        elif num2 > num1:
            print(f'\033[7;30mO número {num2} é maior que {num1}.\033[m\n')
        else:
            print('\033[7;30mNúmeros iguais!\033[m\n')
    elif opcao == 4:
        print('Escolha novos números! ')
        num1 = int(input('Informe um número qualquer: '))
        num2 = int(input('Informe um outro número qualquer: \n'))
    elif opcao == 5:
        print(' \033[7;30mHasta la vista, baby!\033[m')
    else:
        print('Opção inválida! Volte e escolha uma opção válida!')
    


n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5: 
    print('''          
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa: ''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}' .format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado entre {} * {} é {}' .format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor é {}' .format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Finalizando ...')
    else:
        print('Opção Inválida. Tente Novamente!')
    print('=-=' * 10)
print('Fim do programa! Volte Sempre!')






