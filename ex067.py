# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True: #loop infinito
    num = int(input('Informe um número: '))
    if num <= 0: # se for menor ou igual a zero
        break # sai do loop, pois é o número menor que 0
    print('*' * 30)
    print(f'-> TABUADA DO NÚMERO {num} <-')
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    print('*' * 30)
print('Fim do programa!')