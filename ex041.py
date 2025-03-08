#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade: - Até 9 anos: MIRIM; - Até 14 anos: INFANTIL; - Até 19 anos: JUNIOR; - Até 25 anos: SÊNIOR; - Acima: MASTER.

from datetime import date
ano_nascimento = int(input('Informe o ano do nascimento: ')) #recebe o ano do nascimento
ano_atual = date.today().year #ano atual
idade = ano_atual - ano_nascimento #calcular a idade

if idade <= 9:
    print(f'A idade {idade} anos está na categoria: MIRIM.')
elif idade <= 14:
    print(f'A idade {idade} anos está na categoria: INFATIL.')
elif idade <= 19:
    print(f'A idade {idade} anos está na categoria: JUNIOR.')
elif idade <= 25:
    print(f'A idade {idade} anos está na categoria: SÊNIOR.')
else:
    print(f'A idade {idade} anos está na categoria: MASTER.')

