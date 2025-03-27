# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

contador_idade = contador_homens = contador_mulheres = 0

while True:
    sexo = str(input('Informe o Sexo[M/F]: ')) .upper().strip()
    idade = int(input('Informe a idade: '))

    if idade > 18:
        contador_idade += 1
    if sexo == 'M':
        contador_homens += 1
    if sexo == 'F' and idade < 20:
        contador_mulheres += 1

    cadastro = str(input('Deseja continuar cadastrando? [S/N] ')) .upper().strip()
    if cadastro == 'N':
        break

print('Cadastro realizado com sucesso!')
print(f'Foram cadastrados {contador_idade} pessoas maiores de 18 anos.')
print(f'{contador_homens} homens cadastrados.')
print(f'E {contador_mulheres} mulheres com menos de 20 anos.')

###################################

tot18 = totH = totalM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totalM20 += 1
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {tot18} homens cadastrados.')
print(f'Temos total {totalM20} mulheres com menos de 20 anos.')

