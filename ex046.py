#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
for i in range(10, -1, -1): # vai do 10 até 0
    print(f'{i}')
    sleep(1) #pausa de 1s
print("\U0001F4A5" * 5)