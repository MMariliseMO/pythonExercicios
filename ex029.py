#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre um mensagem dizendo que ele será multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite a velocidade atual do carro: '))
multa = velocidade - 80
if velocidade > 80:
    print(f'Você será multado no valor de: R${multa * 7:.1f}, pois está acima do limite.')
else:
    print('Boa viagem! \nDirija com cuidado!')

