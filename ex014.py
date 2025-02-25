# Escreva um programa que converta uma temperatura em graus Celsius para graus Fahrenheit.

#com a fórmula resumida e usando o decimal
'''temperatura = float(input('Qual o valor da temperatura em graus Celsius(°C)? '))

print(f'A temperatura {temperatura}°C, corresponde a {(1.8 * temperatura) + 32:.1f}°F!') #1.8 * °F + 32 é a forma resumida da fórmula
'''

#com a fórmula real 
'''temperatura = float(input('Qual o valor da temperatura em graus Celsius(°C)? '))
f = 9 * temperatura / 5 + 32 # a fórmula real é: °F = (°C × 9/5) + 32

print('A temperatura {:.1f}°C, corresponde a {:.1f}°F!' .format(temperatura, f))
'''
