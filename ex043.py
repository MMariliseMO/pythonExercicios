#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo: 
# Abaixo de 18,5: baixo peso; 
# Entre 18,5 e 25,0: peso ideal; 
# Entre igual a 25 e 30,0: sobrepeso; 
# Entre 30 e 40: obesidade; 
# Acima de 40: Obesidade mórbida.

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
calculo_imc = peso / (altura * altura)

if calculo_imc < 18.5:
    print(f'O IMC é {calculo_imc:.1f}. \nVocê está ABAIXO DO PESO.')
elif 18.5 <= calculo_imc < 25:
    print(f'O IMC é: {calculo_imc:.1f}. \nVocê está com o PESO IDEAL.')
elif 25 <= calculo_imc < 30:
    print(f'O IMC é: {calculo_imc:.1f}. \nVocê está coM SOBREPESO.')
elif 30 <= calculo_imc < 40:
    print(f'O IMC é: {calculo_imc:.1f}. \nVocê está com OBESIDADE.')
else:
    print(f'O IMC é: {calculo_imc:.1f}. \nVocê está com o OBESIDADE MÓRBIDA.')




