#calculadora em python para treino da aula 10 sobre estruturas condicionais

num1 = float(input('Digite o 1º número: '))
operador = input('\nDigite o operador matemática que deseja usar: \n "+" para somar, \n "-" para subtrair, \n "*" para multiplicar e \n "/" para dividir: \n')
num2 = float(input('\nDigite o 2º número: '))

if operador == "+":
    print(f'O resultado da soma é: {num1 + num2}')
elif operador == "-":
    print(f'O resultado da subtração é: {num1 - num2}')
elif operador == "*":
    print(f'O resultado da multiplicação é: {num1 * num2}')
elif operador == "/":
    if num2 == 0:
        print(f'Não é possível dividir por 0')
    else:
        print(f'O resultado da divisão é: {num1 / num2}')
else: 
    print('Operador inválido!')

