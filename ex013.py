# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

# declarando variáveis do salário original e depois com o aumento, uso do .format()
salario = float(input('Qual o valor do seu salário? '))
salario_final = salario * 1.15

print('O salário {}, com aumento de 15% ficou {:.2f}' .format(salario, salario_final))


#apenas variável salario com o uso do f-string
salario = float(input('Digite o valor do seu salário: '))

print(f'O salário {salario} com desconto de 15% ficou {salario * 1.15:.2f}.')
