#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250.00 calcule um aumento de 10%. Para salários inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor do salário: '))

if salario > 1250.00:
    print(f'Com o aumento de 10% o valor do seu novo salário é de: R${(salario * 0.1) + salario}')
else:
    print(f'Com o aumento de 15% o valor do seu novo salário é de: R${(salario * 0.15) + salario}')