#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
anos = int(input('Em quantos anos deseja pagar a casa? '))
prestacao = casa / (anos * 12) #preciso converter os anos em meses
if prestacao > 0.30 * salario:
    print(f'Para pagar uma casa no valor de {casa:.2f} em {anos} anos a prestação é de R$ {prestacao:.2f}. \nEmpréstimo Negado!')
else:
    print(f'Para pagar uma casa no valor de {casa:.2f} em {anos} anos a prestação é de R$ {prestacao:.2f}. \nEmpréstimo Concedido!')

