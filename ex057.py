# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o sexo: [M/F] ')) .strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Inválido! Digite M ou F')
print(f'Sexo {sexo} registrado com sucesso!')

sexo = str(input('Informe seu sexo: [M/F] ')) .strip().upper()[0]
while sexo not in 'MmFm': #not in verifica se um valor não está presente em uma sequência
    sexo = str(input('Dados inválidos! Por favor, informe seu sexo: ')) .strip().upper()[0]
print('Sexo {} registrado com sucesso.' .format(sexo))

